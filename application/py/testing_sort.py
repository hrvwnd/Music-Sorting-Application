eyed3_output = """BLAHBLAHBLAH
liquid"""

def strip_eyed3(eyed3_output):
    return eyed3_output.split("\n",1)[1]

print (strip_eyed3(eyed3_output))