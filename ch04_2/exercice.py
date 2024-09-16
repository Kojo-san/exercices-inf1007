#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name):
	first_p=name.split('-')
	first_part_name=str(first_p[0]).capitalize()  
	return f"Bonjour, {first_part_name}"
	#return "Bonjour, "+ first_part_name

def get_random_sentence(animals, adjectives, fruits):
	random_number=random.randrange(0,2)
	return f"Aujourd'hui, j'ai vu un {animals[random_number]} s'emparer d'un panier {adjectives[random_number]} plein de {fruits[random_number]}"

def encrypt(text, shift):
	text_encrypt=""
	for letter in text:
		if letter.isalpha():
			letter=chr(ord(letter)+shift)
			if not letter.isalpha():
				letter=chr(ord(letter)- 26)
		letter=letter.upper()
		text_encrypt+=letter		
	return text_encrypt

def decrypt(encrypted_text, shift):
	return encrypt(encrypted_text, -shift)


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
