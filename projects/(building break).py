import time as time
import random as ran

# life
lives = 0

# answer messages
yay = r"you did it \( ﾟヮﾟ)/"
oops = r"you got it wrong u lost a life ¯\_(ツ)_/¯"
win = r"☆彡(ノ^ ^)ノ Congratulations ヘ(^ ^ヘ)☆彡"
phrase1 = "Would you like to go through door 1 or 2"
phrase2 = "Would you like to go through door 1, 2 or 3"


# maps
def map1():
    print(r"""

                       you are here
                           |
                           v
                           __ __
                          |__|__|__ __                 
                          |__|__|__|__|__
                          |__|__|__|__|__|


                                    """)


def map2():
    print(r"""\


                                           __ __
                                          |__|__|__ __                 
                                          |__|__|__|__|__
                                          |__|__|__|__|__|
                                                 ^
                                                 | 
                                            you are here


                                                    """)


# life check function
def life_check():
    if lives == 3:
        time.sleep(1.5)
        print("<3 <3 <3")
    elif lives == 2:
        time.sleep(1.5)
        print("<3 <3")
    elif lives == 1:
        time.sleep(1.5)
        print("<3")
    else:
        time.sleep(1.5)
        print("game over ―(x_x)→")
        time.sleep(2.5)
        exit()


# room door numbers
room1 = ran.randint(1, 2)
room2 = ran.randint(1, 2)
room3 = ran.randint(1, 3)
room4 = ran.randint(1, 2)
room5 = ran.randint(1, 2)
room6 = ran.randint(1, 3)
room7 = ran.randint(1, 2)
room8 = ran.randint(1, 2)

# welcoming
print("welcome to Building Break")
print("press s to start or press q to quit")

# start of the game
start = False
while not start:
    ans_start = input()
    if ans_start == "s" or ans_start == "S":
        start = True
        print("starting game")
        print("------game_mode------")
        print("press 1----------Easy")
        print("press 2--------Normal")
        print("press 3----------Hard")
        # Selecting game mode
        mode = False
        while not mode:
            game = input()
            if game == "1":
                lives = 4
                mode = True
            elif game == "2":
                lives = 3
                mode = True
            elif game == "3":
                lives = 1
                mode = True
            else:
                print("invalid input")

        print("You wake up in a dark room. You are stuck in a building and have to get out, but you most rooms has "
              "only 1 right door")

        # View map
        map_ans = False
        while not map_ans:
            print("there is a map on the wall would you like to view it? y/n")
            view_map = input()
            if view_map == "y" or view_map == "Y":
                map1()
                map_ans = True
                time.sleep(2)

            elif view_map == "n" or view_map == "N":
                print("ok")
                map_ans = True

            else:
                print("invalid input")

        # Question 1

        print("room 1")
        print("please input a whole number")
        print("you will be punished for mis-inputs")

        que1 = False
        while not que1:
            if lives == 0:
                break
            room1 = str(room1)
            print(phrase1)
            num1 = input()
            if num1 == room1:
                print(yay)
                que1 = True
            elif num1 != room1:
                print(oops)
                lives = lives - 1
                life_check()
            else:
                print("invalid input")

        # Question 2
        if lives >= 1:
            print("room 2")
            que2 = False
            room2 = str(room2)
            while not que2:
                if lives >= 1:
                    print(phrase1)
                    num2 = input()
                    if num2 == room2:
                        print(yay)
                        que2 = True
                    elif num2 != room2:
                        print(oops)
                        lives = lives - 1
                        life_check()
                    else:
                        print("invalid input")

        # Question 3
        if lives >= 1:
            print("room 3")
            que3 = False
            room3 = str(room3)
            while not que3:
                if lives >= 1:
                    print(phrase2)
                    num3 = input()
                    if num3 == room3:
                        print(yay)
                        que3 = True
                    elif num3 != room3:
                        print(oops)
                        lives = lives - 1
                        life_check()
                    else:
                        print("invalid input")

        # Question 4
        if lives >= 1:
            print("room 4")
            que4 = False
            room4 = str(room4)
            while not que4:
                if lives >= 1:
                    print(phrase1)
                    num4 = input()
                    if num4 == room4:
                        print(yay)
                        que4 = True
                    elif num4 != room4:
                        print(oops)
                        lives = lives - 1
                        life_check()
                    else:
                        print("invalid input")

        # map 2
        if lives >= 1:
            map_ans = False
            while not map_ans:
                print("there is a map on the wall would you like to view it? y/n")
                view_map = input()
                if view_map == "y" or view_map == "Y":
                    map2()
                    map_ans = True
                    time.sleep(2)
                elif view_map == "n" or view_map == "N":
                    print("ok")
                    map_ans = True

                else:
                    print("invalid input")

        # Question 5
        if lives >= 1:
            print("room 5")
            que5 = False
            room5 = str(room5)
            while not que5:
                if lives >= 1:
                    print(phrase1)
                    num5 = input()
                    if num5 == room5:
                        print(yay)
                        que5 = True
                    elif num5 != room5:
                        print(oops)
                        life_check()
                    else:
                        print("invalid input")

        # Question 6
        if lives >= 1:
            print("room 6")
            que6 = False
            room6 = str(room6)
            while not que6:
                if lives >= 1:
                    print(phrase2)
                    num6 = input()
                    if num6 == room6:
                        print(yay)
                        que6 = True
                    elif num6 != room6:
                        print(oops)
                        lives = lives - 1
                        life_check()
                    else:
                        print("invalid input")

        # Question 7
        if lives >= 1:
            print("room 7")
            que7 = False
            room7 = str(room7)
            while not que7:
                if lives >= 1:
                    print(phrase1)
                    num7 = input()
                    if num7 == room7:
                        print(yay)
                        que7 = True
                    elif num7 != room7:
                        print(oops)
                        lives = lives - 1
                        life_check()
                    else:
                        print("invalid input")

        # Question 8
        if lives >= 1:
            print("room 8")
            que8 = False
            room8 = str(room8)
            while not que8:
                if lives >= 1:
                    print(phrase1)
                    num8 = input()
                    if num8 == room8:
                        print(win)
                        que8 = True
                        lives = 0
                    elif num8 != room8:
                        print(oops)
                        lives = lives - 1
                        life_check()
                    else:
                        print("invalid input")

    # quit function
    elif ans_start == "q" or ans_start == "Q":
        print("exiting . . .")
        time.sleep(2)
        exit()
    else:
        print("invalid input")
