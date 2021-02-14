from main import ask_name
# <- blocks here until main is fully loaded
# and ask_name is imported


def say_hi():
    print('hi!')
    ask_name()
