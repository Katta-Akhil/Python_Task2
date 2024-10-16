import re

def count_sentences(text):
    
    sentences = re.split(r'[.!?]+', text)
    
    sentences = [s for s in sentences if s.strip()]
    
    return len(sentences)

text = "Hello! How are you? I'm fine. Thanks."
print(count_sentences(text))  
