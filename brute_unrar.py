from brute import brute
from unrar import rarfile
import os

try:
    input = raw_input
except:
    input = input


def fromDictionary(dicName):
    with open(dicName, "r") as f:
        for word in f:
            yield word.strip()


def crackRar(rarFilename, pwdGenerator):
    rar = rarfile.RarFile(rarFilename)
    found = False
    for pwd in pwdGenerator:
        try:
            rar.extractall(pwd=pwd)
            print("file extracted")
            print("the password is %s" % pwd)
            found = True
            break
        except rarfile.BadRarFile:
            pass
    if not found:
        print("Sorry, cannot find the password")


if __name__ == '__main__':
    print("----------------------------------------------------")
    print('    RAR Cracker')
    print('    by @Ghostish')
    print("----------------------------------------------------")
    filename = input("Please enter the filename: ")
    while not os.path.isfile(filename):
        filename = input("no such file, please enter a valid filename: ")

    mode = ''
    while mode != "dictionary" and mode != "brute":
        mode = input("Please select a working mode [dictionary/brute]: ")

    pwdGen = None
    if mode == "dictionary":
        dic_name = input("Please enter the filename of the dictionary: ")
        while not os.path.isfile(dic_name):
            dic_name = input("no such file, please enter a valid filename: ")
        pwdGen = fromDictionary(dic_name)

    if mode == "brute":
        letters = input("Include letters? [yes/no] (default yes) ") != 'no'
        symbols = input("Include symbols? [yes/no] (default yes) ") != 'no'
        numbers = input("Include numbers? [yes/no] (default yes) ") != 'no'
        spaces = input("Include spaces? [yes/no] (default no) ") == 'yes'
        start_length = int(input("min length: "))
        length = int(input("max length: "))
        pwdGen = brute(start_length=start_length,length=length,letters=letters,numbers=numbers,symbols=symbols,spaces=spaces)

    print("Start cracking")
    print("This may take some time, please wait...")
    crackRar(filename, pwdGen)
