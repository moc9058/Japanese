sinagong_file = open("시나공_tmp.txt", "r", encoding="UTF-8")
sinagong_words = sinagong_file.readlines()

new_file = open("시나공.txt","w", encoding="UTF-8")

for word in sinagong_words:
    split_1 = word[:-1].split("；")
    korean = split_1[0] 
    japanese = split_1[1].split("（")
    if len(japanese) == 1:
        kanji = japanese[0]
        new_file.write(f"{kanji}；{korean}\n")
    else:
        kanji = japanese[0]
        romaji = japanese[1][:-1]
        new_file.write(f"{kanji}；{romaji}({korean})\n")

sinagong_file.close()
new_file.close()