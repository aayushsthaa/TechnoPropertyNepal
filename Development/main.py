import read
import operation
#Variable to loop the program until the usr tells to stop
loop = True
#Looping until the loop is true
while loop:
    try:
        read.all_lands()
        #Prints the choice user has on the screen
        print("\n1.Rent Lands \n2.Return Land \n3.Exit")
        #Taking the iunput from the user
        userin = int(input("Please choose a number from 1-3 : "))
        #If the user input is 1,it will execute the renting of the land
        if userin == 1:
            #Prints all the avialable lands
            read.available_lands()
            #Rents the land according to the user input
            operation.rent_lands()
        #If the user input is 2, it will execute the returning of the land
        elif userin == 2:
            #Returns the land according to the input given by user
            operation.return_lands()
        #If the user input is 3, it will exit the program
        elif userin == 3:
            loop = False
            #Else it will ask the user to type a valid input
        else:
            print("Please type a valid number from 1-3")
    #If the input is anyhting except a number, it will ask the user to type a valid input
    except:
        print("Please type a numeric value and try again")

