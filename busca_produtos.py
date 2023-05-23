from selenium import webdriver

#* Abrindo uma janela no Google Chrome
chrome = webdriver.Chrome()
links = ['https://lista.mercadolivre.com.br/' ]
produto = str(input('Digite o produto que precisa ser pesquisado: '))
busca = chrome.get(links + produto)