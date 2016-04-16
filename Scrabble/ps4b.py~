from ps4a import *
import time


#
#

#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE (available within ps4b.py)
    max_score = 0
    max_word = ''
    # Create a new variable to store the best word seen so far (initially None)  
    for word in wordList:
    # For each word in the wordList
        if (isValidWord(word, hand, wordList)):
            if(getWordScore(word, n) >= max_score):
                max_score = getWordScore(word, n)
                max_word = word
        

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly
    if max_word == '':
        return 
    return max_word
    # return the best word you found.

#

#
def compChooseWord(hand, wordList, n):
    max_score = 0
    max_word = ''
    # Create a new variable to store the best word seen so far (initially None)  
    for word in wordList:
    # For each word in the wordList
        if (isValidWord(word, hand, wordList)):
            if(getWordScore(word, n) > max_score):
                max_score = getWordScore(word, n)
                max_word = word
                
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly
    if max_word == '':
        return
    return max_word
    # return the best word you found.


def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.
    
    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    
    
    score = 0
    len = 0
    len = calculateHandlen(hand)
    # As long as there are still letters left in the hand:
    
    displayHand(hand)
    while ( compChooseWord(hand, wordList, n) ):
        # Display the hand
        
    # Ask user for input
    #word = raw_input("Enter word, or a '.' to indicate that you are finished: ")
        word = compChooseWord(hand, wordList, n)
    # If the input is a single period:
        if word == '.':
            print("Goodbye! Total score: "+str(score)+" points.")
            return
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
                print ("'"+word+"'  earned "+str(points)+" points. Total: "+ str(score) +" points")
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                hand = updateHand(hand, word)
                # Update the hand 
        len = calculateHandlen(hand)
        displayHand(hand)

    
    print("Total score: "+str(score)+" points.")

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    if char == 'e' :
        return

    while (char != 'e' and char != 'n' and char != 'r'):
        print("Invalid command.")
        char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")


    while (char == 'r'):
        print("You have not played a hand yet. Please play a new hand first!")
        char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    if char == 'e' :
        return
    if char == 'n':
        strin = dealHand(HAND_SIZE)
        play = raw_input("Enter u to have yourself play, c to have the computer play: ")
        
                
        while (play != 'u' and play != 'c'):
            print('Invalid Command.')
            play = raw_input("Enter u to have yourself play, c to have the computer play: ")

        if(play == 'u'): 
            playHand(strin , wordList , HAND_SIZE)
               
        if play == 'c':
            compPlayHand(strin , wordList , HAND_SIZE)
    

        
    char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    
    while True :
        if char == 'e':
            return
        if char != 'r' and char != 'n' :
            print ("Invalid command.")
            char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if char == 'r':
            
            play = raw_input("Enter u to have yourself play, c to have the computer play: ")
            while (play != 'u' and play != 'c'):
                print('Invalid Command.')
                play = raw_input("Enter u to have yourself play, c to have the computer play: ")

            if(play == 'u'): 
                playHand(strin , wordList , HAND_SIZE)
                   
            if play == 'c':
                compPlayHand(strin , wordList , HAND_SIZE)
            
            char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if char == 'n':
            strin = dealHand(HAND_SIZE)
            play = raw_input("Enter u to have yourself play, c to have the computer play: ")
            while (play != 'u' and play != 'c'):
                print('Invalid Command.')
                play = raw_input("Enter u to have yourself play, c to have the computer play: ")

            if(play == 'u'): 
                playHand(strin , wordList , HAND_SIZE)
                   
            if play == 'c':
                compPlayHand(strin , wordList , HAND_SIZE)
            char = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
         
#

#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


