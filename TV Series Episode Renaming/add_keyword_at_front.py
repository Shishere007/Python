from os import getcwd, rename
from pathlib import Path
from time import sleep


def main():
    path = Path(getcwd())
    print(f"current path {path}")
    _ = str(input("Press any key to continue"))

    keyword = str(input('Keyword : '))
    try:
        for item in path.glob("*"):
            src = str(item)
            path_list = str(item).split("\\")
            file_name = path_list[-1]
            if file_name.__contains__(".py"):
                continue
            print(file_name)
            # adding keyword at front
            file_name = keyword + " " + file_name
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


if __name__ == "__main__":
    main()
