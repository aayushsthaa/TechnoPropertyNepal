from datetime import datetime
import read
def update_rent_lands(kitta):
    """Takes in kitta,Opens the technoproperty file to change the given kitta from available to not available"""
    #Getting all the lands
    lines = read.read_lands()
    #Opens the property file in writre mode 
    file = open('TechnoPropertyNepal.txt', 'w')
    #For each line in lines 
    for line in lines:
        #In each line it'll split the line and splits the line into parts where there is ','
        parts = line.strip().split(',')
        #if the kitta in parts matches the kitta given by user
        if int(parts[0]) == kitta:
            #Updating the line to not available 
            update_line = parts[0] + ',' + parts[1] + ',' + parts[2] + ',' + parts[3] + ',' + parts[4] + ', Not Available\n'
            #writing the line in the file
            file.write(update_line)
        else:
            #If its not the kitta number given by the user, writing the line without updating in the file
            file.write(line)
    file.close()

def rent_invoice(name,kittas,months):
    """Takes name,kittas,months and combines them with time to form a unique invoice which includes all the rented land details and total price"""
    #Takes in the date and time from the system
    now = datetime.now()
    #Changes the date and time to only hour,minute and second
    current_time = str(now.strftime("%H"+"_"+"%M"+"_"+"%S"))
    #Set the total price to 0
    total_price = 0
    #Set the total display price to 0 
    total_price_display = 0
    #Generates a unique file name by combining name, kitta numbers the user buyed and the current date and time 
    invoice_name = 'Invoice_Rent_'+name
    for i in kittas:
        invoice_name = invoice_name+"_"+str(i)
    invoice_name = invoice_name+"_"+current_time+".txt"
    #Opens the invoice file with the unique invoice name in write mode 
    invoice_file = open(invoice_name,'w')
    #writes the top part of the invoice with name and time in the bill
    invoice_file.write("-"*98+"\n")
    invoice_file.write(" "*33+"Techno Property Nepal Rental Invoice"+"\n")
    invoice_file.write("-"*98+"\n")
    invoice_file.write("Renter's Name = "+ name+" "*(40-len(name))+"Date and time = "+str(now)+"\n\n\n")
    invoice_file.write("Kitta Number"+" "*3+"Location"+" "*7+"Direction"+" "*6+"Aana"+" "*6+"Price"+" "*8+"Months Rented"+" "*4+"Monthly Total" "\n")
    invoice_file.write("-"*98+"\n")
    #Loops for each kitta number in the list
    for i in range(len(kittas)):
        #for each line in the lands list
        for lines in read.read_lands():
            #Replaces the \n with blank space and splits word where there is ','
            line = lines.replace("\n",'').split(", ")
            #restts the monthly total price 
            monthly_total = 0
            #if kitta matches with lines kitta write the line in the file with monthly ptice
            if int(line[0])== kittas[i]:
                    monthly_total +=int(line[4])*int(months[i])
                    invoice_file.write(line[0]+" "*(14-len(line[0]))+line[1]+" "*(15-len(line[1]))+line[2]+" "*(15-len(line[2]))+line[3]+" "*(10-len(line[3]))+line[4]+" "*(14-len(line[4]))+str(months[i])+" "*(17-len(str(months[i])))+str(monthly_total)+"\n")
                    invoice_file.write("-"*98+"\n")
                    total_price +=monthly_total
    #write the total price in the file 
    invoice_file.write("Total Price = " + str(total_price)+"\n")
    invoice_file.close()
    #print the top of invoice in the screen
    print("-"*98+"\n")
    print(" "*33+"Techno Property Nepal Rental Invoice"+"\n")
    print("-"*98+"\n")
    print("Renter's Name = "+ name+" "*(40-len(name))+"Date and time = "+str(now)+"\n\n\n")
    print("Kitta Number"+" "*3+"Location"+" "*7+"Direction"+" "*6+"Aana"+" "*6+"Price"+" "*8+"Months Rented"+" "*4+"Monthly Total" "\n")
    print("-"*98+"\n")
    lands = read.read_lands()
    #for each kitta in kittas list
    for i in range(len(kittas)):
        #for each line in lands list
        for line in lands:
            #Replaces the \n with blank space and splits word where there is ','
            lines = line.replace("\n",'').split(",")
            #reset the monthly total price 
            monthly_total = 0
            #Prints the land if the kitta number matches
            if int(lines[0])== kittas[i]:
                monthly_total +=int(lines[4])*int(months[i])
                print(lines[0]+" "*(14-len(lines[0]))+lines[1]+" "*(15-len(lines[1]))+lines[2]+" "*(15-len(lines[2]))+lines[3]+" "*(10-len(lines[3]))+lines[4]+" "*(14-len(lines[4]))+str(months[i])+" "*(17-len(str(months[i])))+str(monthly_total))
                print("-"*98+"\n")
                total_price_display +=monthly_total
    print("Total Price = " + str(total_price_display)+"\n")

def update_returned_kitta(kitta):
    """Takes kitta as input,opens the technoproperty file and changes the availability to available of the kitta given"""
    lines = read.read_lands()
    #opens the property file in write mode
    file = open('TechnoPropertyNepal.txt', 'w')
    #for each line in lines list
    for line in lines:
        #Changes the line and splits the line in parts where there is ','
        parts = line.strip().split(',')
        #if kitta matches the ktita given by user, change the availability to available
        if int(parts[0]) == kitta:
            update_line = parts[0] + ',' + parts[1] + ',' + parts[2] + ',' + parts[3] + ',' + parts[4] + ', Available\n'
            #write the line in the file
            file.write(update_line)           
        else:
            #Writes the lie as it is if its not the land user returned
            file.write(line)
    file.close()
    

