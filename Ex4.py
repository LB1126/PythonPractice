str_user = input('Please enter a string: ')
new_string = str_user[:3] + str_user[len(str_user)-3:]
if len(str_user) > 5:
    print(new_string)
else:
    print('')