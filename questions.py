def Test():
    print('Welcome to computer theoritical test.')
    choice = input('Do you want to pass the test? Type Q to quit and anything to continue: ')
    if choice == 'q' or choice == 'Q':
        quit()

    else:
        first_name = input('What is your First_name?: ')
        last_name = input('what is your last_name?: ')
        id = input('what is your student ID?: ')
        print('')
        print('The Test is made of short answer and true of false questions.')
        print('Please attempt all questions')
        print('')
        r = input('READY?: ').lower()
        if r != 'yes':
            print('We are sorry not to see you taking this test.')
            print('Feel free to take it later when you are ready.')
            quit()
        
        score = 0

        while True:
            answer1 = input('What does CPU stand for?: ').lower()
            if answer1 == 'central precessing unit':
                score +=1

            else:
                pass
            print('')
            answer2 = input('what does ROM stand for?: ').lower()
            if answer2 == 'read only memory':
                score+=1
            else:
                pass
            print('')
            answer3 = input('What does RAM stands for?: ').lower()
            if answer3 == 'Random access memory':
                score +=1

            else:
                pass
            print('')
            answer4 = input(' Which Computer Unit Performs all Mathematical and Logical Functions: ').lower()

            if answer4 == 'central precessing unit' or answer4 == 'cpu':
                score +=1

            else:
                pass
            print('')

            answer5 = input('What does ALU stands for?: ').lower()
            if answer5 == 'Arithmetic Logic Unit':
                score +=1

            else:
                pass
            print('')
            answer6 = input('which computer program that runs on computer when computer boots up?: ')
            if answer6 == 'operating system':
                score+=1

            else:
                pass

            print('')
            answer7 = input('What Type of Devices are Keyboard, Mouse, and Joystick? ').lower()
            if answer7 == 'input devices':
                score+=1

            else:
                pass

            print('')
            answer8 = input('Which type of Software are MS Excel, MS PowerPoint, and MS Word?: ').lower()
            if answer8 == 'application software':
                score +=1

            else:
                pass

            print('')
            answer9 = input('Which Company made Windows Operating System?: ').lower()
            if answer9 == 'microsoft' or answer9 == 'microsoft corporation':
                score +=1
            else:
                pass

            print('')
            answer10 = input('Which Computer Memory Stores Data “Temporarily: ').lower()
            if answer10 == 'random access memory' or answer10 == 'ram':
                score+=1

            else:
                pass
            print('')
            print('Thank you for sitting for the text up to end.')
            print('Name: ', first_name, last_name)
            print('Student ID: ', id)
            print('You got', score, 'in 10 attempts.')
            if score < 0:
                print(first_name, 'shame on you!!')
            else:
                print('GOOD ATTEMPT!!')
            print('')
            retake = input('Do you want to retake the exam?: ').lower()
            if retake != 'yes':
                quit()
            else:
                continue
