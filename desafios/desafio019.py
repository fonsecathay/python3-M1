'''Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
import random
a1=str(input("Primeiro Aluno:"))
a2=str(input("PSegundo Aluno:"))
a3=str(input("Terceiro Aluno:"))
a4=str(input("Quarto Aluno:"))
lista=[a1, a2, a3, a4]
print("O aluno sorteado é:{}".format(random.choice(lista)))