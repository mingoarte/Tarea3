#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import *
import datetime

# Integrantes:
# Barbara Hernandez. 10-11246
# Domingo Arteaga. 11-10058.

# Clase de Billetera electronica.
class BilleteraElectronica(object):
	
	def __init__(self, Id, Nombre, Apellido, Ci, Pin, Total, Lista_recargas, Lista_consumos):
		self.Id = Id
		self.Nombre = Nombre
		self.Apellido = Apellido
		self.Ci = Ci
		self.Pin = Pin
		self.Total = Total
		self.Lista_recargas = Lista_recargas
		self.Lista_consumos = Lista_consumos

	# Metodo de recargar.
	def recargar(self, monto, fecha, ide):
		self.Total = self.Total + monto
		lista = [monto,fecha,ide]
		self.Lista_recargas.append(lista)

	# Metodo de consumir.
	def consumir(self, monto, fecha, ide, ingrese_pin):
		if ingrese_pin != self.Pin:
			print("Pin invalido. Transaccion fallida.")
		else:
			if self.Total >= monto:
				self.Total = self.Total - monto
				lista = [monto, fecha, ide]
				self.Lista_consumos.append(lista)
			else:
				print("Monto insuficiente.")

	# Metodo que imprime el saldo.
	def saldo(self):
		print(self.Total)
