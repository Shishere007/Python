from os import getcwd, rename
from pathlib import Path
from time import sleep


def main():
    # obtain the current path of current directory
    path: Path = Path(getcwd())
    print(f"current path {path}")
    _ = str(input("Press any key to continue"))
    try:
        for item in path.glob("*"):
            # print (item)
            src = str(item)
            path_list = str(item).split("\\")
            # file name is picked
            file_name = path_list[-1]
            if file_name.__contains__(".py"):
                continue
            print(file_name)
            # no of dots
            dot_count = file_name.count(".")
            # replace n-1 dots in the file name with space
            if item.is_dir():
                new_file_name = file_name.replace(".", " ")
            else :
                new_file_name = file_name.replace(".", " ", dot_count - 1)
            # remove the old file name
            path_list.pop(-1)
            # append new file name
            path_list.append(new_file_name)
            print(new_file_name)
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


if __name__ == "__main__":
    main()
