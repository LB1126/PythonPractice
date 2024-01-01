string = input('give me a string: ')
index = int(input('give me the index of that string: '))
if index < len(string) and string != '':
	print(f'the letter that I picked using the index you gave me was {string[index - 1]}')
elif string == '':
	print('the string you gave was empty')
elif index > len(string):
	print('the index you gave was out of range')
