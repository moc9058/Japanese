words_file = open("N5.txt", 'r', encoding="UTF-8")
i_file = open("1_groups.txt",'w',encoding="UTF-8")

words = words_file.readlines()
factor = ['い', 'え', 'き', 'け', 'し', 'せ', 'ち', 'て', 'に', 'ね', 'ひ', 'へ', 'み', 'め', 'り', 'れ', 'ぎ', 'げ', 'じ', 'ぜ', 'ぢ', 'で', 'び', 'べ', 'ぴ', 'ぺ']
for word in words:
    japanese = word.split("；")
    try:
        if int(japanese[-1][0]) == 1:
            ru = japanese[1][-1]
            before_ru = japanese[1][-2]
            if ru == "）":
                ru = japanese[1][-2]
                before_ru = japanese[1][-3]
            if ru == 'る' and before_ru in factor:
                i_file.write(word)
            
    except:
        pass


words_file.close()
i_file.close()
