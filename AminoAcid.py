#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class AminoAcid:

	def __init__(self, posX = 0.0, posY = 0.0, posZ = 0.0,
				 numAA = 0, nomAA = ""):
		self.posX = posX
		self.posY = posY
		self.posZ = posZ
		self.numAA = numAA
		self.nomAA = nomAA

	def distance_to(self, aa):
		"""Compute distance from self to another amino acid object
		"""
		dist = math.sqrt( (aa.posX - self.posX)**2 
						+ (aa.posY - self.posY)**2 
						+ (aa.posZ - self.posZ)**2)
		return dist

