kanji_file = open("kanji.txt",'r',encoding="UTF-8")
new_file = open("kanji_edited.txt",'w',encoding="UTF-8")

kanjis = kanji_file.readlines()
for kanji in kanjis:
    lst = kanji.split("\t;\t")
    Prob, Ans = lst[0], lst[1]
    Prob += '\n'
    new_file.write(Prob)
    new_file.write(Ans)

kanji_file.close()
new_file.close()