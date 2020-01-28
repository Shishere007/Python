from os import getcwd,rename
from pathlib import Path
from time import sleep


def main() :
    path = Path(getcwd())
    print (f'current path {path}')
    choice = str(input('Press any key to continue'))
    keyword = str(input('Keyword : '))
    keyword_list = keyword.split()
    try :
        for item in path.glob('*'):
            src = str(item)
            path_list = str(item).split("\\")
            file_name = path_list[-1]
            if file_name.__contains__('.py') :
                continue
            print (file_name)
            # to remove 'copy of'
            if file_name.__contains__(keyword) :
                file_name_list = file_name.split()
                last_word_list = file_name_list[-1].split('.')
                for word in keyword_list :
                    try :
                        file_name_list.remove(word)
                    except Exception :
                        if word in last_word_list :
                            file_name_list.pop(-1)
                            last_word_list.remove(word)
                            last_word_list = ['.'] + last_word_list
                            exctension = "".join(last_word_list)
                            file_name_list.append(exctension)
                else :
                    if file_name_list[-2] in ['-'] :
                        file_name_list.pop(-2)
                            
                file_name = " ".join(file_name_list)
            path_list.pop(-1)
            print (file_name)
            path_list.append(file_name)
            dst = "\\".join(path_list)
            # to rename the file
            rename(src,dst)
        else :
            raise UserWarning
            
    except UserWarning :
        _ = input('Done')
    except Exception as e :
        print (e)
        raise UserWarning


if __name__ == "__main__":
    main()