# python_games

Hangman:
      Hangman is a paper and pencil guessing game for two or more players.
      One player thinks of a word, phrase or sentence and the other tries 
      to guess it by suggesting letters or numbers, within a certain number 
      of guesses.
      
      
Scrabble:
Dealing
A player is dealt a hand of n letters chosen at random (assume n=7 for now).
          
The player arranges the hand into as many words as they want out of the letters, 
using each letter at most once.
          
Some letters may remain unused (these won't be scored).
          
Scoring
The score for the hand is the sum of the scores for each word formed.
   
The score for a word is the sum of the points for letters in the word, 
multiplied by the length of the word, plus 50 points if all n letters 
are used on the first word created.
          
Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, 
D is worth 2, E is worth 1, and so on. I have defined the dictionary SCRABBLE_LETTER_VALUES 
that maps each lowercase letter to its Scrabble letter value.
          
For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, 
then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand 
actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!
          
As another example, if n=7 and you make the word 'waybill' on the first try, 
it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, 
plus an additional 50 point bonus for using all n letters).
          
Caesar Cipher:
The idea of the Caesar Cipher is to pick an integer and shift every letter of your 
message by that integer. In other words, suppose the shift is k . Then, all instances 
of the i-th letter of the alphabet that appear in the plaintext should become the (i+k)-th 
letter of the alphabet in the ciphertext. You will need to be careful with the case in which 
i + k > 26 (the length of the alphabet). Here is what the whole alphabet looks like shifted three 
spots to the right:

Original:  a b c d e f g h i j k l m n o p q r s t u v w x y z
3-shift:  d e f g h i j k l m n o p q r s t u v w x y z a b c
Using the above key, we can quickly translate the message "happy" to "kdssb" 
(note how the 3-shifted alphabet wraps around at the end, so x -> a, y -> b, and z -> c).
        
Note!! We are using the English alphabet for this problem - that is, the following letters in the following order:
        
        >>> import string
        >>> print string.ascii_lowercase
        abcdefghijklmnopqrstuvwxyz
We will treat uppercase and lowercase letters individually, so that uppercase letters are 
always mapped to an uppercase letter, and lowercase letters are always mapped to a lowercase letter. 
If an uppercase letter maps to "A", then the same lowercase letter should map to "a". Punctuation and 
spaces should be retained and not changed. For example, a plaintext message with a comma should have a 
corresponding ciphertext with a comma in the same position.
        
        |    plaintext    |  shift    |  ciphertext      |
        | ----------------|-----------|------------------|
        | 'abcdef'        |    2      |  'cdefgh'        |
        | 'Hello, World!' |    5      |  'Mjqqt, Btwqi!' |
        | ''              | any value |  ''              |
