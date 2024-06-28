# Kwizigama
# Inguzanyo
# Raporo
# Amafaranga Uzakira
# Kwemeza Inguzanyo

def Kwemeza():
	print()


def Amafaranga():
	print("Mwitsinda ..., uzakira " + "..." + "Frw muminsi 3 irimbere.")


def Raporo():
	print()


def Kwishura():
	print("Umubare w' amafaranga ushaka kwishura:")
	amafaranga =input()
	print("Shyiramo umubare w' ibanga wishyure " + str(amafaranga) + "Frw mwitsinda ...")
	umubare =int(input())
# if statement for the user password.
	print("Murakoze Kwishyura mwitsinda ...")


def Gusaba():
	print("Andika Umubare W' amafaranga:")
	amafaranga =input()
	print("Usabye " + str(amafaranga) + "Frw shyiramo umubare w' ibanga:")
	umubare =int(input())
# if statement for the user password.
	print("Tegereza umwanzuro uva kubayobozi bitsinda. ")


def Inguzanyo():
	Kuguzwa =["1) Gusaba Inguzanyo", "2) Kwishura Inguzanyo"]
	for a in Kuguzwa:
		print(a)
	choice =input()
	if (choice=="1"):
		Gusaba()
	elif (choice=="2"):
		Kwishura()
	else:
		print("Invalid choice")


def Kwizigama():
	print("Umubare w' amafaranga ushaka kuzigama:")
	global amafaranga
	amafaranga =input()
	print("Shyiramo umubare w' ibanga wemeze kwizigamira " + str(amafaranga) + "Frw mwitsinda ...")
	global umubare
	umubare =int(input())
# if statement for the user password.
	print("Murakoze kwizigamira mwitsinda ...")


def User(*User_option):
	for i in User_option:
		print(i)
User("1) Kwizigama", "2) Inguzanyo", "3) Raporo", "4) Amafaranga Uzakira", "5) Kwemeza Inguzanyo")

global choice
choice =input()

if (choice=="1"):
	Kwizigama()
elif (choice=="2"):
	Inguzanyo()
elif (choice=="3"):
	Raporo()
elif (choice=="4"):
	Amafaranga()
elif (choice=="5"):
	Kwemeza()
else:
	print("Invalid choice")

