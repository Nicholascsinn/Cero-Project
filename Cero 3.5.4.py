###List of STUFF TO DO!###

#1. Attempt to make pygmae
#2. Keep on doing bussiess with other coders and add their promgrams in
#3. Debug EVERYTHNG
#4.Double Check the Command Insert
#5.Type up the pitch
#6. 
#
#
#9.

###Things I am dong
#3-D Printing & Digital Design
#Biotech
#Mobile Game Design
#Arduino Bots
#List of Imports 
import time
import sys

import datetime

from turtle import *
from datetime import datetime
from random import randint
import random
from turtle import Screen, Turtle, mainloop
from time import clock, sleep
#Intro Start 
def mn_eck(p, ne,sz):
    
    turtlelist = [p]
    #create ne-1 additional turtles
    for i in range(1,ne):
        q = p.clone()
        q.rt(360.0/ne)
        turtlelist.append(q)
        p = q
    for i in range(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        # let those ne turtles make a step
        # in parallel:
        for t in turtlelist:
            t.rt(360./ne)
            t.pencolor(1-c,0,c)
            t.fd(sz)


def main():
    s = Screen()
    s.bgcolor("gray") #background color
    p=Turtle()
    p.speed(0)
    p.hideturtle()
    p.pencolor("red") #Turtle Color?
    p.pensize(3)

    s.tracer(36,0)

    at = clock()
    mn_eck(p, 36, 19)
    et = clock()
    z1 = et-at

    sleep(1)

    at = clock()
    while any([t.undobufferentries() for t in
    s.turtles()]):
        for t in s.turtles():
            t.undo()
    et = clock()
    import turtle

    a=turtle.Turtle()
    a.penup()
    a.goto(-208, -4)
    a.write("Welcome to NV's  Joint Cero Python Project", font=("New Times Roman", 20, "normal"))#Makes the words for welcome statement
    a.pendown()



if __name__ == '__main__':
    msg = main()
#Intro End    


#Siri Program Start...
print ("Hi I am Cero enter Command Insert to see all promgrams")
a = " "
running = True
while running:#DON'T TOUCH THIS MARIO! AMD VIRAAJ AND NICHOLAS
    a = input ("Ask me a question or insert a command:")
##############################################################################Jokes 1A##############################################################################################################################################################################

    if a=="Hi" or a== "hi":
        print ("Hi Parents, Students, Teacher and AI!")#@@@
    elif a==("Is John Snow Dead?"):#@@@
        print("Dead is Dead or is it What is dead may never die? No Wait! death is so terribly final? I give up!")
##############################################################################Gumble Game##############################################################################################################################################################################

    elif a == ("ghumble Game"):
        print ("Keep score on a peice of paper")
        print ("aaa to quit")
        import random
        from random import shuffle
        anagrams = ["Fish","Banana","Triangle","Broccoli","Nerd","Python","Fiddle","Anagrams","Disney","Marble","Rock","Noodle","Hat","Cat","Adult","Pencil","Large","Kid","Hot", "Butt"
                   "Rodger","Slug","Hollister","Danger", "Jelly","Doughnut","Snake","Technology","Innovation","Marvelous","Killer Kylie "]


        #Start game's loop
        run_word = True
        while (run_word == True):
             
            Choice_Random = random.randint(0,len(anagrams))
            word_puller = anagrams[Choice_Random]
            shuff_ler = list(word_puller)
            shuffle(shuff_ler)
            shuffled_word = ''.join(shuff_ler)
            print ("The shuffled word is "+shuffled_word)
            guess = input("Guess the word: ")
            correct_guess = False
            while not correct_guess:
                if guess == word_puller:
                    print ("Correct +1")
                    correct_guess = True
                    
                elif guess == ("aaa"):
                    run_word = False
                    break
                else:
                    print ("incorrect -1")
                    guess = input("Guess the word: ")
    elif a==("Command Insert"):

        print("""
        Command Insert
        Hi or hi
        Is John Snow Dead?
        ghumble Game
        Siri, I am your father!
        What's 0 divided by 0
        When is the world going to end?
        Siri I can't take a photo when I am rock climbing
        Stop trying to strap me to your forehead, Ashleigh. It won't work
        "I am naked
        Date Game
        Jpotter
        Forest-Quest
        What is Apple Stocks?
        What is Adobe Stocks?
        What is Ebay Stocks?
        What is Google Stocks?
        What is Microsoft Stocks?
        Weather
        Sports
        Magic Ball 8
        Messages
        Facetime
        Find the Square Root
        Nickname Game
        Calculate the Area of a Triangle
        Convert Kilometers to Miles
        Convert Celsius To Fahrenheit
        Check if a Number is PNZ
        Play Timer
        Check Prime Number
        Check if a Number is Odd or Even
        Check Leap Year
        FLATM
        Find LCM
        FFNUR
        Tech is OMG
        I am sleepy
        How much wood would a woodchuck chuck if a woodchuck could chuck wood?
        What is your favorite movie?
        Make me a sandwich?
        Read me a haiku.
        Do you have any pets?
        Play Math Quiz
        Quit or Quit
        What time is it?
        Play Guessing VM
        Play Number Guess JV
        Play RPG JV
        Play Timer VM
        BOH converter
        Music Box(*)
        Shuffle Deck of Cards
        Display Calendar
        Calculator
        Play Name Game VM
        Play RPG Game
        Play Hogwarts
        Command Insert""")
###############################################################################Joke Start#############################################################################################################################################################################
               
              
            
                                        

    elif a==("Siri, I am your father!"):#@@@
        print("Excuse me while I jump from the maintenance catwalk into the air shaft...and then get sucked into the gas shaft and then cling to a weather vane on the underside of Cloud City...metaphorically") or ("Together, we can rule the universe as Father and Intelligent Assistant!")
    elif a ==("What's 0 divided by 0"):#@@@
        print("Imagine you have 0 cookies and you shared them with zero friends. See? It doesn't make sense. Cookie Monster is sad he has no cookies, and you are sad you have no friends.")
    elif a ==("When is the world going to end?"):#@@@
        print("As long as you keep me charged, we would be just fine")
    elif a ==("Siri I can't take a photo when I am rock climbing"):#@@@
        print("Stop trying to strap me to your forehead, Ashleigh. It won't work")
    elif a == ("I am naked"):#@@@
        print("That is wrong in so many ways, I don't even know where to begin")

################################################################################Forest Quest############################################################################################################################################################################
    elif a == ("Magic Ball 8"):
        
     

        ans = True

        while ans:
            question = input("Ask the magic 8 ball a question: (press enter to quit) ")
            
            answers = random.randint(1,8)
            
            if question == "":
                ans = False
            
            elif answers == 1:
                print ("It is certain")
            
            elif answers == 2:
                print ("Outlook good")
            
            elif answers == 3:
                print ("You may rely on it")
            
            elif answers == 4:
                print ("Ask again later")
            
            elif answers == 5:
                print ("Concentrate and ask again")
            
            elif answers == 6:
                print ("Reply hazy, try again")
            
            elif answers == 7:
                print ("My reply is no")
            
            elif answers == 8:
                print ("My sources say no")
################################################################################Forest Quest############################################################################################################################################################################

    elif a == ("Forest-Quest"):
        #signup page code
        def signup ():
            while (True):
                print ("Welcome to Forest-Quest, a game coded by Kylie R., a.k.a. whyhellothere! Please follow all game instructions. Good luck!")
                user_name = input ("Your username: ")
                player_confirm = input ("Is this information correct? Your username: " + user_name + " ")
                if (player_confirm == "yes"):
                    return user_name
                elif (player_confirm == "Yes"):
                    return user_name

        #game launch code
        def game (user_name):
            player_restart = False
            while (True):
                player_confirm2 = input ("Guide: Hi," + user_name + ", I'm Guide, and I'll be helping you with your Forest-Quest. Are you ready? ")
                if (player_confirm2 == "yes"):
                    pass
                elif (player_confirm2 == "Yes"):
                    pass
                elif (player_confirm2 != "yes" and player_confirm2 != "Yes"):
                    break
                player_weapon = input ("Guide: Which weapon do you prefer- sword or bow? ")
                if (player_weapon == "sword"):
                    pass
                if (player_weapon == "bow"):
                    pass
                weapon_name = input ("Guide: And lastly, what would you like to name your weapon? ")
                weapon_confirm = input ("Guide: Welcome to the Forest, " + user_name + ", master of " + weapon_name + ". (Please type OK to continue) ")
                if (weapon_confirm == "OK"):
                    pass
                elif (weapon_confirm == "ok"):
                    pass
                if (weapon_confirm != "OK" and weapon_confirm != "ok"):
                    break
                #GAME BEGINS HERE
                #CROSSROADS 1
                print ("Guide: Alright. You're ready. First off- there's treasure in the forest. For centuries, Questers have attempted to recover it, only to perish by... well, we don't know. Nobody's ever come back. But I think you can do it! So, it's time for your first choice.")
                left1 = "left"
                right1 = "right"
                guess = str(0)
                while (guess != left1 and guess != right1):
                    guess = input ("Guide: You come to the edge of the forest, and you can take one of two paths- left or right? ") #CROSSROADS ONE
                if (guess == "left"): #GAME PATH A
                    run1 = "run"
                    fight1 = "fight"
                    guess = str (0)
                    while (guess != run1 and guess != fight1): #CROSSROADS 2A
                        guess = input ("Guide: You aren't walking for long when you see a monster in your path. It looks slow, so maybe you can run past it, but remember- you have a weapon. Do you run or fight? ")
                    if (guess == "run"): #user continues the game
                        print ("Guide: You run faster than you've ever run in your life, and you soon lose the monster. Great Job!")
                        climb_over = "climb over"
                        duck_under = "duck under"
                        guess = str (0)
                        while (guess != climb_over and guess != duck_under): #CROSSROADS 3A
                            guess = input ("Soon you come to a wall of thorns. You can choose to attempt to climb over it or duck under it. Climb over or duck under? ") #CROSSROADS THREE
                        if (guess == "climb over"): #user continues the game
                            fight2 = "fight"
                            run2= "run"
                            guess = str (0)
                            while (guess != fight2 and guess != run2): #CROSSROADS 4A
                                guess = input ("You successfully climb over the wall and into a clearing. In the clearing you see a gigantic dragon. it looks fast and strong and mean, but behind the dragon you see a gigantic treasure chest, and a portal out of the forest. You think you'll be able to simply run past the dragon and grab the chest, then get out of there. But you also have " + weapon_name + ". Do you choose to run or fight? ")#CROSSROADS FOUR
                            if (guess == "fight" and player_weapon == "sword"): #USER WINS
                                print ("Guide: Congratulations, " + user_name + "! You beat the dragon with your awesome swordfighting skills and a little bit of luck, and you go home 1,000 gold coins richer!")
                                break
                                #GAME ENDS HERE
                            if (guess == "fight" and player_weapon == "bow"): #user loses
                                print ("You run out of arrows, and the dragon kills you. Sorry, " + user_name + ", you're dead.")
                                restart_confirm = input ("Do you want to restart? Please type yes to try again. Type no to exit. ")
                                if (restart_confirm == "yes"):
                                    player_restart = True
                                elif (restart_confirm == "Yes"):
                                    player_restart = True
                                elif (restart_confirm == "no"):
                                    player_restart = False
                                    break
                                elif (restart_confirm == "No"):
                                    player_restart = False
                                    break
                            if (guess == "run"): #user loses
                                print ("The dragon was even faster than it looked. Sorry, " + user_name + ", you're dead.")
                                restart_confirm = input ("Do you want to restart? Please type yes to try again. Type no to exit. ")
                                if (restart_confirm == "yes"):
                                    player_restart = True
                                elif (restart_confirm == "Yes"):
                                    player_restart = True
                                elif (restart_confirm == "no"):
                                    player_restart = False
                                    break
                                elif (restart_confirm == "No"):
                                    player_restart = False
                                    break
                        if (guess == "duck under"): #user loses
                            print ("Guide: You try to duck under, but are impaled on a thorn, and you die. Sorry, " + user_name + "!")
                            restart_confirm = input ("Do you want to restart? Please type yes to try again. Type no to exit. ")
                            if (restart_confirm == "yes"):
                                player_restart = True
                            elif (restart_confirm == "Yes"):
                                player_restart = True
                            elif (restart_confirm == "no"):
                                player_restart = False
                                break
                            elif (restart_confirm == "No"):
                                player_restart = False
                                break
                    if (guess == "fight"): #user loses
                        print ("Guide: The monster is too strong, and your fighting skills are not enough. You die. Sorry, " + user_name + "!")
                        restart_confirm = input ("Do you want to restart? Please type yes to try again. Type no to exit. ")
                        if (restart_confirm == "yes"):
                            player_restart = True
                        elif (restart_confirm == "Yes"):
                            player_restart = True
                        elif (restart_confirm == "no"):
                            player_restart = False
                            break
                        elif (restart_confirm == "No"):
                            player_restart = False
                            break

                if (guess == "right"):#GAME PATH B
                    run3 = "run"
                    fight3 = "fight"
                    while (guess != run3 and guess != fight3): #CROSSROADS 2B
                        guess = input ("You soon come across a terrifying monster in your path. It looks slow, so maybe you can run past it, but remember- you have a weapon. Do you run or fight? ")
                    if (guess == "fight"):
                        print ("Guide: You fight very well with " + weapon_name + ", and you kill the monster. Great Job!")
                        climb_over = "climb over"
                        duck_under = "duck under"
                        guess = str (0)
                        while (guess != climb_over and guess != duck_under): #CROSSROADS 3B
                            guess = input ("Soon you come to a wall of thorns. You can choose to attempt to climb over it or duck under it. Climb over or duck under? ") #CROSSROADS THREE
                        if (guess == "climb over"): #user continues the game
                            fight2 = "fight"
                            run2= "run"
                            guess = str (0)
                            while (guess != fight2 and guess != run2): #CROSSROADS 4B
                                guess = input ("You successfully climb over the wall and into a clearing. In the clearing you see a gigantic dragon. it looks fast and strong and mean, but behind the dragon you see a gigantic treasure chest, and a portal out of the forest. You think you'll be able to simply run past the dragon and grab the chest, then get out of there. But you also have " + weapon_name + ". Do you choose to run or fight? ")#CROSSROADS FOUR
                            if (guess == "fight" and player_weapon == "bow"): #USER WINS
                                print ("Guide: Congratulations, " + user_name + "! You beat the dragon with your awesome archery skills and a little bit of luck, and you go home 1,000 gold coins richer!")
                                break
                                #GAME ENDS HERE
                            if (guess == "fight" and player_weapon == "sword"): #user loses
                                print ("Your sword is not enough to kill the dragon, and the dragon kills you. Sorry, " + user_name + ", you're dead.")
                                restart_confirm = input ("Do you want to restart? Please type yes to try again. Type no to exit. ")
                                if (restart_confirm == "yes"):
                                    player_restart = True
                                elif (restart_confirm == "Yes"):
                                    player_restart = True
                                elif (restart_confirm == "no"):
                                    player_restart = False
                                    break
                                elif (restart_confirm == "No"):
                                    player_restart = False
                                    break
                            if (guess == "run"): #user loses
                                print ("The dragon was even faster than it looked. Sorry, " + user_name + ", you're dead.")
                                restart_confirm = input ("Do you want to restart? Please type yes to try again. Type no to exit. ")
                                if (restart_confirm == "yes"):
                                    player_restart = True
                                elif (restart_confirm == "Yes"):
                                    player_restart = True
                                elif (restart_confirm == "no"):
                                    player_restart = False
                                    break
                                elif (restart_confirm == "No"):
                                    player_restart = False
                                    break
                        if (guess == "duck under"): #user loses
                            print ("Guide: You try to duck under, but are impaled on a thorn, and you die. Sorry, " + user_name + "!")
                            restart_confirm = input ("Do you want to restart? Please type yes to try again. Type no to exit. ")
                            if (restart_confirm == "yes"):
                                player_restart = True
                            elif (restart_confirm == "Yes"):
                                player_restart = True
                            elif (restart_confirm == "no"):
                                player_restart = False
                                break
                            elif (restart_confirm == "No"):
                                player_restart = False
                                break
                    if (guess == "run"): #user loses
                        print ("Guide: The monster is too fast for you, and it soon catches you. You die. Sorry, " + user_name + "!")
                        restart_confirm = input ("Do you want to restart? Please type yes to try again. Type no to exit. ")
                        if (restart_confirm == "yes"):
                            player_restart = True
                        elif (restart_confirm == "Yes"):
                            player_restart = True
                        elif (restart_confirm == "no"):
                            player_restart = False
                            break
                        elif (restart_confirm == "No"):
                            player_restart = False
                            break
                        
            if player_restart:
                signup ()
                game (user_name)

        user_name = signup ()
        game (user_name)
###########################################################################Tech is OMG#################################################################################################################################################################################
    elif  a == ("Tech is OMG"):
                print("Answer yes or no")
                fj = "Incorrect!"
                gh = "Correct!"

                b = input("Are We Cool?")
                if b == ("yes"):
                    print(gh)
                else:
                        print(fj)
                c = input("Are the instructors helpful?")
                if c == ("yes"):
                    print(gh)
                else:
                        print(fj)
                        
                d = input("Do you always get to go to all exhibits in the tech museum?")
                if d == ("no"):
                    print(gh)
                else:
                        print(fj)
                        
                e = input("Did Python have the best costume on Wednesday?")
                if e == ("yes"):
                    print(gh)
                else:
                        print(fj)
                        
                f = input("Are these computers the best in the world?")
                if f == ("no"):
                    print(gh)
                else:
                        print(fj)
                g = input("Is turtle better than pygame?")
                if g == ("no"):
                    print(gh)
                else:
                    print(fj)
                h = input("Is Siri cool?")
                if h == ("yes"):
                    print(gh)
                else:
                        print(fj)
                j = input("Are our AIs awesome?")
                if j == ("yes"):
                    print(gh)
                else:
                        print(fj)
                k = input("Is the meaning of life piles n piles of fat cash?")
                if k == ("yes"):
                    print(gh)
                else:
                        print(fj)
                l = input("Is Danielle's game not rigged?")
                if l == ("no"):
                    print(gh)
                else:
                        print(fj)

        

    

        

        

        



###########################################################################Stocks#################################################################################################################################################################################

    elif a == ("What is Apple Stocks?"):
        print (" ")
    elif a == ("What is Adobe Stocks?"):
        print (" ")
    elif a == ("What is Ebay Stocks?"):
        print (" ")
    elif a == ("What is Google Stocks?"):
        
        print ("703.93")
    elif a == ("What is Microsoft Stocks"):
        print("50.16")
        
###########################################################################Weather#################################################################################################################################################################################

    elif a == ("Weather"):
        print ("""
Partly Cloudy
77°F | °C
Precipitation: 0%
Humidity: 61%
Wind: 15 mph
TemperaturePrecipitationWind""")

###########################################################################Sports#################################################################################################################################################################################

    elif a == ("Sports"):
        
            iiii = input ("Sport?")
            
            oooo = input ("National Basketball Association (NBA) NBA Development League (NBADL) American Basketball Association (ABA) American Basketball League (ABL) American Professional Basketball League (APBL) Central Basketball Association (CBA) Eastern Basketball Alliance (EBA) Florida Basketball Association Independent Basketball Association (IBA) International Basketball League (IBL) Midwest Basketball League (MBL) Midwest Professional Basketball Association (MPBA) Premier Basketball League (PBL) Tobacco Road Basketball League (TRBL) United Basketball League (UBL) Universal Basketball Association (UBA)")
            yyyy = input ("Team?")
            print ("I am ashamed to say this but the Warriors Lost")
###########################################################################Messages#################################################################################################################################################################################

    elif a == ("Messages"):
            kkkk = input ("Person to Message?")
            uuuu = input ("Message?")
            print ("Message Sent to" + " " + kkkk)
###########################################################################FaceTime#################################################################################################################################################################################

    elif a == ("Facetime"):
            kjdf = input ("Person to Facetime?")
            print ("ERROR this is not a MAC! Facetime option is not available ")
    
            
###########################################################################Find the Square Root#################################################################################################################################################################################

    elif a == ("Find the Square Root"):
            num = float(input('Enter a number: '))
            num_sqrt = num ** 0.5
            print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
###########################################################################Calculate the Area of a Triangle"s#################################################################################################################################################################################

    elif a == ("Calculate the Area of a Triangle"):
            a = int(input("Enter first side: "))
            b = int(input("Enter second side: "))
            c = int(input("Enter third side: "))

            # calculate the semi-perimeter
            s = int((a + b + c) / 2)###Find out how to divide###

            # calculate the area
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
            print('The area of the triangle is %0.2f' %area)
###########################################################################Convert Kilometers to Miles#################################################################################################################################################################################

    elif a == ("Convert Kilometers to Miles"):
            kilometers = float(input('How many kilometers?: '))

            # conversion factor
            conv_fac = 0.621371

            # calculate miles
            miles = kilometers * conv_fac
            print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))
