from Finals_Project_1 import *
from Finals_Project_2 import *
import os
import time
import sys


print("\n\n\t\t\t\t\t\t╔══════════════════════════════════════════════╗")
print("\n\t\t\t\t\t\t\t\b\bWelcome to My Mini Compiler Program!")
print("\n\t\t\t\t\t\t╚══════════════════════════════════════════════╝")
print("\n\t\t\t\t\tThis is a simple compiler program designed for our finals project.")
time.sleep(1.3)
print("\t\t\t\t\t\b\b\bIt supports basic Input or Output, variables, expressions, conditionals, ")
time.sleep(1.3)
print("\t\t\t\t\t\t\t\b\b\b\bloops, lists, and user-defined functions.")
time.sleep(1.3)
input("\n\t\t\t\t\t\t\t    Shall we start? (Enter)")
os.system('cls')




print("\n\n\n\t\t\t\t\t\t\tInitializing Compiler...")
bar_length = 20  

for progress in range(0, 101, 1): 
    filled = int((progress / 100) * bar_length)
    empty = bar_length - filled

    bar = "\t\t\t\t\t\t\t""[" + "█" * filled + "-" * empty + f"] {progress}%"

        
    sys.stdout.write("\r" + bar)
    sys.stdout.flush()

    time.sleep(0.05)  

print("\n\t\t\t\t\t\t\t  Loading Complete!")
time.sleep(3)
os.system('cls')



def tuloy():
    input("Press Enter to Continue >>>")

def go():
    input("\nPress Enter to Go Back to Menu >>>")

def cls():
    os.system('cls')

def ex():
    print("\n==========================================")
    print("\nA - Factorial")
    print("B - Odd Number Accumulator")
    print("C - Multiplication Table Maker")
    print("D - The Final Countdown")
    print("E - Other Examples of for loop")
    print("X - Exit")
    print("\n==========================================")
    choose = input("Pick a Letter:")
    cls()

    if choose.lower() == 'a':
        code_challenge_5()
        go()
        cls()
        ex()
    elif choose.lower() == 'b':
        code_challenge_7()
        go()
        cls()
        ex()
    elif choose.lower() == 'c':
        code_challenge_8()
        go()
        cls()
        ex()
    elif choose.lower() == 'd':
        code_challenge_9()
        go()
        cls()
        ex()

    elif choose.lower() == 'e':
        des()
        activity12()
        tuloy()
        cls()

        des()
        activity13()
        des()
        tuloy()
        cls()

        des()
        activity14()
        des()
        go()
        cls()
        ex()
        

    elif choose.lower() == 'x':
        topic_4()
    else:
        print("Invalid Input. Please Try Again.")
        time.sleep(3)
        cls()
        ex()

def nestfor():
    print("\n==========================================")
    print("\nA - Nested Loop Triangle of Asterisks ")
    print("B - Nested Loop Triangle of Number")
    print("C - Nested Loop Diamond Pattern")
    print("D - Other Examples for Nested For Loop")
    print("X - Exit")
    print("\n==========================================")

    choose = input("\nChoose a letter:")
    cls()

    if choose.lower() == 'a':
        code_challenge_11()
        go()
        cls()
        nestfor()

    elif choose.lower() == 'b':
        code_challenge_12()
        go()
        cls()
        nestfor()

    elif choose.lower() == 'c':
        activity19()
        go()
        cls()
        nestfor()

    elif choose.lower() == 'd':
        des()
        activity16()
        des()
        tuloy()
        cls()

        des()
        activity17()
        des()
        tuloy()
        cls()

        des()
        activity18()
        des()
        go()
        cls()
        nestfor()

    elif choose.lower() == 'x':
        topic_4()
    
    else:
        print("Invalid Input. Please Try Again.")
        time.sleep(3)
        cls()
        nestfor()

def menu():
    while True:


        print("\t\t\t\t\t\t\t         THE MENU")
        print("\n\t\t\t\t\t  ╔══════════════════════════╦══════════════════════════╗")
        print("\t\t\t\t\t  ║          TOPICS          ║          TOPICS          ║")
        print("\t\t\t\t\t  ╠══════════════════════════╬══════════════════════════╣")
        print("\t\t\t\t\t  ║ A. Printing & Input      ║ F. List & Dictionary     ║")
        print("\t\t\t\t\t  ║                          ║                          ║")
        print("\t\t\t\t\t  ║ B. Assignment & Logical  ║ G. Functions             ║")
        print("\t\t\t\t\t  ║    Operator              ║                          ║")
        print("\t\t\t\t\t  ║                          ║ X. Stop the Program      ║")
        print("\t\t\t\t\t  ║ C. Conditional & Nested  ║                          ║")
        print("\t\t\t\t\t  ║    Statements            ║                          ║")
        print("\t\t\t\t\t  ║                          ║                          ║")
        print("\t\t\t\t\t  ║ D. For and Nested Loop   ║                          ║")
        print("\t\t\t\t\t  ║                          ║                          ║")
        print("\t\t\t\t\t  ║ E. While loop            ║                          ║")
        print("\t\t\t\t\t  ╚══════════════════════════╩══════════════════════════╝")
        choice = input("\n\t\t\t\t\t Hello Visitor!, Pick a Topic or 'x' to exit the program:").lower()
        os.system('cls')

        if choice == 'a':
            topic_1()
            
        elif choice == 'b':
            topic_2()

        elif choice == 'c':
            topic_3()

        elif choice == 'd':
            topic_4()

        elif choice == 'e':
            topic_5()

        elif choice == 'f':
            topic_6()

        elif choice == 'g':
            topic_7()

        elif choice == 'x':
            print("MERRY CHRISTMAS! 🎄")
            time.sleep(1.5)
            print("Even your bugs deserve a holiday break!")
            time.sleep(1.5)
            print("                \b🌟")
            time.sleep(1.5)
            print("                *")
            time.sleep(1.5)
            print("               ***")
            time.sleep(1.5)
            print("              *****")
            time.sleep(1.5)
            print("             *******")
            time.sleep(1.5)
            print("            *********")
            time.sleep(1.5)

            print("           ***********")
            time.sleep(1.5)
            print("          *************")
            time.sleep(1.5)
            print("         ***************")
            time.sleep(1.5)
            print("        *****************")
            time.sleep(1.5)
            print("       *******************")
            time.sleep(1.5)
            print("      *********************")
            time.sleep(1.5)
            print("             |||||||")
            time.sleep(1.5)
            print("             |||||||")
            time.sleep(1.5)

            print()
            print("   Santa checked your code...")
            time.sleep(2)
            print("   He said it's 'NICE' — but your variables are on the naughty list!")
            time.sleep(1.5)
            print("\nTHANK YOU!")
            break        
        else:
            print("\n\t\t\t\t\t\t  Invalid Input. Please Try Again.")
            time.sleep(3)
            os.system('cls')

def assignment():
    des()
    print("\n Other Examples of Assignment Operator")
    des()
    print("\nA - Basic Arithmetic Operations in Python")
    print("B - Using Comparison Operators in Python")
    print("C - Bill Denomination Breakdown Program")
    print("X - Go Back")

    choose = input("Please select a Letter or 'x' to go back:").lower()
    cls()

    if choose == 'a':
        activity6()
        go()
        cls()
        assignment()

    elif choose == 'b':
        activity8()
        go()
        cls()
        assignment()

    elif choose == 'c':
        code_challenge_2()
        go()
        cls()
        assignment()

    elif choose == 'x':
        topic_2()

    else:
        print("Invalid Input. Please Try Again.")
        time.sleep(3)
        cls()
        assignment()

def Condition():
    code_challenge_3()
    des()
    tuloy()
    cls()
    activity10()
    go()
    cls()
    topic_3()

def Nestcon():
    code_challenge_4()
    des()
    go()
    cls()
    topic_3()

