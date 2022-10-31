print("-"*19,"ИГРА",18*"-")
print("-"*15,"УГАДАЙ ЧИСЛО",14*"-")
print("-"*43)
print("""привет давай поиграем в игру,я буду загадывать число в таком диапазоне в котором ты скажешь,а ты попытаешься отгадать это число,удачи!""")
print("-"*43)

#####################

import random #генерцая случацного числа
digit=0  #загаданное число пк
lowdigit=0 #мин.число загаданное
highdigit=0 #макс.число загаданное
popitki=0 #кол-во попыток угалать
startScore=100 #начальное число очков
score=0 #текущее кол-во очков
maxScore=0 #максимальное кол-во очков за игру
win=False
playGame=True
x=0 #число написанное пользователем

#####################

while(playGame):
	lowdigit=" "
	while(not lowdigit.isdigit()):
		lowdigit=input("введите минимальное загаднное числа:")
		if(not lowdigit.isdigit()):
			print("."*12,"Введите число,пожалуйста.")
	lowdigit=int(lowdigit)
	highdigit=" "
	while(not highdigit.isdigit()):
		highdigit=input("Введите максимальное загаднное число:")
		if(not highdigit.isdigit()):
			print("."*12,"Введите число,пожалуйста.")
	highdigit=int(highdigit)
	digit=random.randint(lowdigit,highdigit)
	if(digit<5):
		print("Ой,я перезагадал числo, шанс 5%")
		digit=(random.randint(lowdigit,highdigit))
		
	while(not win):
		x=" "
		while(not x.isdigit()):
			x=input(f"Введите число от {lowdigit} до {highdigit}:")
			if(not x.isdigit()):
				print("."*12,"Введите число,пожалуйста.")
		
		
		x=int(x)
		

		if (x != digit):
			bar=abs(x-digit)
			if(bar<3):
				print("."*20,"очень горячо!!!")
			elif(bar<5):
				print("."*20,"горячо!!!")
			elif(bar<=10):
				print("."*20,"тепло.")
			elif(bar<=15):
				print("."*20,"прохладно")
			elif(bar<=20):
				print("."*20,"холодно")
			else:
				print("пиздец холодно и далеко от числа")
		else:
				if (x==digit):
					print("-"*43)
					print("Поздравляем вы угадали число!")
					win=True
				
										
	if(input("start-сыграть еще,введи 0-выход:") == "0"):
		playGame=False
	else:
		win=False
		print("-"*43)
		


#####################
print("*"* 43)
print("""Спасибо что сыграл в меня!
возвращайся ещё!""")