# Google Search PDF Crawler with pdf2txt converter-
Google Search PDF Crawler (with pdf2txt converter)

 

## Requirements (Dependency)
--> **pdfminer.six**    (download via **'pip install pdfminer.six'** or **'conda install pdfminer.six'**)
(not included into base Anaconda)


 
## Usage Example
```python
#api 이용예시 (usage example)
if __name__=="__main__":
    pdfcrawler = pdf2txt(["Water Industry", "Industry 4.0"], pages=10, 
                         start_date='01/01/2013', end_date='12/31/2017', filetype='pdf')
    pdfcrawler.download_search_data()     #download pdfs from list -> ["Water Industry", "Industry 4.0"]
    pdfcrawler.convert_pdfs()     #convert all pdfs to txt
    pdfcrawler.concate_all_txt()  #concate txt files each by search keyword -> to analyze whole txt data
```

- Initial setting : download directory -> ".\donwload\\", converted txt directory -> ".\donwload\txt\\"
- To set download directory manually : give arg as download_dir=r'C:\Users\something\\'   <- should be ended with \


