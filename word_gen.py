import random
mode = input("0:today.txt, 1:회화책.txt, 그 외:시나공\n")
try:
    if int(mode) == 0:
        words_file = open("word/today.txt", 'r', encoding="UTF-8")
    elif int(mode) == 1:
        words_file = open("word/회화책.txt",'r', encoding="UTF-8")
    else:
        words_file = open("word/시나공.txt",'r', encoding="utf-8")
except:
    words_file = open("word/시나공.txt",'r', encoding="utf-8")
    
prob_index, ans_index = 0,1
K_or_J = input("j:일본어를 보여줌, 그 외:한국어를 보여줌\n")
if K_or_J.lower() == 'j':
    prob_index, ans_index = 1,0

words = words_file.readlines()

while True:
    num_words = len(words)
    if num_words == 0:
        break
    random_index = random.randint(1, num_words)-1
    word = words[random_index][:-1]
    word_splitted = word.split("；")
    prob = word_splitted[prob_index]
    ans = word_splitted[ans_index]
    
    print(f"{prob}({num_words} left)", end=" ")
    a = input()
    if a.lower() == 'x':
        break

    print(f"정답: {ans}")
    a = input()
    if a.lower() == 'x':
        break
    elif a.lower() == 'o':
        words.pop(random_index)
    print()
words_file.close()