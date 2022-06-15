import requests
from  tkinter import *

def pegar_cotacoes():
    requisisao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisisao_dic = requisisao.json()

    cotacao_dolar = requisisao_dic['USDBRL']['bid']
    cotacao_euro = requisisao_dic['EURBRL']['bid']
    cotacao_btc = requisisao_dic['BTCBRL']['bid']

    texto = f"""
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}"""

    texto_cotacoes["text"] = texto

janela = Tk()
janela.title("Cotação atual das Moedas")
<<<<<<< HEAD
janela.geometry("300x250")
=======
janela.geometry("300x300")
>>>>>>> 24e9770383d1ddafcd12f7625d04d016de08d432

texto_orientacao = Label(janela, text="CLIQUE PARA VER A COTAÇÃO ATUAL DAS MOEDAS")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar cotações Dólar/Euro/BTC", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=5, pady=10)

texto_cotacoes = Label(janela, text="Refresh a cada 5 segundos")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

<<<<<<< HEAD
def Close():
    janela.destroy()

botao_saida = Button(janela, text="SAIR", command=Close)
botao_saida.grid(pady=8)

janela.mainloop()
=======
janela.mainloop()
>>>>>>> 24e9770383d1ddafcd12f7625d04d016de08d432