###########################################################################CConvert Celsuis To Fahrenheit#################################################################################################################################################################################

    elif a == ("Convert Celsius To Fahrenheit"):
            celsius = float(input('Enter degree Celsius: '))

            # calculate fahrenheit
            fahrenheit = (celsius * 1.8) + 32
            print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
###########################################################################Check if a Number is PNZ#################################################################################################################################################################################

    elif a == (" Check if a Number is PNZ"):
            print (" PNZ = Postive, Negative, Zero")
            num = float(input("Enter a number: "))
            if num > 0:
               print("Positive number")
            elif num == 0:
               print("Zero")
            else:
               print("Negative number")
###########################################################################Check Prime#################################################################################################################################################################################

    elif a == ("Check Prime Number"):
            # take input from the user
            num = int(input("Enter a number: "))

            # prime numbers are greater than 1
            if num > 1:
               # check for factors
               for i in range(2,num):
                   if (num % i) == 0:
                       print(num,"is not a prime number")
                       print(i,"times",num//i,"is",num)
                       break
               else:
                   print(num,"is a prime number")
                   
            # if input number is less than
            # or equal to 1, it is not prime
            else:
               print(num,"is not a prime number") 

###########################################################################Timer NV Version#################################################################################################################################################################################

    elif a ==("Play Timer"):
            k= input ("Please insert the number to countdown from:")
            seconds = float(k)*60
            while seconds > 0:
                time.sleep(1)
                print(seconds)
                seconds-=1
###########################################################################Check if a Number is Odd or Even#################################################################################################################################################################################

    elif a == ("Check if a Number is Odd or Even"):
            num = int(input("Enter a number: "))
            if (num % 2) == 0:
               print("{0} is Even".format(num))
            else:
               print("{0} is Odd".format(num))
###########################################################################Check Leap Year#################################################################################################################################################################################

    elif a == ("Check Leap Year"):
        
            year = int(input("Enter a year: "))
            if (year % 4) == 0:
               if (year % 100) == 0:
                   if (year % 400) == 0:
                       print("{0} is a leap year".format(year))
                   else:
                       print("{0} is not a leap year".format(year))
               else:
                   print("{0} is a leap year".format(year))
            else:
               print("{0} is not a leap year".format(year))
###########################################################################Program to Find the Largest Among Three Numbers#################################################################################################################################################################################

    elif a ==("FLATM"):
        print ("Program to Find the Largest Among Three Numbers")
        # Python program to find the largest number among the three input numbers

        # take three numbers from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))

        if (num1 > num2) and (num1 > num3):
           largest = num1
        elif (num2 > num1) and (num2 > num3):
           largest = num2
        else:
           largest = num3

        print("The largest number is",largest)
###########################################################################Fine LCM#################################################################################################################################################################################

    elif a == ("Find LCM"):
        # Python Program to find the L.C.M. of two input number

        # define a function
        def lcm(x, y):
           """This function takes two
           integers and returns the L.C.M."""

           # choose the greater number
           if x > y:
               greater = x
           else:
               greater = y

           while(True):
               if((greater % x == 0) and (greater % y == 0)):
                   lcm = greater
                   break
               greater += 1

           return lcm


        # take input from the user
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))    
###########################################################################Program to Find Factorial of Number Using Recursion#################################################################################################################################################################################

    elif a ==("FFNUR"):
        print ("Program to Find Factorial of Number Using Recursion")
        def recur_factorial(n):
           """Function to return the factorial
           of a number using recursion"""
           if n == 1:
               return n
           else:
               return n*recur_factorial(n-1)


        # take input from the user
        num = int(input("Enter a number: "))

        # check is the number is negative
        if num < 0:
           print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
           print("The factorial of 0 is 1")
        else:
           print("The factorial of",num,"is",recur_factorial(num))
