
# Care or Ikibinta

# name
# 3 Admins
# R.members
# Rules
# working
# Details(profit, parcentage, delay cost)
#delete

def Gusiba():
	print("Izina ry' Ikibinta:")
	izina =input()
	print("Code y' Ikibinta:")
	code =input()
	input("Shyiramo umubare w' ibanga usibe ....")
	print("Wemeje gusiba ikibinta cyitwa ... gifite code ....")
# izina ry' ikibinta
# code ry' ikibinta


def Gushinga():
	print("Izina ry' Ikibinta:")
	name =str(input())
	umuyobozi =input("Umukuru w' Itsinda:")
	
	
	umuyobozi2 =input("Uwungirije umukuru w' Itsinda:")
	
	umuyobozi2 =input("Umunyamabanga:")


def Ikibinta():
	Option =["1) Gushinga Ikibinta", "2) Gusiba Ikibinta"]
	for c in Option:
		print(c)
	hitamo =str(input())
	if (hitamo=="1"):
		Gushinga()
	elif (hitamo=="2"):
		Gusiba()
	else:
		print("Invalid choice")

def Acc(*Acctype):
	for b in Acctype:
		print(b)
Acc("1) Serivise zi Ikibinta", "2) Serivise za Care")

choice =input()
if (choice=="1"):
	Ikibinta()
elif (choice=="2"):
	Care()
else:
	print("Invalid choice")
