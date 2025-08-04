from src.Cleaner import Cleaner


def option():
    option = input('Please enter your option: ')
    match(option):
        case  '1':
            return
        case '2':
            return
        case '3':
            clean = Cleaner()
            clean.Toupper()
            clean.delete_non_biased()
            clean.Export_a_new_file()

option()





