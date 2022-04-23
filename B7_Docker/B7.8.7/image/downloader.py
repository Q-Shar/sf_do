#!/usr/bin/env python

import os
from urllib.parse import urlparse
import wget
import argparse


def download(site_url, destination_path, is_debug):
    try:
        u = urlparse(site_url)
        scheme = "http" if not u.scheme else u.scheme
        site = u.path.split('/')[0] if not u.netloc else u.netloc
        url = f'{scheme}://{site}/favicon.ico'
        displayProgress = None
        result_file_name = os.path.join(destination_path, f'{site}.ico')

        print(f'urlparse :\t\t{u}') if is_debug else None
        print(f'url :\t\t\t{url}') if is_debug else None
        print(f'result_file_name :\t{result_file_name}') if is_debug else None

        result = wget.download(url, result_file_name, displayProgress)
        print (result)
        return True
    except Exception as e:
        print('An exception occurred: {0}'.format(repr(e)))
        return False
    finally:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", "-s", type=str, required=True, metavar='\'Site URL\'',
                        help="The source site url like http://domain.com/")
    parser.add_argument("--dest", "-d", type=str, required=True, metavar='\'Destination folder\'',
                        help="The destination folder path like 'c:\\' or '/home/user'")
    parser.add_argument("--debug", "-x", type=bool, required=False, metavar='\'Debug mode\'',
                        help="Run in the Debug mode")
    args = parser.parse_args()

    print(f'args :\t\t\t{args}') if args.debug else None

    download(args.site, args.dest, args.debug)
