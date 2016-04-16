
#
# The 6.00 Word Game


import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}



WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	


#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    
    if word == "":
        return 0
    
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    
    score = score * len(word)
    
    if n == len(word):
        score += 50
    return score



#

#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#

#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#

#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    finalhand = dict(hand)
    
    for letter in word:
        if letter in finalhand.keys():
            finalhand[letter] -= 1
    return finalhand


#

#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    word_dic = getFrequencyDict(word)
    for letter in word_dic.keys():
        if letter not in hand.keys():
            return False
        if word_dic.get(letter,0) > hand.get(letter):
            return False
            
    if word not in wordList:
        return False
        
    return True

#

#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    sum = 0
    
    for letter in hand.keys():
        sum += hand[letter]

    return sum


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    
    score = 0
    len = 0
    len = calculateHandlen(hand)
    
    while (len > 0):

    
        # Display the hand
        displayHand(hand)
        # Ask user for input
        word = raw_input("Enter word, or a '.' to indicate that you are finished: ")
        # If the input is a single period:
        if word == '.':
            print("Goodbye! Total score: "+str(score)+" points.")
            break
            # End the game (break out of the loop)
        else:

        # Otherwise (the input is not a single period):
            if (isValidWord(word, hand, wordList) == False) :
            # If the word is not valid:
                print("Invalid word, please try again.")

                # Reject invalid word (print a message followed by a blank line)
            else:
            # Otherwise (the word is valid):
                points = getWordScore(word, n)
                score += points
                print (word + " earned "+str(points)+" points. Total: "+ str(score) +" points")
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                hand = updateHand(hand, word)
                # Update the hand 
        len = calculateHandlen(hand)
    if len < 1 :
        print ("Run out of letters. Total score: "+str(score)+" points.")
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score



def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
   
    #print "playGame not yet implemented."
    char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        
    while (char == 'r'):
        print("You have not played a hand yet. Please play a new hand first!")
        char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    
    if char == 'n':
        strin = dealHand(HAND_SIZE)
        playHand(strin , wordList , HAND_SIZE)
    
        char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    while char != 'e' :
        if char != 'r' and char != 'n' :
            print ("Invalid command.")
            char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if char == 'r':
            playHand(strin , wordList , HAND_SIZE)
            char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if char == 'n':
            strin = strin = dealHand(HAND_SIZE)
            playHand(strin , wordList , HAND_SIZE)
            char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")




#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
