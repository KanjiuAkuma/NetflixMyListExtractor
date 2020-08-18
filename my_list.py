"""
Created by Joscha Vack on 8/18/2020.
"""

from bs4 import BeautifulSoup
import clipboard
import argparse
import re

desc = """\
usage:

Go to https://www.netflix.com/browse/my-list and save the page (right click: `save page as`) to the same directory as my_list.py.

Run `my_list.py -o` from the command line to extract all items and save them to mylist.txt
"""

help_i = """\
Input file; Netflix.html is assumed if not given.
Should be a .html file.
"""

help_o = """\
Output file; If not specified output is printed to console.
If used without filename output is written to mylist.txt.
If used with filename output is written to filename.txt.
"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Netflix's 'My List' Extractor",
        description="Extractor for items of netflix's 'My List'",
        epilog=desc,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-i',
                        dest='input',
                        default='Netflix.html',
                        help=help_i
                        )
    parser.add_argument('-o',
                        dest='output',
                        const='mylist',
                        default=None,
                        nargs='?',
                        help=help_o
                        )
    parser.add_argument('--u',
                        dest='url',
                        action='store_true',
                        help='Extract urls as well')
    parser.add_argument('--c',
                        dest='clip',
                        action='store_true',
                        help='Use clipboard content instead of input file')
    args = parser.parse_args()

    if args.clip:
        soup = BeautifulSoup(clipboard.paste(), 'html.parser')
    else:
        with open(args.input, 'r') as i:
            soup = BeautifulSoup(i, 'html.parser')

    items = soup.find_all('div', {'class': 'boxart-size-16x9 boxart-container'})
    print('Found %d items:' % len(items))
    if args.url:
        # append urls
        items = ['%s (%s)' % (e.text, re.sub(r'[?].*$', '', e.parent['href'])) for e in items]
    else:
        # name only
        items = [e.text for e in items]

    for e in items:
        print(e)

    if args.output:
        with open('%s.txt' % args.output, 'w') as o:
            for e in items:
                o.write(e + '\n')
