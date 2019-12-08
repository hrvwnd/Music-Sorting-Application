import sys
import eyed3

try:
    file = eyed3.load("/home/harveyawendon/harvey/music/test.mp3")
    artist = file.tag.artist
    title = file.tag.title
except AttributeError:
    print ("file does not have id3 tags to read")
else:
    print (file.tag.artist)
    print (file.tag.title)
    
try:    
    file = eyed3.load("/home/harveyawendon/harvey/music/hiphop.mp3")
    artist = file.tag.artist
    title = file.tag.title
except AttributeError:
    print ("file does not have id3 tags")
else:
    print (file.tag.artist)
    print (file.tag.title)

