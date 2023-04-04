words_file = open("N5.txt", 'r', encoding="UTF-8")
i_file = open("i_series.txt",'w',encoding="UTF-8")

words = words_file.readlines()
for word in words:
    japanese = word.split("；")[1]
    if japanese[0] == 'い':
        i_file.write(word)



words_file.close()
i_file.close()
