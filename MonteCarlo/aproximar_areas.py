# -*- coding: utf-8 -*-
""" Aproximacion de 3 areas distintas mediante el uso del algoritmo de montecarlo

Primera Figura: Un circulo de Radio 1 centrado en 0,0
Área de la figura = PI*R² = PI

Segunda Figura: La primera figura menos el area de los segmentos circulares delimintados por
dos rectas verticales a 0.6 del origen
Área de la figura   = (Area de la figura 1)-2*arcos(1-(h/R))+sin(2*arcos(1-(h/R)))
                    = PI-2*arcos(0.6)+sin(2*arcos(0.6))

Tercera Figura: La segunda figura menos el area del ciruclo centrado en 0,0 de radio 12
Área de la figura   = (Area de la figura 2)-PI*r²
                    = PI-2*arcos(0.6)+sin(2*arcos(0.6))-PI*0.5²

Detalles de Implementacion

La funcion de evaluacion se aplica indistintamente del numero de parametros de la funcion a evaluar
Los parametros de entrada de la funcion a evaluar han de ser de tipo entero

"""
import random
import inspect
import math

def loop(iterations,function):

    nptos = 0
    ptosIn = 0
    random.seed(10)
    functionArgs = len(inspect.getargspec(function).args)
    for i in range(0, iterations):
        arguments = [random.random() for x in range(0,functionArgs)]
        nptos += 1
        if function(*arguments): ptosIn += 1
    return ptosIn



def areaCirculo(radio):
    return lambda x,y :x ** 2 + y ** 2 <= radio**2

def area1(x,y):
    return areaCirculo(1)(x,y)

def test1():
    return math.pi;

def area2(x,y):
    return (x<=0.6 and area1(x,y))

def test2():
    alpha = 2.*math.acos(0.6)
    return test1()-(alpha-math.sin(alpha))

def area3(x,y):
    return (area2(x,y) and not areaCirculo(0.5)(x,y))

def test3():
    return test2()-(math.pi*(0.5**2))

def calcularAreaFuncion(iteraciones,funcion):
    return 4.*float(loop(iteraciones,funcion))/float(iteraciones)

def evaluar(resultado1,resultado2):
    print ("Obtenido: "+str(resultado1)+" resultado optimo:"+str(resultado2))

def main():
    iteraciones = 1000000
    evaluar(calcularAreaFuncion(iteraciones,area1),test1())
    evaluar(calcularAreaFuncion(iteraciones, area2),test2())
    evaluar(calcularAreaFuncion(iteraciones, area3),test3())


if __name__ == "__main__":
    main()