import sys
from colorama import init, AnsiToWin32, Fore, Style
import sys
from os import mkdir, path
from collections import deque
import requests
from bs4 import BeautifulSoup
from sys import stdout

try:
    dirName = sys.argv[1]
except:
    dirName = None

if dirName is not None:
    try:
        mkdir(dirName)
    except FileExistsError:
        print("Directory ", dirName, " already exists")

myback = deque()
list_with_art = {}

# init(wrap=False)
# stream = AnsiToWin32(sys.stderr).stream

def get_data(url):
    if url.startswith("http"):
        r = requests.get(url)
        print(r.content)

        return r
    elif "." in url:
        url = "https://" + url
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        taggs = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
        tags = soup.find_all(taggs, text=True)
        for i in tags:
            if "href=" in str(i):
                print(Fore.BLUE + (i.get_text()).strip())
            else:
                print(i.get_text().strip())

        return soup

def file_name(text):
    if "." in text:
        index_of_dot = text.rindex('.')
        if dirName is not None:
            return f"./{dirName}/" + text[:index_of_dot]
        else:
            return text[:index_of_dot]
    else:
        return


def read_from_file(file_name):
    path = list_with_art[file_name]
    with open(path, "r") as f1:
        print(f1.read().encode('utf8'))


def write_file(url):
    with open(file_name(url) + ".txt", "w", errors="ignore") as file:
        soup = get_data(url)
        tags = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li'])
        for i in tags:
            file.write((i.get_text()).strip())


while True:
    input_start = input("Enter URL or Command: ")
    if input_start == 'exit':
        break
    if input_start == 'back' and len(myback) <= 1:
        continue
    if input_start == 'back' and len(myback) > 1:
        myback.popleft()
        read_from_file(file_name(myback[0]))
        continue
    if input_start in list_with_art:
        read_from_file(input_start)
        continue
    if "." not in input_start and input_start not in list_with_art:
        print("Incorrect URL or No Offline Docs")
        continue
    if input_start not in list_with_art:
        write_file(input_start)
        myback.appendleft(file_name(input_start) + ".txt")
        if dirName is not None:
            tmp = file_name(input_start)    # ./google_test/python
            find = tmp.rindex("/")
            tmp = tmp[find + 1:]
            list_with_art[tmp] = file_name(input_start) + ".txt"
            continue
        else:
            list_with_art[file_name(input_start)] = file_name(input_start) + ".txt"
            continue
