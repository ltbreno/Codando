#Escrever um programa que leia o simbolo da operação do usuario e dois numeros reais o programa deve retornar o resultado da operaçao
import math
def verificar(sinal):
    if sinal == ('+'):
        print('é um sinal de soma')
    if sinal == ('-'):
        print('é um sinal de subtração')
    if sinal == ('*'):
        print('é um sinal de multiplicação')
    if sinal == ('/'):
        print('é um sinal de divisão')
sinal = str(input('Escreva o sinal da operação: '))
resultado = verificar(sinal)
a = int(input('Escreva um valor para A: '))
b = int(input('Escreva um valor para B: '))
soma = a + b
sub = a - b
multi = a * b
div = a / b
if (sinal) == ('+'):
    print(a, '+', b,'=', soma)
if (sinal) == ('-'):
    print(a, '-', b,'=', sub)
if (sinal) == ('*'):
    print(a, '*', b,'=', multi)
if (sinal) == ('/'):
    print(a, '/', b,'=', div)

