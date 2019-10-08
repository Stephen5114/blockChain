文本预处理
def cut_sentences(sentence):  
      puns = frozenset(u'.')   
       tmp = []    
       for ch in sentence:       
            tmp.append(ch)        
            if puns.__contains__(ch):         
                   yield ''.join(tmp)          
                   tmp = []   
         yield ''.join(tmp)
