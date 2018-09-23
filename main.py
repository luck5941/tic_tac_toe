#!/usr/bin/python3
# -*- coding: utf-8 -*-
from re import search as rSearch
from Matrix import Matrix
from Logic import Logic
from random import randint


class Game(Matrix):
	dificultad = 0
	jugadores = 1	
	def __init__(self):
		super().__init__()
		self.player1 = 1
		self.player2 = 4
		print("Qué empiece el juego!")
		self.players = int(input("¿Número de jugadores?\n[1] Tu contra la máquina\n[2]Tu y un compañero"))
		#self.dificultad = int(input("¿Qué grado de dificultad quieres?\n[0] dificil (Única opción de momento)\n"))
		self.gameRoutine()
				
	def end(self):
		"""
		Metodo encargado de determinar si la partida ha finalizado o no.
		Acaba si la suma de alguna combinación posible es el 3 o 12 ya que supone una fila completa por el mismo jugador
		"""
		x = self.sum()
		try:			
			return True if 12 in x or 3 in x else False
		except TypeError:			
			return "Empate"

	def tourn(self, tourn):
		"""
		Metodo enccargado de permitir evaluar si es posible donde quiere poner el jugador
		y se analiza si es valida la opción seleccionada. En caso de ser valida
		se establece en el tablero el valor que define a cada jugador
		int player el jugador al que le toque 1 o 2
		"""
		m = None
		while True:
			pos = input("Jugador {} ({}) donde quiere poner? \n[m],[n]".format(tourn, "x" if tourn == 1 else "o"))
			m = rSearch("^([0-2])[\s,]([0-2])$", pos)
			if m is None:
				print("Por favor introduzca una posición valida\n fila,comula | ejemplo: 3,1")
			else:				
				pos = self.table[int(m.group(1))][int(m.group(2))]
				if pos is 0:					
					return int(m.group(1)), int(m.group(2))	
					break					
				else:
					print("Esa casilla ya está seleccionada, por favor, escoja otra")

			
	def gameRoutine(self):
		"""
		metodo encargado de permitir el juego entre dos usuarios reales. Se trata de un bucle en el cual
		se va mostrando el tablero, se pide la posición a través de self.tourn()
		"""		
		#tourn = randint(1,2)
		tourn = 2		
		if self.players is 1:
			l = Logic(0, self.table)
		while True:
			self.drawTable()			
			j, i = self.tourn(tourn) if self.players is 2 or tourn is 1 else l.getWeights()
			self.table[j][i] = 1 if tourn is 1 else 4
			x =self.end()
			if x == True:
				self.drawTable()
				input("="*12)
				print("Gana el jugador {}".format(tourn)) 
				break
			elif x == "Empate":
				self.drawTable()
				print("Vaya parece que habeis quedado en tablas") 
				break
			tourn = 2 if tourn is 1 else 1
			

	def drawTable(self):
		for j in range(len(self.table)):
			s = ""
			for i in range(len(self.table[j])):
				sing = " " if self.table[j][i] == 0 else "x" if self.table[j][i] == 1 else "o"
				s +="|{}".format(sing)
			print(s+"|")
			
		

g = Game()

