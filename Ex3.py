str_user = input('Please enter a string: ')
reversed_list = []
for i in range((len(str_user) -1), -1, -1):
    reversed_list.append(str_user[i])
print(''.join(reversed_list))