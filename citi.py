def citi_country(citi,country,people=''):
    if people:
        a = citi+ ', ' + country + ', ' + str(people)
    else:
        a = citi+ ', ' + country
    return a.title()

