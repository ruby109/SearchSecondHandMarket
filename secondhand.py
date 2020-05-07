# -*- coding: utf-8 -*-

import sys, webbrowser
try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse as urlparse
import tkinter as tk


def open_browsers(event):
    global window
    product = productNameEntry.get()
    searchedArray = []


    if surugayaCheck.get() == True:
        surugayaURL = "https://www.suruga-ya.jp/search?category=&search_word=" + urlparse.quote(product.encode('utf-8'))
        searchedArray.append(surugayaURL)

    if mandarakeCheck.get() == True:
        mandarakeURL = "https://order.mandarake.co.jp/order/listPage/list?keyword=" + urlparse.quote(product.encode('utf-8'))
        searchedArray.append(mandarakeURL)

    if mercariCheck.get() == True:
        mercariURL = "https://www.mercari.com/jp/search/?keyword=" + urlparse.quote(product.encode('utf-8'))
        searchedArray.append(mercariURL)

    if yahooCheck.get() == True:
        yahooURL = "https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&exflg=1&p=" + urlparse.quote(product.encode('utf-8')) + "&x=0&y=0"
        searchedArray.append(yahooURL)

    if otamartCheck.get() == True:
        otamartURL = "https://otamart.com/search/?keyword=" + urlparse.quote(product.encode('utf-8'))
        searchedArray.append(otamartURL)

    for searchPage in searchedArray:
        webbrowser.open_new(searchPage)

window = tk.Tk()
window.title('Second Hand')
# window.geometry('500x500')

productLabel = tk.Label(window, text='商品名')
productLabel.grid(row = 0, column = 0, sticky='w')

productNameEntry = tk.Entry(window)
productNameEntry.grid(row = 0, column = 1)

searchButton = tk.Button(window, text='Search')
searchButton.bind('<Button-1>', open_browsers)
searchButton.grid(row = 0, column = 2)

surugayaCheck = tk.BooleanVar()
surugayaCheckButton = tk.Checkbutton(window, text = "Suruga-ya", variable = surugayaCheck, onvalue = True, offvalue = False, height = 0, width = 0)
surugayaCheckButton.select()
surugayaCheckButton.grid(row = 1, column = 0, sticky='w')

mandarakeCheck = tk.BooleanVar()
mandarakeCheckButton = tk.Checkbutton(window, text = "Mandarake", variable = mandarakeCheck, onvalue = True, offvalue = False, height = 0, width = 0)
mandarakeCheckButton.select()
mandarakeCheckButton.grid(row = 1, column = 1)

mercariCheck = tk.BooleanVar()
mercariCheckButton = tk.Checkbutton(window, text = "Mercari", variable = mercariCheck, onvalue = True, offvalue = False, height = 0, width = 0)
mercariCheckButton.select()
mercariCheckButton.grid(row = 2, column = 0, sticky='w')

yahooCheck = tk.BooleanVar()
yahooCheckButton = tk.Checkbutton(window, text = "Yahoo Auction", variable = yahooCheck, onvalue = True, offvalue = False, height = 0, width = 0)
yahooCheckButton.select()
yahooCheckButton.grid(row = 2, column = 1)

otamartCheck = tk.BooleanVar()
otamartCheckButton = tk.Checkbutton(window, text = "Otamart", variable = otamartCheck, onvalue = True, offvalue = False, height = 0, width = 0)
otamartCheckButton.select()
otamartCheckButton.grid(row = 3, column = 0, sticky='w')

window.mainloop()





