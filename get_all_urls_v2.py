#!/usr/bin/env python3
import os
import re
import sys
import time
import concurrent.futures
from concurrent import futures
try:
    import requests
except:
    sys.exit("Install missing library: pip install requests")
try:
    import urllib3
except:
    sys.exit("Install missing library: pip3 install urllib3")
urllib3.disable_warnings()

def helplk():
    print("follow the examples: ")
    print()
    print("%s -h"%(sys.argv[0]))
    print("%s --help"%(sys.argv[0]))
    print("%s -u https://www.site.com.br --save out.txt"%(sys.argv[0]))
    print("%s --url https://www.site.com.br --save out.txt"%(sys.argv[0]))
    sys.exit()

if len(sys.argv) <=1:
    helplk()
    sys.exit()
elif len(sys.argv) ==2:
    choice = str(sys.argv[1])
    if choice == "-u":
        print("insert valid url")
        sys.exit()
    elif choice == "--url":
        print("insert valid url")
        sys.exit()
    elif choice == "-h":
        helplk()
        sys.exit()
    elif choice == "--help":
        helplk()
        sys.exit()
    else:
        print("invalid option")
        print()
        helplk()
        sys.exit()
elif len(sys.argv) ==3:
    print("insert output save-file")
    sys.exit()
elif len(sys.argv) ==4:
    choice = str(sys.argv[3])
    if choice == "--save":
        print("enter a destination location")
        sys.exit()
    else:
        print("invalid option")
        print()
        helplk()
        sys.exit()
elif len(sys.argv) >=6:
    print("incorrect parameters")
    sys.exit()
else:
    pass

url_st = str(sys.argv[2])
try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(
                lambda: requests.get(url_st))
        for _ in range(1)
    ]

    results = [
        f.result().text
        for f in futures
    ]

    regex = r"((http?).)://+[\w\d:#@%/;$()~_?\+-=\\.&]*"
    matches = re.finditer(regex, str(results), re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        print("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        file_save = open(str(sys.argv[4]), 'a')
        atxt = ["{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()),'\n']
        file_save.writelines(atxt)
        file_save.close()

except requests.exceptions.Timeout:
    time.sleep(5)
    pass
except requests.exceptions.TooManyRedirects:
    print("url error")
    pass
except requests.exceptions.RequestException as error:
    print("A serious problem happened, like an SSLError or InvalidURL")
    print("Error: {}".format(error))
except KeyboardInterrupt:
    sys.exit()
except Exception as error:
    print(error)
    pass
