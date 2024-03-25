'''# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
   # Any code taken from other sources is referenced within my code solution.
   # Student ID:[IIT:- 20221476],[UoW:- w1956171]
   # Date: 20/11/2022'''

#-----------------------------------------------------------------------Part-4(Dictionary)-----------------------------------------------------------------------------

#Assigning variables for credit level inputs & total
credits_pass = 0
credits_defer = 0
credits_fail = 0
total = 0

dictionary = {}  #Opening an empty dictionary


def get_input(prompt_message):
    """This function is for the user input process"""
    global user_input  #Turning 'user_input' variable as a global variable
    values = [0, 20, 40, 60, 80, 100, 120]  #Assigning a variable for the list of valid input values
    while True:
        try: #Exceptional handeling
            user_input = int(input(prompt_message))  #Assigning a variable for user inputs
        except ValueError:
            print("An integer is required!\n")  #Error message for ValueError
            continue

        if user_input not in values:
            print("Your value is out of range!\n")  #Error message for invalid credit input
            continue
        else:
            break
    return user_input  #Returning the input value and save it for later process


def update_dictionary(outcome_str):
    """This function is to append data to the dictionary"""
    dictionary["w"+str(student_ID)] = outcome_str+str(credits_pass)+','+str(credits_defer)+','+str(credits_fail)  #Updating the empty dictionary with keys and values


loop_Get_ID = True  #Assigning a boolean variable for getting ID loop
while loop_Get_ID:
    try:   #Exceptional handeling
        student_ID = int(input("Enter student ID: w"))   #Assigning a variable for student ID input
        if len(str(student_ID)) != 7:   #Condition for the length of 'student_ID'
            print("INVALID ID!\n")   #Error message for invalid ID length
            continue
    except ValueError:
        print("ID Contains Only Numbers!\n")   #Error message for ValueError
        continue
    else:
        credits_input = True  #Asssigning a boolean variable for credits input loop
        while credits_input:
            #Calling 'get_input' function for 3 credit level inputs
            credits_pass = get_input("Enter total credits at PASS level: ")
            credits_defer = get_input("Enter total credits at DEFER level: ")
            credits_fail = get_input("Enter total credits at FAIL level: ")

            total = credits_pass + credits_defer + credits_fail   #Updating the 'total' variable  
            if total != 120:   #Condition for the total of credit levels
                print("Total Incorrect!\n")   #Error message for incorrect total
                continue
            else:
                if credits_pass == 120:  # Condition for outcome-1
                    print("=>Progress\n")
                    update_dictionary("Progress - ")  # Calling 'update_dictionary' function for 1st argument

                elif credits_pass == 100:  # Condition for outcome-2
                    print("=>Progress (module trailer)\n")
                    update_dictionary("Progress (module trailer) - ")  # Calling 'update_dictionary' function for 2nd argument

                elif credits_fail >= 80:  # Condition for outcome-3
                    print("=>Exclude\n")
                    update_dictionary("Exclude - ")  # Calling 'update_dictionary' function for 3rd argument

                else:  # Condition for outcome-4
                    print("=>Do not Progress (module retriever)\n")
                    update_dictionary(
                        "Do not Progress (module retriever) - ")  # Calling 'update_dictionary' function for 4th argument

                loop_multiple = True   #Assigning a boolean variable for multiple outcomes loop
                print('Would you like to enter another set of data?')
                while loop_multiple:
                    decision = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()  #Assigning a variable for decision input

                    if decision == 'y':  #Condition for the 1st decision
                        print()
                        loop_multiple = False #Closing multiple outcomes loop
                        credits_input = False #Closing credits input loop
                        loop_Get_ID = True #Activating getting ID loop

                    elif decision == 'q':  #Condition for the 2nd decision
                        print('-' * 64)
                        print("PART 4:\n")
                        for dic_items in dictionary.keys():  # This for loop is to access the keys of the updated 'dictionary'
                            print(dic_items, ':', dictionary[dic_items])  # Printing key:value pairs in the dictionary

                        loop_multiple = False  #Closing multiple outcomes loop
                        credits_input = False  #Closing credits input loop
                        loop_Get_ID = False  #Closing getting ID loop

                    else:
                        print('Invalid Input!\n') #Error message for invalid decision input
                        continue








