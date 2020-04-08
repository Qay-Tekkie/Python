import random
import string

user_list = []

def program_start():
    user_details = {}

    first_name = input('Enter your first name: ')
    last_name = input ('Enter your last name: ')
    email = input('Enter your email address: ')

    pass1 = first_name[0:2]
    pass2 = last_name[-2:]

    def random_letters(stringLenght = 5):
        letters = string.ascii_lowercase
        return (''.join(random.choice(letters) for i in range(stringLenght)))
    

    pass3 = random_letters(5)
    password = pass1 + pass2 + pass3

    verify = input(f'Do you want > {password} < as your password?(yes/no) ')

    if verify.lower() == 'yes':
        print('***************************************************')
        print(first_name + ' ' + ' ' + last_name) 
        print(email + ' ' + ' ' + password)
        print('**************************************************')

    elif verify.lower() == 'no':
        new_password = input('Enter your password: ')

        input_count = 0
        while len(new_password) < 7:
            print('passwords must have at least 7 characters')
            new_password = input('Enter your password: ')
            input_count +=1
            if len(new_password) == 7:
                break
        else:
            print('***************************************************')
            print(first_name + ' ' + ' ' + last_name) 
            print(email + ' ' + ' ' + new_password)
            print('**************************************************')
    else:
        print('Enter a yes/no')

    user_details.update({
    'First name': first_name,
    'Last name': last_name,
    'Email': email
    })

    if verify.lower() == 'yes':
        user_details.update({'Password': password})
    else:
        user_details.update({'Password': new_password})
    
    user_list.append(user_details)
    program_end = input('Do you wish to quit?(yes/no) ')


    if program_end.lower() == 'no':
        program_start()
    

program_start()  
      
print(user_list)



   







