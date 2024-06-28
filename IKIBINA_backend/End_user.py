
# Kwizigama
# Inguzanyo
# Raporo
# Amafaranga Uzakira

def Guhindura_umubare_option():
	Guhindura_option_input =["1) Ukoresheje umubare w' ibanga", "2) Ukoresheje indangamuntu"]
	for e in Guhindura_option_input:
		print(e)
	Guhindura_choice =input()
	if (Guhindura_choice=="1"):
		Guhindura_umubare()
	elif (Guhindura_choice=="2"):
		SIM()
	else:
		print("Invalid choice")


def SIM():
	print("Shiramo numero nshya: ")
	Numero_nshya =input()
	print("Ongera uyishiremo: ")
	Numero_nshya2 =input()
	if(Numero_nshya==Numero_nshya2):
		print("Shiramo umubare w' ibanga:")
		umubare =int(input())
		print("Numero yawe y' itsinda ni" + str(umubare))
	else:
		print("Numero y' ibanga ntihura, Ongera usubiremo")
		SIM()
	
	

def Guhindura_umubare():
	print("Shiramo umubare w' ibanga munshya: ")
	umubare_munshya =input()
	print("Ongera uyishiremo umubare w' ibanga munshya: ")
	umubare_munshya2 =input()
	if(umubare_munshya==umubare_munshya2):
		print("Shiramo umubare w' ibanga USANGANWE:")
		umubare =int(input())
		print("Umubare w' ibanga wahinduwe")
	else:
		print("Umubare w' ibanga ntihura, Ongera usubiremo")
		Guhindura_umubare()

	

def Konti():
	print("Ikaze muri Konti yawe: ")
	Konti_option =["1) Guhindura umubare w'ibanga", "2) Guhindura SIM"]
	for e in Konti_option:
		print(e)
	Guhindura =input()
	if (Guhindura=="1"):
		Guhindura_umubare_option()
	elif (Guhindura=="2"):
		SIM()
	else:
		print("Invalid choice")


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
	print("Murakoze kwizigamira mwitsinda ...")
# if statement for the user password.
	


def User(*User_option):
	for i in User_option:
		print(i)
User("1) Kwizigama", "2) Inguzanyo", "3) Raporo", "4) Amafaranga Uzakira","5) Konti yanjye y' ITSINDA","6) Ibyemezo bitaranozwa")

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
	Konti()
elif (choice=="6"):
	Ibyemezo()
else:
	print("Invalid choice")
