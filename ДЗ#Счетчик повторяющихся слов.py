from collections import Counter

with open ('счетчик_повторяющихся_слов','r') as t:
    txt=t.read()
    '''Из фаила счетчик_повторяющихся_слов выводим текст в переменную txt '''
word_list = []
import re
txt_one=re.findall(r'\w+',txt)
for letter in txt_one:
    clear_word = ''
    if letter.isalpha():
        clear_word += letter.lower()
        word_list.append(clear_word)
print(Counter(word_list))
