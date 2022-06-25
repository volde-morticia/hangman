import random
from colorama import Fore, Style

hangman = ['''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

animal = ["C A M E L", "A N T E A T E R", "M A N D R I L L", "M O N G O O S E", "M E E R K A T", "P L A T Y P U S", "P A R R O T", "B U F F A L O", "C O Y O T E", "W H A L E", "P A N D A", "L I Z A R D", "C H I M P A N Z E E", "W E A S E L", "C A N A R Y", "P I G E O N", "G O R I L L A", "B E A V E R", "P O R C U P I N E", "B A D G E R", "B E E T L E", "H E D G E H O G", "P A R A K E E T", "L E M U R", "J A G U A R", "C R O C O D I L E", "A L L I G A T O R"]

country = ["Z I M B A B W E", "P A R A G U A Y", "S I N G A P O R E", "P A L E S T I N E", "T R I N I D A D", "M A C E D O N I A", "A Z E R B A I J A N", "A R G E N T I N A", "I N D O N E S I A", "B E L G I U M", "C R O A T I A", "C A M B O D I A", "G E R M A N Y", "V E N E Z U E L A", "E T H I O P I A", "U Z B E K I S T A N", "G R E E N L A N D", "C Y P R U S", "L E B A N O N", "B A N G L A D E S H", "P H I L I P P I N E S", "P O R T U G A L", "M Y A N M A R", "D E N M A R K", "S W I T Z E R L A N D", "I C E L A N D", "A R M E N I A"]

foods = ["T O A S T", "C A L Z O N E", "P U D D I N G", "B R E A D S T I C K S", "W A F E R S", "C A N T A L O U P E", "C H I C K E N", "N A C H O S", "B L U E B E R R I E S", "A V O C A D O", "H O R S E R A D I S H", "M A C A R O N I", "E N C H I L A D A S", "S C A L L O P S", "R A V I O L I", "R I S O T T O", "T O R T I L L A", "T A Q U I T O S", "C H O W M E I N", "C U P C A K E", "F A J I T A", "P O P C O R N", "C O O K I E S", "P I S T A C H I O", "C R O I S S A N T", "B I R Y A N I", "N O O D L E S"]

five = ["S H A K Y", "C L U M P", "S L A S H", "C L A C K", "S C I O N", "B I G O T", "C R U E L", "S Q U A D", "S H R U G", "C R A Z E", "S A U C E", "S T U N K", "P U L S E", "I N L A Y", "G L E A N", "E D G E D", "H A V O C", "E A V E S", "D A N C E", "S P O R E", "S P I T E", "T R U C E", "E X I S T", "Q U I C K", "D R E A M", "P R O X Y", "S O B E R"]

seven = ["E A R N E S T", "L E A S H E D", "D I S P U T E", "D I S C A R D", "R E T R A C T", "B A L L O O N", "A N Y B O D Y", "P L E A S E D", "G N A R L E D", "P R E P A R E", "F U R T H E R", "R E C O U N T", "H O R I Z O N", "O U T D O O R", "C O N S U L T", "E N V I O U S", "M A N A G E D", "S T U N N E D", "I M P L I E D", "B L A D D E R", "E N L A R G E", "B L A Z I N G", "A N G U I S H", "T I C K I N G", "B U L L I E D", "W H I S K E R", "C A P T I V E"]

ten = ["A S S I M I L A T E", "S O L I D I F I E D", "E X H I L A R A N T", "I N I T I A T I V E", "B I R T H P L A C E", "A N A L O G I C A L", "L A C K L U S T R E", "I M P R O P E R L Y", "L E X I C O N I S T", "N O M I N A L I S T", "P L A Y G R O U N D", "S T E R E O T Y P E", "O R N A M E N T A L", "H A B I L I T A T E", "S U S C E P T I O N", "O R D A I N M E N T", "S Y N T H E S I Z E", "D I S S U A S I V E", "I N S E C U R I T Y", "P A T H O G E N I C", "D I S F I G U R E D", "L U M I N A T I O N", "P A R L I A M E N T", "Y E S T E R N O O N", "T H R O U G H O U T", "I N E V I T A B L E", "I N C A R N A T E D"]


def category_choice():
  category = input('''
Type A for Animal Names
Type B for Country Names
Type C for Food Names
Type D for random 5-letter words
Type E for random 7-letter words
Type F for random 10-letter words\n
''').upper()

  if category == "A":
    chosen = animal
  elif category == "B":
    chosen = country
  elif category == "C":
    chosen = foods
  elif category == "D":
    chosen = five
  elif category == "E":
    chosen = seven
  elif category == "F":
    chosen = ten
  else:
    print("Invalid input! Please select a valid category to play.\n")
    category_choice()
  game(chosen)

def game(words):
  
  # selecting a random word from the chosen list of words, extracting each letter and storing it in a different list, and extracting the number of letters in the word
  word_full = random.choice(words)
  word_full_2 = ""
  word = word_full.split(" ")
  for x in word:
    word_full_2 += x
  
  repeat = [" "] # to check for repeated guesses

  # to print the same number of blanks as the number of letters in the word
  blank = "_"
  blanks = ["_"]
  length = len(word)
  for i in range(0, length-1):
    blanks.append(blank)
  for blnk in blanks:
    print(blnk, end = " ")
  print("\n")
  
  tries_left = 6
  letters = length
  
  while letters > 0 and tries_left > 0:
    
    check = 0  #resets
    
    guess = input("Enter a letter.\n").upper()
    
    if guess in repeat:
      print(Fore.RED + "You have already tried that letter. Try a different one.\n")
      print(Style.RESET_ALL)
      print("\n")
      
    else:
      repeat.append(guess)
      
      for num in range(0,length):
        if word[num] == guess:
          blanks[num] = guess
          letters -= 1
          check = 1

      # if the guess was wrong
      if len(guess) == 1 and check == 0:
        tries_left -= 1
        if tries_left == 5:
          print(hangman[0] + "\n")
        elif tries_left == 4:
          print(hangman[1] + "\n")
        elif tries_left == 3:
          print(hangman[2] + "\n")
        elif tries_left == 2:
          print(hangman[3] + "\n")
        elif tries_left == 1:
          print(hangman[4] + "\n")
        elif tries_left == 0:
          print(hangman[5] + "\n")
          print(Fore.RED + "You lost. The word is " + word_full + "\n")
          print(Style.RESET_ALL)
        if tries_left != 0:
          print(Fore.RED + f"The letter you guessed doesn't exist in the word. You have {tries_left} tries left!\n")
          print(Style.RESET_ALL)
          for letter in blanks:
            print(letter, end=' ')
          print("\n")
          print("\n")

      # if the guess was correct
      elif check == 1:
        print(Fore.GREEN + "The letter you guessed exists in the word!\n")
        print(Style.RESET_ALL)
        for letter in blanks:
          print(letter, end=' ')
        print("\n")
        print("\n")

      # attempt to guess the entire word
      elif len(guess) > 1:
        if guess == word_full_2:
          print(Fore.GREEN + "That is correct! You guessed the word!")
          print(Style.RESET_ALL)
          letters = 0
        else:
          tries_left -= 1
          if tries_left == 5:
            print(hangman[0] + "\n")
          elif tries_left == 4:
            print(hangman[1] + "\n")
          elif tries_left == 3:
            print(hangman[2] + "\n")
          elif tries_left == 2:
            print(hangman[3] + "\n")
          elif tries_left == 1:
            print(hangman[4] + "\n")
          elif tries_left == 0:
            print(hangman[5] + "\n")
            print(Fore.RED + "You lost. The word is " + word_full + "\n")
            print(Style.RESET_ALL)
          if tries_left != 0:
            print(Fore.RED + f"That's not the right word. You have {tries_left} tries left!\n")
            print(Style.RESET_ALL)
            for letter in blanks:
              print(letter, end=' ')
            print("\n")
            print("\n")
          
    if letters == 0:
      print(Fore.GREEN + "You won!\n")
      print(Style.RESET_ALL)
      
  # prompt to play again    
  again = input("Would you like to play again? Type YES or NO\n").upper()
  print("\n")
  
  if again == "YES":
    choice_diff = input("Do you want to choose a different category? Type YES or NO\n").upper()
    print("\n")
    if choice_diff == "YES":
      category_choice()
    elif choice_diff == "NO":
      game(words)
      
  elif again == "NO":
    print("Thanks for playing! This game was made by Maryam <3") # game ends


user_input = input('''
  _                                                   
 | |__    __ _  _ __    __ _  _ __ ___    __ _  _ __  
 | '_ \  / _` || '_ \  / _` || '_ ` _ \  / _` || '_ \ 
 | | | || (_| || | | || (_| || | | | | || (_| || | | |
 |_| |_| \__,_||_| |_| \__, ||_| |_| |_| \__,_||_| |_|
                       |___/                          
                   
Welcome to HANGMAN! 

How to play: You have to guess what\nthe word is, one letter at a time.\nIf you guess a letter that is in\nthe word, it will appear at its\nposition(s). If you guess a letter that\nisn't in the word, the little man will be\none step closer to death.

Type 'PLAY' to start the game.\n
''').upper()
print("\n")

if user_input == "PLAY":
  print("Pick a category")
  category_choice()