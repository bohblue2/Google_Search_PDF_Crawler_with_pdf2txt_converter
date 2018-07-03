# Google-Search-PDF-Crawler-pdf2txt-
Google Search PDF Crawler (with pdf2txt converter)

 

## Requirements (Dependency)
(not included into base Anaconda)

--> **pdfminer.six**    (download via **'pip install pdfminer.six'** or **'conda install pdfminer.six'**)



 
## Usage Example
'''
api 이용예시 (usage example)
if __name__=="__main__":
    pdfcrawler = pdf2txt(["Water Industry", "Industry 4.0"], pages=10, start_date='01/01/2013', end_date='12/31/2017', filetype='pdf')
    pdfcrawler.download_search_data()
    pdfcrawler.convert_pdfs()
    pdfcrawler.concate_all_txt()
'''

Initial settinh -> ".\donwload\", ".\donwload\txt"
To set download directory manually -> give argument as download_dir=r'C:\Users\something\'   <- should be ended with '\'


