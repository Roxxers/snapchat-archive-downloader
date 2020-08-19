# Copyright © 2020 Roxie Gibson

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”),
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

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
