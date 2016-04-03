import mystery_word as mw
from collections import Counter

def get_signature(candidate_word, guesses):
    signature = []
    for each_letter in candidate_word:
        if each_letter in guesses:
            signature.append(each_letter)
        else:
            signature.append('_')
    return ''.join(signature)

def get_all_signatures(candidate_word_list,guesses):
    signatures = {}
    for each_word in candidate_word_list:
            signature = get_signature(each_word, guesses)
            if signature in signatures:
                signatures[signature].append(each_word)
            else:
                signatures[signature] = [each_word]
    return signatures

def evaluate_guess(candidate_word_list,guesses):
    signatures = get_all_signatures(candidate_word_list,guesses)
    count = 0
    signature = ''
    for key in signatures.keys():
        if len(signatures[key]) >= count:
            count = len(signatures[key])
            signature = key
    return signature

def get_candidates(candidate_word_list,guesses,signature):
    return get_all_signatures(candidate_word_list,guesses)[signature]

def display_status(guesses, signature):
    print(20*'=')
    print("Guess #{}".format(len(guesses)+1))
    print("Word: "+signature)
    print("Misses: {}".format([x for x in guesses if x not in signature]))

def play_a_turn(candidate_word_list,guesses, max_misses):
    display_status(guesses, evaluate_guess(candidate_word_list,guesses))
    guess = input("> ")
    guesses.append(guess)
    signature = evaluate_guess(candidate_word_list,guesses)
    # print(candidate_word_list[:10])
    # print(signature)
    return(get_candidates(candidate_word_list,guesses,signature))
    #display status
    #prompr for guess
    #evaluate guesses


def is_round_over(candidate_word_list, guesses, max_misses):
    if len(candidate_word_list) ==0:
        return True
    word_signature = evaluate_guess(candidate_word_list,guesses)
    if "_" not in word_signature:
        return True
    misses = [x for x in guesses if x not in word_signature]
    if len(misses) >max_misses:
        return True
    return False

def play_game_round(candidate_word_list):
    max_misses = 26
    length = 4
    candidate_word_list = [x for x in candidate_word_list if len(x) == length]
    guesses = []
    while True:
        if is_round_over(candidate_word_list, guesses, max_misses):
            display_status(guesses,evaluate_guess(candidate_word_list,guesses))
            # finish_round(secret_word, guesses, max_misses)
            break
        else:
            candidate_word_list = play_a_turn(candidate_word_list, guesses, max_misses)


def main():
    word_list = mw.read_dictionary()

    while True:
        play_game_round([x.lower() for x in word_list])
        if not mw.should_play_again():
            print("Thanks for playing.")
            break
    print("Goodbye.")

if __name__ == '__main__':
    main()
