# -*- coding: <utf-8> -*-
import requests
import sys
import io
import os
import time
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from bs4 import BeautifulSoup
from random import randint 

#--------parameter zone--------
pages = 2 #pages to download
search_keyword = '자동차산업'
start_date = '01/01/2016' #search start date
end_date = '03/21/2018'  #search end date
filetype = 'pdf' #filetype to search 
download_dir = "./download/" #directory to download pdf
txt_dir = './download/txt/'  #directory to save converted txt
#--------parameter zone--------

def is_downloadable(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

def get_link(search_keyword, filetype, startdate, end_date, pages, show_links = False):
    linklist = []
    print("search keyword : ", search_keyword)
    print("expected time(getting links) : ", pages*1, "seconds~", pages*2,"seconds")
    print("----getting links----")
    for page in range(0, pages*10, 10):
        params = {'as_epq': '', 
                  'tbs':'cdr:1,cd_min:01/01/2017,cd_max:01/03/2018', 
                  'start' : '0', 
                  'as_filetype' : 'pdf'}
        params['as_epq'] = search_keyword
        params['tbs'] = "cdr:1,cd_min:"+start_date+",cd_max:"+end_date
        params['start'] = str(page)
        params['as_filetype'] = filetype
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        html = requests.get("https://www.google.com/search", params=params, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        #soup = BeautifulSoup(htmlpage.text, 'lxml')

        for result_table in soup.findAll("div", {"class": "g"}):
            a_click = result_table.find("a")
            if show_links == True:
                print(a_click['href'])
            linklist.append(a_click['href'])
            
        time.sleep(randint(1, 2))
    
    return linklist

def download_pdf_from_links(links, filetype, directory):
    print("----downloading----")
    print("files to download : ", len(links))
    for num, link in enumerate(links):
        try:
            r = requests.get(link, stream=True)
            with open(download_dir+str(num+1)+'.'+filetype, 'wb') as f:
                f.write(r.content)
            print(str((num+1)/len(links)*100)+"% done")
        except:
            print("download error on : ", link)
            
#(c) 2016 Masha Gorkovenko stanford.edu
#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = io.StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    print("----converting pdf to txt----")
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            try:
                pdfFilename = pdfDir + pdf 
                print("converting :", pdfFilename)
                text = convert(pdfFilename) #get string of text content of pdf
                textFilename = txtDir + pdf + ".txt"
                textFile = open(textFilename, "w") #make text file
                textFile.write(text) #write text to text file
            except:
                print("error on converting :", pdfFilename)
        

if __name__=="__main__":
    link = get_link(search_keyword, filetype, start_date, end_date, pages, show_links = True)
    download_pdf_from_links(link, filetype, download_dir)
    convertMultiple(download_dir, txt_dir)