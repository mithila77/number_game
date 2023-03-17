import random #for guessing a random number
import sys #for system exit
import time #for calculating the time 
import pygame #for adding music

pygame.mixer.init() #initialization
correct_sound = pygame.mixer.Sound("correct.mp3") #importing the correct sound
incorrect_sound = pygame.mixer.Sound("wrong.mp3") #importing wrong sound

def get_highest_score(): #function body if guessed right then it will open 'highest_score.txt' write the time
    try:
        with open('highest_score.txt', 'r') as f: 
            highest_score = int(f.read())
    except FileNotFoundError:
        highest_score = None      
    return highest_score


def main():
    number = random.randint(1, 100) #for a random number
    guesses = 0 #initial guess set to 0
    #print(number)
    start_time = time.time() #calling the time function to start 

    while True:
        guess = input("Guess the number (between 1 and 100) or enter q to quit: ")
        
        if guess == "q": #condition if user enter 'q' then the application stop
            print("Thank you for participating!")
            sys.exit(0)
        
        highest_score = get_highest_score()
        guess = int(guess)
        guesses += 1
        if guess == number: #checking the random and guessed number are same
            correct_sound.play() #if two number are same then correct sound will be played
            end_time = time.time() #the time will stop
            time_taken = round(end_time - start_time) #subtract start time from end time to calculate how much it took
            
            print(f"You guessed the number in {guesses} guesses in {time_taken} seconds.") #succes message
            if highest_score is None or guesses < highest_score: #checking if user beat the previous score
                highest_score = guesses #if user beat his previous score then file will be rewrite the score and set a new record
                with open('highest_score.txt', 'w') as f:
                    f.write(str(highest_score))
                print(f"Congratulations! You set a new high score!")
            else: #if user guessed the right number but did't beat his previous score
                print("The current high score is", highest_score, "guesses.")
            
            break
        
        if guess < number:
            incorrect_sound.play()
            print("Too low. Try again.") #if the guess number is lower than the random number then wrong music will play and the message below will be displayed
        else:
            incorrect_sound.play() #if the guess number is greater than the random number then wrong music will play and the message below will be displayed
            print("Too high. Try again.")

if __name__ == "__main__":
    main() 