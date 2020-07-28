from os import system, getcwd, listdir
from pathlib import Path


def to_zip() -> None:
    
    current_path = Path(getcwd())
    for folder in listdir(current_path):
        if folder.__contains__(".py") or folder.__contains__(".zip"):
            continue
        folder = folder.replace(" ", "_")
        #print(f"7z a -tzip '{folder}.zip' '{folder}'")
        #_ = input()
        system(f"7z a -tzip {folder}.zip {folder}")


if __name__ == "__main__":
    print('''
    this script wont work if there is space in folder name
    and only folders and this script should be in the main folder
    press any key to continue
    ''')
    _ = input()
    to_zip()
    # a = listdir(Path(getcwd()))
    # print(a)