#######################################################################################NV Joke 2#####################################################################################################################################################################

    elif a == ("I am sleepy"):
        print("Listen to me. But down this iPhone right now and take a nap. I'll wait here.")
    elif a == ("How much wood would a woodchuck chuck if a woodchuck could chuck wood?"):
        print ("An Apple spokesperson declined to comment")
   
    elif a == ("What is your favorite movie?"):
        print("I have heard that Blade Runner is a very realistic and sensitive depiction of intelligent assistants")
    elif a == ("Make me a sandwich?"):
        print("I am not permitted to make food.")
    elif a == ("Read me a haiku."):
        print("I will give it a try,/ although I would rather tell you/ if it is raining out")
    elif a == ("Do you have any pets?"):
        print("I used to have an Albo. But it turned on me")
####################################################################################Math Quiz########################################################################################################################################################################

    elif a == ("Play Math Quiz"):
        secret = random.randint(1, 99)
        guess = 0
        tries = 0
        print("Welcome to NV's Math QUIZ")
        print ("10*25")
        answer = 250 or 00
        guess = 0
        tries = 0
        while guess != answer and tries < 3: #while guess does not eual the answer  and tries less than3
            guess = int(input("What is the evaluation?")) #what is the guess of the question
            if guess < answer:   
                print ("Too low!")
            elif guess > answer:
                print ("Too high!")

            tries = tries + 1
        if guess == answer:
            print ("Correct!")
        else:
            print ("Incorrect!")

        print ("30*120")
        answer = 3600 or 00
        guess = 0
        tries = 0
        while guess != answer and tries < 3: #while guess does not eual the answer  and tries less than3
            guess = int(input("What is the evaluation?")) #what is the guess of the question
            if guess < answer:   
                print ("Too low!")
            elif guess > answer:
                print ("Too high!")

            tries = tries + 1
        if guess == answer:
            print ("Correct!")
        else:
            print ("Incorrect!")

        print ("932*232")
        answer = 216224
        guess = 0
        tries = 0
        while guess != answer and tries < 3: #while guess does not eual the answer  and tries less than3
            guess = int(input("What is the evaluation?")) #what is the guess of the question
            if guess < answer:   
                print ("Too low!")
            elif guess > answer:
                print ("Too high!")

            tries = tries + 1
        if guess == answer:
            print ("Correct!")
        else:
            print ("Incorrect!")
        print ("12/3 * 45 + 23.32 / 2")
        answer = 191.66 or 00
        guess = 0
        tries = 0
        while guess != answer and tries < 3: #while guess does not eual the answer  and tries less than3
            guess = int(input("What is the evaluation?")) #what is the guess of the question
            if guess < answer:   
                print ("Too low!")
            elif guess > answer:
                print ("Too high!")

            tries = tries + 1
        if guess == answer:
            print ("Correct!")
        else:
            print ("Incorrect!")
        print ("x = 9 ~~~ 4/x / 5 * 8 + 42.32 / 4")
        answer = 11.2911111 or aw
        guess = 0
        tries = 0
        while guess != answer and tries < 3: #while guess does not eual the answer  and tries less than3
            guess = int(input("What is the evaluation?")) #what is the guess of the question
            if guess < answer:   
                print ("Too low!")
            elif guess > answer:
                print ("Too high!")

            tries = tries + 1
        if guess == answer:
            print ("Correct!")
        else:
            print ("Incorrect!")

        print ("x = 21 y = 93 z = 43 ~~~ x/34 + 5/y * z/342 + 254 / 373 * 34/x ")
        answer = 1.72692179 or aw 
        guess = 0
        tries = 0
        while guess != answer and tries < 3: #while guess does not eual the answer  and tries less than3
            guess = int(input("What is the evaluation?")) #what is the guess of the question
            if guess < answer:   
                print ("Too low!")
            elif guess > answer:
                print ("Too high!")

            tries = tries + 1
        if guess == answer:
            print ("Correct!")
        else:
            print ("Incorrect!")
        print ("2 − 3 − 1 − 2")
        answer = -12 or 00 
        guess = 0
        tries = 0
        while guess != answer and tries < 3: #while guess does not eual the answer  and tries less than3
            guess = int(input("What is the evaluation?")) #what is the guess of the question
            if guess < answer:   
                print ("Too low!")
            elif guess > answer:
                print ("Too high!")

            tries = tries + 1
        if guess == answer:
            print ("Correct!")
        else:
            print ("Incorrect!")
        print ("tan(253/(|(599-log(34)^31)|))*10323257277.998704940572409110325 ")
        answer = 83339 or 00 
        guess = 0
        tries = 0
        while guess != answer and tries < 3: #while guess does not eual the answer  and tries less than3
            guess = int(input("What is the evaluation?")) #what is the guess of the question
            if guess < answer:   
                print ("Too low!")
            elif guess > answer:
                print ("Too high!")

            tries = tries + 1
        if guess == answer:
            print ("Correct!")
        else:
            print ("Incorrect!")
    elif a == ("Play Guessing Game"):
            secret = random.randint(1,99)
            guess = 0
            tries = 0
            print ("This is a guess the number game! I've picked a number between 0 and 999. You've got to guess it. I'll reply more or less. ")
            while guess != secret and tries < 99:
                try:
                    guess = int(input(" Your Guess?"))
                except:
                    print("Sorry, not a number")
                if guess < secret :
                    print (" More") 
                elif guess > secret:
                    print ("Less")
                elif guess == str:
                    print("You Lose")
                tries = tries + 1
                if guess == secret:
                    print ("You win! Your prize is... a great job!")


