words_file = open("1_groups.txt", 'r', encoding="UTF-8")
i_file = open("1_groups_backup.txt",'w',encoding="UTF-8")

words = words_file.readlines()
for word in words:
    japanese = word.replace("；","\t;\t")
    i_file.write(japanese)


words_file.close()
i_file.close()
