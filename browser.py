import os
import sys
from . import pydoc_scraper


args = sys.argv

# check for correct number of passed arguments in terminal & create directory
if len(args) != 2:
    print('Error: The script should be called with two arguments')
else:
    dir_Name = args[1]
    try:
        os.mkdir(dir_Name)
        print('Directory', dir_Name, 'created')
    except FileExistsError:
        print('Error: Directory', dir_Name, 'already exist')

# to save visited pages
saved_tabs = []

while True:

    url = input('Enter a URL or saved tab: ')

    # exit from browser
    if url.lower() == 'exit':
        exit()

    # back to go to previous page
    elif url == 'back':
        if len(saved_tabs) > 1:
            saved_tabs.pop()
            last_tab = saved_tabs[-1]
            with open(f'{dir_Name}/{last_tab}.txt', 'r') as f:
                print(f.read())

    # check for saved tabs
    elif url in saved_tabs:
        with open(f'{dir_Name}/{url}.txt', 'r') as f:
            print(f.read())

    # check for valid url
    elif url.count('.') < 1 and url not in saved_tabs:
        print('Error: Incorrect URL')

    # save shortened url and append to saved tabs
    else:
        a = url.split('.')
        a.pop()
        shortened_url = '.'.join(a)
        saved_tabs.append(shortened_url)

        # concatenate https:// if not present
        if url.startswith('https://', 0, 8):
            pass
        else:
            url = 'https://' + url

        # get the requested url and prints text
        page = pydoc_scraper.my_scraper(url)
        print(page)

        # save visited page to directory
        with open(f'{dir_Name}/{shortened_url}.txt', 'w+') as f:
            f.write(page)