######################################################################################### Credits ###################################################################################################################################################################

    elif a == ("quit") or a == ("Quit"):
            print("""Credits: NV Cero Project wish to give credit to the fellowing programmers
             Director: Nicholas Sinn
             Director : Viraaj

             ~~~~~~~

             Debugging Team : Mr. Evan The AI, (Scott, Shan, Kassandra, and
             Dylan )Aditya, Michaelle, Matei, and Danielle

             ~~~~~~~

             Game Designer Team:

             Viraaj/Nicholas: Siri Jokes
             Danielle : RPG Game D version
             Nicholas : Timer
             Viraaj :   Guessing Game
             Kassandra : Math Quiz
             Nicholas : Math Quiz
             Michelle : Harry Potter Sorting Hat game
             Nicholas : Real Time Clock
             Turtle Team : Real Time Clock
             Joseph :RPG J Version
             Joseph : Number Guessing Game Version J
             Joseph : In fogetter
             Ryan : Date CalculationProgram
             Matei : Time Countdown Version M
             Matei : Guess Version M
             Matei : Name Generator
             Matei : RPG Version M
             Kylie : Forest-Quest
             Jamaya : Gumble Game
             Viraaj : True or False Tech
             Nicholas :Stocks
             Virraj : Rock paper Scissors
             Nicholas :Weather
             Nicholas :Sports
             Nicholas :Messages
             Nicholas :Facetime
             Jospeh : Music Box
             Nicholas :Find the Square Root
             Nicholas :Calculate the Area of a Triangle
             Nicholas :Convert Kilometers to Miles
             Nicholas :Convert Celsius To Fahrenheit
             Nicholas :Check if a Number is PNZ
             Nicholas :Check Prime Number
             Nicholas :Check if a Number is Odd or Even
             Nicholas :Check Leap Year
             Nicholas :FLATM
             Nicholas :Find LCM
             Nicholas :FFNUR
             Nicholas :BOH converter
             Nicholas :Shuffle Deck of Cards
             Nicholas :Display Calendar
             Nicholas :Calculator
             
             
             

             ~~~~~~~~

             Soures:
             Siri:
             http://www.macworld.co.uk/feature/iosapps/60-funny-things-ask-siri-on-ios-2016-mac-3633686/
             http://www.cheatsheet.com/gear-style/20-questions-to-ask-siri-for-a-hilarious-response.html/?a=viewall

             ~~~~~~~~

             Special Thanks to:
             Kassandra for sitting down with us for 30 min just to help us
             Evan for being such a WOW! teacher
             Virraj for being a great bud and coder
             Danielle for being an awesome friend
             Manav for being a amesome debugger and friend!
             Michelle: For always smiling and being a amesome helper and friend

             And most of all

             For all the Staff for making this week at camp "Jolly" and Merry

             This will not be a farewell so me and the team wll see you soon!

            

             \(^-^)/

            
             
             """)
             
             
             
             
             
             
             

            
   
             
            running = False
#################################################################################Real Time Clock ###########################################################################################################################################################################

    elif a == ("What time is it?"):
            from turtle import *
            from datetime import datetime

            def jump(distanz, winkel=0):
                penup()
                right(winkel)
                forward(distanz)
                left(winkel)
                pendown()

            def hand(laenge, spitze):
                fd(laenge*1.15)
                rt(90)
                fd(spitze/2.0)
                lt(120)
                fd(spitze)
                lt(120)
                fd(spitze)
                lt(120)
                fd(spitze/2.0)

            def make_hand_shape(name, laenge, spitze):
                reset()
                jump(-laenge*0.15)
                begin_poly()
                hand(laenge, spitze)
                end_poly()
                hand_form = get_poly()
                register_shape(name, hand_form)

            def clockface(radius):
                reset()
                pensize(7)
                for i in range(60):
                    jump(radius)
                    if i % 5 == 0:
                        fd(25)
                        jump(-radius-25)
                    else:
                        dot(3)
                        jump(-radius)
                    rt(6)

            def setup():
                global second_hand, minute_hand, hour_hand, writer
                mode("logo")
                make_hand_shape("second_hand", 125, 25)
                make_hand_shape("minute_hand",  130, 25)
                make_hand_shape("hour_hand", 90, 25)
                clockface(160)
                second_hand = Turtle()
                second_hand.shape("second_hand")
                second_hand.color("gray20", "gray80")
                minute_hand = Turtle()
                minute_hand.shape("minute_hand")
                minute_hand.color("blue1", "red1")
                hour_hand = Turtle()
                hour_hand.shape("hour_hand")
                hour_hand.color("blue3", "red3")
                for hand in second_hand, minute_hand, hour_hand:
                    hand.resizemode("user")
                    hand.shapesize(1, 1, 3)
                    hand.speed(0)
                ht()
                writer = Turtle()
                #writer.mode("logo")
                writer.ht()
                writer.pu()
                writer.bk(85)

            def wochentag(t):
                wochentag = ["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday"]
                return wochentag[t.weekday()]

            def datum(z):
                monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
                         "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
                j = z.year
                m = monat[z.month - 1]
                t = z.day
                return "%s %d %d" % (m, t, j)

            def tick():
                t = datetime.today()
                sekunde = t.second + t.microsecond*0.000001
                minute = t.minute + sekunde/60.0
                stunde = t.hour + minute/60.0
                try:
                    tracer(False)  # Terminator can occur here
                    writer.clear()
                    writer.home()
                    writer.forward(65)
                    writer.write(wochentag(t),
                                 align="center", font=("Courier", 14, "bold"))
                    writer.back(150)
                    writer.write(datum(t),
                                 align="center", font=("Courier", 14, "bold"))
                    writer.forward(85)
                    tracer(True)
                    second_hand.setheading(6*sekunde)  # or here
                    minute_hand.setheading(6*minute)
                    hour_hand.setheading(30*stunde)
                    tracer(True)
                    ontimer(tick, 100)
                except Terminator:
                    pass  # turtledemo user pressed STOP

            def main():
                tracer(False)
                setup()
                tracer(True)
                tick()
                return "EVENTLOOP"

            if __name__ == "__main__":
                mode("logo")
                msg = main()
                print(msg)
                mainloop()
##################################################################################Guessing Game Version Matei##########################################################################################################################################################################

    elif a == ("Play Guess VM"):
        rand = str(random.randint(0, 100))
        guess = ""
        guesses = 0
        while(guess != rand):
            guess = input("Guess the number! Your guess: ")
            guesses = (guesses + 1)
            #print("You have guessed " + str(guesses) + " times.")
        print("Congrats, " + guess + " is correct! It took you " + str(guesses) + " guesses.")
##################################################################################Guessing Game Version Joseph##########################################################################################################################################################################

    elif a == (" Play Number Guess JV"):

        running = True
        while running:
            guess = -1
            guessTaken = 0
            answer = random.randint(1, 100)
            print("I am thinking of a number between 1 and 100\n")
            while guess != answer:
                print("Take a guess")
                guess = int(input())
                guessTaken = guessTaken + 1
                if guess > answer:
                    print("Sorry, that is too high\n")
                if guess < answer:
                    print("Sorry, that is too low\n")
                if guess == answer:
                    print("Correct!\n")
                    running = False
                    print("You got the answer in " + str(guessTaken) + " guesses")
                    break
                if guessTaken == 6:
                    print("Sorry, you have used all your attempts\n")
                    print("The answer was " + str(answer))
                    print("\n")
                    break
