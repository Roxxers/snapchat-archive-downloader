# Snapchat Archive Downloader

## Background

When trying to download my data from Snapchat via their GDPR request form, they provided a set of JSON and HTML files. These did not contain my images but rather HTML pages with links that would download each image and video individually. This sucks so much. I wasn't a massive Snapchat user or anything but I had enough images and videos in my memories that this was a massive pain in the ass. This was made even worse when I realised Snapchat does not give you the direct URLs, but rather just links to an endpoint that then returns the actual URL on some random Amazon S3 server.

Hence this script was made.

## Installation

```sh
git clone https://github.com/roxxers/snapchat-archive-downloader
cd snapchat-archive-downloader
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Then just run `python3 dl.py` and enter the path to your `memories_history.json` file in the archive that Snapchat provided. This is the JSON file with all of the memories data. There is no other images or videos to download in the data. The rest is just logs and metadata they have on your account.

## Caveats

- One issue with this archive is that Snapchat does not store the image with the caption in the archive they give you. I assume Snapchat stores captions, filters, and added graphics as metadata to be applied to the original images. To get the edited photos, you will need to manually go through the app and export each one manually. You can select up to 100 at a time in the app so this isn't super awful but it is worth knowing.
