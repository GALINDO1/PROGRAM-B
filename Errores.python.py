# -*- coding: utf-8 -*-


Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tu9NzawCLWOrMmleMdkdGxGh46gBSRec



**SyntaxError: positional argument follows keyword argument**

Este error ocuure cuando se pone en una posicion después de usar un argumetos.
"""

print ( sep = " My name is " , " Giovanni . " , sep = " " ) 
print ( "but everyone calls me jorgo " )

"""Division by zero

Etse error ocurre cuando se divide por cero uno o mas numero
"""

n=7
ñ=0
d=n/ñ
print(d)

"""Invalid sitax

Este error ocurre cuando se usa mal un sintaxis y el código muestra donde esta el error.
"""

print(/"My name is Giovanni Jordo.but everyone calls me jorgo")

"""Positional argument follows keyword argument

Este error ocurre cuando se utiliza un argumentos de posicion en una función despues de uno argumento de una palabra clave
"""

print ( "/My name is Giovanni Jordo " but everyone calls me jorgo" \ " )

""" EOL while scanning string literal

indica que el intérprete de Python esperaba que ocurriera un carácter o conjunto de caracteres en particular en una línea de código,pero lo caracter no esta al final de la linea. 
"""

print("/My name is Giovanni Jordo""but everyone calls me jorgo"/")

"""INVALID LITERAL FOR INT() with base 10:Dies

Este error se produce cuando se intenta comvertir un objeto en un entero
"""

Giovanni=int ( input ( " Write the age of Giovanni #1 : " ))
Jordo = int ( input ( " Write the age of Jordo # 2 :"))
Dio=int ( input ( " Write the age of Dio # 3 : "))

"""Name "Jordo" is nod define

Este error ocurre por no escribir bien la variable,o no definiste la variable
"""

type(Jordo)

"""List.remove(x):not is list

Este ocurre cuando uno intenta quitar un elemento de la lista que no esta.Para resolver el problema toca ver si esta el elemento en la lista.
"""

Giovanni=[2]
Giovanni.remove(4)

"""Modulo "panda" has no attribute 'dataframe'

Este ocurre cuando en lugar de poner "pd.DateFrame" se pone "pd.dateframe" o tambien por poner panda en vez de pd.
"""

import pandas as pd

Catalogocompras={"Productos":["Combo 1","Combo 2","Combo 3","Combo 4","Papas ","Jugos naturales ","Cerveza","Agua","Gaseosas"],"":["$","$","$","$","$","$","$","$","$"],"Coste":[20000,25000,18000,24500,3000,7000,3500,4000,2500]}
pd.dataframe.from_dict(Catalogocompras)
