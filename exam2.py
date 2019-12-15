
#exam2

number = int(input("Input a Num: "))
answer = 0

for i in range(1,number+1):
	if (i % 3 == 0 and i % 5 == 0):
		answer += 1
	elif (i % 3 == 0):
		pass
	elif (i % 5 == 0):
		pass
	else:
		answer += 1
		
print(answer)