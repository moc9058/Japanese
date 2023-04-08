words_file = open("kanji2kor.txt", 'r', encoding="UTF-8")
i_file = open("kor2kanji.txt",'w',encoding="UTF-8")

words = words_file.readlines()
for word in words:
    tmp = word.split("\t;\t")
    prob = tmp[1][:-1]
    ans = tmp[0]
    i_file.write(f"{prob}\t;\t{ans}\n")


words_file.close()
i_file.close()
