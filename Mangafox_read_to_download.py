from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import sys
import os
import errno
# use this image scraper from the location that 
#you want to save scraped images to
def readingtxt():
    lines = tuple(open('mangafox.txt','r'))
    for link in lines:
        #print(link)
        get_images(link)
def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html,"lxml")

def get_images(url):
    nurl = url.replace('/manga/','/roll_manga/')
    #print(nurl)
    mchapter = url.split('/')[-2]
    mtitle = url.split('/')[-3]
    newfulldic=""
    if (mtitle[0].capitalize()=='V' and (mtitle[1]=='1' or mtitle[1]=='0')):
        mvol = mtitle
        newfulldic = url.split('/')[-4]+"/"+mvol+"/"+mchapter
    else:
        newfulldic = mtitle+"/"+mchapter
    #print(mvol)
    #print(mchapter)
    #print(mtitle)
    #print (newfulldic)
     
    url = nurl
    #print (url)
    soup = make_soup(url)
    #this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img','reader-page')]
    #printing list of imagelink
    #for mim in images:
        #print ( mim)
    print (str(len(images)) + " images found.\nDownloading images to "+newfulldic+" directory.")

    if not os.path.exists(newfulldic):
        os.makedirs(newfulldic)
    
    #compile our unicode list of image links
    image_links = [each.get('data-original') for each in images]
    for each in image_links:
        filename=each.split('/')[-1]        
        print(filename)
        filename = newfulldic+"/"+filename
        urllib.request.urlretrieve(each, filename)
    return image_links
     
#a standard call looks like this
#getlink = input("Enter Mangafox Manga Link : ")
#get_images(getlink)
#get_images('http://m.mangafox.me/manga/sword_girls/c005/1.html')
readingtxt()
