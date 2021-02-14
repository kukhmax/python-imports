from lib import say_hi
# <- blocks here until lib is fully loaded
# and say_hi is imported

def ask_name():
    print('what is your name?')


def main():
    say_hi()


if __name__ == '__main__':
    main()
