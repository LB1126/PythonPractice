closed_brackets = input('Give me a set of brackets: ')
counter = 0
for x in closed_brackets:
	if x == '[':
		counter += 1
	else:
		counter -= 1
	if counter < 0: 
		print('False')
		break
if counter == 0:
	print('True')