def return_invoice(name,kittas,months_rented,months_returned):
    """Takes name,kittas,months_rented,months_returned as input and generates a unique invoice of all the lands returned and total price"""
    #takes dateand time from the system
    now = datetime.now()
    #creates a string of date and time
    current_time = str(now.strftime("%H"+"_"+"%M"+"_"+"%S"))
    #Stets the total price as 0
    total_price = 0
    #Stets the total display price as 0
    total_price_display = 0
    #Stets the remaining month to 0
    remaining_month = 0
    #Adds the name to the invoice name
    invoice_name = 'Invoice_Return_'+name
    #Adds all the kittas given by usder into file name
    for i in kittas:
        invoice_name = invoice_name+"_"+str(i)
    #Adds the current tiem to the file name
    invoice_name = invoice_name+"_"+current_time+".txt"
    #opens the unique invoice file with invoice name in write mode
    invoice_file = open(invoice_name,'w')
    #writes the top part of the invoice in the file 
    invoice_file.write("-"*150+"\n")
    invoice_file.write(" "*59+"Techno Property Nepal Return Invoice"+"\n")
    invoice_file.write("-"*150+"\n")
    invoice_file.write("Renter's Name = "+ name+" "*(92-len(name))+"Date and time = "+str(now)+"\n\n\n")
    invoice_file.write("Kitta Number"+" "*5+"Location"+" "*9+"Direction"+" "*8+"Aana"+" "*10+"Price"+" "*7+"Months Rented"+" "*7+"Months Returned"+" "*5+"Monthly Rent"+" "*8+"Extra Charge"+"\n")
    invoice_file.write("-"*150+"\n")
    #Loops for easch kitta given by user to return
    for i in range(0,len(kittas)):
        #loops for all the llands in the lands list
        for lines in read.read_lands():
            #Replaces the \n with blank space and splits word where there is ','
            line = lines.replace("\n",'').split(",")
            #Sets the monthly price to 0
            monthly_price = 0
            #Sets the extra charge to 0
            extra_charge = 0
            #Charges the monthly price according to months, if the kitta number matches
            if int(line[0])== kittas[i]:
                monthly_price += int(line[4])*months_returned[i]
                if months_rented[i] > months_returned[i] or months_rented[i] == months_returned[i]:
                    total_price += monthly_price                   
                elif months_rented[i] < months_returned[i]:
                    remaining_month = months_returned[i] - months_rented[i]
                    extra_charge = (0.1*int(line[4]))*remaining_month
                    total_price += monthly_price + extra_charge
                #Writes the land in the invoice file with all the monthly price and extra charge  
                invoice_file.write(line[0]+" "*(16-len(line[0]))+line[1]+" "*(17-len(line[1]))+line[2]+" "*(17-len(line[2]))+line[3]+" "*(14-len(line[3]))+line[4]+" "*(13-len(line[4]))+str(months_rented[i])+" "*(20-len(str(months_rented[i])))+str(months_returned[i])+" "*(20-len(str(months_returned[i])))+str(monthly_price)+" "*(20-len(str(monthly_price)))+str(extra_charge)+"\n")
                invoice_file.write("-"*150+"\n")
    #Writes the total price in the return file            
    invoice_file.write("Total Price = " + str(total_price)+"\n")
    invoice_file.close()
    #prints the invoice top part on the screen
    print("-"*130+"\n")
    print(" "*46+"Techno Property Nepal Return Invoice"+"\n")
    print("-"*130+"\n")
    print("Renter's Name = "+ name+" "*(72-len(name))+"Date and time = "+str(now)+"\n\n\n")
    print("Kitta Number"+" "*3+"Location"+" "*7+"Direction"+" "*6+"Aana"+" "*5+"Price"+" "*6+"Months Rented"+" "*2+"Months Returned"+" "*3+"Monthly Rent"+" "*3+"Extra Charge"+"\n")
    print("-"*130+"\n")
    #loops for all the lands given by user to return
    for i in range(0,len(kittas)):
        #loops for all the lands in the lands list
        for lines in read.read_lands():
            #splits the words where there is ',' and replaces \n with blank space
            line = lines.replace("\n",'').split(",")
            #Sets the montholy price to 0
            monthly_price = 0
            #Sets the extra charge to 0
            extra_charge = 0
            #if the kitta number of the line matches with the kitta number provided by the user, it will calculate the price and display the land on the screen
            if int(line[0])== kittas[i]:
                monthly_price += int(line[4])*months_returned[i]
                if months_rented[i] > months_returned[i]:
                    total_price_display += monthly_price
                elif months_rented[i] < months_returned[i]:
                    remaining_month = months_returned[i] - months_rented[i]
                    extra_charge += (0.1*int(line[4]))*remaining_month
                    total_price_display += monthly_price + extra_charge
                elif months_rented[i] == months_returned[i]:
                    total_price_display += monthly_price
                print(line[0]+" "*(14-len(line[0]))+line[1]+" "*(15-len(line[1]))+line[2]+" "*(15-len(line[2]))+line[3]+" "*(9-len(line[3]))+line[4]+" "*(12-len(line[4]))+str(months_rented[i])+" "*(15-len(str(months_rented[i])))+str(months_returned[i])+" "*(18-len(str(months_returned[i])))+str(monthly_price)+" "*(15-len(str(monthly_price)))+str(extra_charge)+"\n")
                print("-"*130+"\n")
    print("Total Price = " + str(total_price_display)+"\n")

