#Esse será o modulo o main central
import os
from tkinter import *

#criando lista para as mensagens
mensagem = []

#pede o nome do usuario
nome = input("Nome: ")

#função para loop infinito
while True:

    #Limpar terminal
    os.system('cls')

     #len(mensagem) retorna o tamanho da lista
    if len(mensagem) > 0:
        for m in mensagem:
            print(m['Nome'], "-", m['Texto'])
    
    print("________________")

    #obtendo texto
    texto = input("Mensagem: ")
    if texto == "fim":
        break

    #adicionando mensagem na lista
    mensagem.append({
        "Nome": nome,
        "Texto": texto
    })