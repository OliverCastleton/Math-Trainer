import random
import os
import sys
import fractions
import time
Q1 = ""
x = 0
y = 0
solution = 0
start_time = 0

def main():
    print()
    print()
    print()

    nt = 1
    streak = 10

    def Answer():
        if Q1 == "1" or Q1.lower == "addition": print(x, " + ", y," = ?")
        elif Q1 == "2" or Q1.lower == "subtraction": print(x, " - ", y," = ?")
        elif Q1 == "3" or Q1.lower == "moltiplication": print(x, " x ", y," = ?")
        elif Q1 == "4" or Q1.lower == "division": print(x, " : ", y," = ?")
        response = int(input("Your:answer:  "))
        if response == solution:
            print("Correct!!!")
        else:
            print("Wrong!!!")
            streak = streak - 1

    def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Time Lfapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

            
    #Here the real program starts

    Q1 = input("""What do you want to do:
    1) Addition
    2) Subtraction
    3) Moltiplication
    4) Division \n """)
    if Q1 == "1" or Q1 == "Addition" or Q1 == "addition":
        Q2 = input("""    1) Easy
    2) Medium
    3) Difficult \n """)
        if Q2 == "1" or Q2 ==  "Easy" or Q2 == "easy":
            input("Press Enter to start")
            start_time = time.time()
            while (nt < 11):
                nt = nt + 1 
                x = random.randint(1,100)
                y = random.randint(1,100)
                z = x + y
                solution = z
                Answer()
            print(streak,"/10")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            if streak == 0:
                print("NICE, You answerd to all 10 questions correctly!!!!!")
            main()
        elif Q2 == "2" or Q2 ==  "Medium" or Q2 == "medium":
            input("Press Enter to start")
            start_time = time.time()
            while (nt < 11):
                nt = nt + 1 
                x = random.randint(100,10000)
                y = random.randint(100,10000)
                z = x + y
                solution = z
                Answer()
            print(streak,"/10")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            if streak == 0:
                print("NICE, You answerd to all 10 questions correctly!!!!!")
            main()
        elif Q2 == "3" or Q2 ==  "Difficult" or Q2 == "difficult":
            input("Press Enter to start")
            start_time = time.time()
            while (nt < 11):
                nt = nt + 1 
                x = random.randint(1000,100000)
                y = random.randint(1000,100000)
                z = x + y
                solution = z
                Answer()
            print(streak,"/10")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            if streak == 0:
                print("NICE, You answerd to all 10 questions correctly!!!!!")
            main()
    if Q1 == "2" or Q1 == "Subtraction" or Q1 == "subtraction":
        Q2 = input("""    1) Easy
    2) Medium
    3) Difficult \n """)
        if Q2 == "1" or Q2 ==  "Easy" or Q2 == "easy":
            input("Press Enter to start")
            start_time = time.time()
            while (nt < 11):
                nt = nt + 1 
                x = random.randint(1,100)
                y = random.randint(1,100)
                z = x - y
                solution = z
                Answer()
            print(streak,"/10")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            if streak == 0:
                print("NICE, You answerd to all 10 questions correctly!!!!!")
            main()
        elif Q2 == "2" or Q2 ==  "Medium" or Q2 == "Medium":
            input("Press Enter to start")
            start_time = time.time()
            while (nt < 11):
                nt = nt + 1 
                x = random.randint(100,10000)
                y = random.randint(100,10000)
                z = x - y
                solution = z
                Answer()
            print(streak,"/10")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            if streak == 0:
                print("NICE, You answerd to all 10 questions correctly!!!!!")
            main()
        elif Q2 == "3" or Q2 ==  "Difficult" or Q2 == "difficult":
            input("Press Enter to start")
            start_time = time.time()
            while (nt < 11):
                nt = nt + 1 
                x = random.randint(1000,100000)
                y = random.randint(1000,100000)
                z = x - y
                solution = z
                Answer()
            print(streak,"/10")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            if streak == 0:
                print("NICE, You answerd to all 10 questions correctly!!!!!")
            main()
    if Q1 == "3" or Q1 == "Moltiplication" or Q1 == "moltiplication":
        Q2 = input("""    1) Easy
    2) Medium
    3) Difficult \n """)
        if Q2 == "1" or Q2 ==  "Easy" or Q2 == "easy":
            input("Press Enter to start")
            start_time = time.time()
            while (nt < 11):
                nt = nt + 1 
                x = random.randint(1,15)
                y = random.randint(1,15)
                z = x * y
                solution = z
                Answer()
            print(streak,"/10")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            if streak == 0:
                print("NICE, You answerd to all 10 questions correctly!!!!!")
            main()
        elif Q2 == "2" or Q2 ==  "Medium" or Q2 == "Medium":
            input("Press Enter to start")
            start_time = time.time()
            while (nt < 11):
                nt = nt + 1 
                x = random.randint(15,50)
                y = random.randint(15,50)
                z = x * y
                solution = z
                Answer()
            print(streak,"/10")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            if streak == 0:
                print("NICE, You answerd to all 10 questions correctly!!!!!")
            main()
        elif Q2 == "3" or Q2 ==  "Difficult" or Q2 == "difficult":
            input("Press Enter to start")
            start_time = time.time()
            while (nt < 11):
                nt = nt + 1 
                x = random.randint(50,100)
                y = random.randint(50,100)
                z = x * y
                solution = z
                Answer()
            print(streak,"/10")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            if streak == 0:
                print("NICE, You answerd to all 10 questions correctly!!!!!")
            main()

main()