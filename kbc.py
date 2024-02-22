print("Welcome to KBC!")

print("Here's the Q1.")
print("What is the odd one out, Please type the answer as it is...")
list1 = ["Cat","Dog"]
list2 = ["Tree","Wolf"]
print(list1)
print(list2)
print("\n")
answer1 = input()
if (answer1 == list2[0]):
    print("\n")
    print("Right answer and you have earned ₹\.100!")  
    print("\n")
    print("Here's the Q2.")
    print("What is the odd one out, Please type the answer as it is...")
    list3 = ["Mouse","Keyboard"]
    list4 = ["Speakers","Bottle"]
    print(list3)
    print(list4)
    print("\n")
    answer2 = input()
    if (answer2 == list4[1]):
        print("\n")
        print("Right answer and you have earned ₹\.1000!")  
        print("\n")
        print("Here's the Q3.")
        print("What is the odd one out, Please type the answer as it is...")
        list5 = ["Chair","Pen"]
        list6 = ["Furniture","Table"]
        print(list5)
        print(list6)
        print("\n")
        answer3 = input()
        if (answer3 == list5[1]):
            print("\n")
            print("Right answer and you have earned ₹\.10000!")
            print("\n")
            print("Here's the Q4.")
            print("What is the odd one out, Please type the answer as it is...")
            list7 = ["Home","Apartment"]
            list8 = ["Commercial Complex","Road"]
            print(list7)
            print(list8)
            print("\n")
            answer4 = input()
            if (answer4 == list8[1]):
                print("\n")
                print("Right answer and you have earned ₹\.100000!")  
                print("\n")
                print("Here's the Q5.")
                print("What is the odd one out, Please type the answer as it is...")
                list9 = ["Rose","Air Conditioner"]
                list10 = ["Heater","Fan"]
                print(list9)
                print(list10)
                print("\n")
                answer5 = input()
                if (answer5 == list9[0]):
                    print("\n")
                    print("Right answer and you have earned ₹\.1000000!")
                    print("\n")
                    print("This is the complete end of the game")  
                else:
                    print("\n")
                    print("Wrong Answer and you have earned ₹\.100000!")
            else:
                print("\n")
                print("Wrong Answer and you have earned ₹\.10000!")         
        else:
            print("\n")
            print("Wrong Answer and you have earned ₹\.1000! ")
    else:
        print("\n")
        print("Wrong Answer and you have earned ₹\.100! ")
else:
    print("\n")
    print("Wrong Answer and you have earned ₹\.0! ")

    






















    




