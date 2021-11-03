__auther__ = "Shishere"
__verion__ = 1.0

import os
from pathlib import Path, WindowsPath
import shutil
from typing import List
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count


class CleanFolder:
    def __init__(self, folder: str, out_folder: str, copy: bool = False) -> None:
        self.folder = folder
        self.action = self.__action(copy=copy)
        self.files = {}
        self.out_folder = out_folder

    def __action(self, copy: bool):
        return shutil.copy if copy else shutil.move

    def get_dir(self, ) -> List[str]:
        return [
            file.name
            for file in Path(self.out_folder).glob('*')
            if file.is_dir()
        ]

    def get_files(self, ) -> None:
        for file in Path(self.folder).glob('*'):
            if file.is_dir():
                continue
            ext = file.suffix
            if not ext:
                ext = 'Other'
            else:
                ext = ext[1:]
            if ext in self.files:
                self.files[ext].append(file)
            else:
                self.files[ext] = [file]

    def __perform_action(self, data: List[WindowsPath]) -> None:
        ind, length, folder, file = data
        print(f"({ind+1}/{length}) : {file.name}")
        self.action(file, os.path.join(folder, file.name))

    def create_folder(self, folder: str) -> None:
        folders = self.get_dir()
        if not Path(folder).name in folders:
            os.mkdir(folder)
            print(f"New folder Created: {folder}")

    def reorder(self, ) -> None:
        for ext, files in self.files.items():
            new_folder = os.path.join(self.out_folder, ext)
            self.create_folder(new_folder)
            length = len(files)
            with ThreadPoolExecutor(max_workers=4) as exe:
                exe.map(
                    self.__perform_action,
                    [
                        [ind, length, new_folder, file]
                        for ind, file in enumerate(files)
                    ]
                )
                # for file in files:
                #     self.action(file, os.path.join(new_folder, file.name))

    def perform(self, ) -> None:
        self.get_files()
        self.reorder()


if __name__ == "__main__":
    CleanFolder(
        folder=r"C:\Users\Shishere\Desktop\New folder",
        out_folder=r"C:\Users\Shishere\Desktop\New folder\Output",
        copy=True
    ).perform()
