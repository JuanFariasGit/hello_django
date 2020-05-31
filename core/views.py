from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("HOME")

def hello(request, nome, idade):
    return HttpResponse("<h1 style='display: flex; justify-content: center'>Hello {} de {} anos</h1>".format(nome, idade))

def soma(request, num1, num2):
    return HttpResponse("<h1 style='display: flex; justify-content: center'>{} + {} = {}</h1>".format(num1, num2, num1 + num2))

def multiplicacao(request, num1, num2):
    return HttpResponse("<h1 style='display: flex; justify-content: center'>{} x {} = {}</h1>".format(num1, num2, num1 * num2))

def divisao(request, num1, num2):
    return HttpResponse("<h1 style='display: flex; justify-content: center'>{} / {} = {}</h1>".format(num1, num2, num1 / num2))

def tabuada_multiplicacao(request, num):
    tabuada = []
    for n in range(11):
        tabuada.append("<h1 style='display: flex; justify-content: center'>{} x {} = {}</h1>".format(num, n, num * n))
    return HttpResponse(tabuada)

def numeros_primos(request, num):
    lista_numeros_primos = [] 
    for n in range(1, num + 1):
        cont = 0
        for i in range(1, n + 1):
            if (n % i == 0):
                cont += 1
        if cont == 2:
            lista_numeros_primos.append("<h1 style='display:flex; justify-content: center'>{}</h1>".format(n))
    return HttpResponse(lista_numeros_primos)

def fizzbuzz(request):
    lista_resultados = []
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            lista_resultados.append("<h1 style='display:flex; justify-content: center'>FizzBuzz</h1>")
        elif n % 3 == 0:
            lista_resultados.append("<h1 style='display:flex; justify-content: center'>Fizz</h1>")
        elif n % 5 == 0:
            lista_resultados.append("<h1 style='display:flex; justify-content: center'>Buzz</h1>")
        else:
            lista_resultados.append("<h1 style='display:flex; justify-content: center'>{}</h1>".format(n))
    return HttpResponse(lista_resultados)