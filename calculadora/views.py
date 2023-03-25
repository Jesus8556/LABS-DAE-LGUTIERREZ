from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Calculadora de Jesus Gutierrez<h1>")

def calculo(request, simbolo, numero1, numero2):
    if simbolo == 'sumar':
        resultado = numero1 + numero2
        operacion = "suma"
        signo = "+"
    elif simbolo == 'restar':
        resultado = numero1 - numero2
        operacion = "resta"
        signo = "-"
    elif simbolo == 'multiplicar':
        resultado = numero1 * numero2
        operacion = "multiplicación"
        signo = "*"
    elif simbolo == 'dividir':
        resultado = numero1 / numero2
        operacion = "division"
        signo = "/"
    else:
        return HttpResponse("Operación no válida")

    respuesta = f"La operación es {operacion} y el resultado de {numero1} {signo} {numero2} =  {resultado}"
    return HttpResponse(respuesta)