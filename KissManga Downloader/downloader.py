import requests
from bs4 import BeautifulSoup
from os import mkdir
import concurrent.futures
import multiprocessing

def prepare_soup(link:str)->BeautifulSoup:
    html = requests.get(link)
    if html.status_code == 200:
        return BeautifulSoup(html.text,'html.parser')
    return False

def download_image(image):
    filename = image[0]
    url = image[1]
    ind = image[2]
    cnt = image[3]
    print(f"({ind}?{cnt})" ,end=":")
    open(filename,'wb').write(requests.get(url).content)

def create_folder(foldername):
    try:
        mkdir(foldername)
        return True
    except FileExistsError:
        return False

def format_manga_name(manga:str):
    manga = manga.lower()
    manga = manga.replace("read","")
    manga = manga.replace('manga',"")
    if manga[0] in [" ","_"]:
        manga = manga[1:]
    if manga[-1] in [" ","_"]:
        manga = manga[:-1]
    return manga.capitalize()

def thread_download(imaga_list):
    POOL_SIZE = multiprocessing.cpu_count() * 2
    print(f"allotting {POOL_SIZE} threads for multiprocessing")
    with concurrent.futures.ThreadPoolExecutor(max_workers=POOL_SIZE) as executor:
        executor.map(download_image,[link for link in imaga_list])

def download_chapter(link):
    soup = prepare_soup(link)
    img_list_temp = [item.attrs['src'] for item in soup.find(id='centerDivVideo').find_all('img')]
    image_list = []
    manga_name = format_manga_name(link.split("/")[-2])
    chapter = link.split("/")[-1]
    create_folder(manga_name)
    folder = manga_name + "/" + chapter + "/"
    create_folder(folder)
    cnt = len(img_list_temp)
    for ind,url in enumerate(img_list_temp):
        ext = url.split(".")[-1]
        page = str(ind + 1)
        if len(page) == 1:
            page = "0" + page
        filename = folder + page + "." + ext
        image_list.append((filename,url,ind+1,cnt))
    print(f"Downloading {chapter}",end=" -> ")
    thread_download(image_list)
    print("\n")

if __name__ == "__main__":
    link = 'https://kissmanga.org/chapter/read_horimiya_manga/chapter_28.2' 
    download_chapter(link)