#!/usr/bin python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

print( 'hello1' )
def getHTML( url ):
    r = requests.get( url )
    return r.text

print( 'hello2' )
def parserHTML( html ):
    soup = BeautifulSoup( html, 'html.parser' )

    print( 'hello3' )
    body = soup.body
    company_middle = body.find('div',attrs={'class':'middle'})
    company_list_ct = company_middle.find('div',attrs={'class':'list-ct'})
    print( 'company_list_ct', company_list_ct )
    print( 'hello4' )
    for company_ul in company_list_ct.find_all( 'ul', attrs = { 'class':'company_list' } ):
        print( 'hello5' )
        for company_li in company_ul.find_all( 'li' ):
            print( 'hello6' )
            company_url = company_li.a[ 'href' ]
            company_info = company_li.get_text()

            print( company_url, company_info )
            print( company_info )

URL = 'http://www.cninfo.com.cn/cninfo-new/information/companylist'
html = getHTML( URL )
parserHTML( html )
