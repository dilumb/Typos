'''
Created on Oct 7, 2018

@author: Dilum Bandara
'''

import sys
import os
from PDF_Handler import PDF_Handler
from Word_Handler import Word_Handler
from ScanText import ScanText 

pattern_file = 'Patterns.txt'
dump_file = 'Typos.txt'

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Command should be of the form Typos <PDF or Word> <file name including path>')
        sys.exit()
    
    st = ScanText()
    st.load_patterns(pattern_file)
    
    doc_text = ''
    
    file_type = sys.argv[1]
    
    if file_type == 'PDF':
        ph = PDF_Handler(sys.argv[2])
        doc_text = ph.get_all_text()
        print('Succesfully open PDF file.')
    elif file_type == 'Word':
        wd = Word_Handler(sys.argv[2])
        doc_text = wd.get_all_text()
        print('Succesfully open Word file')
    else:
        print('Unknown file type. Only PDF and Word are supported')
        sys.exit()
    print("Searching for typos...")
    st.scan_all(doc_text, -1)
    path = os.path.dirname(os.path.abspath(sys.argv[2]))
    st.dump_all(path + '\\' + dump_file)
    
    if st.typos_found:
        print("Typos found!")  
    print("Searching for typos complete.")