def topic_1():
    print("\n==========================================")
    print("\nPrinting and Input")
    print("\nA - How to Print a String in Python")
    print("B - How to Use Input Function")
    print("C - How to Use Escape Characters")
    print("D - Using the len() and type() Function.")
    print("E - Diamond Creation using escape sequence")
    print("X - Go Back to Main Menu")
    print("\n==========================================")

    select = input("\nChoose a Topic or 'x' to go back:")
    os.system('cls')
    
    if select.lower() == 'a':
        activity1()
        go()
        cls()
        topic_1()
        cls()

    elif select.lower() == 'b':
        activity2()
        go()
        cls()
        topic_1()
        cls()

    elif select.lower() == 'c':
        activity3()
        go()
        cls()
        topic_1()
        cls()

    elif select.lower() == 'd':
        activity4_5()
        go()
        cls()
        topic_1()
        cls()

    elif select.lower() == 'e':
        code_challenge_1()
        go()
        cls()
        topic_1()
        pass


    elif select.lower() == 'x':
        return
    
    else:
        print("Invalid Input. Please Try again.")
        time.sleep(3)
        os.system('cls')
        topic_1()

def topic_2():
    print("\n==========================================")
    print("\nAssignment and Logical Operator")
    print("\nA - What is Assignment and Logical Operator")
    print("B - Example of Assignment Operator")
    print("C - Example of Logical Operator")
    print("D - Other Examples of Assignment Operator")
    print("X - Go Back to Main Menu")
    print("\n==========================================")

    select = input("\nChoose a topic or 'x' to go back:")
    cls()

    if select.lower() == 'a':
        print("\n==========================================")
        print("\nASSIGNMENT OPERATOR")
        print("\nAssignment operators in Python are used to store \nvalues in variables. They can also combine an operation \nwith assignment to update a variable more concisely.")

        print("\nBelow are the assignment operator:")
        print("\n+="  "\t- Addition Assignment")   
        print("-="  "\t- Subtraction Assignment")   
        print("*="  "\t- Multiplication Assignment")   
        print("/="  "\t- Division Assignment")   
        print("//=" "\t- Floor Division Assignment")  
        print("%="  "\t- Modulus Assignment")   
        print("**=" "\t- Exponent Assignment")
        print("\n==========================================")
        tuloy()
        cls()

        print("\n==========================================")
        print("\nLOGICAL OPERATOR")
        print("\nLogical operators in Python are used to evaluate \nboolean expressions and determine \ntruth values by combining conditions.")
        print("\nBelow are the Logical Operator.")
        print("\nExamples:")
        print(" \nand - True only if both conditions are true.")
        print("or - True if at least one condition is true.")
        print("not - Reverses the truth value.")
        print("\n==========================================")

        go()
        cls()
        topic_2()

    elif select.lower() == 'b':
        activity7()
        go()
        cls()
        topic_2()

    elif select.lower() == 'c':
        activity9()
        go()
        cls()
        topic_2()

    elif select.lower() == 'd':
        assignment()

    elif select.lower() == 'x':
        return
    
    else:
        print("Invalid Input. Please Try Again.")
        time.sleep(3)
        os.system('cls')
        topic_2()

def topic_3():
    print("\n==========================================")
    print("\nConditinal and Nested Statements")
    print("\nA - What is a Conditional statements and Example")
    print("B - What is a Nested Conditional Statements and Example ")
    print("C - Other Example of Conditional Statement")
    print("D - Other Example of Nested Conditional Statement")
    print("X - Go Back to Main Menu")
    print("\n==========================================")
    
    select = input("\nChoose a topic or 'x' to go back:")
    cls()

    if select.lower() == 'a':
        activity11()
        print("\n==================")
        print("Flashy, isn't it?")
        print("==================")
        go()
        cls()
        topic_3()
        
    elif select.lower() == 'b':
        ots()
        go()
        cls()
        topic_3()

    elif select.lower() == 'c':
        Condition()
    
    elif select.lower() == 'd':
        Nestcon()
    
    elif select.lower() == 'x':
        return
    else:
        print("Invalid Input. Please Try Again.")
        time.sleep(3)
        os.system('cls')
        topic_3()

def topic_4():
    print("\n==========================================")
    print("\nFor and Nested Loop")
    print("A - What is A For Loop")
    print("B - For loop Example")
    print("C - What is a Nested For Loop")
    print("D - Nested For Loop Example")
    print("X - Go Back to Main Menu")
    print("\n==========================================")

    select = input("\nChoose a topic or 'x' to go back:")
    cls()

    if select.lower() == 'a':
        print("\n==========================================")
        print("\nFOR LOOP")
        print("\nfor loop - A for loop is a control structure that repeats \na block of code a specific number of times. \nIt's perfect when you know how many \niterations you need.")
        print("\n==========================================")
        print("\nTHE START,STOP, STEP")
        print("\nfor <variable> in range(start,stop,step)")
        print("\nSTART is where the counting begins.\nSTOP is where the counting ends but is NOT included.\nSTEP is how much the number changes each time.")
        print("==========================================")
        print("\nExample:")
        print("\nfor i in range(1,6,1):")
        print("    print(\"Hello World\")")
        print("\nOutput:")
        print("\nHello World\nHello World\nHello World\nHello World\nHello World")
        print("\n==========================================")
        go()
        cls()
        topic_4()


    elif select.lower() == 'b':
        ex()

    elif select.lower() == 'c':
        print("The Nested for loop")
        print("\nA nested for loop means one loop inside another loop.")
        print("The outer loop controls the number of rows.")
        print("The inner loop controls the number of columns.")
        print("For every single step of the outer loop, the inner loop runs completely.")
        print("This allows us to create patterns, grids, or repeated combinations.")

        print("\nExample:")
        print('\nfor x in range(11, 0, -1):')
        print('    for y in range(1, x):')
        print('        print(f"*", end=" ")')
        print('    print()')

        print("\nOutput:")
        print("""\n\b\b\t* * * * * * * * * *
        * * * * * * * * *
        * * * * * * * *
        * * * * * * *
        * * * * * *
        * * * * *
        * * * *
        * * *
        * *
        *""")
        go()
        cls()
        topic_4()

    elif select.lower() == 'd':
        nestfor()

    elif select.lower() == 'x':
        return

    else:
        print("Invalid Input. Please Try Again.")
        time.sleep(3)
        os.system('cls')
        topic_4()

def topic_5():
    des()
    print("\nWhile loop")
    print("\nA - What is while loop ")
    print("B - While loop program ")
    print("C - Guessing Game using while loop")
    print("D - Odd Number Selector using while loop")
    print("X - Go Back to Main Menu")
    des()
    choose = input("\nChoose a topic or 'x' to go back to Main Menu:").lower()
    cls()

    if choose == 'a':
        print("\n==========================================")
        print("\nThe While Loop")
        print("\nA while loop repeats a block of code \nas long as a condition is true.")
        print("It is useful when you do not know \nthe exact number of repetitions.")
        print("\n==========================================")
        go()
        cls()
        topic_5()

    elif choose == 'b':
        activity20()
        go()
        cls()
        topic_5()

    elif choose == 'c':
        activity21()
        go()
        cls()
        topic_5()

    elif choose == 'd':
        code_challenge_13()
        go()
        cls()
        topic_5()

    elif choose == 'x':
        return
    
    else:
        print("Invalid Input. Please Try Again.")
        time.sleep(3)
        cls()
        topic_5()

def topic_6():
    des()
    print("\n The List function")
    print("\nA - What is a List")
    print("B - List Function Example")
    print("C - What is a Dictionary")
    print("D - Dictionary Example")
    print("E - Anime List Collector Program")
    print("F - Student Information System")
    print("X - Go Back to Main Menu")
    des()

    choose = input("\nChoose a Topic or 'x' to Go back to Main Menu: ").lower()
    cls()

    if choose == 'a':
        des()
        print("\nWhat is a List in Python?")
        print(" \nA list in Python is a data structure \nthat can store multiple values \nin a single variable.")
        print("It is ordered, changeable, and \nallows duplicate items.")
        print("\nThink of a list like a container \nthat can hold many items at once.")
        des()
        go()
        cls()
        topic_6()

    elif choose == 'b':
        lizt()
        tuloy()
        cls()
        list_method()
        go()
        cls()
        topic_6()

    elif choose == 'c':
        dictionary()
        go()
        cls()
        topic_6()

    elif choose == 'd':
        di_example()
        go()
        cls()
        topic_6()

    elif choose == 'e':
        code_challenge_14()
        go()
        cls()
        topic_6()

    elif choose == 'f':
        code_challenge_15()
        go()
        cls()
        topic_6()
        
    elif choose == 'x':
        return
    
    else:
        print("Invalid Input. Please Try Again.")
        time.sleep(3)
        cls()
        topic_6()

