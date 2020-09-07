def first_word(text):
    import re
    x = re.findall(r'\w+.\w*',text)
    y = re.findall(r'\w+',text)
    if "'" in x[0]:
        return x[0]
    else:
        return y[0]
print(first_word("I"))