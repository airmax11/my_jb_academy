import os
import re

import requests
from bs4 import BeautifulSoup
import string


saved_articles = []

number_of_pages = int(input())
article_type = input()

news = "https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page="


def get_req(inp, tag="article"):
    r = requests.get(inp, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soap = BeautifulSoup(r.content, 'html.parser')
    art = soap.find_all(tag)
    return art


def replace_values(inp, article_type="News"):
    dict_lib = {}
    for a in inp:
        child = a.find('span', {'class': "c-meta__type"})
        if child.get_text() == article_type:
            a_element = a.find('a')
            title = a_element.get_text()
            link = a_element.get('href')
            for b in title:
                if b in string.punctuation or b == " ":
                    title = title.replace(b, "_")
                if "__" in title:
                    title = title.replace("__", "_")
            dict_lib[title] = link
    return dict_lib


def read_write(dictionary):
    start = "https://www.nature.com"
    for a, b in dictionary.items():
        link = requests.get(start + b, headers={'Accept-Language': 'en-US,en;q=0.5'})
        soap = BeautifulSoup(link.content, 'html.parser')
        regex = re.compile(".*body.*")
        art = soap.find('div', {'class': regex}).text.strip()
        with open(f'{a}.txt', 'wb') as file:
            saved_articles.append(f'{a}.txt')
            file.write(art.encode(encoding='UTF-8'))
        with open(f'{a}.txt', 'r+', encoding='UTF-8') as fd:
            lines = fd.readlines()
            fd.seek(0)
            fd.writelines(line for line in lines if line.strip())
            fd.truncate()


def main_run():
    current_path = os.getcwd()
    for page in range(1, number_of_pages + 1):
        article = get_req(news + str(page))
        dictionary = replace_values(article, article_type)
        # if len(dictionary) == 0:
        #     continue
        try:
            os.mkdir(f"Page_{str(page)}")
        except:
            print("The directory exists.")
        os.chdir(f"Page_{str(page)}")
        read_write(dictionary)
        os.chdir(current_path)
    print("Saved all articles.")

main_run()
