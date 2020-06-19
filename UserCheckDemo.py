print("\n \t ~ To Do List Demo ~ ")

print("Important: Password must be longer than 6 characters.")

user_dict = {}

username = input("Enter your desired username: ")
password = input("Enter your desired password: ")

hold = True #placeholder for the while loop
	
#This loop determines if the password fulfilled the character requirement.
while(hold):
	if len(password) < 6:
		print("Error: Password is not valid.")
		hold = False
		break
	else:
		user_dict[username] = password
		break

print(" ")

to_do_list = []

#After the user makes their decision,
#this function will execute the decision that they have made
def testLst():
	user_decision = input("Enter your decision: ").upper()
	hold = True
	while(hold):
		if user_decision == "A":
			userinput = input("Enter task: ")
			to_do_list.append(userinput)
			menu()

		if user_decision == "C":
			item_to_be_changed = int(input("Enter task number: "))
			replace = input("Enter new task: ")
			to_do_list[item_to_be_changed] = replace
			menu()

		if user_decision == "R":
			delete_item = int(input("Enter task number: "))
			del(to_do_list[delete_item])
			menu()

		if user_decision == "V":
			print(to_do_list)
			menu()
			
	
		if user_decision == "Q":
			print("To-Do-List Demo has ended. Goodbye.")
			break

def menu():
	print("""[A]dd item to the list\n[C]hange item\n[R]emove item\n[V]iew List\n[Q]uit """)
	testLst()

print("Welcome to Command Central.\nPlease enter your password again for further verification.")
password_check = input("Enter your password: ")

if password_check == password:
	print("What would you like to do today?")
	menu()
else:
	print("Error: Incorrect Password. Restart the program.")