##################################################################################Guessing Game Version Joseph##########################################################################################################################################################################
    elif a == ("Play RPG JV"):
        while True:
            a = "Joseph"
            print("Hi my name is " + a)
            name = input("What is your name?:")
            print("Hello " + name)
            print("You are going to be entering a cave with two paths")
            answer = input("1 or 2?:")
            if answer == "1":
                print("A dragon jumps out at you and you don't have enough time to defend yourself")
                restart = input("If you would like to restart press r:")
                if restart == "r":
                    continue
                else:
                    break
            if answer == "2":
                print("You find stacks and stacks of gold")
            print("You approach 5 ninjas are you going to run away or attempt to fight them?")
            answer2 = input("Please choose run or fight:")
            if answer2 == "run":
                print("The ninjas don't expect you to run and you are a lot faster")
                print("You find a safe place to sleep for the night")
            if answer2 == "fight":
                print("The ninjas corner you and you do not have a weapon")
                restart = input("If you would like to restart press r:")
                if restart == "r":
                    continue
                else:
                    break
            print("The next morning you find a axe, while you are walking to the axe you see someone approaching you")
            print("The man says he is trustworthy, He asks you if your going to trust him")
            answer3 = input("y/n:")
            if answer3 == "y":
                print("When you go to sleep the man steels your axe and kills you")
                restart = input("If you would like to restart press r:")
                if restart == "r":
                    continue
                else:
                    break
            if answer3 == "n":
                print("The man walks away and you feel that you have said the right thing")
                print("You start a fire and think about what you are going to do today...")
                print("You start to remember what happened before all this started, you were assigned a mission to steal a diamond and bring it to the President")
                print("You feel a bit hungry so decide to go find some food")
                print("You see a tree full of berries, you go and pull some of the berries they look good to eat")
                print("But you are not sure if they are edible, are you going to eat them?")
                answer4 = input("y/n:")
                if answer4 == "y":
                    print("You feel sick and fall to the ground")
                    restart = input("If you would like to restart press r:")
                    if restart == "r":
                        continue
                    else:
                        break
            if answer4 == "n":
                print("You drop the berries and go find something else to eat")
                print("A rabbit runs across your path, you start to run after it")
                print("You use your axe to kill it")
                print("You have a good meal and then take a nap")
                print("In the morning you look at your map and decide you are going to go the final destination where the diamond is stored")
                print("The final destination is the Tech Museum")
                print("Your suprised that the Tech Museum has the diamond")
                print("You start your long journey to the Tech Museum")
                print("After two hours you arrive at the Tech Museum")
                print("You enter the area were the diamond is stored, but there are ten ninjas guarding it")
                print("Before they see you, you start to run")
                print("You think of a plan to defeat the ninjas")
                print("You choke one of the ninjas to death, still nine more to go")
                print("You pull out your breifcase with two guns")
                print("The two guns are the RPG and the MP40")
                gun = input("RPG or MP40:")
                if gun == "RPG":
                    print("Nice Job! All of the ninjas are dead you pick up the diamond")
                    print("You give the diamond to President and you recieve 10,000$")
                if gun == "MP40":
                        print("You take out another ninja, but all the other ninjas notice you and start to charge at you")
                        print("They all corner you and you have no chance of making it out")
                        restart = input("If you would like to restart press r:")
                        if restart == "r":
                            continue
                        else:
                            break
                print("You go back to your house with a lot of money")
                print("You are so happy you accomplished the mission")
                print("You go to the store to buy some food")
                print("Your thinking about what your going to buy")
                print("You decide to buy some chips")
                print("You walk up to the stoorkeeper and he says the bag of chips in 4.99")
                print("You go back to your house and watch a moive")
                print("Suddenly someone knocks on the door")
                print("Are you going to answer to the door or not?")
                door = input("y/n:")
                if door == "y":
                    print("One of your neighbors gives you 100$ for getting the diamond")
                    print("You are so suprised that your neighbor gave you that much money")
                if door  == "n":
                        print("You have just missed out on a prize from your neighbor")
                        print("You feel really bad but you go on with it")
                        print("You continue to watch your moive")
                print("In the morning you decide to take a walk to the park")
                print("On the way there a theif asks you for all the money you won for getting the diamond")
                print("You reply with the answer no, but he pulls out a knife says he will kill you if you don't give him the money")
                print("Are you going to try to steal the knife")
                print("Or are you going to run")
                answer5 = input("run or steal the knife:")
                if answer5 == "run":
                        print("You run away unharmed, but the theif steals your wallet witch luckily does not contain much money")
                        print("Your sad you lost the money, but it was only 20$")
                        print("You decide to keep your money very safe so no one will steal it")
                        print("You sprawl onto your bed and start to sleep")
                        print("...5 years later you recieve a call from the President")
                        print("He says you have a mission to find out if there is life on mars")
                        print("TO BE CONTINUED!")
                        print("Thank you for playing Mission Alert")
                        restart = input("If you would like to restart press r:")
                        if restart == "r":
                            continue
                        else:
                            break
                if answer5 == "steal the knife":
                        print("You steal knife, but the theif cuts your hand")
                        print("The theif starts to run away")
                        print("No money was stoled, but you are seriously cut so you call 911")
                        print("You walk out of the hospital knowing that your hand is severly cut")
                        print("You decide to keep your money very safe so no one will steal it")
                        print("You sprawl onto your bed and start to sleep")
                        print("...5 years later you recieve a call from the President")
                        print("He says you have a mission to find out if there is life on mars")
                        print("TO BE CONTINUED!")
                        print("Thank you for playing Mission Alert")
                        restart = input("If you would like to restart press r:")
                        if restart == "r":
                            continue
                        else:
                            break
                        
                
            

                
                
        
            
            
            
        
        
                   
    
       
    
    

        
        
    


##################################################################################Timer Version Matei##########################################################################################################################################################################



    elif a == ("Play Timer VM"):
        print("Welcome to the timer!\n")
        t = 0 #the variable for time in seconds
        while (t >= 0):
            d = int(input("Please type in amount of days to time: "))
            h = int(input("Please type in amount of hours to time: "))
            m = int(input("Please type in amount of minutes to time: "))
            s = int(input("Please type in mount of seconds to time: "))
            t = d*86400 + h*3600 + m*60 + s #calculates time inseconds
            while t > 0:
                seconds = (int(t%60))
                minutes = (int(((t-t%60)/60))%60)
                hours = (int((t-t%3600)/3600)%24)
                days = (int((t-t%86400)/86400))
                dd = " days  " #text shown for days/hrs/mins/secs
                hh = " hours  "
                mm = " minutes  "
                ss = " seconds"
                if days == 1: #singular text change
                    dd = " day  "
                if hours == 1:
                    hh = " hour  "
                if minutes == 1:
                    mm = " minute  "
                if seconds == 1:
                    ss = " second"
                if days == 0 and hours == 0 and minutes == 0:#hides unneeded variables like days if they are 0
                    print(str(seconds) + ss)
                elif days == 0 and hours == 0:
                    print(str(minutes) + mm + str(seconds) + ss)
                elif days == 0:
                    print(str(hours) + hh + str(minutes) + mm + str(seconds) + ss)
                else:
                    print(str(days) + dd + str(hours) + hh + str(minutes) + mm + str(seconds) + ss)
                t = t - 1
                time.sleep(1)
            print("Timer ended!")
        print("\nThank you for using the timer!\n")
##################################################################################Python Program to Convert Decimal to Binary, Octal and Hexadecimal##########################################################################################################################################################################


    elif a == ("BOH converter"):
        if a == ("BOH converter"):
            running1 = True
        print("This promgram can convert Decimal to Binary, Octal and Hexadecimal")
        dec = int(input("Enter an integer: "))

        print("The decimal value of",dec,"is:")
        print(bin(dec),"in binary.")
        print(oct(dec),"in octal.")
        print(hex(dec),"in hexadecimal.")

        qwq = input ("Quit")
        if qwq == ("Yes"):
                running1 = False
        elif qwq == ("No"):
                running2 = True

##################################################################################Shuffle Deck of Cards##########################################################################################################################################################################

    elif a == ("Shuffle Deck of Cards"):
        # import modules
        import itertools, random

        # make a deck of cards
        deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

        # shuffle the cards
        random.shuffle(deck)

        # draw five cards
        print("You got:")
        for i in range(5):
           print(deck[i][0], "of", deck[i][1])
##################################################################################Display Calendar##########################################################################################################################################################################
                
                
    elif a == ("Display Calendar"):
        import calendar

        # ask of month and year
        yy = int(input("Enter year: "))
        mm = int(input("Enter month: "))

        # display the calendar
        print(calendar.month(yy,mm))
##################################################################################Calculator##########################################################################################################################################################################

    elif a == ("Calculator"):
        # take input from the user
        def add(x, y):
           """This function adds two numbers"""

           return x + y

        def subtract(x, y):
           """This function subtracts two numbers"""

           return x - y

        def multiply(x, y):
           """This function multiplies two numbers"""

           return x * y

        def divide(x, y):
           """This function divides two numbers"""

           return x / y
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        choice = input("Enter choice(1/2/3/4):")

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
           print(num1,"+",num2,"=", add(num1,num2))

        elif choice == '2':
           print(num1,"-",num2,"=", subtract(num1,num2))

        elif choice == '3':
           print(num1,"*",num2,"=", multiply(num1,num2))

        elif choice == '4':
           print(num1,"/",num2,"=", divide(num1,num2))
        else:
           print("Invalid input")
        

        
##################################################################################Name Game Matei##########################################################################################################################################################################

    elif a == ("Play Name Game"):
        print("Please write your name below:")
        name = input("Hello, my name is ")
        if name == "":
            name = "John Doe"
            print("Hello, random person!")
        else:
            print("Hello, " + name + "!")
        print("\nPlease write your age below:")
        age = input("Hi, I'm " + name + " and my age is ")
        if age == "":
            age = "21"
        print("\nPlease write your gender below (male/female):")
        gender = input("Hi, I'm " + name + ", and I am " + age + " years old. I am a ")
        if gender != "male" and gender != "female":
            gender = "hermaphroditic"
        print("\nHello, my name is " + name + ". I am a " + gender + " " + age + " year old.")

    elif a == ("Play Text Game"):
        print("Welcome to the world of text!\n")
        input("Press return/enter to start the adventure...\n\n")
        print("You are walking along a path, when a monster with a slingshot appears.\n")
        input("Press return/enter to continue...\n\n")
        health = 3
        print("The monster is about to shoot you. You get ready to attempt to dodge.\nType R to dodge right or L to dodge left.\nYour health: "+ str(health) +"\n")
        var1 = input("Press return/enter to submit.\n(Type anything else and you WILL be hit by the rock!)\nYour action: ")
        if var1 == "R" or var1 == "r":
            print("\n\nYou dodged the first rock. Good job! Your health: "+str(health)+"!")
        else:
            health = health - 1
            print("You are hit by the rock and lose a health point. Your health: "+ str(health) +"\n")
        input("Press return/enter to continue...\n\n")
        print("The monster is going to shoot again. Once more, you get ready to attempt to dodge.\nType R to dodge right or L to dodge left.\nYour health: "+ str(health) +"\n")
        var1 = input("Press return/enter to submit.\n(Type anything else and you WILL be hit by the rock!)\nYour action: ")
        if var1 == "L" or var1 == "l":
            print("\n\nYou dodged the second rock. Good job! Your health: "+str(health)+"!\nThe monster goes away.")
        else:
            health = health - 1
            print("\n\nYou are hit by the rock and lose a health point. Your health: "+ str(health) +"\nThe monster goes away.")
        input("Press return/enter to continue...\n\n")
        print("You see 5 smoothies. One of them will heal you (it's a Jamba juice), two of them will damage you (they are Pufferfish smoothies), and the other two won't do anything (they are unflavored shaved ices).\nSelect a smoothie to drink by typing 1, 2, 3, 4, or 5.")
        var1 = input("\nPress return/enter to submit.\n(Type anything else and you WILL be forced to drink a pufferfish smoothie!)\nYour action: ")
        if var1 == "2" or var1 == "5":
            print("\n\nYou drink the shaved ice. You're safe! Your health: "+str(health)+"!\n")
        elif var1 == "4":
            health = health + 1
            print("\n\nYou drink the jamba juice and gain a health point! Your health: "+str(health)+"!\n")
        else:
            health = health - 1
            print("\n\nYou drink the poisonous pufferfish smoothie and lose a health point. Your health: "+ str(health) +"\n")
        if health == 0:
            print("Game over: you died, better luck next time!")
        else:
            input("Press return/enter to continue...\n\n")
            print("You keep walking down the path, waiting for something exciting to happen.\n")
            input("Press return/enter to continue...\n\n")
            print("The path splits into two. There is a sign saying danger, but it is unclear to which way it points.\nType R to take the right way or L to take the left way.\nYour health: "+ str(health) +"\n")
            var1 = input("Press return/enter to submit.\n(Type anything else and you WILL be hurt!)\nYour action: ")
            if var1 == "L" or var1 == "l":
                print("\n\nYou take the path. You are safe! Your health: "+str(health)+"!\n")
            else:
                health = health - 1
                print("You take the path and fall into a pit, which scratches you. You lose a health point. Your health: "+ str(health)+"\n")
            if health == 0:
                print("Game over: you died, better luck next time!")
            else:
                input("Press return/enter to continue...\n\n")
                print("You find a banana\n")
                input("Press return/enter to pick it up...\n\n")
                inventory = ["Banana"]
                print("You see a large gorilla blocking your path. You want to pass it.\nType F to feed it the banana.\nType T to throw the banana to the side.\nType S to smack it with the banana.\nYour health: "+ str(health) +"\nYour inventory: " + str(inventory) + "\n")
                var1 = input("Press return/enter to submit.\n(Type anything else and the gorilla will punch you!)\nYour action: ")
                inventory = []
                if var1 == "F" or var1 == "f":
                    print("\n\nYou feed the banana to the gorilla and it falls asleep. You carefully walk over it to pass it. Good job! Your health: "+str(health)+"\n")
                elif var1 == "T" or var1 == "t":
                    print("\n\nYou throw the banana to the side. The gorilla walks over to it, eats it, and it falls asleep. Good job! Your health: "+str(health)+"\n")
                    input("Press return/enter to continue...\n\n")
                    print("You find a golden key in the place where the gorilla was sitting.\n")
                    input("Press return/enter to pick it up...\n\n")
                    inventory.append("Golden Key")
                else:
                    health = health - 1
                    print("You hit the gorilla with your banana. It gets angry and hits you. You lose a health point. Your health: "+ str(health) +"\n")
                input("Press return/enter to continue...\n\n")
                if health == 0:
                    print("Game over: you died, better luck next time!")
                else:
                    print("You see a safe with a keyhole.\nType L to leave it alone.\nType C to crack it with your hands.")
                    if (inventory[0] == "Golden Key"):
                        print("Type U to open it with your key.")
                    print("Your health: "+str(health)+"\nYour inventory: " + str(inventory) + "\n")

