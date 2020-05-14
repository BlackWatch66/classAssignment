# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"
GUESS_OUTPUT_NAME = "myGuessWords.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split() #空格分开的单词
    print("  ", len(wordlist), "words loaded.")
    return wordlist #返回list

wordlist=load_words()
def choose_word(wordlist):
    return random.choice(wordlist) #随机获取一个单词

def save_result(list_guessed, state) :
    guessed = " ".join(list_guessed)
    f = open(GUESS_OUTPUT_NAME,'w')
    f.write(guessed)
    f.write("\n")
    f.write(state)
    f.close()
    return 

#判断玩家猜测是否正确
def is_word_guessed(secret_word, letters_guessed):
    list_secret=list(secret_word)
    #只要目标中出现一个字母不在玩家猜测结果中，返回False,都在的话，返回True
    for i in list_secret:
        if i not in letters_guessed:
            return False
    return True

#获取玩家已猜对字母
def get_guessed_word(secret_word, letters_guessed):
    length=len(secret_word)
    list_secret=['_ ']*length #列表元素先全部初始化为'_'
    for i in letters_guessed:
        for j in range(length): 
            if i==secret_word[j]: #用猜对的字母替换掉对应位置的'_'
                list_secret[j]=secret_word[j]
    
    string="".join(map(lambda x:str(x),list_secret)) #列表转字符串
    return string


#获取剩余可猜测字母范围
def get_available_letters(letters_guessed):
    #初始化可猜字母为全部小写字母
    letters_all="abcdefghijklmnopqrstuvwxyz"
    for i in letters_all:
        if i in letters_guessed: #如果玩家已经猜过 i 则将其替换为'_ '
            letters_all=letters_all.replace(i,'')
    return letters_all
   

def hangman(secret_word):
    list_unique=[] #用于secret_word去重
    for i in secret_word:
        if i not in list_unique:
            list_unique.append(i)
    unique_numbers=len(list_unique) #目标单词中不同字符的数量，用于计算玩家分数
    vowels="aeiou"
    print("Welcome to the game hangman!")
    length=len(secret_word) #目标单词长度
    print("I'm thinking of a word that is {} letters long!".format(length))
    times_left=6 #玩家剩余猜测次数
    warning_left=3 #玩家剩余警告次数
    print("You have {} warnings left.".format(warning_left))
    print("------------- ")
    list_guessed=[]
    while times_left>0: #玩家猜测次数没用完
        print("You have {} guesses left.".format(times_left))
        print("Available letters:",get_available_letters(list_guessed))
        char=input("Please guess a letter:")
        x=str.lower(char)
        if x in list_guessed:#玩家已经猜过这个字母
            if warning_left>0:  #警告次数没用完
                warning_left-=1
                print("Oops! You've already guessed that letter.You have {} warnings left:".format(warning_left),get_guessed_word(secret_word,list_guessed))
            else:           #警告次数为0了 扣guessing次数
                times_left-=1
                print("Oops! You've already guessed that letter.You have no warnings left,so you lose one guess:",get_guessed_word(secret_word,list_guessed))
            
        else: #玩家尚未猜测过这个字母
            list_guessed.append(x) #先存储玩家猜测结果
            if not str.isalpha(x): #玩家输入不是是字母
                if warning_left>0:
                    warning_left-=1
                    print("Oops!That is not a valid letter.You have {} warnings left:".format(warning_left),get_guessed_word(secret_word,list_guessed))
                else:
                    times_left-=1
                    print(" Oops! That is not a valid letter. You have no warnings left,so you lose one guess:",get_guessed_word(secret_word,list_guessed))
            #玩家输入是字母时
            elif x in secret_word:#玩家猜测字母在目标中
                print("Good guess:",get_guessed_word(secret_word,list_guessed))
                # 玩家猜出全部字母
                if secret_word==get_guessed_word(secret_word,list_guessed):
                    print("------------- ")
                    print("Congratulations, you won!")
                    total_score=times_left*unique_numbers
                    print("Your total score for this game is:",total_score)
                    save_result(list_guessed, "lose")
                    return 
            else: #玩家猜测字母不在目标中
                print("Oops! That letter is not in my word.",get_guessed_word(secret_word,list_guessed))
                if x in vowels: #没有猜中，且是元音字母
                    times_left -= 2
                else:
                    times_left -= 1 
        print("------------- ")
    print("Sorry, you ran out of guesses.The word was {}".format(secret_word)) #失败
    save_result(list_guessed, "lose")
    return 

if __name__ == "__main__":  
    secret_word=choose_word(wordlist)
    hangman(secret_word)    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints("apple")