def topic_7():
    des()
    print("\nProgrammer/User Defined Function:")
    print("A - What is function")
    choose = input("\nChoose a Topic or 'x' to Go back to Main Menu: ").lower()
    cls()

    if choose == 'a':
        activity23()
        go()
        cls()
        topic_7()

    elif choose == 'x':
        return

    else:
        print("Invalid Input. Please Try Again.")
        time.sleep(3)
        cls()
        topic_7()


import os
import time

def des():
    print("\n==========================================")

def activity1():
    print("\nThe Printing Function:")
    print("\nThe print() function prints the specified message to the screen,") 
    print("or other standard output device.The message can be a string,") 
    print("or any other object, the object will be converted into") 
    print("a string before written to the screen.")
    print("\n======================================================")
    print("\nSyntax:")
    print("\\print(\"Hello World\")")

    print("\nOutput:")
    print("Hello World")
    print("======================================================")

    print("\nTry it yourself!")
    test = input("\nEnter your text here:")
    print("\nYour Output:")
    print(test)
    print("========================================================")
    
def activity2():
    print("\nThe Input Function")
    print("\nIn Python, \"input\" primarily refers to data provided") 
    print("to a program by a user or an external source. The most")
    print("common way to get user input in Python is through")
    print("the built-in input() function.")
    print("\n========================================================")
    print("\nSyntax:")
    print("\\name = \"input(\"What is your name?\")")

    print("\n\\print(\"Hi!\",name,\"Welcome to the matrix\")")

    print("\nOutput:")
    print("Hi!<name>, Welcome to the matrix")
    print("\n========================================================")
    print("\nTry it yourself!")
    name = input("What is your name?:")

    print("\nOutput:")
    print(f"Hi! {name}, Welcome to the matrix")
    
def activity3():

    print("Escape Character - A special symbol used in strings to ")
    print("represent characters that are hard to type or have special")
    print("meaning, like \"\\n\" for a new line or \"\\t\" for a tab.")
    print("\n==============================================")

    print("\nBelow is an example of Escape Character:")
    print("\nBackslash - " "\\\\")  # Backslash
    print("Single Quote - ""\\'")   # Single quote
    print("Double Quote - "'\\"')   # Double quote   
    print("Backspace - ""\\b")   # Backspace
    print("Formfeed - ""\\f")   # Formfeed
    print("Newline - ""\\n")   # Newline
    print("Carriage Return - ""\\r")   # Carriage Return
    print("Horizontal Tab - ""\\t")   # Horizontal Tab
    print("Vertical Tab""\\v")   # Vertical Tab
    print("Null Character - ""\\0")   # Null character
    print("\n==============================================")

    print("\nSyntax:")
    print("print(\"Hello\\nhow\\nare\\nyou\")")




    print("\nOutput:")
    print("Hello\nhow\nare\nyou")
    print("\n==============================================")

def activity4_5():
    print("\nThe len() and type() function")
    print("\nlen() - A built in function that returns how many")
    print("items are inside something (like characters in a string)")
    print("or elements in a list).")
    print("\n========================================================")

    print("\ntype() - A built-in Python function used to \ndetermine the data type of a variable or object.")
    print("\n========================================================")

    print("Example:")
    print("\\name = input(\"\nWhat is your name?:\")")
    print("\\print(\"Welcome to my program","name)")
    print("\\print(\"Your name has\",len(name), \"characters\", type(name))")

    print("\nOutput:")
    print("What is your name?:")
    print("Welcome to my program <name>") 
    print("Your name has 4 characters <class 'str'>")
    print("\n========================================================")

    print ("Try it yourself!")
    name = input("\nWhat is your name?:")
    print("Welcome to my program",name)
    print("Your name has", len(name), "characters", type(name))

