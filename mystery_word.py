import random
DICTIONARY_PATH = '/usr/share/dict/words'

# I got the ordinal function from:
# http://codereview.stackexchange.com/questions/41298/producing-ordinal-numbers
# I would probably not have thought to use the .get and would have filled in the
# SUFFIXES dictionary but otherwise the code seems straight forward.
# Comments were in the source.
SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def ordinal(num):
    # I'm checking for 10-20 because those are the digits that
    # don't follow the normal counting scheme.
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        # the second parameter is a default.
        suffix = SUFFIXES.get(num % 10, 'th')
    return str(num) + suffix
# Copied code ends here

def ordinal_to_print(number, last):
    number == last:
        return 'last'
    else:
        return ordinal(number)

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
        print("I'm sorry that is not a valid selection.")
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
    guesses = []
    difficulty = get_difficulty()
    secret_word = get_word(word_list,difficulty)
    return secret_word, guesses, difficulty

def get_wrong_guesses_form(wrong_guesses,max_misses):
    return(''[''+''join(wrong_guesses)+(max_misses-len(wrong_guesses))*'-'+']'')

def get_word_print_form(secret_word,guesses):
    print_form = []
    for each_letter in secret_word:
        if each_letter in guesses:
            print_form.append(each_letter.upper())
        else:
            print_form.append("_")
    return ' '.join(print_form)

def display_status(secret_word, guesses, max_misses):
    wrong_guesses = get_wrong_guesses(secret_word,guesses)
    print(10*'-'+"Guess #{}"10*'-'+'\n')
    print("The word so far> "+get_word_print_form(secret_word, guesses)+'\n')
    print("Misses>"+get_wrong_guesses_form(wrong_guesses,max_misses)+'\n')

def play_a_turn(secret_word, guesses, max_misses):
    display_status(secret_word, guesses, max_misses)
    while True:
        user_input = input("What's your {} guess?".format(ordinal(len(guesses)+1))
        cleaned_input = cleanup_input(user_input):
        if cleaned_input:
            if cleaned_input in guesses:
                print("You already guessed {}. Please try again.".format(cleaned_input))
            else:
                guesses.append(cleaned_input.lower())
                break
        else:
            print("I'm sorry {} is not valid. Please enter exactly 1 alphabetical character.".format(user_input))

def is_word_guessed(secret_word, guesses):
    for each_letter in secret_word:
        if each_letter not in guesses:
            return False
    return True

def get_wrong_guesses(secret_word, guesses):
    wrong_guesses = []
    for each_guess in guesses:
        if each_guess not in secret_word:
            wrong_guesses.append
    return wrong_guesses

def is_time_up(secret_word, guesses, max_misses):
    return len(get_wrong_guesses) >= max_misses)


def is_round_over(secret_word, guesses, max_misses):
    return is_word_guessed(secret_word, guesses) or is_time_up(secret_word, guesses)

def finish_round(secret_word, guesses, max_misses):
    display_status(secret_word, guesses, max_misses)
    if is_word_guessed(secret_word, guesses):
        print("You win!")
    else:
        print("Sorry time's up, you lose.")


def play_game_round():
    secret_word, guesses, difficulty = start_round(word_list)
    max_misses = 8
    while True:
        if is_round_over(secret_word, guesses, max_misses):
            finish_round(secret_word, guesses, max_misses)
            break
        else:
            play_a_turn(secret_word, guesses)

def should_play_again():
    user_input = input("Do you want to play again? (y/N)")
    if len(user_input) == 0 or user_input[0].lower() == 'n':
        return False
    elif user_input[0].lower == 'y':
        return True
    else:
        return should_play_again()

def main():
    word_list = read_dictionary()
    while True:
        play_game_round(word_list)
        if not should_play_again():
            print("Thanks for playing.")
            break
    print("Goodbye.")



if __name__ == '__main__':
    main()
