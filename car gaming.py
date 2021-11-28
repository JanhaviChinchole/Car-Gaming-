#Car gaming python programming

command=""
while command != "quit":
    command=input("Enter command: ")
    if command == 'start':
        print('car is started')
    elif command=="stop":
        print("car is stopped")
    elif command =="help":
        print(
            '''
            start = too start the car
            stop=too stop the car
            quit=to exit
            '''
        )
    elif command =='quit':
        break
    else:
        print('invalid command!')