##################################################################################Guessing Game Version Danielle##########################################################################################################################################################################

    elif a == ("Play RPG Game"):
            apple = [1]
            donut = [2]
            chisps = [2]
            pie = [3]

            wooden_sword = [1]
            iron_sword = [2]
            bow_and_arrow = [2]

            shop = {'apple':3,'donut':4,'chisps':5,'pie':6,'iron sword':100,'bow and arrow':100}
            inventory = ['wooden sword','apple','apple']

            hp = 10
            lv = 0
            gold = 0
            exp = 0

            monsterHealth = 0
            monsterDamage = 0
            monsterGold = 0

            isWrapped = 0


            def canItHeal(item):
                healingValues = {'apple':2,'donut':3,'chisps':3,'pie':4}
                if item in healingValues:
                    return healingValues[item]
                return -1

            def battleGhoul():
                global monsterHealth
                global monsterDamage
                global monsterGold

                global hp
                global lv
                global exp
                global gold


                #prints all the info about User
                print(" ")
                print("health-"+str(hp))
                print(" ")
                print("level-"+str(lv))
                print(" ")
                print("exp-"+str(exp))
                print(" ")
                print(inventory)
                print(" ")
                
                fleeInspectFight = input("Flee Inventory Inspect Fight ")

                #FLEE
                if fleeInspectFight == '1':

                    #50% chance of fleeing and not fleeing
                    toFleeOrNotToFlee = (randint(1,2))
                    if toFleeOrNotToFlee == 1:
                        input("You fled! You coward.")
                        return
                    else:
                         
                        input("You failed in your fleeing.")
                        
                #INVENTORY       
                if fleeInspectFight == '2':
                    print(inventory)
                    
                    #HEAL OR NO HEAL?
                    toHealOrNotToHeal = input("Do you want to (1)heal or (2)not heal?")

                    #HEAL
                    if toHealOrNotToHeal == '1':
                        
                        #WHICH ITEM?
                        healingItem = input("Which Item do you wish to heal with?(spell it out)")
                        healAmount = canItHeal(healingItem)

                            
                        if healAmount != -1:
                            #IS FOOD AND SPELLED RIGHT.
                            print("You used "+healingItem+".")
                            #takes the item out
                            inventory.pop(inventory.index(healingItem))
                            hp += healAmount
                            
                        else:
                            #IS WEAPON OR SPELLED WRONG
                            print("Silly goose! You either spell horribly or you thought you could eat a sword!")
                            
                    #DON'T HEAL
                    if toHealOrNotToHeal == '2':
                        input("Booorrinnng.")
                        
                #INSPECT    
                if fleeInspectFight == '3':
                    input("health-"+str(monsterHealth)+". The ghoul is shivering slightly. It's either scared or cold or very excited. Or all of the above.")

                #FIGHT
                if fleeInspectFight == '4':
                    if 'iron sword' in inventory:
                        input("You use iron sword! Ghoul takes 5 damage.")
                        monsterHealth -= 5
                    elif 'bow and arrow' in inventory:
                        input("You use bow and arrow! Ghoul takes 5 damage.")
                        monsterHealth -= 5
                    elif 'wooden sword' in inventory:
                        input("You use wooden sword! Ghoul takes 2 damage.")
                        monsterHealth -= 2
                    
                    if monsterHealth <= 0:
                        input("You win! +"+str(monsterGold)+" gold +10 exp")
                        gold += monsterGold
                        exp += 10
                      
                        return
                    
                        
                    
                ghoulAttack = (randint(1,2))
                attackWork = (randint(1,2))

                #GHOSTLY SLAP
                if ghoulAttack == 1:
                    if attackWork == 1:
                        print("Ghoul uses Ghostly Slap! -1 health.")
                        input("Feels transparent.")
                        hp = hp - 1
                        if hp <= 0:
                            return      
                        battleGhoul()
                        
                    elif attackWork == 2:
                        input("Ghoul uses Ghostly Slap!... It doesn't work.")
                        battleGhoul()

                #DISAPPEAR             
                elif ghoulAttack == 2:
                    
                    if attackWork == 1:
                        print("Ghoul uses disappear!...He's gone.")
                        input("You won! +0 gold +0 exp")
                        
                    elif attackWork == 2:
                        input("Ghoul uses disappear!... It doesn't work.")
                        battleGhoul()
                    if hp <= 0:
                        return        
                    if hp > 10:
                        hp = 10   
            def battleSpider():
                global monsterHealth
                global monsterDamage
                global monsterGold

                global hp
                global lv
                global exp
                global gold
                
                global isWrapped


                #prints all the info about User
                print(" ")
                print("health-"+str(hp))
                print(" ")
                print("level-"+str(lv))
                print(" ")
                print("exp-"+str(exp))
                print(" ")
                print(inventory)
                print(" ")


                #Wrapped is a attack that makes you lose a turn.
                if isWrapped == False:

                    print(" ")
                    fleeInspectFight = input("(1)Flee (2)Inventory (3)Inspect (4)Fight")

                    #FLEE
                    if fleeInspectFight == '1':
                        toFleeOrNotToFlee = (randint(1,2))
                        if toFleeOrNotToFlee == 1:
                            input("You fled! You coward.")
                            return
                        else:
                            input("You failed in your fleeing.")

                    #INVENTORY    
                    if fleeInspectFight == '2':
                        print(inventory)
                    
                        #HEAL OR NO HEAL?
                        healOrNoHeal = input("Will you (1)Heal or (2)Not heal?")

                        #HEAL
                        if healOrNoHeal == '1':
                        
                            #WHICH ITEM?
                            healingItem = input("Which Item do you wish to heal with?(Type in the whole word)")
                            healAmount = canItHeal(healingItem)


                            if healAmount != -1 and healingItem in inventory:
                                #IS FOOD AND SPELLED RIGHT
                                print("You used "+healingItem+".")
                                #takes the item out
                                inventory.pop(inventory.index(healingItem))
                                hp += healAmount
                            else:
                                #IS WEAPON OR SPELLED WRONG
                                print("Silly goose! You either spell horribly, you thought you could eat a sword, or that item wasn't even in your inventory!")
                                pass               

                            
                        #DON'T HEAL
                        if healOrNoHeal == '2':
                            input("Booorrinnng.")

                    #INSPECT
                    if fleeInspectFight == '3':
                        input("health-"+str(monsterHealth)+" The spider is very sticky. And webby. It's hard to move around.")

                    #FIGHT
                    if fleeInspectFight == '4':
                        if 'iron sword' in inventory:
                            input("You use iron sword! Giant Spider takes 5 damage.")
                            monsterHealth -= 5
                        elif 'bow and arrow' in inventory:
                            input("You use bow and arrow! Giant Spider takes 5 damage.")
                            monsterHealth -= 5
                        elif 'wooden sword' in inventory:
                            input("You use wooden sword! Giant Spider takes 2 damage.")
                            monsterHealth -= 2
                    
                        if monsterHealth <= 0:
                            input("You win! +"+str(monsterGold)+" gold +15 exp")
                            gold += monsterGold
                            exp += 10
                      
                            return
                else:
                    #IS WRAPPED TRUE
                    input("You're wrapped! You can't do anything this round.")
                    
                isWrapped = False    
                spiderAttack = (randint(1,2))
                attackWork = (randint(1,2))

                #WEB
                if spiderAttack == 1:
                    if attackWork == 1:
                        print("Giant spider uses web! -2 health.")
                        input("Feels Sticky.")
                        hp = hp - 2
                        if hp <= 0:
                            return      
                        battleSpider()
                        
                    elif attackWork == 2:
                        input("Giant spider uses web!...It doesn't work.")
                        battleSpider()

                #WRAP        
                elif spiderAttack == 2:
                    
                    if attackWork == 1:
                        print("Giant spider uses wrap! -2 health.")
                        input("Feels very Sticky.")
                        hp = hp - 2
                        isWrapped = True
                        if hp <= 0:
                            return       
                        battleSpider()
                        
                    elif attackWork == 2:
                        input("Giant spider uses wrap!... It doesn't work.")
                        battleSpider()
                    if hp > 10:
                        hp = 10      


            def game():
                global gold
                global hp
                global lv
                global exp

                #INVENTORY IS FULL
                while len(inventory) > 5:
                    print(" ")
                    print("You are carrying too much!")
                    print (inventory)
                    droppedItem = input("Which one of these items do you wish to drop?(use numbers please)?")
                    while int(droppedItem) > len(inventory):
                        droppedItem = input("Are you trying to break the game? Try again, silly.")
                    input("You dropped the " + inventory.pop(int(droppedItem)-1))

                #decides which option to take        
                Option = randint(0,12)
                
                #NOTHING    
                if Option == 0 or Option == 1 or Option == 2:
                    print(" ")
                    optionZero = input("Nothing happened. Do you wish to check your inventory or keep moving?")
                    if optionZero == '1':
                        print(inventory)
                        print("You have " + str(gold) + " Gold.")
                        input("Your health is at " + str(hp) + ".")

                        #HEAL OR NO HEAL?
                        toHealOrNotToHeal = input("Do you want to (1)heal or (2)not heal?")

                        #HEAL
                        if toHealOrNotToHeal == '1':
                        
                            #WHICH ITEM?
                            healingItem = input("Which Item do you wish to heal with?(spell it out)")
                            healAmount = canItHeal(healingItem)

                            
                            if healAmount != -1:
                                #IS FOOD AND SPELLED RIGHT.
                                print("You used "+healingItem+".")
                                #takes the item out
                                inventory.pop(inventory.index(healingItem))
                                hp += healAmount
                            
                            else:
                                #IS WEAPON OR SPELLED WRONG
                                print("Silly goose! You either spell horribly or you thought you could eat a sword!")
                            
                        #DON'T HEAL
                        elif toHealOrNotToHeal == '2':
                            input("Booorrinnng.")
                    else:
                        pass

                #INN
                elif Option == 3 or Option == 4 or Option == 5:
                    print(" ")
                    optionOne = input("You have encountered a inn! Do you wish to buy something or rest[10 gold]?")

                    #SHOP
                    if optionOne == '1':
                        print("Hello! I'm the inn keeper.")
                        print("apple-$3, donut-$4, chisps-$5, pie-$6, iron sword-$100, bow and arrow-$100")
                        print("You have " + str(gold) + " Gold.")
                        
                        whatYouBuy = input("What do you wish to buy?(Just type in the whole word)")

                        #PRESSES ENTER
                        if whatYouBuy == '':
                            input("So you don't want anything?")


                        #NO MONEY 
                        elif whatYouBuy in shop and gold < shop[whatYouBuy] or whatYouBuy not in shop: 
                            whatYouBuy = input("Sorry, but you can't buy that!")

                        #HAS ZE CASH    
                        else:
                            input("You bought the " + whatYouBuy + ".")
                            gold -= shop[whatYouBuy]
                            inventory.append(whatYouBuy)
                            
                    #REST    
                    if optionOne == '2':
                        if gold < 10:
                            input("You don't have enough money!")
                        else:
                            hp = 10
                            input("Health replenished.")

                #CHEST
                elif Option == 6:
                    chest = (randint(5,10))
                    gold += chest
                    print(" ")
                    print("You found a chest!")
                    input("There was " + str(chest) + " gold inside.")

                #MONEY STOLEN
                elif Option == 7:
                    print(" ")
                    input("Oh no! Someone stole some of your money!")
                    if gold == 0:
                        input("Well, actually, you didn't have any money in the first place.")
                    gold = gold - (randint(1,100))

                #MONSTER ATTACK
                elif Option == 8 or Option == 9 or Option == 10 or Option == 11:
                    
                    monster = (randint(1,3))

                    #GHOUL
                    if monster == 1 or monster == 2:
                        global monsterHealth
                        global monsterDamage
                        global monsterGold
                
                        monsterHealth = 10
                        monsterGold = (randint(1,4))
                        
                        print(" ")
                        print(" ")
                        print("You've encountered a ghoul!")
                        battleGhoul()

                    #GIANT SPIDER   
                    if monster == 2:
                        monsterHealth = 10
                        monsterGold = (randint(3,6))
                        
                        print(" ")
                        print(" ")
                        print("You've encountered a giant spider!")
                        battleSpider()
                        
                #CAVE
                elif Option == 12:
                    print(" ")
                    optionTwelve = input("You found a cave! Do you explore the cave or keep moving?")

                    #EXPLORE
                    if optionTwelve == '1':
                        
                        print("It's dark. You move your hand across the cave wall.")
                        leftOrRight = input("The cave divides into two paths. (1)Left or (2)right?")

                        #1. LEFT
                        if leftOrRight == '1':
                            
                            input("You keep traveling downward.")
                            input("...")
                            input("...")
                            input(".....AHH! You find yourself falling a few feet into dirt. You slide down and find yourself slipping into water.")
                            
                            cavernOrPath = input("You see a cavern in the depths of the water, but also see a path leading out of the water with strange markings etched into it. Do you go into the (1)cavern or follow the (2)path?")

                            #2. CAVERN
                            if cavernOrPath == '1':
                                
                                input("You swim towards the cavern. You hear movement behind you. You turn around and see two sharks following you! They drag you into the cavern.")
                                leftOrRight1 = input("You find yourself draped across rocks. Your vision is blurry, and all you can see is a orange color to your left and a blueish color to your right. Do you go (1)Left or (2)Right?")

                                #3. ORANGE
                                if leftOrRight1 == '1':
                                    print("You stumble toward the orange color. You fall into fire and burn to death.")
                                    hp = 0

                                #3. BLUE.
                                if leftOrRight1 == '2':
                                    print("You stumble toward the blue color. You fall into the water and drown.")
                                    hp = 0

                            #2. PATH
                            elif cavernOrPath == '2':
                                input("You follow the path, the etched symbols glowing. You look down at the symbols. Too bright! Your vision shatters.")
                                input("You find yourself outside. Your pockets feel heavy and you look down. They're filled to the brim with gold! Happy, you keep moving on your way. +20 gold")
                                gold += 20
                                
                                    
                        #1. RIGHT        
                        if leftOrRight == '2':
                            
                            print("You keep traveling downward.")
                            input("...")
                            input("...")
                            input("...")
                            input(".....AHH! You find yourself falling onto sharp rocks.")
                            hp = 0

                    #KEEP MOVING
                    else:
                        pass

                if exp >= 50:
                    lv+=1
                    print(" ")
                    print("You leveled up! You are now level "+str(lv)+"!")
                    exp = 0

                if hp > 10:
                    hp = 10

                if gold < 0:
                    gold = 0
                        
                    
                
            def gameStart():
                print("Legend RPG")
                print(" ")
                print("By Danielle P.")

                Start = input("Press a To Begin.")
                if Start == 'a':
                    input("We live in a land of poor programming... Were everything is randomly generated... And whenever you leave a place you never find it again due to poor programming...")
                    userName = input("Hello, young traveller. I would ramble for a long time except no one wants to read that. What's your name, young adventurer?")
                    input("Ah, you are young, " + userName + ". Travel on, young adventurer. ")
                    input("Instuctions: Use 1,2,3, and 4 to choose the first, second, third, or fouth option. PRESS ENTER TO MOVE ON! Press enter to begin!")
                    while hp > 0:
                       game()
                    print("Game Over.")
            gameStart()
    elif a ==("Credits"):
        

            print("""Credits: NV Cero Project wish to give credit to the fellowing programmers
             Director: Nicholas Sinn
             Director : Viraaj

             ~~~~~~~

             Debugging Team : Mr. Evan The AI, (Scott, Shan, Kassandra, and
             Dylan )Aditya, Michaelle, Matei, and Danielle

             ~~~~~~~

             Game Designer Team:

             Viraaj/Nicholas: Siri Jokes
             Danielle : RPG Game D version
             Nicholas : Timer
             Viraaj :   Guessing Game
             Kassandra : Math Quiz
             Nicholas : Math Quiz
             Michelle : Harry Potter Sorting Hat game
             Nicholas : Real Time Clock
             Turtle Team : Real Time Clock
             Manav : JPotter
             Viraaj : Alien Invaders
             Joseph :RPG J Version
             Joseph : Number Guessing Game Version J
             Joseph : In fogetter
             Ryan : Date CalculationProgram
             Matei : Time Countdown Version M
             Matei : Guess Version M
             Matei : Name Generator
             Matei : RPG Version M
             Kylie : Forest-Quest
             Jamaya : Gumble Game
             Viraaj : True or False Tech
             Jospeh : Music Box
             
             
             
             

             ~~~~~~~~

             Soures:
             Siri:
             http://www.macworld.co.uk/feature/iosapps/60-funny-things-ask-siri-on-ios-2016-mac-3633686/
             http://www.cheatsheet.com/gear-style/20-questions-to-ask-siri-for-a-hilarious-response.html/?a=viewall

             ~~~~~~~~

             Special Thanks to:
             Kassandra for sitting down with us for 30 min just to help us
             Evan for being such a WOW! teacher
             Virraj for being a great bud and coder
             Danielle for being an awesome friend
             Manav for being a amesome debugger and friend!
             Michelle: For always smiling and being a amesome helper and friend

             And most of all

             For all the Staff for making this week at camp "Jolly" and Merry

             This will not be a farewell so me and the team wll see you soon!

            

             \(^-^)/

            
             Note Please type in command "Credits_2" to see the full version. Please note that no plagiarism was commited but the promgram writer himself decided to hold his credits out from the main list

             """)
