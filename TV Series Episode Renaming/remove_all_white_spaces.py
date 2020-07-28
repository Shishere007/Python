from os import getcwd, rename
from pathlib import Path
from time import sleep


def main():
    path = Path(getcwd())
    print(f"current path {path}")
    _ = str(input("Press any key to continue"))

    #extension = str(input('Extension : '))
    try:
        for item in path.glob("*"):
            src = str(item)
            path_list = str(item).split("\\")
            file_name = path_list[-1]
            if file_name.__contains__(".py"):
                continue
            print(file_name)
            # extension to be added
            file_name = file_name.replace(" ","")
            path_list.pop(-1)
            path_list.append(file_name)
            print(file_name)
            dst = "\\".join(path_list)
            # to rename the file
            rename(src, dst)
        else:
            raise UserWarning

    except UserWarning:
        _ = input("Done")
    except Exception as e:
        print(e)
        raise UserWarning

def list_file() :
    try:
        for item in path.glob("*"):
            src = str(item)
            path_list = str(item).split("\\")
            file_name = path_list[-1]
            if file_name.__contains__(".py"):
                continue
            print(file_name)
    except Exception :
        pass

if __name__ == "__main__":
    main()
