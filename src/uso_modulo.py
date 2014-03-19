#! /urs/bin/python
#! encoding: UTF-8

import modulo

t_upla=(10,100,1000,10000,100000,1000000,10000000,100000000,1000000000)
for i in t_upla:
   print modulo.aprox(i)
   
#el numero maximo de la t_upla es el valor 100000000
#para los elementos de 10 valores, es decir 1000000000
#si se puede poniendo: 1e1, 1e2, 1e3...


