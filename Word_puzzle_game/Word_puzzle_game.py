# Problem Statement: You have to write a Word Puzzle Game in which the user has to form
# the correct word out of a given set of characters. In the game the user has to solve this
# puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
# in random sequence. Give the user score +1 for each correct answer and give -1 for each
# wrong answer. At last print the final score. You can store any number of words in the list, but
# in each round of the game only 5 words are shown to the user.


import random
import string

# return the word 
def puzzlelist(puzzle_list):
    
    len_of_lis=len(puzzle_list)
    random_index=random.randint(0,len_of_lis-1)
    selected_word=puzzle_list.pop(random_index)
    return selected_word


# check the user input
def user_input(selected_word,score):
        check=str()
        for i in selected_word:
            check+=i
        
        random.shuffle(selected_word)
        for j in selected_word:
            print(j,end="")
        print()
        user_input=input()

        if check==user_input:
            print("☑")
            score+=1
        else:
            print('☒')
            score-=1
        return score


# main body of the program
if __name__=="__main__":

    score=0
    puzzle_list=['FATHER','GREEN','AEROPLANE','BREAK','INEURON','MYSIRG','TELUSKO','PYTHON']

    print("*"*50)
    print(":::RULES:::")
    print("1.ENTER THE INPUT IN UPPERCASE")
    print("2.+1 FOR CORRECT ANSWER")
    print("3.-1 FOR WRONG ANSWER")
    print("*"*50)

    for i in range(0,5):
        print("Arrange the letters to form a valid word: ")
        selected_word=list(puzzlelist(puzzle_list))
        score=user_input(selected_word,score)

    print("Net score is ",score)

       
