import sys, webbrowser

keywords = '%20'.join(sys.argv[1:])

surugaya = "https://www.suruga-ya.jp/search?category=&search_word=" + '+'.join(sys.argv[1:])
mandarake = "https://order.mandarake.co.jp/order/listPage/list?keyword=" + '%20'.join(sys.argv[1:])
mercari = "https://www.mercari.com/jp/search/?keyword=" + '+'.join(sys.argv[1:])
yahoo = "https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&exflg=1&p=" + '+'.join(sys.argv[1:]) + "&x=0&y=0"

searchedArray = [surugaya, mandarake, mercari, yahoo]

for searchPage in searchedArray:
    webbrowser.open_new_tab(searchPage)