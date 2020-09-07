def left_join(phrases):
    import re
    answer = re.sub(r'right','left',','.join(phrases))
    return(answer)

print(left_join(["left", "right", "left", "stop"]))