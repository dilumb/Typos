'''
Created on Oct 7, 2018

@author: DilumBandara
'''

import PyPDF2

class PDF_Handler(object):
    '''
    classdocs
    '''


    def __init__(self, file_name):
        '''
        Constructor
        '''
        self.file_name = file_name
        self.pdf_reader = PyPDF2.PdfFileReader(self.file_name)
        
    def get_text(self, page_no):
        '''
        Get text on given page
        '''
        page = self.pdf_reader.getPage(page_no)
        return page.extractText()


    def get_all_text(self):
        '''
        Get text on all pages
        '''        
        full_text = ''
        for i in range(self.pdf_reader.getNumPages()):
            page = self.pdf_reader.getPage(i)
            full_text += page.extractText() + "\n"
        return full_text
    
    
    def get_no_pages(self):
        '''
        Get no of pages in document
        '''
        return self.pdf_reader.getNumPages()