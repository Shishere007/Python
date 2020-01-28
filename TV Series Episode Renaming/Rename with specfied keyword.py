from os import getcwd, rename
from pathlib import Path
from time import sleep

# change series episode name as specified by the user
# provided filename follows a pattern

def main() :
    path = Path(getcwd())
    print(f"current path {path}")
    choice = str(input("Press any key to continue"))
    print(
        """
        Give the filename in the following format
        Attack on Titan S01 E
    """
    )
    new_file_name = str(input("Filename : "))
    new_file_name_list = new_file_name.split()
    try :
        episode = int(input('Starting Episode : '))
        try :
            for item in path.glob('*'):
                src = str(item)
                if src.__contains__('.py') :
                    continue
                path_list = str(item).split("\\")
                current_file_name = path_list[-1]
                print (current_file_name)
                file_extension = current_file_name.split()[-1]
                file_extension_list = file_extension.split('.')

                
                temp_list = []
                temp_list.append(str(new_file_name))
                if episode < 10 :
                    temp_list.append((str(0)+str(episode)))
                else :
                    temp_list.append(str(episode))
                temp_list.append('.' + file_extension_list[-1])  
                current_file_new_name = "".join(temp_list)
                #print (temp_list)
                episode += 1
                
                path_list.pop(-1)
                path_list.append(current_file_new_name)
                print (current_file_new_name)
                dst = "\\".join(path_list)
                # to rename the file
                rename(src,dst)
                #break
            else :
                raise UserWarning
        except Exception as e :
            #print (e)
            raise UserWarning
            
    except UserWarning :
        _ = input('done')
    except Exception as e :
        #print (e)
        raise UserWarning



if __name__ == "__main__":
    main()