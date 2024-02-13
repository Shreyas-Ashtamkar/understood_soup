"""
    * Description : Simple program to practice python
    * Programmning Paradigm : Functional
    * Author : Shreyas Ashtamkar
    * Date : 2024-02-12
    * Problem statement : 
        Demonstrate the following 
        1. Queues 
        2. Dictionary
        3. Set Operations
        4. Finding Factorials
        5. Exception Handling
"""
from os import system
from time import sleep
clear = lambda : system("cls")
def ask_continue(prompt = "Do you want to continue (Yes/No) ? : "):
    print()
    print()
    choice = input(prompt).strip().lower()
    if choice in ("y", "yes", "ya", "yaa", "1", "true", "please", "c", "cont", "continue"):
        return True
    else:
        return False

queue      = list()
dictionary = dict()
sets       = { "A":set(), "B":set()}

def demonstrate_queues():
    global queue
    keep_running = True
    while keep_running:
        clear()
        print(" Demonstrating Queues ")
        print("----------------------")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Show Queue")
        print("4. Reset Queue")
        print("5. Go back to Main Menu")
        print("----------------------")
        choice = input("What do you want to see ? ")

        if not choice.isnumeric() or (int(choice) not in (1, 2, 3, 4, 5)):
            print("Invalid Choice :", choice, ". Please retry.")
            continue

        choice = int(choice)
        if choice == 1:
            element = input("\nEnter data to add in Queue : ")
            queue.append(element)
            print("\nUpdated Queue = [ " + " <- ".join(queue) +" ]")
        elif choice == 2:
            if len(queue) > 0:
                queue.pop(0)
            else:
                print("\n! ERROR : Queue is empty !")
            print("\nUpdated Queue = [ " + " <- ".join(queue) +" ]")
        elif choice == 3:
            print("\nUpdated Queue = [ " + " <- ".join(queue) +" ]")
        elif choice == 4:
            queue.clear()
            print("\nUpdated Queue = [ " + " <- ".join(queue) +" ]")
        else:
            break

        keep_running = not ask_continue("Press enter to continue... [Enter Y for main menu] : ")

def demonstrate_dictionary():
    global dictionary
    keep_running = True
    while keep_running:
        clear()
        print(" Demonstrating Dictionary ")
        print("----------------------")
        print("1. Add key-value pair")
        print("2. Get value of a key")
        print("3. Remove a key-value pair")
        print("4. Show dictionary")
        print("5. Reset dictionary")
        print("6. Go back to Main Menu")
        print("----------------------")
        choice = input("What do you want to see ? ")

        if not choice.isnumeric() or (int(choice) not in (1, 2, 3, 4, 5, 6)):
            print("Invalid Choice :", choice, ". Please retry.")
            continue

        choice = int(choice)
        if choice == 1:
            print("\nAdding to dictionary.")
            key     = input("    Enter Key    : ")
            value   = input("    Enter Value  : ")
            dictionary[key] = value
            print("\nUpdated Dictionary = " + str(dictionary))
        elif choice == 2:
            print("\nGetting value associated with a key in dictionary.")
            key     = input("    Enter Key    : ")
            if key in dictionary:
                print("Key : " + key + ",  Value : " + dictionary[key])
            else:
                raise KeyError("Invalid Key : " + key)
        elif choice == 3:
            print("\nRemoving key-value pair from dictionary.")
            key     = input("    Enter Key    : ")
            if key in dictionary:
                del dictionary[key]
            else:
                raise KeyError("Invalid Key : " + key)
            print("\nUpdated Dictionary = " + str(dictionary))
        elif choice == 4:
            print("\nUpdated Dictionary = " + str(dictionary))
        elif choice == 5:
            del dictionary
            dictionary = {}
            print("\nUpdated Dictionary = " + str(dictionary))
        else:
            break

        keep_running = not ask_continue("Press enter to continue... [Enter Y for main menu] : ")
        # keep_running = ask_continue()

