import read
import write
def input_month_rented():
    """
    This function takes user input for the number of months rented and 
    returns the month after it satisfies the condition.
    The condition is that the month should be between 1 and 12.
    """
    # Variable for the loop until the input is valid
    month_check = True
    
    while month_check:
        try:
            # Taking user input for the number of months rented
            month = int(input("Enter the no of month's rented : "))
            
            # If the input is greater than 12 and less than 0, print error message
            if month > 12 or month <= 0:
                print("Invalid Input, Months rented must be between 1-12.")
            else:
                # If input is valid, return month 
                month_check = False
                return month
        except:
            # If input is invalid, prints error message and ask user to try again
            print("Invalid Input, Please try again")
            
def input_month_returned():
    """
    This function takes user input for the number of months after returned
    and returns the month if the month is positive and greater than 0 
    """
    # Variable to loop until the input is valid
    check = True
    
    while check:
        try:
            # Taking input from the user for the number of months after returned
            month_returned = int(input("Enter the number of month after returned: "))
            
            # Checking if the input is greater than 0
            if month_returned > 0:
                # If input is valid, return the month
                check = False
                return month_returned
            else:
                # If input is negetive, print error message and ask user to try again
                print("Please provide a positive number in returned months. ")
        except:
            # If input is invalid, print error message and ask user to try again
            print("Invalid months input, Please type in numbers again. ")

def input_kitta_rent():
    """used to take kitta and then check for its availability and returns true if it's available"""
    check = True
    while check:
        try:
            kitta = int(input("Enter kitta number of the land you want to rent: "))
            check_kitta = read.check_kitta(kitta)
            if check_kitta == True:
                check = False
                return kitta
            else:
                print("Kitta not available or not in the system, Please try again. ")
        except:
            print("Invalid Input in Kitta,Please try again")

def input_kitta_return():
    """
    This function takes user input for the kitta number of the land
    to be returned, checks its availability and returns true
    if it's not available and in the system.
    """
    # Variable to loop until the input is valid
    check = True
    while check:
        try:
            # Taking input from the user for the kitta number of the land
            kitta = int(input("Enter kitta number of the land you want to return: "))
            
            # Checking if the kitta number is available
            check_return_kitta = read.return_check_kitta(kitta)
            
            # If the kitta number is available, return it
            if check_return_kitta == True:
                check = False
                return kitta
            else:
                # If the kitta number is not in system or available, print error message and ask user to try again
                print("Either the kitta number has been returned or the kitta number is not in our system. Please check your kitta number and try again.")
        except:
            # If user input is invalid, print error message and ask user to try again
            print("Invalid input in Kitta number, Please try again")


def rent_lands():
    """
    This function is used to rent the land. It takes user input for kitta number and
    number of months rented. The function rents the land, updates the system and
    generates an invoice.
    """
    # Variable to loop until the user is done renting
    rent_land = True
    
    # Variable to loop until the kitta number is available
    kitta_available = True
    
    # Variable to loop until the user gives valid input if they want to rent more or not.
    rent = True
    
    # Lists to store kitta numbers and number of months rented
    kittas = []
    months = []
    
    # Taking user input for their full name
    name = input("Please type your full name: ")
   #looping until the user rents the land  
    while rent_land:
        # Looping until the kitta number is available
        while kitta_available:
            # Taking user input for kitta number and number of months rented
            kitta = input_kitta_rent()
            month = input_month_rented()
            #Adding the kitta number and no of months to the list
            kittas.append(kitta)
            months.append(month)
            
            # Updating the system and changing the availability of the kitta number user input to not available
            write.update_rent_lands(kitta)
            
            # Looping until the user doesnt gives a valid answer
            rent = True
            while rent == True:
                # Taking user input to rent another land or not
                rent_more = input("Do you want to rent another land?(y/n): ").lower()
                if rent_more == 'yes' or rent_more == 'y':
                    # If user wants to rent another land, resetting variables
                    kitta_available = True
                    rent_land = True
                    rent = False
                elif rent_more == 'no' or rent_more == 'n':
                    # If user is done renting, generating invoice and ending the loops
                    kitta_available = False
                    rent_land = False
                    rent = False
                    print("Generating Invoice...")
                    write.rent_invoice(name,kittas,months)
                    
                    # Taking garbage input to go to home screen
                    garbage = input("Press Enter key to go to Home Screen")
                else:
                    # If user inputs invalid input, printing error message
                    print("Please type a valid input and try again")
                    rent = True
                    
            
                               
def return_lands():
    """
    This function takes user input for the kitta number, number of months rented and number of months after returned,
    updates the system, generates an invoice.
    """
    # Lists to store kitta numbers, number of months rented and number of months after returned
    months_rented = []
    months_returned = []
    kittas = []

    # Variables to loop until the user is done returning lands
    return_land = True
    return_more = True
    
    # Taking user input for their full name
    name = input("Please enter your full name: ")

    # Looping until the user is done returning lands
    while return_land == True:
        # Taking user input for kitta number, number of months rented and number of months after returned
        kitta = input_kitta_return()
        month_rented = input_month_rented()
        month_returned = input_month_returned()

        # Adding the kitta number, number of months rented and number of months after returned to their corresponding list
        kittas.append(kitta)
        months_rented.append(month_rented)
        months_returned.append(month_returned)

        # Updating the system and changing the availability of the kitta number user input to available.
        write.update_returned_kitta(kitta)

        return_more = True
        # Looping until the user doesnt gives a valid answer
        while return_more:
            # Taking user input to return another land or not
            return_more = input("Do you want to return another land? (y/n) : ").lower()
            if return_more == 'yes' or return_more == 'y':
                # If user wants to return another land, resetting variables
                return_land = True
                return_more = False
            elif return_more == 'no' or return_more == 'n':
                # If user is done returning, generating invoice and ending the loops
                return_land = False
                return_more = False
                print("Generating Invoice...")
                write.return_invoice(name,kittas,months_rented,months_returned)
                garbage = input("Press Enter to go to home Screen")
            else:
                # If user input is invalid input, printing error message
                print("Please type yes or no and Please try again")

