'''# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
   # Any code taken from other sources is referenced within my code solution.
   # Student ID:[IIT:- 20221476],[UoW:- w1956171]
   # Date: 20/11/2022'''

#-------------------------------------------------------------------------Part-1(Main Version)--------------------------------------------------------------------------

#Assigning histogram counting variables
progress = 0
trailer = 0
retriever = 0
excluded = 0
counter = 0

#Assigning variables for credit level inputs & total
credits_pass = 0
credits_defer = 0
credits_fail = 0
total = 0

data_list = []  #Opening an empty list for part-2
dictionary = {}  #Opening an empty dictionary for part-4 


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


def appending(outcome_str):
    """This function is to append data to the empty list and dictionary"""
    data_list.append([outcome_str, credits_pass, ',', credits_defer, ',', credits_fail])  #Appending data to the empty list
    dictionary["w"+str(student_ID)] = outcome_str+str(credits_pass)+','+str(credits_defer)+','+str(credits_fail)  #Updating the empty dictionary with keys and values


main_loop = True  #Assigning a boolean variable for main loop
print("PART 1:\n")
while main_loop:
    option = input("\t\tEnter '1' to Open Student Version\n"  #Assigning a variable for option input
                   "\t\tEnter '2' to Open Staff Version\n"
                   "\t\tEnter '3' to End the program\n"
                   "\nEnter the option: ")
    print('~' * 80)

    if option == '1':  #Condition for option 1
        loop_student_v = True  #Assigning a boolean variable for student version loop
        print("|||STUDENT VERSION|||\n")
        while loop_student_v:
            #Calling 'get_input' function for 3 credit level inputs
            credits_pass = get_input("Please enter your credits at PASS level here: ")
            credits_defer = get_input("Please enter your credits at DEFER level here: ")
            credits_fail = get_input("Please enter your credits at FAIL level here: ")

            total = credits_pass + credits_defer + credits_fail  #Updating the 'total' variable
            if total != 120:  #Condition for the total of credit levels
                print("=>Total Incorrect!\n")  #Error message for incorrect total
                continue
            else:
                if credits_pass == 120:   #Condition for outcome-1
                    print("=>Progress\n")

                elif credits_pass == 100:  #Condition for outcome-2
                    print("=>Progress (module trailer)\n")

                elif credits_fail >= 80:   #Condition for outcome-3
                    print("=>Exclude\n")

                else:   #Condition for outcome-4
                    print("=>Do not Progress (module retriever)\n")
            loop_student_v = False  #Closing the student version loop

    elif option == '2':  #Condition for option 2
        print("|||STAFF VERSION|||\n")
        loop_Get_ID = True  #Assigning a boolean variable for getting ID loop
        while loop_Get_ID:
            try:  #Exceptional handeling
                student_ID = int(input("Enter student ID: w"))  #Assigning a variable for student ID input
                if len(str(student_ID)) != 7:  #Condition for the length of 'student_ID'
                    print("INVALID ID!\n")  #Error message for invalid ID length
                    continue
            except ValueError:
                print("ID Contains Only Numbers!\n")  #Error message for ValueError
                continue
            else:
                loop_Get_ID = False  #Closing the getting ID loop

            loop_staff_v = True  #Assigning a boolean variable for staff version loop
            while loop_staff_v:
                #Calling 'get_input' function for 3 credit level inputs
                credits_pass = get_input("Enter total credits at PASS level: ")
                credits_defer = get_input("Enter total credits at DEFER level: ")
                credits_fail = get_input("Enter total credits at FAIL level: ")

                total = credits_pass + credits_defer + credits_fail  #Updating the 'total' variable
                if total != 120:  #Condition for the total of credit levels
                    print("Total Incorrect!\n")  #Error message for incorrect total
                    continue
                else:
                    if credits_pass == 120:   #Condition for outcome-1
                        print("=>Progress\n")
                        appending("Progress - ")  #Calling 'appending' function for 1st argument
                        progress += 1  #Updating progress count
                        counter += 1  #Updating total outcomes count

                    elif credits_pass == 100:  #Condition for outcome-2
                        print("=>Progress (module trailer)\n")
                        appending("Progress (module trailer) - ")  #Calling 'appending' function for 2nd argument
                        trailer += 1  #Updating trailer count
                        counter += 1  #Updating total outcomes count

                    elif credits_fail >= 80:   #Condition for outcome-3
                        print("=>Exclude\n")
                        appending("Exclude - ")  #Calling 'appending' function for 3rd argument
                        excluded += 1  #Updating excluded count
                        counter += 1  #Updating total outcomes count

                    else:   #Condition for outcome-4
                        print("=>Do not Progress (module retriever)\n")
                        appending("Do not Progress (module retriever) - ")  #Calling 'appending' function for 4th argument
                        retriever += 1  #Updating retriever count
                        counter += 1  #Updating total outcomes count

                    loop_multiple = True #Assigning a boolean variable for multiple outcomes loop
                    print('Would you like to enter another set of data?')
                    while loop_multiple:
                        decision = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()  #Assigning a variable for decision input

                        if decision == 'y':  #Condition for the 1st decision
                            print()
                            loop_multiple = False  #Closing multiple outcomes loop
                            loop_staff_v = False  #Closing staff version loop
                            loop_Get_ID = True  #Activating getting ID loop
                            
                        elif decision == 'q':  #Condition for the 2nd decision
                            print("\n" + "-" * 64 + "\n>>Histogram<<\n\nProgress ", progress, "\t:", "*" * progress, end="")
                            print("\nTrailer ", trailer, "\t:", "*" * trailer, end="")
                            print("\nRetriever ", retriever, "\t:", "*" * retriever, end="")
                            print("\nExcluded ", excluded, "\t:", "*" * excluded, end="\n\n")
                            print(counter, "outcome(s) in total\n" + "-" * 64)
                            loop_multiple = False   #Closing multiple outcomes loop
                            loop_staff_v = False  #Closing staff version loop
                            loop_Get_ID = False  #Closing getting ID loop

