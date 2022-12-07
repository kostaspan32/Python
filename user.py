import json
cnt = 0
with open('users.json') as f:
    users = json.load(f)

username = input('Please type your username: ')

while True:
    for user in users:
        if username == user['Username: ']:
            cnt += 1
            password = input('Please type your password: ')
            while password != user['Password: ']:
                password = input('Wrong password, try again! : ')
            if user['Role: '] == 'admin':
                print('Welcome admin! ')

            else:
                print(f'Welcome {user["Full Name: "]}')

    if cnt == 1:
        break

    else:
        username = input('Username not found, please try again! : ')

