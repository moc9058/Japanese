import random
mode = input("0:today.txt, 1:verbs.txt, 그 외:N5.txt\n")
try:
    if int(mode) == 0:
        words_file = open("words/today.txt", 'r', encoding="UTF-8")
    elif int(mode) == 1:
        words_file = open("VA/verbs.txt",'r', encoding="UTF-8")
    else:
        words_file = open("words/N5.txt",'r', encoding="utf-8")
except:
    words_file = open("words/N5.txt",'r', encoding="utf-8")
    
prob_index, ans_index = 0,1
words = words_file.readlines()
num_cycle = -1
wrong_cycles = []
wrong_words = []
while True:
    num_cycle += 1
    num_words = len(words)
    try:
        random_index = random.randint(0, num_words-1)
    except:
        break
    word = words[random_index][:-1]
    try:
        if num_words == 0 or num_cycle == wrong_cycles[0]:
            wrong_cycles.pop(0)
            word = wrong_words.pop(0)
    except:
        pass

    word_splitted = word.split("；")
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
        words.pop(random_index)
    else:
        wrong_cycles.append(num_cycle + 5)
        wrong_words.append(word)

    print()
words_file.close()