#-----------------------------------------------------------------------Part-2(List)-------------------------------------------------------------------------------

                            print('PART 2:\n')
                            for nested_lists in data_list:  #This for loop is to access the nested lists of the appended 'data_list'
                                for elements in nested_lists:  #This for loop is to access the elements of each nested list
                                    print(elements, end='')
                                print() #This print statement is to break sets of elements
                            print('\n' + '-' * 64)

#---------------------------------------------------------------------Part-3(Text File)----------------------------------------------------------------------------

                            text_file = open('records.txt', 'w')  #Assigning a variable to open a text file(In writing mode) 
                            text_file.write("PART 3:\n")
                            for nested_lists in data_list:  #This for loop is to access the nested lists of the appended 'data_list'
                                text_file.write('\n')  #This new line character is to break sets of elements
                                for elements in nested_lists:   #This for loop is to access the elements of each nested list
                                    text_file.write(str(elements))
                            text_file.close()  #Closing the text file

                            #Opening previous text file for reading & automatic file closing through context manager
                            with open('records.txt', 'r') as text_file: 
                                data = text_file.read() #Assigning a variable to read data in the text file
                            print(data)
                            print('\n' + '-' * 64)

#---------------------------------------------------------------------Part-4(Dictionary)---------------------------------------------------------------------------
#---------------------------------------------------------This part has also done in a separate program------------------------------------------------------------
                            print("PART 4:\n")
                            for dic_items in dictionary.keys():  #This for loop is to access the keys of the updated 'dictionary'
                                print(dic_items, ':', dictionary[dic_items]) #Printing key:value pairs in the dictionary
                            print()
                        else:
                            print('Invalid Input!\n')  #Error message for invalid decision input
                            continue

    elif option == '3':   #Condition for option 3
        print("Program Ended Successfully...\nThank You!")
        main_loop = False  #Closing main loop
    else:
        print("Invalid Option!\n") #Error message for invalid option input
        continue









