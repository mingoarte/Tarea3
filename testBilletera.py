#!/usr/bin/env python
# -*- coding: utf-8 -*-
from billeteraelectronica import * 
from datetime import *
import unittest , datetime

# Integrantes:
# Barbara Hernandez. 10-11246
# Domingo Arteaga. 11-10058.

class TestBilletera(unittest.TestCase):

	def testMalicia1(self):
		prueba = BilleteraElectronica(1,'bárbara', 'herñandez', 123123, 999, 0, [] , [])
		f = date(2017,1,31)
		prueba.recargar(500, f, 21332)
		prueba.consumir(200 , f, 'feofekofe',999)
		self.assertEqual(prueba.Total,300)
	
	def testMalicia2(self):
		prueba = BilleteraElectronica(1,'bárbüra', 'hernan-dez', 123123, 999, 0, [] , [])
		f = date(2017,1,31)
		prueba.recargar(500, f, 21332)
		prueba.consumir(200 , f, 'feofekofe',999)
		self.assertEqual(prueba.Total,300)	

	def testMalicia3(self):
		prueba = BilleteraElectronica(1,'bárbüra', 'hernan-dez', 123123, 999, 0, [] , [])
		f = date(2017,1,31)
		prueba.recargar(500, f, 21332)
		prueba.recargar(5300, f, 213)
		prueba.recargar(100, f, 21)
		prueba.consumir(700 , f, 'feofekofe',999)
		prueba.consumir(200 , f, 12134,999)
		prueba.consumir(2000 , f, 254,999)
		self.assertEqual(prueba.Total,3000)	

	def testMalicia4(self):
		prueba = BilleteraElectronica(1,'bárbüra', 'hernan-dez', 123123, 999, 0, [] , [])
		f = date(2017,1,31)
		prueba.recargar(5000, f, 21332)
		prueba.recargar(5300, f, 213)
		prueba.recargar(200, f, 21)
		prueba.consumir(7000 , f, 'feofekofe',999)
		prueba.consumir(500 , f, 12134,999)
		prueba.consumir(2000 , f, 254,999)
		self.assertEqual(prueba.Total,1000)		

	def testFrontera1(self):
		prueba = BilleteraElectronica(1,'bárbüra', 'herna-ñndez', 123123, 999, 0, [] , [])
		f = date(2017,1,31)
		prueba.recargar(500, f, 21332)
		prueba.consumir(500 , f, 'feofekofe',999)
		self.assertEqual(prueba.Total,0)
	
	def testFrontera2(self):
		prueba = BilleteraElectronica(1,'bárbüra', 'herna-ñndez', 123123, 999, 0, [] , [])
		f = date(2017,1,31)
		prueba.recargar(500, f, 21332)
		prueba.consumir(0 , f, 'feofekofe',999)
		self.assertEqual(prueba.Total,500)

	def testEsquina1(self):
		prueba = BilleteraElectronica(1,'bárbüra', 'herna-ñndez', 123123, 999, 0, [] , [])
		f = date(2017,1,31)
		prueba.recargar(500, f, 21332)
		prueba.consumir(499 , f, 'feofekofe',999)
		self.assertEqual(prueba.Total,1)

	def testEsquina2(self):
		prueba = BilleteraElectronica(1,'bárbüra', 'herna-ñndez', 123123, 999, 0, [] , [])
		f = date(2017,1,31)
		prueba.recargar(500, f, 21332)
		prueba.consumir(1 , f, 'feofekofe',999)
		self.assertEqual(prueba.Total,499)