def demonstrate_sets(): 
    global sets   
    keep_running = True
    while keep_running:
        clear()
        print("Demonstrating Operations over Sets ")
        print("----------------------")
        print("1. Show sets")
        print("2. Add elements to sets")
        print("3. Remove elements from sets")
        print("4. Perform Set operations")
        print("5. Reset Sets")
        print("6. Go back to Main Menu")
        print("----------------------")
        choice = input("What do you want to see ? ")

        if not choice.isnumeric() or (int(choice) not in (1, 2, 3, 4, 5, 6)):
            print("Invalid Choice :", choice, ". Please retry.")
            continue

        choice = int(choice)
        if choice == 1:
            print("\nUpdated Sets : ")
            print("    Set A : ", sets["A"])
            print("    Set B : ", sets["B"])
        elif choice == 2:
            print("\nAdding elements to Sets : ")
            value = input("Enter a value : ").strip().split()
            setChoice = input("Select a set ( A, B ) : ").strip()
            if setChoice in sets:
                sets[setChoice].update(value)
            else:
                raise NameError("Invalid set : "+ setChoice)
            print("\nUpdated Sets : ")
            print("    Set A : ", sets["A"])
            print("    Set B : ", sets["B"])
        elif choice == 3:
            print("\nRemoving from Sets : ")
            setChoice = input("Select a set ( A, B ) : ").strip()
            if setChoice not in sets:
                raise NameError("Invalid set : "+ setChoice)
            value = input("Enter value : ")
            sets[setChoice].remove(value)
            print("\nUpdated Sets : ")
            print("    Set A : ", sets["A"])
            print("    Set B : ", sets["B"])
        elif choice == 4:
            print("\nSet Operations")
            print("\nCurrent Sets : ")
            print("    Set A : ", str(sets["A"]))
            print("    Set B : ", str(sets["B"]))
            print("-"*max(len(str(sets["A"])),len(str(sets["B"]))))
            print("Available Operations : ")
            print("1. Union")
            print("2. Intersection")
            print("3. Difference")
            print("4. Symmetric Difference")
            print("5. Check disjoint")
            print("6. Check Subset")
            print("7. Check superset")
            print("\n Enter 0 to go back to previous Menu.")
            opsChoice = input("Enter the operation to demonstrate : ")
            print("---------------------------------------")
            if opsChoice not in "01234567":
                print("Invalid operation : ", opsChoice)
            else:
                if opsChoice == "0":
                    continue
                elif opsChoice == "1":
                    print("Operation : A UNION B")
                    print(sets["A"].union(sets["B"]))
                elif opsChoice == "2":
                    print("Operation : A INTERSECTION B")
                    print(sets["A"].intersection(sets["B"]))
                elif opsChoice == "3":
                    print("Operation : A DIFFERENCE B")
                    print(sets["A"].difference(sets["B"]))
                elif opsChoice == "4":
                    print("Operation : A SYMMETRIC_DIFFERENCE B")
                    print(sets["A"].symmetric_difference(sets["B"]))
                elif opsChoice == "5":
                    print("Operation : A ISDISJOINT B")
                    print(sets["A"].isdisjoint(sets["B"]))
                elif opsChoice == "6":
                    print("Operation : A ISSUBSET B")
                    print(sets["A"].issubset(sets["B"]))
                elif opsChoice == "7":
                    print("Operation : A ISSUPERSET B")
                    print(sets["A"].issuperset(sets["B"]))
                else:
                    print("Invalid Operation", opsChoice)
        elif choice == 5:
            print("\nReset sets")
            setChoice = input("Select a set ( A, B, None ) [Leave Blank to reset both]: ").strip()
            if setChoice in ("A", "B"):
                sets[setChoice].clear()
            elif setChoice == "":
                sets["A"].clear()
                sets["B"].clear()
            else:
                raise NameError("Invalid set : "+ setChoice)
            
            print("\nUpdated Sets : ")
            print("    Set A : ", sets["A"])
            print("    Set B : ", sets["B"])
        else:
            break

        keep_running = not ask_continue("Press enter to continue... [Enter Y for main menu]: ")
        # keep_running = ask_continue()

def fact(num=0, _show=False):
    res = num
    for i in range(num-1, 0, -1):
        if _show :
            sleep(0.3)
            print(f"  {res} x {i} = {res*i}")
        res *= i
    res = 1 if res <= 0 else res 
    return res

