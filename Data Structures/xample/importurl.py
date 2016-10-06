import urllib
import os
import re

htmlfile = urllib.urlopen("https://in.finance.yahoo.com/q?s=FB&ql=0")
htmltext = htmlfile.read()

regex = '<span id="yfs_l84_fb">(.+?)</span>'
pattern = re.compile(regex)
title = re.findall(pattern,htmltext)
print title
os.system("start C:\Users\Nikhil\Downloads\Music\motar.mp3")

