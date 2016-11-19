'''
	+-----------------------------------+
	|  author  : church		    |
	|  Blog    : evilchurch.cc	    |
	|  Github  : github.com/evilchurch  |
	+-----------------------------------+
'''



#!/usr/bin/env python

import zipfile
import itertools, string

def extract(zfile, passwd):
	try:
		zfile.extractall(pwd=passwd)
		print '[+] Passwd Found: { ' + passwd +' }'
		return True
	except:
		pass

def createpassfile(min_len, max_len):
	passfile = open('passFile.txt', 'w')
	chars = string.printable.replace(' \t\n\r\x0b\x0c', '')
	print '[*] Creating passFile...'

	for x in xrange(int(min_len), int(max_len)+ 1):
		for i in itertools.product(chars, repeat=x):
			s = ''.join(i)
			passfile.write("%s\n" % s)
	passfile.close()

def crack(zfile, passfile):
	zfile = zipfile.ZipFile(zfile)
	with open(passfile) as p:
		for line in p.readlines():
			passwd = line.strip('\n')
			if extract(zfile, passwd):
				break

def main():
	print '[*] Please choose the options:\n 1. Get Password with passFile\n 2. Get Password with Brute Force.'
	option = raw_input('[*] Enter Option: ')
	if option == '1':
		zfile = raw_input('[*] Enter zip Filename: ')
		passfile = raw_input('[*] Enter *.txt passFile: ')
		print '[*] Getting Password...'
		crack(zfile, passfile)

	elif option == '2':
		passfile = 'passFile.txt'
		zfile = raw_input('[*] Enter zip Filename: ')
		min_len = raw_input('[*] Enter the Min-Length of Password: ')
		max_len = raw_input('[*] Enter the Max-Length of Password: ')
		if min_len > max_len:
			print '[-] Wrong.. Min-length must be smaller or same as Max-length.'
			exit()
		createpassfile(min_len, max_len)
		print '[*] Getting Password...'
		crack(zfile, passfile)

if __name__ == '__main__':	
	main()
