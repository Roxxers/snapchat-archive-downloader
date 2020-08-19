import os
import json
import datetime

import requests

types = {"IMAGE": "PHOTO", "VIDEO": "VIDEO"}

memories_file = input("Path to 'memories_history.json' file: ")

with open(memories_file, "r") as fp:
    memories = json.loads(fp.read())["Saved Media"]

for memory in memories:
    date = memory.get("Date")
    mem_type = memory.get("Media Type")
    link = memory.get("Download Link")

    filedate = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S %Z")
    filename_date = filedate.strftime("%Y-%m-%d_%H%M%S")

    if mem_type == types["IMAGE"]:
        ext = "jpg"
    else:
        ext = "mp4"
    file_url = requests.post(link).text
    filename = "scrape/snapchat_{}.{}".format(filename_date, ext)

    with open(filename, "wb") as img:
        img.write(requests.get(file_url).content)
        print("Downloaded " + filename)
