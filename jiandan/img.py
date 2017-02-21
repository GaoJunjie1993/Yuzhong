import requests
import urllib.request
from bs4 import BeautifulSoup
from time import sleep

class jiandan( object ):
    def __init__( self ):
        pass
    
    def getHTML( self, url ):
        response = requests.get( url, headers )
        return response.text

    def parserHTML( self, html ):
        soup = BeautifulSoup( html, 'html.parser' )
        img = soup.find_all( 'img' )

        download = []
        pic_path = '/home/yz/python/JiandanPic/'

        download_new = []

        for pic_img in img:
            pic_link = pic_img.get( 'src' )
            download.append( pic_link )

        print( download )
        for temp in download:
            download_new.append( temp[ 2: ] ) 
        print( download_new )
    
        for item in download_new:
            urllib.request.urlretrieve( 'http://' + item, pic_path + item[ -10: ] ) 
            print( 'Done' )
            sleep( 3 )


url = 'http://jiandan.net/pic-2016/page-100'
headers = { 
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
my_pic = jiandan()
html = my_pic.getHTML( url )
my_pic.parserHTML( html )
