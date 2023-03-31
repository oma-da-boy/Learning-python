import pandas as pd
import time as time
request_num = 244

# menu
print("welcome to query quest")
print("=================menu=================")
print("press 1 for - Hardware issues")
print("press 2 for - Software issues")
print("press 3 for - Tech support access")
print("press 4 to exit")

# username
print("enter your username")
username = input()

# selecting and describing problem
valid = False
while valid == False:
    print("enter your number")
    query = int(input())
    correct = False


    if query == 1:
        print("please describe your hardware issue")
        desc = input()
        query_type = ("hardware")
        valid = True
    elif query == 2:
        print("please describe your Software issue")
        desc = input()
        query_type = ("software")
        valid = True

    elif query == 3:
        while correct == False:
            print("please enter admin password")
            password = input()
            if password == ("bingus is awesome"):
                print("welcome tech to support")
                correct = True

                desc = ("empty")

                print("=================admin menu=================")
                print("press 1 to - see how many ticket are open")
                print("press 2 to - open to see how many ticket are closed")
                print("press 3 to - exit")
                admin = input()
                admin_val = False
                while admin_val == False:
                    if admin == 1:
                        print("no ticket open")
                    elif admin == 2:
                        print("10 ticket are closed")
                    elif admin == 3:
                        print("closing")
                        time.sleep(1)
                        exit()
                        admin_val = True
                    else:
                        print("invalid")
            else:
                print("wrong password")
                correct = False
        query_type = ("admin")
        valid = True
    elif query == 4:
        print("closing program")
        valid = True
        time.sleep(1)
        exit()
    else:
        print("invalid input")

# confirming request
print("can u confirm that your issue is", desc, "y/n")
ans = input()
val_ans = False
while val_ans == False:
    if ans == "Y" or "y":
        request_num = request_num + 1
        print("your requst number is", request_num)
        print("we will try our best to get back to you")
        val_ans = True
    elif ans == "N" or "n":
        print("please restart \n closing program")

        val_ans = True
        time.sleep(1)
        exit()
    else:
        print("invalid input")

ticket = {
"name": ["", username],
"query": ["", query_type],
"request number":["",request_num]
}
ticket_dis = pd.DataFrame(ticket)
print()
print(ticket_dis)