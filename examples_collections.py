def best_stock(stocks):
    from collections import defaultdict
    '''Данная функция принимает одно значение - stocks - словарь, где ключи - 
    названия компаний, а значения - цена за акцию. Функция позволяет выводить
     лучшее предложение(т.е. название компании, у которой самые большие цены за акции '''
    mirror = defaultdict(list)
    for a, v in stocks.items():
        mirror[v].append(a)

    answer = max(mirror.keys())
    return (mirror.get(answer))



def repeating_word_counter(text):
    '''Данная функция принимает одно значение - текст. на выходеПолучаем словарь,
     где ключ - слово или предлог, значение - сколько раз в тексте встречается это слово'''
    from collections import Counter
    word_list = []
    for word in text.split():
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
    return(Counter(word_list))


def popular_words(text: str,words: list) -> dict:
    from collections import Counter
    words_by_frequency = Counter(text.lower().split())
    '''Производится подсчет слов в переменной, в которой !!СПЕРВА!!текст 
    переводится в нижний регистр, после разделяется методом split и зписывается
     в список'''
    answer = {
        word: words_by_frequency.get(word, 0)
        for word in words
    }
    '''Словарь, ключ - новая переменная - каждый элемент из списка words,
    значение - значение из словаря words_by_frequency, которому передан ключ, и указан 
    параметр default = 0'''
    return (answer)

