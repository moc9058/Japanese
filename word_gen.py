import random
mode = input("t:today.txt, 그 외:words.txt\n")
if mode.lower() == 't':
    words_file = open("today.txt",'r', encoding="UTF-8")
else:
    words_file = open("words.txt",'r', encoding="utf-8")

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