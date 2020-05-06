# -*- coding: utf-8 -*-

import sys, webbrowser, urllib.parse

surugaya = "https://www.suruga-ya.jp/search?category=&search_word=" + urllib.parse.quote(' '.join(sys.argv[1:]).encode('utf-8')) 
mandarake = "https://order.mandarake.co.jp/order/listPage/list?keyword=" + urllib.parse.quote(' '.join(sys.argv[1:]).encode('utf-8'))
mercari = "https://www.mercari.com/jp/search/?keyword=" + urllib.parse.quote(' '.join(sys.argv[1:]).encode('utf-8'))
yahoo = "https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&exflg=1&p=" + urllib.parse.quote(' '.join(sys.argv[1:]).encode('utf-8')) + "&x=0&y=0"
otamart = "https://otamart.com/search/?keyword=" + urllib.parse.quote(' '.join(sys.argv[1:]).encode('utf-8'))

searchedArray = [surugaya, mandarake, mercari, yahoo, otamart]
for searchPage in searchedArray:
    webbrowser.open_new(searchPage)