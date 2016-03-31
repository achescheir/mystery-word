import random
DICTIONARY_PATH = '/usr/share/dict/words'

def parse_difficulty(user_input):
    if user_input[0].lower() == 'e':
        return 'easy'
    elif user_input[0].lower() == 'n':
        return 'normal'
    elif user_input[0].lower() == 'h':
        return 'hard'
    else:
        return ''

def get_difficulty():
    user_input = input("Please Select a difficulty: (E)asy, (N)ormal, or (H)ard. ")
    difficulty = parse_difficulty(user_input):
    if len(difficulty) >0:
        return difficulty
    else:
        print("I'm sorry that is not a valid seletion.")
        return get_difficulty()

def read_dictionary():
    word_list = []
    with open(DICTIONARY_PATH, 'r') as word_file:
        for each_word in word_file:
            word_list.append(each_word)
    return word_list

def get_word(word_list,difficulty):
    if diffuculty == 'easy':
        return random.choice([x for x in word_list if len(x) >=4 and len(x) <= 6])
    elif diffuculty == "normal":
        return random.choice([x for x in word_list if len(x) >=6 and len(x) <= 8])
    elif diffuculty == "hard":
        return random.choice([x for x in word_list if len(x) >=8])
    else:
        raise ValueError("{} is not a valid difficulty; should be 'easy','normal', or 'hard'.")


def start_round(word_list):
    # explain rules with word length
    #initialize variables
    
    get_word(word_list,get_difficulty())
    pass

def play a turn():
    #display status
    #handle input
    #update status
    pass

def is_round_over():
    # is word guessed?
    #are rounds up?
    pass

def finish_round():
    #display final status
    #play again?
    pass

def play_game_round():
    #start game
    #play a turn
    #finished?
    #finish game
    pass

def main():
    word_list = read_dictionary()
    # Get word
    # Play game
    pass

if __name__ == '__main__':
    main()
