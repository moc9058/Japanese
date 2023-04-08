import random
mode = input("0:today.txt, 1:verbs.txt, 2:N5.txt, 3:kanji.txt 그 외:kanji_words.txt\n")
try:
    if int(mode) == 0:
        words_file = open("words/today.txt", 'r', encoding="UTF-8")
    elif int(mode) == 1:
        words_file = open("VA/verbs.txt",'r', encoding="UTF-8")
    elif int(mode) == 2:
        words_file = open("words/N5.txt",'r', encoding="utf-8")
    elif int(mode) == 3:    
        words_file = open("words/kanji.txt",'r', encoding="utf-8")
    else:
        words_file = open("words/kanji_words.txt",'r',encoding="utf-8")
except:
    words_file = open("words/kanji_words.txt",'r', encoding="utf-8")
    
    
prob_index, ans_index = 0,1
words = words_file.readlines()
num_cycle = -1
wrong_cycles = []
wrong_words = []
while True:
    num_cycle += 1
    num_words = len(words)
    again = False

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