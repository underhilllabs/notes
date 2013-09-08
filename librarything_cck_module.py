#!/usr/bin/python
import re, urllib, csv,time
"""
this script:
1. reads in a Librarything Export CSV file
2. downloads the cover for each book with an ISBN into a directory
3. it saves the image file as "med_%s." % isbn  
"""


"""
CCK import librarything data
"""
CSV_FILE='/home/bart/Downloads/LibraryThing_export.csv'
IMG_DIR='/home/bart/img/'
DEV_KEY = 'YOUR_LIBRARYTHING_DEV_KEY'
IMG_URL = "http://covers.librarything.com/devkey/"+DEV_KEY+"/large/isbn/"

isbn=0
# read in the Librarything Export File
lt = csv.DictReader(open(CSV_FILE))
for row in lt:
    #print dir(lt)
    time.sleep(2)
    mystr = row["'ISBN'"]
    mymatch = re.match(r"\[(\d+)\]",mystr)
    if mymatch is None:
        print "blank isbn for: %s" % row["'TITLE'"]
    else:
        isbn = mymatch.group(1)
        myurl = "http://covers.librarything.com/devkey/a73beb25296cf74b050435aa5d8fd08e/large/isbn/%s" % isbn
        myfile = "%slarge_%s" % (IMG_DIR,isbn)
        urllib.urlretrieve(myurl,myfile)
        print "myurl: %s, myfile: %s" % (myurl,myfile)


#for i in isbn:
#    url = "http://covers.librarything.com/devkey/a73beb25296cf74b050435aa5d8fd08e/medium/isbn/%d" % i
    



