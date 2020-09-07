from collections import Counter

with open ('счетчик_повторяющихся_слов','r') as t:
    txt=t.read()
    '''Из фаила счетчик_повторяющихся_слов выводим текст в переменную txt '''
import re
word_list = []
for word in txt.split():
    clear_word = ''
    '''clear_word - переменная, в которую в последующем будем записывать только буквы'''
    for letter in word:
        '''Проходимся по каждому элементу слова по символьно'''
        if letter.isalpha():
            '''если символ является алфавитом'''
            clear_word += letter.lower()
            '''то мы этот символ записываем в переменную clear_word'''
    word_list.append(clear_word)
    '''в список word_list добавляем слова из clear_word'''
a = Counter(word_list)
print(a)
#print(word_list)


