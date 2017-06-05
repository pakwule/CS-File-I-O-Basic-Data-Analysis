#HW6 Preston Akwule
#Collaboration Statement: I worked on this assignment alone and used only this semesters course materials
from datetime import datetime
import csv
import urllib.request
import time

def improve_fight_song(replacement):
    ramblinFile = open("RamblinWreck.txt","r") #opens file up for read mode
    ramblinFileText = ramblinFile.read() #Stores all text lines in a list
    ramblinFile.close()
    if replacement == "":
        i = 0 #needed some random condition to make sure that the 2 conditions below are not carried out in the case of a null statement
    elif replacement[0] not in "aeiou":
        ramblinFileText = ramblinFileText.replace(" an "," a ")
        ramblinFileText = ramblinFileText.replace("engineer",replacement)
    elif replacement[0] in "aeiou":
        ramblinFileText = ramblinFileText.replace("engineer",replacement)
    ramblinFileText = ramblinFileText.splitlines() #Splits at every line
    newRamblinFile = open("ImprovedFightSong.txt","w")
    if replacement == "": #If the replacement is null then just write as usual but without looking for the replaced word
        for element in ramblinFileText:
            if "engineer" not in element:
                newRamblinFile.write("\t"+element+"\n")
            else:
                newRamblinFile.write(element+"\n")
    else:
        for element in ramblinFileText:
            if replacement not in element: #Now looking for lines that didnt have the replacement word/engineer to tab
                newRamblinFile.write("\t"+element+"\n")
            else:
                newRamblinFile.write(element+"\n")
    newRamblinFile.close()
   
def my_chat(sender,receiver,msg,time):
    chatlog = open("log.txt","a")
    time = time.strftime("%m/%d/%y %I:%M%p -- ")
    chatlog.write(str(time)+" From: "+sender+" To: "+receiver+"\n"+"Message: "+str(msg)+"\n")
    chatlog.write("\n")
    chatlog.close()
#Second test case breaks code

def song_by_artist(infoList):
    songfile = open("songInfo.txt","w")
    firstnames = []
    for element in infoList:
        if element[1] not in firstnames:
            firstnames.append(element[1])
    firstnames.sort()
    for musician in firstnames:
        songfile.write(musician+"\n")
        count = 1
        for element in infoList:
            if musician in element:
                songfile.write(str(count)+". "+element[0]+", "+str(element[2])+"\n")
                count += 1
        songfile.write("\n")
    songfile.close()


#fortune500.csv formatted at YEAR,RANK,COMPANY,REVENUEPERMILLION,PROITPERMILLION. Remember all entered as string

def top_companies(year,numofcompanies):
    filename = "fortune500.csv"
    with open(filename) as fortune500data: #Takes care of close step and names file as what you put after as
        reader = csv.reader(fortune500data) #Iterates through each row in data selected
        next(reader) #starts reader at the next line so we can skip the header
        rowcounter = 0
        companylist = []
        if year > 2009 or year < 1955 or type(numofcompanies) != int or numofcompanies < 0:
            return companylist
        if numofcompanies > 500:
            for row in reader:
                if int(row[0]) == year:
                    companylist.append(row[2])
            return companylist
        for row in reader:
            if rowcounter == numofcompanies:
                break
            if int(row[0]) == year:
                companylist.append(row[2])
                rowcounter +=1
    return companylist


def company_ranking(companyname, year):
    filename = "fortune500.csv"
    with open(filename) as fortune500data:
        reader = csv.reader(fortune500data)
        next(reader)
        companylist = []
        companyfinal = []
        for row in reader:
            if (int(row[0]) == year) and (row[2] == companyname):
                ranking = int(row[1])
                revenue = float(row[3].replace(",","")) #Removes the commas in the numbers
                profit = float(row[4].replace(",",""))
                companyfinal.append(ranking)
                companyfinal.append(revenue)
                companyfinal.append(profit)
                companylist.append(row[2])
        if companyname not in companylist:
            return None
    return tuple(companyfinal)


def company_average(companyname):
    filename = "fortune500.csv"
    with open(filename) as fortune500data:
        reader = csv.reader(fortune500data)
        next(reader)
        count = 0
        rankperyear = 0
        finallist = []
        for row in reader:
            if row[2] == companyname:
                rankperyear += int(row[1])
                count += 1
        if count == 0:
            return None
        companyaverage = round(float((rankperyear)/count),2)
        finallist = [companyaverage,count]
    return tuple(finallist)

def format_url(url, msg):
    return url+"?str={}".format(urllib.parse.quote(msg))


def encrypt_message(msg):
    site = format_url("http://cs1301.com/encrypt.php", msg)
    encryptsite = urllib.request.urlopen(site)
    encryptsite = encryptsite.read().decode('utf-8')
    return encryptsite
        

def decrypt_message(msg):
    site = format_url("http://cs1301.com/decrypt.php", msg)
    decryptsite = urllib.request.urlopen(site)
    decryptsite = decryptsite.read().decode('utf-8')
    return decryptsite
    
    
def my_chat_listen(filename):
    initial = open(filename,"r")
    initialcontent = initial.readlines()
    for line in initialcontent:
        print(line,end="")
    counter = 0
    while True:
        newcontent = initial.readline()
        if newcontent == "" or newcontent == "\n":
            continue
        print(newcontent, end="")
        time.sleep(1)
    initial.close()
        
def my_chat_send(filename):
    while True:
        filetowrite = open(filename,"a")
        whatToWrite = str(input("What would you like to say?"))+""
        filetowrite.write(whatToWrite)
        filetowrite.close()

    
                
                
        
