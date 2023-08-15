
import random
print ("Welcome to Hangman Game")

name = input("What is your name? : ")
print ("\n"+str(name)+ ", Lets Begin the Game ," + "\nStart Guessing...")
print("You will have 10 Turns")

wordlist = ["education", "newspaper", "hospital", "umbrella", "management"]
rand = random.randint(0,5)

word = (wordlist[rand])

guesses = ''

turns = 10

while turns > 0:         
    failed = 0
    print("The Word stands now is :  ", end="")                
    for char in word:
             
        if char in guesses:
            print (char,end=""),    

        else: 
            print ("_",end=""),     
            failed += 1    

    if failed == 0:        
        print ("\n\nCongratulations, You won the Game\n")
        break            
    guess = input("\n\nGuess a Letter for the Word:  ") 

    guesses += guess                    
    if guess not in word:  
 
        turns -= 1        
        print ("\nIncorrect Guess")  
 
        print ("Number of guesses remaining  :  " + str(turns) )
        if turns == 0:           
    
            print ("Sorry! You lost this Game\n")