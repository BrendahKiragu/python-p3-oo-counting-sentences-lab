#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")      

    #ensures the string is not empty then checks if the last values is "."
    def is_sentence(self):
         if self.value.endswith('.'):
             return True
         else:
             return False        

    def is_question(self):
        if self.value.endswith('?'):
            return True
        else:
            return False 

    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else:
            return False    

    def count_sentences(self):
        value = self.value
        for punctuation in ['!','?']:
            value = value.replace(punctuation, '.')
    
        total_sentences = [sentence for sentence in value.split('.') if sentence]
    
        return len(total_sentences)  

sample_sentences = MyString("hello! como estas? estoy, bien.")
print(sample_sentences.is_sentence())