from os import system, getcwd, path
from shutil import move
from pathlib import Path



def main():
    current_path = Path(getcwd())
    print(f"current path {current_path}")
    _ = str(input("Press any key to continue"))
    desired_name = input("folder Name : ")
    try:
        for item in current_path.glob("*"):
            if not path.isdir(item):
                file_name = str(item).split("\\")[-1]
                if file_name.__contains__(".py"):
                    continue
                temp_name = file_name.split(".")
                temp_name.pop(-1)
                if len(temp_name) == 2:
                    folder_name = "_".join(temp_name)
                else:
                    folder_name = temp_name[-1]
                folder_name = "_".join(folder_name.split("_")[:-1])
                
                folder_name = desired_name+folder_name
                if not path.exists(folder_name):
                    print(folder_name)
                    system(f"mkdir {folder_name}")
                folder_loc = "\\".join(str(item).split("\\")[:-1]+[folder_name])
                system(f"move {item} {folder_loc}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
