#!/usr/bin/python3

import re


vAxiomas = ["Entre tres puntos, solo pasa una línea recta", "Una proposición no puede ser verdadera y falsa al mismo tiempo", "Si dos números naturales tienen el mismo sucesor, esos dos números son el mismo número.",
            "Todas las rectas tienen una cantidad infinita de puntos.", "Dos rectas paralelas nunca se tocan", "Dos líneas rectas nunca encierran algo."]


class axiomaModel:
    def obtenerAxioma(self, vNroEscogido):
         if vNroEscogido >= 1:

             vResult = vAxiomas[vNroEscogido>=1]
           
             return vResult

         else:
          
            if vNroEscogido == 0:

             vResult = "El numero que ah ingresado es incorrecto"
             
         return vResult