##################################################################################Guessing Game Version Michelle##########################################################################################################################################################################

    elif a == ("Credits_2"):
        
        ("""
Nicholas:Stocks
Nicholas:Weather
Nicholas:Sports
Nicholas:Messages
Nicholas:Facetime
Nicholas:Find the Square Root
Nicholas:Calculate the Area of a Triangle
Nicholas:Convert Kilometers to Miles
Nicholas:Convert Celsius To Fahrenheit
Nicholas:Check if a Number is PNZ
Nicholas:Check Prime Number
Nicholas:Check if a Number is Odd or Even
Nicholas:Check Leap Year
Nicholas:FLATM
Nicholas:Find LCM
Nicholas:FFNUR
Nicholas:BOH converter
Nicholas:Shuffle Deck of Cards
Nicholas:Display Calendar
Nicholas:Calculator
""")





    
    
##################################################################################Guessing Game Version Michelle##########################################################################################################################################################################

    elif a ==("Play Hogwarts"):
            #Hogwarts House variables
            Gryffindor = 0
            Ravenclaw = 0
            Hufflepuff = 0
            Slytherin = 0
            #Starting Message/first question
            sorting_hat = input("Welcome to the Hogwarts sorting hat program,a program created by Michelle. When entering your answers, do not add a space before your answer. Once you have typed in your answer, press enter. "
                                "If you want to skip a question hit return without entering an answer. To find out what house you belong in, type start.")#introduction
            if sorting_hat != "start":
                print("Please restart program and follow the instructions.")
            else:
               sorting_hat2 = input("If you would rather 1)raft the Grand Canyon please type a "
                                    "2)read a book please type b 3)hang out with friends please type c or 4)be princepal of your school please type d")#first question
            #scoring system   
            if sorting_hat2 == "a":
                Gryffindor = Gryffindor + 1
            if sorting_hat2 == "b":
                Ravenclaw = Ravenclaw + 1
            if sorting_hat2 == "c":
                Hufflepuff = Hufflepuff + 1
            if sorting_hat2 == "d":
                Slytherin = Slytherin + 1
            #second question
            sorting_hat3 = input("If you would want to have the job 1)teacher please type a "
                                 "2)wildlife photographer please type b 3)government official please type c or 4)park manager please type d")
            #scoring system
            if sorting_hat3 == "b":
                Gryffindor = Gryffindor + 1
            if sorting_hat3 == "a":
                Ravenclaw = Ravenclaw + 1
            if sorting_hat3 == "d":
                Hufflepuff = Hufflepuff + 1
            if sorting_hat3 == "c":
                Slytherin = Slytherin + 1
            #third question
            sorting_hat4 = input("If you would rather have 1)the power to give your enimies dettention please type a 2)a library with 1,000 books please type b "
                                 "3)tons of loyal friends please type c or 4)unlimited rides on a terrifying rollercoaster please type d")
            #scoring system
            if sorting_hat4 == "d":
                Gryffindor = Gryffindor + 1
            if sorting_hat4 == "b":
                Ravenclaw = Ravenclaw + 1
            if sorting_hat4 == "c":
                Hufflepuff = Hufflepuff + 1
            if sorting_hat4 == "a":
                Slytherin = Slytherin + 1
            #fourth question
            sorting_hat5 = input("If you think your patronus would be a 1)tiger please type a 2)owl please type b 3)beaver please type c or 4)scorpion please type d")
            #scoring system
            if sorting_hat5 == "a":
                Gryffindor = Gryffindor + 1
            if sorting_hat5 == "b":
                Ravenclaw = Ravenclaw + 1
            if sorting_hat5 == "c":
                Hufflepuff = Hufflepuff + 1
            if sorting_hat5 == "d":
                Slytherin = Slytherin + 1
            #fifth question
            sorting_hat6 = input("If you would rather 1)go ziplining please type a 2)participate in a beach clean up please type b 3)visit a science museum please type c or "
                                 "4)play a prank on your worst enemy please type d")
            #scoring system
            if sorting_hat6 == "a":
                Gryffindor = Gryffindor + 1
            if sorting_hat6 == "c":
                Ravenclaw = Ravenclaw + 1
            if sorting_hat6 == "b":
                Hufflepuff = Hufflepuff + 1
            if sorting_hat6 == "d":
                Slytherin = Slytherin + 1
            #sixth question
            sorting_hat7 = input("Would you enjoy sky-diving? If yes please type y, if no please type n.") 
            if sorting_hat7 == "y":
                Gryffindor = Gryffindor + 1
            #seventh question
            sorting_hat8 = input("Would you rather eat your favorite food or know if aliens exist? If you would rather eat your favorite food please type a, "
                                 "if you would rather know if aliens exist please type b.")
            if sorting_hat8 =="b":
                Ravenclaw = Ravenclaw + 1
            #8th question
            sorting_hat9 = input("Would you wash dishes for 4 hours to earn house points? If yes please type y, if no please type n.")
            if sorting_hat9 == "y":
                Hufflepuff = Hufflepuff + 1
            #ninth question
            sorting_hat10 = input("Would you go without food for 3 days for a chance to be Headmaster for a week? If yes, please type y, if no, please type n.")
            if sorting_hat10 == "y":
                Slytherin = Slytherin + 1
            #tenth question
            sorting_hat11 = input("Would you fight a troll to protect a stray cat? If yes, please type y, if no, please type n.")
            if sorting_hat11 == "y":
                Gryffindor = Gryffindor + 1
            #eleventh question
            sorting_hat12 = input("Would you enjoy doing homework that helps you learn? If yes, please type y, if no, please type n.")
            if sorting_hat12 == "y":
                Ravenclaw = Ravenclaw + 1
            #12th question
            sorting_hat13 = input("Would you spend all weekend helping a friend with homework instead of playing video games? If yes, please type y, if no, please type n.")
            if sorting_hat13 == "n":
                Hufflepuff = Hufflepuff + 1
            #13th question
            sorting_hat14 = input("Would you rather have unlimited amounts of free candy or be able to talk to snakes? If you would rather have unlimited candy, please type a, "
                                  "if you would rather be able to talk to snakes, please type b.")
            if sorting_hat14 == "b":
                Slytherin = Slytherin + 1
            #14th question
            sorting_hat15 = input("If your life's goal is to 1)climb Mt. Everest please type a 2)learn to speak 6 languages fluently please type b 3)spend 500 hours volunteering"
                                  " at an animal shelter please type c or 4)become president of America type d.")
            #scoring system
            if sorting_hat15 == "a":
                Gryffindor = Gryffindor + 1
            if sorting_hat15 == "b":
                Ravenclaw = Ravenclaw + 1
            if sorting_hat15 == "c":
                Hufflepuff = Hufflepuff + 1
            if sorting_hat15 == "d":
                Slytherin = Slytherin + 1
            #15th question
            sorting_hat16 = input("If Voldemort told you to join his cause or he would kill you, you would 1)join and try to cause a rebellion later, please type a "
                                  "2)join only to protect your friends and family, and try to secretly help the Order of the Phoenix whenever possible, please type b"
                                  "3)join and spy on Voldemort for the Order of the Phoenix, please type c, or 4)tell Voldemort that you would rather die, please type d.")
            #scoring system
            if sorting_hat16 == "d":
                Gryffindor = Gryffindor + 1
            if sorting_hat16 == "c":
                Ravenclaw = Ravenclaw + 1
            if sorting_hat16 == "b":
                Hufflepuff = Hufflepuff + 1
            if sorting_hat16 == "a":
                Slytherin = Slytherin + 1
            #message results
            if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
                print("You are a Gryffindor! Gryffindors generally are brave and do not let fear stop them from doing what's right.")
            if Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
                print("You are a Ravenclaw! Ravenclaws are generally extremely intelligent and are constantly pursuing knowledge.")
            if Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
                print("You are a Hufflepuff! Hufflepuffs are generally honest and hardworking, and are extremely loyal to their friends.")
            if Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
                print("You are a Slytherin! Slytherins are generally ambitious, determined, and clever.")
            if Gryffindor == Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
                print("You would do equally well in Gryffindor or Ravenclaw!")
            if Gryffindor > Ravenclaw and Gryffindor == Hufflepuff and Gryffindor > Slytherin:
                print("You would do equally well in Gryffindor or Hufflepuff!")
            if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor == Slytherin:
                print("You would do equally well in Gryffindor or Slytherin!")
            if Ravenclaw > Gryffindor and Ravenclaw == Hufflepuff and Ravenclaw > Slytherin:
                print("You would do equally well in Ravenclaw or Hufflepuff!")
            if Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw == Slytherin:
                print("You would do equally well in Ravenclaw or Slytherin!")
            if Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff == Slytherin:
                print("You would do equally well in Hufflepuff or Slytherin!")
            if Gryffindor == Ravenclaw and Gryffindor == Hufflepuff and Gryffindor > Slytherin:
                print("You would do equally well in Gryffindor, Ravenclaw, or Hufflepuff!")
            if Gryffindor == Ravenclaw and Gryffindor > Hufflepuff and Gryffindor == Slytherin:
                print("You would do equally well in Gryffindor, Ravenclaw, or Slytherin!")
            if Gryffindor > Ravenclaw and Gryffindor == Hufflepuff and Gryffindor == Slytherin:
                print("You would do equally well in Gryffindor, Hufflepuff, or Slytherin.")
            if Ravenclaw > Gryffindor and Ravenclaw == Hufflepuff and Ravenclaw == Slytherin:
                print("You would do equally well in Ravenclaw, Hufflepuff, or Slytherin.")
            if Gryffindor == Ravenclaw and Gryffindor == Hufflepuff and Gryffindor == Slytherin:
                print("You would do equally well in any of the four houses!")
            #exact results
            print("Gryffindor:")
            print(Gryffindor)
            print("Ravenclaw:")
            print(Ravenclaw)
            print("Hufflepuff:")
            print(Hufflepuff)
            print("Slytherin:")
            print(Slytherin)

    else:
        a= ["Sorry I could not get that", "Should I search the web for that?", "Sorry I could not understand", "Wait What?"]
        print (random.choice(a))
#Fine out how to loop....
