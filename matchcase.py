def do_this():
    print('Doing This')

def do_that():
    print('Doing That')

match input("Do this or that? "):
    case 'this':
        do_this()
    case 'that':
        do_that()
    case _:
        print('Invalid input')