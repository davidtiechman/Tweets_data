from src.Cleaner import Cleaner
from src.LoadFile import load_file
from src.Writes_to_json import WritesToJson

def option():
    option = input('Please enter your option: ')
    match(option):
        case'1':
            df = load_file()
            print(df)
            return
        case  '2':
            writes = WritesToJson()
            writes.write_to_json()
            return
        case '3':
            clean = Cleaner()
            clean.Toupper()
            clean.delete_non_biased()
            clean.Export_a_new_file()

option()





