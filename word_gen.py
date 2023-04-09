import random
print("0:today.txt, 101:verbs.txt, 102:N5.txt, 103:kanji2kor.txt, 104:kor2kanji.txt") 
print("1,2:kanji_words_1,2강, 3:kanji_words_3강, 그 외:kanji_words_통합.txt")
mode = input()
restrict = False
try:
    if int(mode) == 0:
        words_file = open("words/today.txt", 'r', encoding="UTF-8")
    elif int(mode) == 101:
        words_file = open("VA/verbs.txt",'r', encoding="UTF-8")
    elif int(mode) == 102:
        words_file = open("words/N5.txt",'r', encoding="utf-8")
    elif int(mode) == 103:    
        words_file = open("words/kanji/kanji2kor.txt",'r', encoding="utf-8")
        restrict = True
    elif int(mode) == 104:
        words_file = open("words/kanji/kor2kanji.txt",'r', encoding="utf-8")
        restrict = True
    elif int(mode) in [1,2]:
        words_file = open("words/kanji/kanji_words_1,2강.txt",'r', encoding="utf-8")
    elif int(mode) == 3:
        words_file = open("words/kanji/kanji_words_3강.txt",'r', encoding="utf-8")

    else:
        words_file = open("words/kanji/kanji_words_통합.txt",'r',encoding="utf-8")
except:
    words_file = open("words/kanji_words_통합.txt",'r', encoding="utf-8")
    
    
prob_index, ans_index = 0,1
words = words_file.readlines()
num_cycle = -1
wrong_cycles = []
wrong_words = []
thres_length = max(0,len(words) - 50)

while True:
    num_cycle += 1
    num_words = len(words)
    again = False
    if num_words == thres_length and restrict:
        break
    try:
        random_index = random.randint(0, num_words-1)
    except:
        break
    word = words[random_index][:-1]
        
    try:
        if num_words == 0 or num_cycle == wrong_cycles[0]:
            wrong_cycles.pop(0)
            word = wrong_words.pop(0)
            again = True
    except:
        pass
    
    if word in wrong_words:
        again = True
    word_splitted = word.split("\t;\t")
    korean = word_splitted[0]
    if restrict:
        print(f"{korean}({num_words-thres_length} left)", end=" ")
    else:
        print(f"{korean}({num_words} left)", end=" ")
    a = input()
    if a.lower() == 'x':
        break
    
    to_print = word_splitted[1]
    if len(word_splitted) > 2:
        to_print += f", {word_splitted[2]}그룹"
    print(to_print)

    a = input()
    if a.lower() == 'x':
        break
    elif a.lower() == 'o':
        try:
            if not again:
                words.pop(random_index)
        except:
            print("Error")
            break
    else:
        wrong_cycles.append(num_cycle + 5)
        wrong_words.append(word)

    print()
words_file.close()