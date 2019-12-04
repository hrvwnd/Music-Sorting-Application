import id3reader 

id3r = id3reader.Reader("test")
id3r.getValue('album')
#print (id3r.getValue('album'))