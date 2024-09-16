#!/usr/bin/env python

import math


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage**2/resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	# v1[0] et v2[0] pour accéder au X
	# v1[1] et v2[1] pour accéder au Y
	'''
	if (v1[0]*v2[0]+v1[1]*v2[1]==0) or  (v1[0]==0 and v1[1]==0) or (v2[0]==0 and v2[1]==0):
		print(f'{v1} et {v2} sont orthogonaux')
	else :
		print(f'{v1} et {v2} ne sont pas orthogonaux')
	pass'''
	#or  (v1[0]==0 and v1[1]==0) or (v2[0]==0 and v2[1]==0) c'est inutile
	#parce que le produit scalaire va toujours donner 0
	return v1[0]*v2[0]+v1[1]*v2[1]==0
	

def point_in_circle(point, circle_center, circle_radius):
	# TODO: Retourner vrai si le point est à l'intérieur du cercle, faux sinon.
	# point[0] et circle_center[0] pour accéder au X
	# point[1] et circle_center[1] pour accéder au Y
	
	''' 
	#if math.sqrt((point[0]-circle_center[0])**2 + (point[1]-circle_center[1])**2) < circle_radius:
	# 	return True
	# else:
	# 	return False 
	# pass'''
	return math.sqrt((point[0]-circle_center[0])**2 + (point[1]-circle_center[1])**2) <= circle_radius

def cash(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$, 25¢, 10¢ et 5¢ à remettre pour représenter la valeur. Il faut arrondir à la pièce de 5¢ près. Il faut remplir les variables twenties, tens, fives, twos, ones, quarters, dimes et nickels avec le quantité de chaque dénomination.
	twenties=round(value//20)
	value-=twenties*20
	tens=round(value//10)
	value-=tens*10
	fives=round(value//5)
	value-=fives*5
	ones=round(value//1)
	value-=ones*1
	quarters=round(value//0.25)
	value-=quarters*0.25
	dimes=round(value//0.10)
	value-=dimes*0.10
	#nickels=round(value//0.05) #arrondi par défaut 
	#en arrondi par excès, on aura:
	nickels=math.ceil(value/0.05)

	

	return twenties, tens, fives,ones, quarters, dimes, nickels
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$, 25¢, 10¢ et 5¢ à remettre pour représenter la valeur. Il faut arrondir à la pièce de 5¢ près. Il faut remplir les variables twenties, tens, fives, ones, quarters, dimes et nickels avec le quantité de chaque dénomination.

	return twenties, tens, fives, ones, quarters, dimes, nickels

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres.
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result=""
	abs_value=abs(value)
	while abs_value !=0:
		rest=abs_value%base
		result+=digit_letters[rest]
		abs_value//=base
		pass
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		result += '-'
		pass
	
	return result [::-1]

	'''result = ""
	list_rest=[]
	abs_value = abs(value)
	while abs_value != 0:
		while abs_value//base !=0:
			list_rest.append(value%base)
			list_rest=list_rest.reverse
		for element in list_rest:
			result+=digit_letters[element]			
		#pass
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		result='-'+result
		#pass
	return result '''
	'''result = ""
	rest=""
	abs_value = abs(value)
	while abs_value != 0:
		while abs_value//base !=0:
			rest+=str(abs_value%base)
			rest=rest[::-1]	
		for element in rest:
			result+=digit_letters[int(element)]
		
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		result='-'+result
		
	return result'''

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(point_in_circle([-1, 1], [1, -1], 2))
	print(cash(137.38))
	print(format_base(-42, 16, "0123456789ABCDEF"))
