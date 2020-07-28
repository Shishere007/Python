from os import getcwd, rename
from pathlib import Path
from time import sleep


# a menu driven program to rename bulk files like
# series episodes at once


class rename_files:
    def __init__(self):
        self.path = Path(getcwd())

    def menu_section(self):
        try:
            print(f"current path {self.path}")
            print(
                """
            1 - Remove dots from file name
            2 - Remove spcific keyword from filename
            3 - Rename files with specific Keyword
            4 - List files
            5 - Add keyword at the front
            6 - Add keyword at the end
            7 - Add extension
            8 - Stop/Quit
            """
            )
            try:
                choice = int(input("Choice : "))
            except Exception:
                raise UserWarning
            if choice == 1:
                self.remove_dots()
            elif choice == 2:
                self.remove_specific_word()
            elif choice == 3:
                self.rename_files_as_specified()
            elif choice == 4:
                self.list_file()
            elif choice == 5:
                self.add_keyword_at_front()
            elif choice == 6:
                self.add_keyword_at_end()
            elif choice == 7:
                self.add_extension()
            elif choice == 8:
                quit(0)
            else:
                raise UserWarning
        except UserWarning:
            print("wrong option")
        except Exception as e:
            print(f"rename_files.menu_selection := {e}")

    def remove_dots(self):
        # obtain the current path of current directory
        try:
            for item in self.path.glob("*"):
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
                else:
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
            print(f"remove_dots :- {e}")
            raise UserWarning

    def remove_specific_word(self):
        print("please note : \nThe specified words will be deleted from first to last.")
        keyword = str(input("Keyword : "))
        keyword_list = keyword.split()
        try:
            for item in self.path.glob("*"):
                src = str(item)
                path_list = str(item).split("\\")
                file_name = path_list[-1]
                if file_name.__contains__(".py"):
                    continue
                print(file_name)
                # to remove 'copy of'
                if file_name.__contains__(keyword):
                    file_name_list = file_name.split()
                    last_word_list = file_name_list[-1].split(".")
                    for word in keyword_list:
                        try:
                            file_name_list.remove(word)
                        except Exception:
                            if word in last_word_list:
                                file_name_list.pop(-1)
                                last_word_list.remove(word)
                                last_word_list = ["."] + last_word_list
                                exctension = "".join(last_word_list)
                                file_name_list.append(exctension)
                    else:
                        if file_name_list[-2] in ["-"]:
                            file_name_list.pop(-2)

                    file_name = " ".join(file_name_list)
                path_list.pop(-1)
                print(file_name)
                # print(list(file_name))
                path_list.append(file_name)
                dst = "\\".join(path_list)
                # to rename the file
                rename(src, dst)
            else:
                raise UserWarning

        except UserWarning:
            _ = input("Done")
        except Exception as e:
            print(f"remove_specific_word :- {e}")
            raise UserWarning

    def rename_files_as_specified(self):
        print(
            """
            Give the filename in the following format
            Attack on Titan S01 E
        """
        )
        new_file_name = str(input("Filename : "))
        new_file_name_list = new_file_name.split()
        try:
            episode = int(input("Starting Episode : "))

            try:
                for item in self.path.glob("*"):
                    src = str(item)
                    if src.__contains__(".py"):
                        continue
                    path_list = str(item).split("\\")
                    current_file_name = path_list[-1]
                    print(current_file_name)
                    file_extension = current_file_name.split()[-1]
                    file_extension_list = file_extension.split(".")

                    temp_list = []
                    temp_list.append(str(new_file_name))
                    if episode < 10:
                        temp_list.append((str(0) + str(episode)))
                    else:
                        temp_list.append(str(episode))
                    temp_list.append("." + file_extension_list[-1])
                    current_file_new_name = "".join(temp_list)
                    # print (temp_list)
                    episode += 1

                    path_list.pop(-1)
                    path_list.append(current_file_new_name)
                    print(current_file_new_name)
                    dst = "\\".join(path_list)
                    # to rename the file
                    rename(src, dst)
                    # break
                else:
                    raise UserWarning
            except Exception as e:
                # print (e)
                raise UserWarning

        except UserWarning:
            _ = input("done")
        except Exception as e:
            print(f"rename_files_as_specified :- {e}")
            raise UserWarning

    def add_extension(self):
        extension = str(input("Extension : "))
        try:
            for item in path.glob("*"):
                src = str(item)
                path_list = str(item).split("\\")
                file_name = path_list[-1]
                if file_name.__contains__(".py"):
                    continue
                print(file_name)
                # extension to be added
                file_name = file_name + extension
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
            print(f"add_extension :- {e}")
            raise UserWarning

    def add_keyword_at_end(self):
        keyword = str(input("Keyword : "))
        try:
            for item in self.path.glob("*"):
                src = str(item)
                path_list = str(item).split("\\")
                file_name = path_list[-1]
                if file_name.__contains__(".py"):
                    continue
                print(file_name)
                # adding keyword at end
                file_name_list = file_name.split(".")
                extenstion = file_name_list[-1]
                file_name_list.pop(-1)
                extenstion = keyword + "." + extenstion
                file_name_list.append(extenstion)
                file_name = " ".join(file_name_list)
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
            print(f"add_keyword_at_end :- {e}")
            raise UserWarning

    def add_keyword_at_front(self):
        keyword = str(input("Keyword : "))
        try:
            for item in self.path.glob("*"):
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
                dst = "\\".join(path_list)
                print(file_name)
                # to rename the file
                rename(src, dst)
            else:
                raise UserWarning

        except UserWarning:
            _ = input("Done")
        except Exception as e:
            print(f"add_keyword_at_end :- {e}")
            raise UserWarning

    def list_file(self):
        try:
            for item in self.path.glob("*"):
                src = str(item)
                path_list = str(item).split("\\")
                file_name = path_list[-1]
                if file_name.__contains__(".py"):
                    continue
                print(file_name)
        except Exception as e:
            print(f"list_files :- {e}")


class_call_rename_files = rename_files()
if __name__ == "__main__":
    _ = str(input("Press any key to continue"))
    while True:
        class_call_rename_files.menu_section()
