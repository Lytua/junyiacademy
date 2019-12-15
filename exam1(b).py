
# exam1(b)

str = input("A String: ")
word_reverse = ""
str_answer = ""

for c in str:
	if c == " ":
		word_reverse += c
		str_answer += word_reverse		
		word_reverse = ""
	else:
		word_reverse = c + word_reverse
	
str_answer += word_reverse

print(str_answer)