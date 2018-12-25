'''
Created on Oct 7, 2018

@author: DilumBandara
'''

import re

class ScanText(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.patterns = {}
        self.typos_found = False
        

    def load_patterns(self, file_name):
        '''
        Load patterns to be checked
        File format should be wrong-patter correct-patter type-of-check 
        '''
        fd_patterns = open(file_name)
        for line in fd_patterns:
            line = line.replace('\n', '')
            if line[0] == '#':  #Skip comment line
                continue
            tmp_txt = line.split("\t")
            #print(tmp_txt)
            self.patterns[tmp_txt[0]] = [tmp_txt[1], tmp_txt[2], tmp_txt[3], 0, []]
            
        fd_patterns.close()

    def search_any(self, pattern, text):
        '''
        Scan for given pattern in any location of text
        '''
        text = text.lower()
        return text.count(pattern + ' ')
    
    def search_begin(self, pattern, text):
        '''
        Scan for given pattern in begining of a sentence
        '''        
        p = re.compile('(^|\.\s)' + pattern + ' ')
        results = p.findall(text)
        return len(results)
    
    def search_end(self, pattern, text):
        '''
        Scan for given pattern in end of a sentence
        '''
        p = re.compile(pattern + '\.')
        results = p.findall(text)
        return len(results)
    
    def search_case(self, pattern, text):
        '''
        Scan for given pattern in end of a sentence
        '''
        return text.count(pattern + ' ')

    def search_regex(self, pattern, text):
        '''
        Scan for given pattern in end of a sentence
        '''
        p = re.compile(pattern)
        results = p.findall(text)
        return len(results)
    
    
    def scan_all(self, text, page_no):
        for p in self.patterns:
            count = 0
            if self.patterns[p][2] == 'Any':
                count = self.search_any(p, text)
            elif self.patterns[p][2] == 'Begin':
                count = self.search_begin(p, text)
            elif self.patterns[p][2] == 'End':
                count = self.search_end(p, text)
            elif self.patterns[p][2] == 'Case':
                count = self.search_case(p, text)               
            elif self.patterns[p][2] == 'RegEx':
                count = self.search_regex(p, text)  
            else:
                print('Unknwon search pattern', p, self.patterns[p])
                break
            
            if count > 0:
                self.patterns[p][3] += count
                self.patterns[p][4].append(page_no)
                self.typos_found = True
    
    def dump_all(self, file_name):
        fd_dump = open(file_name, 'w')
        text_start = 'This is an auto-generated list of typos found in your thesis/paper/report.\n' + \
            'You should attempt to fix all the typos. You may ignore false positives.\n' + \
            'If you notice any errors please let me know.\n' + \
            '\nIdentified typos are listed as:\n' + \
            'Error Term\tCorrect Term\tDescription\tNo of Occurrences\tPages (absolute)\n'
        fd_dump.write(text_start)        
        for p in self.patterns:
            if self.patterns[p][3] > 0:
                text_to_dump = p + '\t' +  self.patterns[p][0] + '\t' + \
                    self.patterns[p][1] + '\t' + str(self.patterns[p][3]) + '\t' + \
                    ', '.join(str(x) for x in self.patterns[p][4]) + '\n' 
                fd_dump.write(text_to_dump)
        fd_dump.close()
        
