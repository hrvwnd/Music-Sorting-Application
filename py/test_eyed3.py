import sys
import eyed3

file = eyed3.load("test.mp3")
print (file.tag.artist)
print (file.tag.title)
