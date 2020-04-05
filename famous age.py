#want this to take a famous person as input and return current age
import urllib.request

personname = "einstein"
personurltext = "https://www.google.com/search?q=" + personname + "+date+of+birth"
personurl = urllib.request.urlopen(personurltext)
persondata = personurl.read()
personbday = '<div class="Z0LcW">'
personcurrentage = 0
def inputPerson (personname):
	print ("Who would you like to know the age of?")
	personname = input()
	return personname

def findbday (persondata, personbday):
	date = "string"
	date = persondata.find(personbday)
	date = date.partition("<")
	personbday = date
	print("They were born on" + personbday + ".")
	return personbday

def findcurrentAge (personbday):
	from datetime import date
	todaysdate = date.today()
	todaysdate = todaysdate.string()
	difference = todaysdate - personbday
	differenceinyears = difference // 365
	return	differenceinyears


personname = inputPerson(personname)
personbday = findbday(persondata, personbday)
personcurrentage = findcurrentAge(personbday)