def activity6():
    des()
    print("\nCode:")
    print("""\n\t\b\b\b\bn1 = eval(input("Enter the first number that comes out to your mind -->"))
    n2 = eval(input("Enter the second number that comes out to your mind -->"))

    s = n1 + n2
    q = n1 - n2
    p = n1 * n2
    r = n1 / n2

    print("\\nThe sum of", n1, "and", n2, "is", s)
    print("The difference of", n1, "and", n2, "is", q)
    print("The product of", n1, "and", n2, "is", p)
    print("The quotient of", n1, "and", n2, "is", r)
    print(n1, "exponent by", n2, "is", n1**n2)
    print("The remainder of", n1, "and", n2, "is", n1%n2)
    print("The floor division of", n1, "and", n2, "is", n1//n2)
    """)
    des()
    input("Press (Enter) to see the Output.")
    os.system('cls')
    
    print("Output:")

    n1 = eval(input("Enter the first number that comes out to your mind -->"))
    n2 = eval(input("Enter the second number that comes out to your mind -->"))

    s = n1 + n2
    q = n1 - n2
    p = n1 * n2
    r = n1 / n2

    print("\nThe sum of", n1,"and", n2, "is",s)
    print("The difference of", n1, "and", n2, "is", q)
    print("The product of", n1, "and", n2, "is", p)
    print("The quotient of",n1, "and", n2, "is", r)
    print(n1, "exponent by", n2,"is",n1**n2)
    print("The remainder of", n1,"and", n2, "is", n1%n2)
    print("The floor division of", n1, "and",n2,"is",n1//n2)

def activity7():
    des()
    print("\nExample of Assignment Operator:")
    print("\na = 5")
    print("print(\"The value of a is\", a)")
    print("")
    print("a += 5")
    print("print(\"The value of a is\", a)")
    print("")
    print("a += 5")
    print("a += 13")
    print("a -= 1")
    print("a *= 50")
    print("")
    print("print(\"The value of a is\", a)")
    des()

    print("\nOutput:")

    a = 5

    print("The value of a is",a)

    a += 5

    print("The value of a is",a)

    a += 5
    a += 13
    a -= 1
    a *= 50

    print("The value of a is",a)

    des()
    
def activity8():
    des()
    print("\nCode:")
    print("""\t\b\b\b\ba = 5
    b = 4

    name1 = 'John'
    name2 = 'manuel'


    print( a == b )
    print( name1 != name2 ) 
    """)
    des()
    input("Press (Enter) to see the Output.")
    print("==========================================")

    a = 5
    b = 4

    name1 = 'John'
    name2 = 'manuel'


    print( a == b )
    print( name1 != name2 ) 

def activity9():
    os.system('cls')
    print("\n==========================================")
    print("\n\"and\"")
    print("True only if both conditions are true.")
    print("\nx = 10")
    print("y = 5")
    print("")
    print("print(x > 5 and y < 10)   # True")
    print("print(x > 5 and y > 10)   # False")
    print("\n==========================================")

    print("\n\"or\"")
    print("True if at least one condition is true.")
    print("x = 3")
    print("y = 20")
    print("")
    print("print(x > 5 or y > 10)    # True")
    print("print(x > 5 or y < 2)     # False")
    print("\n==========================================")

    print("\n\"not\"")
    print("Reverses the truth value.")
    print("is_raining = False")
    print("")
    print("print(not is_raining)     # True")
    print("print(not True)           # False")
    print("\n==========================================")

def activity10():
    print("\nThis is a simple User Authentication System")
    print(
    "\nfrom getpass import getpass\n"
    "username = 'helloworld@gmail.com'\n"
    "password = 'hello_how_are_you'\n\n"
    "u = input('Please Enter Your Username/Email:')\n"
    "p = input('Please Enter Your Password:')\n\n"
    "if (u == username) and (p == password ):\n"
    "    print('Access Granted!')\n"
    "else:\n"
    "    print('Incorrect Username/Password.')"
    )

    input("Press Enter to Run the Program.")
    os.system('cls')

    print(
    "This program checks if the username and password \nentered by the user match the "
    "pre-set login credentials. \nIf both the email and password are correct, it displays "
    "'Access Granted!'. \nIf either one is incorrect, it shows an error message telling "
    "\nthe user that the username or password is incorrect."
    )

    print("\nTry it yourself!")
    print("username - helloworld@gmail.com")
    print("pass - hello_how_are_you")

    from getpass import getpass
    username = 'helloworld@gmail.com'
    password = 'hello_how_are_you'

    u = input("\nPlease Enter Your Username/Email:")
    p = input("Please Enter Your Password:")

    if (u == username) and (p == password ):
        print("Access Granted!")
    else:
        print("Incorrect Username/Password.")

def activity11():
    print("\n============================================")
    print("\nCONDITIONAL STATEMENTS")
    print("Conditional statements allow a program to make decisions. \nThey check whether a condition is true or false, \nand then run specific code based on that result.")
    print("\n============================================")

    print('\ntemp = float(input("\\nEnter temperature -->"))')

    print('\nif temp >= 1 and temp <= 20:')
    print('print("\\nYou need to wear jacket.")')

    print('\nelif temp >= 21 and temp <= 30:')
    print('print("\\nYou can wear your usual clothes...")')

    print('\nelif temp >= 31 and temp <= 37:')
    print('print("\\nIt\'s luke warm huh")')

    print('\nelif temp >= 38 and temp <= 45:')
    print('print("\\nYou need to hydrate more...")')

    print('\nelif temp >= 45 and temp <= 50:')
    print('print("\\nPut your sunblock on!!")')

    print('\nelif temp > 50:')
    print('print("\\nWarning!! It\'s Dangerous!!")')

    print('\nelse:')
    print('print("\\nInvalid Input")')
    
    input("\nPress Enter to Run the Code.")
    os.system('cls')

    print("Try it yourself!")
    temp = float(input("\nEnter temperature -->"))

    if temp >= 1 and temp <= 20:
        print("\nYou need to wear jacket.")

    elif temp >= 21 and temp <= 30:
        print("\nYou can wear your usual clothes...")

    elif temp >= 31 and temp <= 37:
        print("\nIt's luke warm huh")

    elif temp >= 38 and temp <= 45:
            print("\nYou need to hydrate more...")\
    
    elif temp >= 45  and temp <= 50:
        print("\nPut your sunblock on!!")

    elif temp > 50:
        print("\nWarning!! It's Dangerous!!")

    else:
        print("\nInvalid Input")

def activity12():

    print("\nCode:")
    print("""\nfor damit in range(1,11,1):
        print(damit,"Labhan")

        print("\n\tLalabhan ang",damit,"kasi madumi na.")""")
    des()
    input("Press (Enter) to see the Output.")
    os.system('cls')

    print("Output:")
    for damit in range(1,11,1):
        print(damit,"Labhan")

        print("\n\tLalabhan ang",damit,"kasi madumi na.")
    
def activity13():

    print("\nCode:")
    print("""\nsum = 0
    for x in range(1,11,1):
        print(x)
        number = eval(input("Enter the number that you want to sum -->"))
        sum += number

    print("\n\tThe sum of all the given numbers is",sum)""")
    des()
    input("Press (Enter) to run the program.")
    os.system('cls')

    print("\nOutput:")
    sum = 0
    for x in range(1,11,1):
        print(x)
        number = eval(input("Enter the number that you want to sum -->"))
        sum += number

    print("\n\tThe sum of all the given numbers is",sum)
    
def activity14():
    print("\nCode:")
    print("""\nfor i in range(20,0,-1):
        print(i)""")
    des()
    print("\nOutput:")
    for i in range(20,0,-1):
        print(i)

def activity15():
    des()
    print("\nNested Loop Example")
    print('\nfor i in range(1, 11, 1):')
    print('    for j in range(1, 11, 1):')
    print('        print(i, end=" ")')
    print('    print()')
    des()

    print("\nOutput:")
    for i in range(1,11,1):
        for j in range(1,11,1):
            print(i, end=" ")
    print()
    print("\n==========================================")
    
def activity16():

    print("\nCode:")

    print("""\nfor i in range(1,8,1):
        for j in range(6,i,-1):
            print(i, end=" ")
    print()""")     
    des()
    print("\nOutput:")
    print("\n1 1 1 1 1")
    print("2 2 2 2")   
    print("3 3 3")     
    print("4 4")       
    print("5")     
    
def activity17():
    print("Code:")
    print("""\nfor i in range(1,11,1):
        for j in range(11,i,-1):
            print(i,end=" ")
    print()""")
    des()
    print("Output:")
    print("\n1 1 1 1 1 1 1 1 1 1")
    print("2 2 2 2 2 2 2 2 2") 
    print("3 3 3 3 3 3 3 3")     
    print("4 4 4 4 4 4 4")       
    print("5 5 5 5 5 5")        
    print("6 6 6 6 6") 
    print("7 7 7 7") 
    print("8 8 8") 
    print("9 9")
    print("10") 
    
def activity18():
    print("\nCode:")
    print("""\nfor i in range(1,11,1):
        for j in range(1,i,1):
            print("^",end=" ")
        for f in range(11,i,-1):
             print("*",end=" ")
    print()""")
    des()
    print("\nOutput:")
    print("\n* * * * * * * * * *")
    print("^ * * * * * * * * *")
    print("^ ^ * * * * * * * *")
    print("^ ^ ^ * * * * * * *")
    print("^ ^ ^ ^ * * * * * *")
    print("^ ^ ^ ^ ^ * * * * *")
    print("^ ^ ^ ^ ^ ^ * * * *")
    print("^ ^ ^ ^ ^ ^ ^ * * *") 
    print("^ ^ ^ ^ ^ ^ ^ ^ * *")
    print("^ ^ ^ ^ ^ ^ ^ ^ ^ *") 
    
def activity19():
    des()
    print("\nExample:")
    print('for i in range(1, 11, 1):')
    print('    for j in range(10, i, -1):')
    print('        print(" ", end=" ")')
    print('    for f in range(1, i, 1):')
    print('        print("*", end=" ")')
    print('    for v in range(i - 1, 1, -1):')
    print('        print("*", end=" ")')
    print('    print()')
    print()
    print('for i in range(9, 0, -1):')
    print('    for j in range(10, i, -1):')
    print('        print(" ", end=" ")')
    print('    for f in range(1, i):')
    print('        print("*", end=" ")')
    print('    for v in range(i - 1, 1, -1):')
    print('        print("*", end=" ")')
    print('    print()')
    des()
    input("\nPress(Enter) to see the Output")
    os.system('cls')
    print("\nOutput:")
    print("                *")
    print("              * * *")
    print("            * * * * *")
    print("          * * * * * * *")
    print("        * * * * * * * * *")
    print("      * * * * * * * * * * *")
    print("    * * * * * * * * * * * * *")
    print("  * * * * * * * * * * * * * * *")
    print("* * * * * * * * * * * * * * * * *")
    print("  * * * * * * * * * * * * * * *")
    print("    * * * * * * * * * * * * *")
    print("      * * * * * * * * * * *")
    print("        * * * * * * * * *")
    print("          * * * * * * *")
    print("            * * * * *")
    print("              * * *")
    print("                *")

def activity20():
    des()
    print("student = True")
    print("")
    print("while student:")
    print("    answer = input(\"Are you student?(yes or no?): \").lower()")
    print("")
    print("    if answer == 'yes':")
    print("        print(\"You Are Eligible for A discount!\")")
    print("        continue")
    print("")
    print("    elif answer == 'no':")
    print("        print(\"Sorry but only student are eligible.\")")
    print("        break")
    print("")
    print("    else:")
    print("        print(\"Invalid Input. Try Again\")")    
    print("        continue")
    des()
    input("\nPress (Enter) to run this program")
    os.system('cls')

    student = True
    while student:
        answer = input("\nAre you student?(yes or no?):").lower()

        if answer == 'yes':
            print("\nYou Are Eligible for A discount!")
            time.sleep(3)
            os.system('cls')
            continue

        elif answer == 'no':
            print("\nSorry but only student are eligible")
            break
        else:
            print("\nInvalid Input. Try Again")
            time.sleep(3)
            os.system('cls')
            continue

def activity21():

    print("\nThe Number Guessing Game")
    des()
    print("This program is a simple number-guessing game. It asks for the player's name, generates a random")
    print("number from 1 to 5, and repeatedly prompts the user to guess it. Each wrong guess increases the try")
    print("count until the correct number is entered. When the player wins, the program displays a message with")
    print("their name and the total number of attempts.")
    des()

    print("import random")
    print("")
    print("print(\"Guess a Number\")")
    print("print(\"---------------------\")")
    print("")
    print("random_value = random.randint(1,5)")
    print("tries = 0")
    print("guess = True")
    print("")
    print("name = input(\"What's your name?-->\")")
    print("while guess == True:")
    print("    number = eval(input(\"Guess a number from 1 - 5-->\"))")
    print("    tries += 1")
    print("")
    print("    if number == random_value:")
    print("        print(\"You Win!\")")
    print("        break")
    print("    else:")
    print("        print(\"Please Guess again.\")")
    print("        continue")
    print("")
    print("print(f\"Hi {name},Congratulations, your guess is correct!, Number of tries {tries}\")")
    des()
    input("Press (Enter) to run the code.")
    os.system('cls')
    
    import random

    print("Guess a Number")
    print("---------------------")

    random_value = random.randint(1,5)
    tries = 0
    guess = True


    name = input("What's your name?-->")
    while guess == True:
        number = eval(input("Guess a number from 1 - 5-->"))
        tries += 1

        if number == random_value:
            print("You Win!")
            break
        else:
            print("Please Guess again.")
            continue

    print(f"Hi {name},Congratulations, your guess is correct!, Number of tries {tries}")

def activity22():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']

    print(months)

    months.reverse()
    print(months)

    fullname = 'John Manuel C. Andog'

    newlist = list(fullname)
    newlist.reverse()
    print(newlist)

    newlist.sort()
    print(newlist)

def lizt():
    des()
    print("\nExample of a list:")
    print("months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']")

    print("\"print(months)")
    des()
    print("\nOutput:")

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']

    print(months)
    des()
    print("\nWhat does this line do?")
    time.sleep(2)
    print("\n" \
    "months - is the variable name")
    time.sleep(2)
    print("The \"=\" sign assigns value to the variable. ")
    time.sleep(2)
    print("Each item in the list is a string representing a month")
    time.sleep(2)
    print("To Display the list on our screen, we use the \"print()\" function")
    time.sleep(2)
    print("We put the variable inside the print")
    time.sleep(2)
    print("so that we can display the list")
    des()
    time.sleep(2)

def list_method():
    des()
    print("\nappend() - Adds item to the end")
    print("insert() - Add items at index")
    print("extend() - Add multiple items")
    print("remove() - Remove by value")
    print("pop() - Remove by index")
    print("clear() - Remove all items")
    print("index() - Find Position of Value")
    print("count() - Count occurences")
    print("sort() - Sort list")
    print("reverse() - Reverse list")
    print("copy() - Copy list")
    des()
    print("\nPython lists comes with a set of built in methods\nthese are functions that let you work with lists easily. ")
    print("These Methods allows you to add items, \nremove items, sort data and more.")
    des()

def dictionary():
    des()
    print("\nDICTIONARY IN PYTHON")
    print("\nIt is used to store data in \"key:value\" pair.")
    print("A dictionary is a collection which is ordered, \nchangeable and do not allow duplicates.")
    print("Dictionaries are written with curly braces, \nand have keys and values.")
    des()

def di_example():
    des()
    print("\nDictionary Items")
    print("These are ordered, changeable, and not allowing duplicate items.")
    des()
    print("Example:")

    print("""thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(thisdict["brand"])""")
    des()

    print("Output:")
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(thisdict["brand"])
    des()
    input("\nPress (Enter) to run the code")
    os.system('cls')

    des()
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

    key = input("Please input brand, model, or year:")
    print(thisdict[key])
    des()
    print("\nYou can access values in a dictionary \nby calling it's corresponding key")

def activity23_1():
    from activity23 import Myfirstfunction

    Myfirstfunction()
    
def activity23():
    des()
    print("\nUser Defined Function")
    print("A User-Defined Function is a Function created \nby the user to perform specific tasks in program.")
    print("Unlike built in functions like \"len()\",\"print()\",\n UDFs allow customization and code reusability,")
    print("Improving program structure and efficiency.")
    des()

    print("Example:")

    print("\nname = input(\"Enter your name -->\")")

    print("\ndef Myfirstfunction():")
    print("\tprint(f\"Hello {name}, How are you?\")")
    print("\tprint(f\"Don't worry {name}, you can do it!\")")
    print("\nMyfirstfunction()")
    des()
    print("\nThis program first asks the user to enter their \nname,stores that name in a variable, defines a \nfunction that uses the stored name to display \ntwo personalized messages, and \nfinally calls the function so the \nmessages appear on the screen.")
    input("\nPress(Enter) to run the program")
    os.system('cls')

    print("Try it yourself!")

    name = input("Enter your name -->")

    def Myfirstfunction():
        print(f"Hello {name}, How are you?")
        print(f"Don't worry {name}, you can do it!")

    Myfirstfunction()










import time
import os

def clear():
    os.system('cls')

def cont():
    input("Press (Enter) to run the program.")

def des():
    print("\n==========================================")

def t():
    time.sleep(2)

def code_challenge_1():
    des()
    print("\nCode:")
    print("""\n\t\b\b\b\bname = input("What is your name?:")
    print("Hello",name,"welcome to the matrix")


    print("\\n\\n\\t\\t\\t\\t\\t*"
      "\\n\\t\\t\\t\\t*"
      "\\t\\t*"
      "\\n\\t\\t\\t*"
      "\\t\\t\\t\\t*"
      "\\n\\t\\t*"
      "\\t\\t\\t\\t\\t\\t*"
      "\\n\\t*"
      "\\t\\t\\t\\tHi",name,"\\t\\t\\t*"
      "\\n\\n\\t\\t*"
      "\\t\\t\\t\\t\\t\\t*"
      "\\n\\n\\t\\t\\t*"
      "\\t\\t\\t\\t*"
      "\\n\\n\\t\\t\\t\\t*"
      "\\t\\t*"
      "\\n\\n\\t\\t\\t\\t\\t*")""")
    des()
    input("Press (Enter) to run the code.")
    os.system('cls')
    print("\nOutput:")

    name = input("What is your name?:")
    print("Hello",name,"welcome to the matrix")



    print("\n\n\t\t\t\t\t*" "\n\t\t\t\t*" "\t\t*" "\n\t\t\t*" "\t\t\t\t*" "\n\t\t*" "\t\t\t\t\t\t*" "\n\t*" "\t\t\t" "\t""Hi",name,"\t\t\t*" "\n\n\t\t*" "\t\t\t\t\t\t*" "\n\n\t\t\t*" "\t\t\t\t*" "\n\n\t\t\t\t*" "\t\t*" "\n\n\t\t\t\t\t*")

def code_challenge_2():
    des()
    print("""\nEXPLANATION OF THE CODE:
    This program breaks down any amount into bills using:
    - // (floor division) to count how many bills fit
    - % (modulo) to get the remaining balance""")    
    des()
    cont()
    clear()
    des()
    print("\nTry it yourself!")
    amount = eval(input("\nEnter the amount that you want to deposit-->"))
    print("Here's the breakdown of your deposit-->")

    onethou = amount // 1000
    amount = amount % 1000
    print(onethou,"\t- 1000")

    fivehund = amount // 500 
    amount = amount % 500
    print(fivehund,"\t- 500")

    twohund = amount // 200
    amount = amount % 200
    print(twohund,"\t- 200")

    onehund = amount // 100
    amount = amount % 100
    print(onehund,"\t- 100")

    fifty = amount // 50
    amount = amount % 50
    print(fifty,"\t- 50")

    twenty = amount // 20
    amount = amount % 20
    print(twenty,"\t- 20")

    ten = amount // 10
    amount = amount % 10
    print(ten,"\t- 10")

    five = amount // 5
    amount = amount % 5
    print(five,"\t- 5")

    one = amount // 1
    amount = amount % 1
    print(one,"\t- 1")

    des()
 
def code_challenge_3():
    des()
    print("""
    "This program greets the user, asks for their name, fare amount, "
    "and whether they are a student. If the user answers 'yes', the program "
    "calculates a 20% discount and shows the reduced fare. Otherwise, it "
    "informs the user that they are not eligible for the student discount.
    """)
    cont()
    os.system('cls')
    
    des()
    print("\nTry it yourself!")
    print("\nStudent Fare Discount System")

    print("\nGreetings!! from Transportation Inc.")
    name = input("What is your name?:")
    fare = eval(input("Enter the amount of your fare fee:"))
    student = input("Are you a student?Yes/No:")
    discount = fare * 0.2

    if student.lower().strip() == 'yes':
        fare = fare - discount
        print("Hello", name, "here is your discounted fare", fare)
    else:
        print("Apologies",name,"but you are not eligible of the student discount.")

def code_challenge_4():
    des()
    print("\nManga Recommendation System")
    print(
    "\nThis program is a manga recommendation system. \n\nIt asks the user to choose a genre "
    "(Shonen, Josei, or Seinen), \n\nthen select a year range, and finally choose whether "
    "they want a long or \n\nshort series. Based on these choices, the program displays \n\na "
    "list of recommended manga titles. \n\nIf the user enters an invalid option at any \n\nstep, "
    "the program shows an error message and asks them to restart."
)
    
    cont()
    os.system('cls')

    des()
    print("\nWelcome to Mangago!!")
    print("\nWhat genre do you prefer?")
    print("Shonen - 1")
    print("Josei - 2")
    print("Seinen - 3")
    genre_choice = input("\\nSelect a number from the genre (1/2/3):")
    os.system('cls')

    if genre_choice == "1":
        genre1 = 'Shonen'
        print("You selected:", genre1)

        print("\nChoose a year")
        print("\n1999 - 2005  (a)")
        print("2005 - 2010  (b)")
        print("2010 - 2025 (c)")
        year = input("\\nFrom what year?:").lower()
        os.system('cls')

        if year == 'a':
            print("\nWhat kind of series do you want? (long/short):")
            length = input("Enter the length that you want.:").lower()
            os.system('cls')

            if length == 'long':
                print("\nHere are the manga recommendations for you from the year ", year, "and length", length)
                print("\nOne Piece")
                print("Naruto")
                print("Bleach")
                print("Prince of Tennis")
                print("Eyeshield")
                print("Zatchbell!")
                print("Shaman King")
                print("Hunter x Hunter")
                print("\\nThank You for using Mangago!!!")

            elif length == 'short':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nFull Metal Alchemist")
                print("Hikaru No Go")
                print("\nThank you for using Mangago!!!")

            else:
                print("\nInvalid Selection. Please restart and choose long/short.")

        elif year == 'b':
            print("\nWhat kind of series do you want? (long/short):")
            length = input("Enter the length that you want.:").lower()
            os.system('cls')

            if length == 'long':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("Gintama")
                print("Fairy Tail")
                print("Katekyo Hitman reborn")
                print("Toriko")
                print("D.Gray-man")
                print("\nThank you for using Mangago!!!")

            elif length == 'short':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nDeathnote")
                print("Bakuman")
                print("Soul Eater")
                print("Beelzebub")
                print("Blue Exorcist")
                print("\nThank you for using Mangago!!!")

            else:
                print("\nInvalid Selection. Please restart and choose long/short.")

        elif year == 'c':
            print("What kind of series do you want?(long/short)")
            length = input("Enter the length that you want.:").lower()
            os.system('cls')

            if length == 'long':
                print("\nHere are the manga recommendations for you from year", year, "and length", length)
                print("\nMy Hero Academia")
                print("Black Clover")
                print("The Seven Deadly Sins")
                print("Fire Force")
                print("Tokyo Revengers")
                print("Jujutsu Kaisen")

            elif length == 'short':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nDemon Slayer: Kimetsu no Yaiba")
                print("Dr.Stone")
                print("Chainsaw Man")
                print("Spy x Family")
                print("Mashle: Magic and Muscles")
                print("Kaiju No.8")
                print("\nThank you for using Mangago!!!")

            else:
                print("\nInvalid Selection. Please restart and choose long/short.")

        else:
            print("\nInvalid Selection. Please restart and choose a/b/c")

    elif genre_choice == "2":
        genre2 = 'Josei'
        print("You selected:", genre2)

        print("\nChoose a year")
        print("\n1999 - 2005  (a)")
        print("2005 - 2010  (b)")
        print("2010 - 2025 (c)")
        year = input("\nFrom what year?:").lower()
        os.system('cls')

        if year == 'a':
            print("\nWhat kind of series do you want? (long/short):")
            length = input("Enter the length that you want.:").lower()
            os.system('cls')

            if length == 'long':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nNana")
                print("Tramps like Us (Kimi wa Pet)")
                print("Boys Be...L Co-op")
                print("\nThank you for using Mangago!!!")

            elif length == 'short':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nParadise Kiss")
                print("Hataraki Man")
                print("Happy Mania")
                print("Gokusen")
                print("\nThank you for using Mangago!!!")

            else:
                print("\nInvalid Selection. Please restart and choose long/short.")

        elif year == 'b':
            print("\nWhat kind of series do you want? (long/short):")
            length = input("Enter the length that you want.:").lower()
            os.system('cls')

            if length == 'long':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nHoney and Clover")
                print("Nodame Cantabile")
                print("07 - Ghost")
                print("\nThank you for using Mangago!!!")

            elif length == 'short':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nButterflies, Flowers (Chou yo Hana yo)")
                print("Otomen")
                print("Himitsu - The Top Secret")
                print("A Thousand Years of Snow (Sennen no Yuki)")
                print("\nThank you for using Mangago!!!")

            else:
                print("\nInvalid Selection. Please restart and choose long/short")

        elif year == 'c':
            print("What kind of series do you want?(long/short)")
            length = input("Enter the length that you want.:").lower()
            os.system('cls')

            if length == 'long':
                print("\nHere are the manga recommendations for you from year", year, "and length", length)
                print("\nChihayafuru")
                print("Kurahagime (Princess Jellyfish)")
                print("Perfect World")
                print("\nThank you for using Mangago!!!")

            elif length == 'short':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nTokyo Tarareba Girls")
                print("My Androgynous Boyfriend")
                print("Will You Marry Me Again If You Are Reborn?")
                print("An Incurable Case of Love (Koi wa Tsuzuku yo Doko Made mo)")
                print("A Condition Called Love (Hananoi-kun to Koi no Yamai)")
                print("\nThank you for using Mangago!!!")

            else:
                print("\nInvalid Selection. Please Restart and choose long/short.")

        else:
            print("\nInvalid Selection. Please restart and enter a/b/c.")

    elif genre_choice == "3":
        genre3 = 'Seinen'
        print("You selected:", genre3)

        print("\nChoose a year:")
        print("\n1999 - 2005 (a)")
        print("2005 - 2010 (b)")
        print("2010 - 2025 (c)")
        year = input("\\nFrom what year?:").lower()
        os.system('cls')

        if year == 'a':
            print("\nWhat kind of series do you want?(long/short):")
            length = input("Enter the length that you want:").lower()
            os.system('cls')

            if length == 'long':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nVagabond")
                print("20th Century Boys")
                print("Gantz")
                print("Berserk (continued)")
                print("Homunculus")
                print("\nThank you for using Mangago!!!")

            elif length == 'short':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nMonster (ended 2001)")
                print("Planetes")
                print("Battle Royal")
                print("Old Boy")
                print("Ikigami: The Ultimate Limit")
                print("\nThank you for using Mangago!!!")

            else:
                print("\nInvalid Selection. Please restart and choose long/short.")

        elif year == 'b':
            print("\nWhat kind of series do you want?(long/short):")
            length = input("Enter the length that you want:").lower()
            os.system('cls')

            if length == 'long':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nVinland Saga")
                print("Zetman")
                print("Higanjima")
                print("Black Lagoon")
                print("\nThank you for using Mangago!!!")

            elif length == 'short':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nEden it's an Endless World! (Ended 2008)")
                print("Solanin")
                print("Bokurano")
                print("Mushishi (ended 2008)")
                print("Alive: The Final Evolution")
                print("\nThank you for using Mangago!!!")

            else:
                print("\nInvalid Selection. Please restart and choose long/short.")

        elif year == 'c':
            print("What kind of series do you want?(long/short)")
            length = input("Enter the length that you want.:").lower()
            os.system('cls')

            if length == 'long':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nKingdom")
                print("Golden Kamuy")
                print("Terra Formars")
                print("Ajin: Demi-Human")
                print("Blue Giant")
                print("\nThank you for using Mangago!!!")

            elif length == 'short':
                print("\nHere are the manga recommendations for you from the year", year, "and length", length)
                print("\nInuyashiki")
                print("Goodnight Punpun (Oyasumi Punpun)")
                print("I Am a Hero")
                print("Fire punch")
                print("Blood on the tracks (Chi no Wadachi)")
                print("\nThank you for using Mangago!!!")

            else:
                print("Invalid Selection. Please restart and choose long/short.")

        else:
            print("\nInvalid Selection, Please restart and choose a/b/c.")

    else:
        print("\nInvalid Selection. Please restart and Enter 1/2/3")
  
def ots():
    print("\n===========================================")
    print("\nNested Conditional Statements")
    print("\nA nested conditional is simply an if statement \ninside another if statement.You use this \nwhen you need multiple layers of checking.")
    print("\n===========================================")

    print("\ntemperature = float(input(\"Enter the temperature in °C: \"))")
    print("")
    print("if temperature >= 0:")
    print("    print(\"The temperature is above freezing.\")")
    print("")
    print("    if temperature >= 30:")
    print("        print(\"It's hot outside.\")")
    print("    else:")
    print("        print(\"The weather is warm but not too hot.\")")
    print("")
    print("else:")
    print("    print(\"The temperature is below freezing.\")")
    print("")
    print("    if temperature <= -10:")
    print("        print(\"It's extremely cold.\")")
    print("    else:")
    print("        print(\"It's cold, but not extreme.\")")
    des()
    input("\nPress Enter to run the program.")
    os.system('cls')
    
    temperature = float(input("\nEnter the temperature in °C: "))

    if temperature >= 0:
        print("\nThe temperature is above freezing.")

        if temperature >= 30:
            print("\nIt's hot outside.")
        else:
            print("\nThe weather is warm but not too hot.")

    else:
        print("\nThe temperature is below freezing.")

        if temperature <= -10:
            print("\nIt's extremely cold.")
        else:
            print("\nIt's cold, but not extreme.")

def code_challenge_5():
    print("\n==========================================")
    print("\nThe Factorial Program Using For Loop")

    print("\nfactorial = 1\n"
        "number = eval(input('Enter a number to get the factorial --> '))\n\n"
        "for i in range(number, 0, -1):\n"
        "    factorial *= i\n\n"
        "print('The factorial of', number, 'is', factorial)")
    print("\n==========================================")
    
    input("\nPress (Enter) to run the program")
    os.system('cls')

    print("\n")
    factorial = 1
    number = eval(input("Enter a number to get the factorial -->"))

    for i in range(number,0,-1):
        factorial *= i

    print("\nThe factorial of",number,"is",factorial)
    print("\n==========================================")
    print("\nA factorial is the product of all whole numbers from a given number down to 1.")
    time.sleep(2)
    print("For example, 5! = 5 x 4 x 3 x 2 x 1.")
    time.sleep(2)
    print("We start with factorial = 1 because multiplying by 1 keeps the value the same.")
    time.sleep(2)
    print("The user enters a number, and we use a for loop that counts DOWN using range(number, 0, -1).")
    time.sleep(2)
    print("Each time the loop runs, we multiply factorial by the current value of i.")
    time.sleep(2)
    print("When the loop ends, factorial contains the final answer.")
    time.sleep(2)
    print("\n==========================================")
   
def code_challenge_7():
    print("\n===========================================")
    print("\nOdd number accumulator Program Using For loop")


    print("\nsum = 0\n"
      "for i in range(1, 11, 1):\n"
      "    number = eval(input(f'Enter a number {i}:'))\n\n"
      "    if number % 2 == 1:\n"
      "        sum += number\n\n"
      "print('\\nSum of all numbers:', sum)")
    print("\n===========================================")
    input("\nPress (Enter) to run the program")
    os.system('cls')

    des()
    sum = 0
    for i in range(1,11,1):
        number = eval(input(f"Enter a number {i}:"))
    
        if number % 2 == 1:
            sum += number

    print("\nSum of all numbers:",sum)
    print("\n===========================================")

    print("\nThis program asks the user to enter 10 numbers.")
    time.sleep(1)
    print("A for loop repeats from 1 to 10 using range(1, 11, 1).")
    time.sleep(1)
    print("Each time, the user enters a number.")
    time.sleep(1)
    print("We check if the number is odd using number % 2 == 1.")
    time.sleep(1)
    print("If it is odd, we add it to the variable 'sum'.")
    time.sleep(1)
    print("After the loop ends, we print the total of all odd numbers.\n")
    time.sleep(1)

def code_challenge_8():
    print("\n==========================================")
    print("Multiplication Table Maker")

    print('print("\\nCreate your own multiplication Table.")')
    print('number = eval(input("\\nEnter a number -->"))')
    print('print("Multiplication Number for", number)')
    print('')
    print('for i in range(1, 11):')
    print('    print(number, f"x {i} =", number * i)')
    print("\n==========================================")

    input("\nPress (Enter) to run the program")
    os.system('cls')

    print("\nCreate your own multiplication Table.")
    number = eval(input("\nEnter a number -->"))
    print("\nMultiplication Number for", number)

    for  i in range(1,11):
        print(number,f"x {i} =",number * i)

    print("\nThis program creates a multiplication table for any number the user enters.")
    t()
    print("It first prints a title to show what the program does.")
    t()
    print("Then it asks the user to enter a number.")
    t()
    print("After that, it prints a header showing which number the table belongs to.")
    t()
    print("A for loop runs from 1 to 10 to generate each line of the multiplication table.")
    t()
    print("Inside the loop, the program multiplies the number by i and prints the result.\n")
    t()

def code_challenge_9():
    des()
    print("Countdown Simulator using for loop")

    print('import time')
    print('')
    print('print("⏳ COUNTDOWN TIMER SIMULATOR")')
    print('number = eval(input("Enter the starting number for count down -->"))')
    print('')
    print('for i in range(number, 0, -1):')
    print('    print(i)')
    print('    time.sleep(1)')
    print('')
    print('print("Liftoff!")')
    des()

    input("\nPress (Enter) to run the program")
    os.system('cls')

    import time

    print("\n⏳ COUNTDOWN TIMER SIMULATOR")
    number = eval(input("Enter the starting number for count down -->"))

    for i in range(number,0,-1):
        print(i)
        time.sleep(1)

    print("Liftoff!")
    des()

    print("\nThis program simulates a countdown timer.")
    t()
    print("It first prints a title to show what the program does.")
    t()
    print("Then it asks the user to enter a starting number for the countdown.")
    t()
    print("A for loop counts down from the number to 1 using range(number, 0, -1).")
    t()
    print("Inside the loop, each number is printed one at a time.")
    t()
    print("time.sleep(1) pauses the program for one second between numbers.")
    t()
    print("After the countdown reaches zero, the program prints 'Liftoff!'\n")
    t()

def code_challenge_10():
    #Triangle pattern

    for x in range(11,0,-1):
        for y in range(1,x):
            print(f"*", end=" ")
        print()

def code_challenge_11():

    print("\nExample:")
    print('\nprint("\\t\\t   ", end="*")')
    print('for i in range(1, 11, 1):')
    print('    for x in range(11, i, -1):')
    print('        print(" ", end=" ")')
    print('    for y in range(1, i, 1):')
    print('        print("*", end=" ")')
    print('    for z in range(1, i, 1):')
    print('        print("*", end=" ")')
    print('print()')

    print("\nOutput:")
    
    print("               *")
    print("              * *")
    print("            * * * *")
    print("          * * * * * *")
    print("        * * * * * * * *")
    print("      * * * * * * * * * *")
    print("    * * * * * * * * * * * *")
    print("  * * * * * * * * * * * * * *")
    print("* * * * * * * * * * * * * * * *")
 
def code_challenge_12():
    des()
    print("Example:")
    print('for i in range(1, 7, 1):')
    print('    for x in range(6, i, -1):')
    print('        print(" ", end=" ")')
    print('    for y in range(i, 0, -1):')
    print('        print(y, end=" ")')
    print('    for z in range(2, i + 1):')
    print('        print(z, end=" ")')
    print('    print()')
    des()

    print("\nOutput:")
    for i in range(1,7,1):
        for x in range(6,i,-1):
            print(" ",end=" ")
        for y in range(i,0,-1):
            print(y,end=" ")
        for z in range(2,i+1):
            print(z,end=" ")
        print()
    
def code_challenge_13():
    des()
    print("\nThe Odd number Selector")
    print("\nname = input(\"Hi, what is your name? -->\")")
    print("sum = 0")
    print("odd = \"\"")
    print("print(\"\\n++++++++++++++++++++++++++++++++++++\")")
    print("print(\"\\nODD NUMBER SELECTOR, press 0 to stop the loop.\")")
    print("")
    print("number = True")
    print("")
    print("while number == True:")
    print("    random = eval(input(\"\\nInput a random number-->\"))")
    print("")
    print("    if random % 2 == 1:")
    print("        print(\"Odd number detected\")")
    print("        sum += random")
    print("        odd += str(random) + \" \"")
    print("        continue")
    print("    elif random == 0:")
    print("        print(\"Loop Terminated.\")")
    print("        break")
    print("    else:")
    print("        if random % 2 == 0:")
    print("            print(\"Even number detected\")")
    print("        else:")
    print("            print(\"Invalid input, please try again.\")")
    print("            continue")
    print("print(\"Hi\", name, \"the summation of all the odd numbers is\", sum)")
    print("print(\"The Odd numbers are the ff\", odd)")
    print("")
    des()
    input("Press (Enter) to run the program.")
    os.system('cls')

    des()
    print("\nThis program asks the user to enter numbers continuously.\n"
      "It detects odd numbers, adds them to a sum, and keeps track of them.\n"
      "Even numbers are noted, and the loop ends when the user enters 0.\n"
      "At the end, the program displays the total sum and all odd numbers entered.")
    des()
    print("\nTry it yourself!")
    name = input("\nHi, what is your name? -->")
    sum = 0
    odd = ""
    print("\n++++++++++++++++++++++++++++++++++++")
    print("\nODD NUMBER SELECTOR")

    number = True

    while number == True:
        random = eval(input("\nInput a random number (Enter '0' to stop the loop).-->"))

        if random % 2 == 1:
            print("Odd number detected")
            time.sleep(1.5)
            os.system('cls')
            sum += random
            odd += str(random) + " "
            continue
        elif random == 0:
            print("Loop Terminated.")
            break
        else: 
            if random % 2 == 0:
                print("Even number detected")
                time.sleep(1.5)
                os.system('cls')
            else:
                print("Ivalid input, please try again.")
                continue
    print("Hi",name,"the summation of all the odd numbers is",sum)
    print("The Odd numbers are the ff", odd)
    
def code_challenge_14():
    des()
    print("anime_list = []")
    print("")
    print("while True:")
    print("    anime = input(\"Enter the title of the anime (or type 'exit' to finish):\")")
    print("")
    print("    if anime.lower() == \"exit\":")
    print("        print(\"\\nYou have exited the anime entry program.\")")
    print("        break")
    print("")
    print("    anime_list.append(anime)")
    print("    print(f\"{anime} has been added to your anime list.\")")
    print("")
    print("print(\"\\nYour anime list includes:\")")
    print("for a in anime_list:")
    print("    print(f\"- {a}\")")
    des()
    input("Press (Enter) to run the program.")
    os.system('cls')

    print("\n Try it yourself!")
    des()
    print("This program lets the user create a list of anime titles.\n"
      "The user can enter as many titles as they like and type 'exit' to finish.\n"
      "Each title is added to a list, and at the end, the program displays \nall the anime titles entered.")
    des()

    print("\nCode:")
    anime_list = []

    while True:
        anime = input("\nEnter the title of the anime (or type 'exit' to finish):")
        os.system('cls')

        if anime.lower() == "exit":
            print("\nYou have exited the anime entry program.")
            break

        anime_list.append(anime)
        print(f"{anime} has been added to your anime list.")

    print("\nYour anime list includes:")
    for a in anime_list:
        print(f"- {a}")
    
    des()

def code_challenge_15():

    print("\n=======================================================================================")
    print("STUDENT INFORMATION SYSTEM")
    print("\nThis program is a simple Student Information System that stores student records in a dictionary.")
    print("It repeatedly displays a menu where the user can add new students, view all records, search by ID,")
    print("delete a student, or edit existing information.")
    print("The program can also export all data to a JSON file and import previously saved data back into the system.")
    print("It continues running in a loop until the user chooses the option to exit.")
    print("\n=======================================================================================")
    print("\nTry it yourself!")
    print("\n=======================================================================================")
    import os
    import json
    print("\nDLL Student Information System")
    print("=============================================")

    stud_record = {}
    while True:
        print("Select From The Following Options")
        print("A - Adding Student Record")
        print("B - Print All Student Information")
        print("C - Search Student")
        print("D - Delete Student Record")
        print("E - Edit Student Info")
        print("F - Export Data")
        print("G - Import Data")
        print("X - Exit System")

        choice = input("Input your choice: ").lower().strip()

        if choice == 'a':
            student_id = input("Input ID Number ---> ")
            first_name = input("Enter First Name ---> ")
            last_name = input("Enter Last Name ---> ")
            course = input("Enter Course ---> ")
            section = input ("Enter Section ---> ")
            email = input("Enter Your EMail ---> ")
            print("DATA SAVED")

            stud_record[student_id] = [first_name, last_name, course, section, email]
            os.system('cls')
            continue

        elif choice == 'b':
        
            print("PRINTING STUDENT INFORMATION...")
            print("======================================")

            for id, info in stud_record.items():
                print(f"STUDENT ID {student_id} - RECORD - {info}")
        
            continue

        if choice == 'c':
            os.system('cls')

            print("SEARCHING STUDENT RECORD...")

            search_id = input ("INPUT STUDENT ID ---> ").lower()
            for each_student in stud_record.keys():
                if search_id in stud_record.keys():
                    print("\n\nRecord Found")
                
                    for id in stud_record[search_id]:
                        print(f"--- {id} ---")

                else:
                    print("NO RECORD FOUND")

                break
            continue

        if choice == 'd':
            os.system('cls')

            print("DELETE STUDENT RECORD...")

            search_id = input ("INPUT STUDENT ID ---> ").lower()
            for each_student in stud_record.keys():
                if search_id in stud_record.keys():
                    print("\n\nRecord Found")
                
                    for id in stud_record[search_id]:
                        print(f"--- {id} ---")

                    stud_record.pop(search_id)

                    print("DATA DELETED")

                else:
                    print("NO RECORD FOUND")

                break
            continue

        if choice == 'e':
            print("UPDATING STUDENT RECORD...")
            search_id = input ("INPUT STUDENT ID ---> ").lower()
            for each_student in stud_record.keys():
                if search_id in stud_record.keys():
                    print("\n\nRecord Found")
                
                    for id in stud_record[search_id]:
                        print(f"--- {id} ---")

                    first_name = input("Enter First Name ---> ")
                    last_name = input("Enter Last Name ---> ")
                    course = input("Enter Course ---> ")
                    section = input ("Enter Section ---> ")
                    email = input("Enter Your EMail ---> ")
                    print("DATA SAVED")

                    stud_record[search_id][0] = first_name
                    stud_record[search_id][1] = last_name
                    stud_record[search_id][2] = course
                    stud_record[search_id][3] = section
                    stud_record[search_id][4] = email
                    print("RECORD UPDATED")


                else:
                    print("NO RECORD FOUND")

                break
            continue

        if choice == 'f':
            print("EXPORT DATA")

            with open ('student_record.json', 'w') as new_file:
                json.dump(stud_record, new_file, indent = 4)
        
            continue

            print("DATA SAVED SUCCESSFULLY....")

        if choice == 'g':
            with open('student_record.json', 'r') as new_file:
                imported_student = json.load(new_file)

            stud_record = imported_student
            print("DATA IMPORTED SUCCESSFULLY")
            continue

        if choice == 'x':
            break

menu()