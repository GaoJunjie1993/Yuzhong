import requests
from bs4 import BeautifulSoup

def getHTML( url ):
    r = requests.get( url )
    return r.content

def parserHTML( html ):
    soup = BeautifulSoup( html, 'html.parser' )

    body = soup.body
    company_middle = body.find('div',attrs={'class':'middle'})
    company_list_ct = company_middle.find('div',attrs={'class':'list-ct'})

    for company_ul in company_list_ct.find_all( 'ul', attrs = { 'class':'company_list' } ):
        for company_li in company_ul.find_all( 'li' ):
            company_url = company_li.a[ 'href' ]
            company_info = company_li.get_text()

            print( company_url, company_info )
            print( company_info )

URL = 'http://www.cninfo.com.cn/cninfo-new/information/companylist'
html = getHTML( URL )
parserHTML( html )
