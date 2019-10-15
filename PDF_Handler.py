'''
Created on Oct 7, 2018
Updated on Oct 15, 2019

@author: Dilum Bandara
Replacing PyPDF2 with PDFMiner
'''

#import PyPDF2
import pdfminer.layout
import pdfminer.high_level
import io

class PDF_Handler(object):
    '''
    classdocs
    '''

    def __init__(self, file_name):
        '''
        Constructor
        '''
        self.file_name = file_name


    def get_all_text(self):
        '''
        Get text on all pages
        '''
        output = io.StringIO()
        laparams = pdfminer.layout.LAParams()

        with open(self.file_name, "rb") as pdffile:
            pdfminer.high_level.extract_text_to_fp(pdffile, output, laparams=laparams)

        return output.getvalue()
