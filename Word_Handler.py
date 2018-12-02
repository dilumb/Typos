'''
Created on Oct 11, 2018

@author: DilumBandara
'''

from docx import Document

class Word_Handler(object):
    '''
    classdocs
    '''


    def __init__(self, file_name):
        '''
        Constructor
        '''
        self.file_name = file_name
        self.word_reader = Document(self.file_name)
        
        
    def get_all_text(self):
        '''
        Get text on all pages
        '''        
        full_text = []
        for para in self.word_reader.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)

