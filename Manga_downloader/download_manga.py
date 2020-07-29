from os import system


try:
    import manga_py
except Exception:
    system("pip install manga-py")


class manga:
    def __init__(self):
        pass

    def all_chapter(self, site: str, name: str):
        system(f"manga-py {site} --name {name}")

    def first_n_chapter(self, site: str, maximum_chapter: int, name: str):
        system(f"manga-py --max-volume {maximum_chapter} {site} --name {name}")

    def skip_n_chapter(self, site: str, skip_chapter: int, name: str):
        system(f"manga-py --skip-volume {skip_chapter} {site} --name {name}")

    def skip_n_then_m_chapter(
        self, site: str, skip_chapter: int, maximum_chapter: int, name: str
    ):
        system(
            f"manga-py --skip-volume {skip_chapter} --max-volume {maximum_chapter} {site} --name {name}"
        )

    def download_all(self):
        with open("site_list.txt", "r") as file:
            sites = file.readlines()
        for item in sites:
            site = str(item)
            name = site.split("//")[-1]
            self.all_chapter(site=site, name=name)

    def main(self):
        while True:
            print(
                """
                1 - Download all (from saved sites in file)
                2 - Download one manga
                3 - Download skipping N chapter
                4 - Download first N chapter
                5 - Download N chapter skipping M chapter
                6 - Exit
            """
            )
            try:
                choice = int(input("Choice : "))
            except:
                continue
            if choice == "":
                continue

            if choice == 6:
                break
            if choice == 1:
                self.download_all()
                continue
            site = str(input("manga URL : "))
            if site == "":
                print("no input found")
                continue
            name = str(input("manga name : "))
            if name.__contains__(" "):
                name.replace(" ", "_")
            if name == "":
                name = site.split("/")[-1]
            if choice == 2:
                self.all_chapter(site=site, name=name)
            elif choice == 3:
                skip_chapter = int(input("chapter skip count : "))
                self.skip_n_chapter(site=site, name=name, skip_chapter=skip_chapter)
            elif choice == 4:
                maximum_chapter = int(input("chapter count : "))
                self.first_n_chapter(
                    site=site, name=name, maximum_chapter=maximum_chapter
                )
            elif choice == 5:
                skip_chapter = int(input("chapter skip count : "))
                maximum_chapter = int(input("chapter count : "))
                self.skip_n_then_m_chapter(
                    site=site,
                    name=name,
                    skip_chapter=skip_chapter,
                    maximum_chapter=maximum_chapter,
                )


if __name__ == "__main__":
    manga().main()
