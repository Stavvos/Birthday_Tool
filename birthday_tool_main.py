import birthday_tool
from datetime import date 

def main():
	
	people_array = []
	people_array = read_file(people_array)
	birthday_finder(people_array)
	



def read_file(people_array):
	
	input_file = open('Place file path for birthdays.txt file here', "r")
	
	for line in input_file:
		count = 0
		
		selection_algorithm(line, count, people_array)
	
	input_file.close()
	
	return people_array
	
def selection_algorithm(line, count, people_array):
	
	name = ""
	day = 0
	month = 0
	
	for word in line.split():
			
		if word.isalpha():
			name = word
			count = 1
		elif count == 1:
			day = word
			count = 2
		elif count == 2:
			month = word
			count = 0
	
	if name != "" and day != 0 and month != 0: 
		person = birthday_tool.Person(name,day,month)
		people_array.append(person)
	
def birthday_finder(people_array):
	today = date.today()
	
	formattedDate = today.strftime ("%d/%m")

	for i in range (len(people_array)): 
		
		comparisonDate = date(2022, int(people_array[i].get_month()), int(people_array[i].get_day()))
		
		if comparisonDate.strftime("%d/%m") == formattedDate:
			print( people_array[i].get_name() , "'s birthday is today", comparisonDate)


def display_people_array(people_array):
	for i in range (len(people_array)):
		display_person(people_array[i])

def display_person (birthday_tool):
	print()
	print ("Name: ", birthday_tool.get_name())
	print ("Day: ", birthday_tool.get_day())
	print ("Month: ", birthday_tool.get_month(), "\n")
	
main()

