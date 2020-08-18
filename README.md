Netflix My List
===

> CLI to Extract names and urls from Netflix's 'My List'

by Kanjiu Akuma

Requirements
===
Python 3.8 (https://www.python.org/downloads/)

Run `pip install -r requirements.txt` to install required packages


Usage
===
Go to https://www.netflix.com/browse/my-list and save the page (right click: `save page as`)
to the same folder as this script (File should be named 'Netflix.html' by default).

Run `my_list.py -o` from the command line to extract all items and save them to mylist.txt

To see all available arguments run `my_list.py -h`
