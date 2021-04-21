'''
move files in the current folder with random names. 
with one copy saved in another folder
'''


from pathlib import Path
from os import getcwd,system,rename,path
from string import ascii_lowercase,digits
from random import choice


def random_name()->str:
    characters = list(ascii_lowercase + digits)
    string = "".join([choice(characters) for _ in range(10)])
    return string
    


def main()->None:
    current_path = Path(getcwd())
    new_folder_name = input("new folder name : ")


    old_folder_loc = str(current_path) + "\\" + "original files"
    new_folder_loc = str(current_path) + "\\" + new_folder_name
    if not path.exists(new_folder_name):
        system(f'mkdir "{new_folder_name}"')
        print(f"{new_folder_name} created")
    if not path.exists("original files"):
        system(f'mkdir "original files"')
    
    for item in Path(current_path).glob('*'):
        src = str(item)
        file_name_split = str(item).split("\\")
        file_name = file_name_split[-1]
        
        if file_name_split[-1].__contains__(".py") or Path(item).is_dir(): 
            continue

        system(f'copy "{src}" "{old_folder_loc}"')
        
        new_name = random_name() + "." + file_name.split(".")[-1]
        
        #changing name of file
        dst = "\\".join(file_name_split[:-1] + [new_name])
        rename(src,dst)
        
        system(f'move "{dst}" "{new_folder_loc}"')




main()
