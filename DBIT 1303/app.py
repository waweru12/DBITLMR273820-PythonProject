import time
def func(seconds):
    '''
    >>> func(9)
    Yields the countdown in seconds.
    '''
    for i in range(seconds):
        print(str(seconds-i),end="\r")
        time.sleep(1)


def intro():
    '''
    >>> intro()
    Runs the traffic lights program
    '''

    print("Hey there! Welcome to Traffic app\n")
    print("Enter the name of the place you want to control the traffic lights\n") 
    place = input().lower()
    print("Controlling traffic in "+place.upper()+"\n")
    time.sleep(1)
    while True:
       
        print('Use these short codes ')
        print('-'*22)
        print("stop - for red lights\n wait - for amber lights\n go - for green lights\n exit - to exit  ")
        print('-'*22)
        print('\n')
        short_code = input().upper()
        print('\n')
        if short_code == 'STOP':
            print("Stop behind the line for 9 seconds")
            func(9)
            print('Ready')
            print('\n')
            time.sleep(1)
        elif short_code == 'WAIT':

            print("Get ready to go in")
            func(3)
            print('Go')
            print('\n')
            time.sleep(1)


        elif short_code == 'GO':
           
            print("You can go\n")
            func(9)
            print("Stop")
            print('\n')
            time.sleep(1)

        elif short_code == 'EXIT':

            print("Logging off... \n")
            time.sleep(1)
            print('\n')
            break
            
        
        else:
            print(" _ I cant understand that, please use these codes \n")
if __name__ == '__main__':

    intro()