def demonstrate_factorial():
    keep_running = True
    while keep_running:
        clear()
        print(" Demonstrating Factorial ")
        print("-------------------------")
        print("1. Direct Factorial")
        print("2. Step-wise show Factorial")
        print("3. Go back to Main Menu")
        print("-------------------------")
        choice = input("What do you want to see ? ")

        if not choice.isnumeric() or (int(choice) not in (1, 2, 3)):
            input("Invalid Choice :", choice, ". Please press enter to retry....")
            continue

        choice = int(choice)

        if choice == 1:
            num = int(input("\nEnter number to calculate factorial : "))
            print("\nResult :", fact(num))
        elif choice == 2:
            num = int(input("\nEnter number to calculate factorial : "))
            print("\nStep-wise factorial : ")
            print("\n\nResult :", fact(num, True))
        else:
            break
        keep_running = not ask_continue("Press enter to continue... [Enter Y for main menu]: ")

def calculator():
    clear()
    print("Caculator Program Demo.")
    print("First provide values to apply operations on: ")
    val1 = int(input("Value 1: "))
    val2 = int(input("Value 2: "))
    print("Available operations : ")
    print("-----------------------")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("-----------------------")
    choice = input("\nEnter your choice: ")
    if not choice.isnumeric() or (int(choice) not in (1, 2, 3, 4)):
        raise ValueError("Invalid Choice :", choice, ". Please press enter to retry....")
    
    if choice == "1":
        print("Addition :", val1+val2)
    elif choice == "2":
        print("Subtraction :", val1-val2)
    elif choice == "3":
        print("Multiplication :", val1*val2)
    elif choice == "4":
        print("Division :", val1/val2)

def calculator():
    clear()
    print("Caculator Program Demo.")
    print("First provide values to apply operations on: ")
    val1 = int(input("Value 1: "))
    val2 = int(input("Value 2: "))
    print("Available operations : ")
    print("-----------------------")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("-----------------------")
    choice = input("\nEnter your choice: ")
    if not choice.isnumeric() or (int(choice) not in (1, 2, 3, 4)):
        raise ValueError("Invalid Choice :", choice, ". Please press enter to retry....")
    
    if choice == "1":
        print("Addition :", val1+val2)
    elif choice == "2":
        print("Subtraction :", val1-val2)
    elif choice == "3":
        print("Multiplication :", val1*val2)
    elif choice == "4":
        print("Division :", val1/val2)

def demonstrate_exception_handling():
    keep_running = True
    while keep_running:
        clear()
        print(" Demonstrating Exception Handling ")
        print("----------------------------------")
        print("1. Demo : Calculator")
        print("2. Back to Main Menu")
        print("----------------------------------")
        choice = input("What do you want to see ? ")

        if not choice.isnumeric() or (int(choice) not in (1, 2)):
            input("Invalid Choice :", choice, ". Please press enter to retry....")
            continue

        choice = int(choice)

        try :
            if choice == 1:
                calculator()
            else:
                break
        except Exception as e:
            print("Caught the exception :", e, "of type", type(e))
        keep_running = not ask_continue("Press enter to continue... [Enter Y for main menu]: ")

keep_running = True
while keep_running:
    clear()
    print("-------------------------")
    print("       Main Menu ")
    print("-------------------------")
    print("1. Queues")
    print("2. Dictionary")
    print("3. Set Operations")
    print("4. Finding Factorials")
    print("5. Exception Handling")
    print("6. Exit")
    print("-------------------------")
    choice = input("Please enter a choice : ")
    print("-------------------------")

    try:
        if not choice.isnumeric() or (int(choice) not in (1, 2, 3, 4, 5, 6)):
            raise ValueError("Invalid Choice : "+choice)

        choice = int(choice)
        if choice == 1:
            demonstrate_queues()
        elif choice == 2:
            demonstrate_dictionary()
        elif choice == 3:
            demonstrate_sets()
        elif choice == 4:
            demonstrate_factorial()
        elif choice == 5:
            demonstrate_exception_handling()
        else:
            break
    except NotImplementedError as e:
        input(str(e)+"\n\nPress enter to continue...")
    except Exception as e:
        print("\n!! ERROR : "+str(e)+" !!")
        input("\n\nRedirecting to Main Menu... Press enter to continue...")
    
print("\n\nThank you for using this program. Do come back again !\n\n")
