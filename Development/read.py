
def all_lands():
    """Opens the file and prints all the lands in the file"""
    #opensthe techno property file in read mode
    file = open('TechnoPropertyNepal.txt','r')
    print("\n\n\n"+"-"*130)
    print(' '*61+"All Lands")
    print('-'*130)
    print(" "*20+"Kitta Number"+" "*4+"Location"+" "*7+"Direction"+" "*6+"Aana"+" "*11+"Price"+" "*9+"Availability")
    print("-"*130)
    #for each line in the file, replaces the \n with blank space '' and then splits the word where there is ',' and then prints all the lines 
    for line in file.readlines():
        line = line.replace("\n",'').split(",")
        print(" "*20+line[0]+" "*(15-len(line[0]))+line[1]+" "*(15-len(line[1]))+line[2]+" "*(15-len(line[2]))+line[3]+" "*(15-len(line[3]))+line[4]+" "*(15-len(line[4]))+line[5])
    file.close()
def available_lands():
    """Opens the file and prints all the available lands only"""
    #Opens the techno property file in read mode
    file = open('TechnoPropertyNepal.txt','r')
    print("\n\n\n"+"-"*130)
    print(' '*58+"Available Lands")
    print('-'*130)
    print(" "*20+"Kitta Number"+" "*4+"Location"+" "*7+"Direction"+" "*6+"Aana"+" "*11+"Price"+" "*9+"Availability")
    print("-"*130)
    #for each line in the file, it replaces the \n with blank space, splits the word where there is ',' and then checks the availability of the land, if available prints the land in the terminal
    for line in file.readlines():
        line = line.replace("\n",'').split(",")
        if line[5].strip().lower() == "available":
            print(" "*20+line[0]+" "*(15-len(line[0]))+line[1]+" "*(15-len(line[1]))+line[2]+" "*(15-len(line[2]))+line[3]+" "*(15-len(line[3]))+line[4]+" "*(15-len(line[4]))+line[5])
    file.close()

def check_kitta(kitta):
    """Takes kitta as input,Opens the file and checks kitta, returns true if available """
    #Opens the file TechnoPropertyNepal in read mode
    file = open('TechnoPropertyNepal.txt','r')
    #for each line in the file,it replaces the \n with blank space then splits the words where there is ','.
    for line in file.readlines():
        line = line.replace("\n",'').split(",")
        #If the line is available and the user input is equals to the kitta number in the line, it returns true
        if line[5].strip().lower() == "available" and int(line[0])== kitta:
            return True
    file.close()

def return_check_kitta(kitta):
    """Opens the file and checks for kitta, returns true if not available"""
    #Opens the property file in read mode
    file = open('TechnoPropertyNepal.txt','r')
    for line in file.readlines():
        #for each line in the file, it replaces the \n with blank space then splits the words where there is ','
        line = line.replace("\n",'').split(",")
        #If the line is not available and the user input is equals to the kitta number in the line, it returns true
        if int(line[0]) == kitta and line[5].strip().lower() == "not available":
            return True
    file.close()

def read_lands():
    """Opens the TechnoPropertyNepal file in read mode and prints all the lines in the file"""
    #Opens the TechnoPropertyNepal file in read mode
    file = open('TechnoPropertyNepal.txt','r')
    lands = []
    for line in file.readlines():
        line.replace("\n",'').split(",")
        lands.append(line)
    return lands
