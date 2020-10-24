#!/usr/bin/python

"""
date: 2017.09.05-11
author: Vladyslav Mambetov
"""


def initialization():
	write('\033]0;Crypt\007')#change the title of the window
	cursoroff()
	clrscr()
	return


def show_menu():

	#initial values
	menu_quantity_items = 6
	menu_select_item = 0

	display_menu(menu_select_item, menu_quantity_items)

	while True:

		menu_key = getkey()

		menu_select_item = switch_item(menu_key, menu_select_item, menu_quantity_items)

		if menu_key == 13 or menu_key == 67:
			if menu_select_item == 0:
				program1()
			if menu_select_item == 1:
				program2()
			if menu_select_item == 2:
				program3()
			if menu_select_item == 3:
				program4()
			if menu_select_item == 4:
				program5()	
			if menu_select_item == menu_quantity_items - 1:
				return 

		clrscr()
		display_menu(menu_select_item, menu_quantity_items)

	return

def finalization():
	clrscr()
	return


"""==============================================================================
->next function:
	display_menu()
	display_program1()
	switch_selection()
	program1()
	program2()
	program3()
	program4()
	program5()
	encrypt1()
	decrypt1()
	getpassword1()
	encrypt2()
	decrypt2()
	getpassword2()
	encrypt3()
	decrypt3()
	getpassword3()
"""
def display_menu(item, max_item):

	if item == 0:
		print '>>program 1'
	else:
		print '  program 1'

	if item == 1:
		print '>>program 2'
	else:
		print '  program 2'

	if item == 2:
		print '>>program 3'
	else:
		print '  program 3'

	if item == 3:
		print '>>program 4'
	else:
		print '  program 4'

	if item == 4:
		print '>>program 5'
	else:
		print '  program 5'

	print ''

	if item == max_item - 1:
		print '>>exit'
	else:
		print '  exit'

	return

def display_program1(item, max_item):
	if item == 0:
		print '>>encrypt'
	else:
		print '  encrypt'

	if item == 1:
		print '>>decrypt'
	else:
		print '  decrypt'

	print ''

	if item == max_item - 1:
		print '>>back'
	else:
		print '  back'
	return

def switch_item(menu_key, item, max_item):

	result = item

	if menu_key == 66:
		result = (item + 1) % max_item

	if menu_key == 65:
		if item == 0:
			result = max_item - 1
		else:
			result = item - 1

	if menu_key == 127 or menu_key == 68:
		result = max_item - 1

	return result

def program1():

	#initial values
	program1_quantity_items = 3
	program1_select_item = 0

	clrscr()
	display_program1(program1_select_item, program1_quantity_items)

	while True:

		program1_key = getkey()

		program1_select_item = switch_item(program1_key, program1_select_item, \
			program1_quantity_items)

		if program1_key == 127 or program1_key == 68:
			return

		if program1_key == 13 or program1_key == 67:
			if program1_select_item == 0:

				clrscr()

				#key = '6231547' -- used for testing
				key = getpassword2('Enter the key for encryption: ')
				while key == False:
					print 'Error. The password is incorrect.'
					key = getpassword2('Enter the key for encryption: ')

				f1 = open('origin.txt')
				f2 = open('res.txt', 'w')

				txt = f1.read()
				txt = encrypt2(txt, key)
				f2.write(txt)

				f1.close()
				f2.close()

				print ''
				print 'Text is encrypted from the file "origin.txt"'\
					+ ' to the file "res.txt"'
				pause()

			if program1_select_item == 1:

				clrscr()

				#key = '6231547' -- used for testing
				key = getpassword2('Enter the key for decryption: ')
				while key == False:
					print 'Error. The password is incorrect.'
					key = getpassword2('Enter the key for decryption: ')

				f1 = open('origin.txt', 'w')
				f2 = open('res.txt')

				txt = f2.read()
				txt = decrypt2(txt, key)
				f1.write(txt)

				f1.close()
				f2.close()

				print ''
				print 'The text is decrypted from the file "res.txt"'\
					+ ' to the file "origin.txt"'
				pause()

			if program1_select_item == program1_quantity_items - 1:
				return 

		clrscr()
		display_program1(program1_select_item, program1_quantity_items)

	return

def program2():

	#initial values
	program1_quantity_items = 3
	program1_select_item = 0

	clrscr()
	display_program1(program1_select_item, program1_quantity_items)

	while True:

		program1_key = getkey()

		program1_select_item = switch_item(program1_key, program1_select_item, \
			program1_quantity_items)

		if program1_key == 127 or program1_key == 68:
			return

		if program1_key == 13 or program1_key == 67:
			if program1_select_item == 0:

				clrscr()

				#key = 'g' -- used for testing
				key = getpassword2('Enter the key for encryption: ')
				while key == False:
					print 'Error. The password is incorrect.'
					key = getpassword2('Enter the key for encryption: ')

				f1 = open('origin.txt')
				f2 = open('res.txt', 'w')

				txt = f1.read()
				txt = encrypt2(txt, key)
				f2.write(txt)

				f1.close()
				f2.close()

				print ''
				print 'Text is encrypted from the file "origin.txt"'\
					+ ' to the file "res.txt"'
				pause()

			if program1_select_item == 1:

				clrscr()

				#key = 'g' -- used for testing
				key = getpassword2('Enter the key for decryption: ')
				while key == False:
					print 'Error. The password is incorrect.'
					key = getpassword2('Enter the key for decryption: ')

				f1 = open('origin.txt', 'w')
				f2 = open('res.txt')

				txt = f2.read()
				txt = decrypt2(txt, key)
				f1.write(txt)

				f1.close()
				f2.close()

				print ''
				print 'The text is decrypted from the file "res.txt"'\
					+ ' to the file "origin.txt"'
				pause()

			if program1_select_item == program1_quantity_items - 1:
				return 

		clrscr()
		display_program1(program1_select_item, program1_quantity_items)

	return

def program3():

	#initial values
	program1_quantity_items = 3
	program1_select_item = 0

	clrscr()
	display_program1(program1_select_item, program1_quantity_items)

	while True:

		program1_key = getkey()

		program1_select_item = switch_item(program1_key, program1_select_item, \
			program1_quantity_items)

		if program1_key == 127 or program1_key == 68:
			return

		if program1_key == 13 or program1_key == 67:
			if program1_select_item == 0:

				clrscr()

				#key = '123qwE' -- used for testing
				key = getpassword3('Enter the key for encryption: ')
				while key == False:
					print 'Error. The password is incorrect.'
					key = getpassword3('Enter the key for encryption: ')

				f1 = open('origin.txt')
				f2 = open('res.txt', 'w')

				txt = f1.read()
				txt = encrypt3(txt, key)
				f2.write(txt)

				f1.close()
				f2.close()

				print ''
				print 'Text is encrypted from the file "origin.txt"'\
					+ ' to the file "res.txt"'
				pause()

			if program1_select_item == 1:

				clrscr()

				#key = '123qwE' -- used for testing
				key = getpassword3('Enter the key for decryption: ')
				while key == False:
					print 'Error. The password is incorrect.'
					key = getpassword3('Enter the key for decryption: ')

				f1 = open('origin.txt', 'w')
				f2 = open('res.txt')

				txt = f2.read()
				txt = decrypt3(txt, key)
				f1.write(txt)

				f1.close()
				f2.close()

				print ''
				print 'The text is decrypted from the file "res.txt"'\
					+ ' to the file "origin.txt"'
				pause()

			if program1_select_item == program1_quantity_items - 1:
				return 

		clrscr()
		display_program1(program1_select_item, program1_quantity_items)

	return

def program4():
	clrscr()
	print 'Not finished.'
	getkey()
	return

def program5():
	clrscr()
	print 'Not finished.'
	getkey()
	return

def encrypt1(txt, key):

	#alignment
	if len(txt) % len(key) > 0:
		txt += ' ' * (len(key) - len(txt) % len(key))

	st1_key = 0
	txt2 = ''

	for j in range(len(txt) / len(key)):
		st1 = ''

		for i in range(len(key)):
			st1 += txt[st1_key]
			st1_key += 1

		st2 = ''

		for i in range(len(key)):
			st2 += st1[int(key[i]) - 1]

		txt2 += st2

		txt2 = txt2.strip(' ')

	return txt2

def decrypt1(txt, key):

	#alignment
	if len(txt) % len(key) > 0:
		txt += ' ' * (len(key) - len(txt) % len(key))

	st1_key = 0
	txt2 = ''

	for j in range(len(txt) / len(key)):
		st1 = ''

		for i in range(len(key)):
			st1 += txt[st1_key]
			st1_key += 1

		st2 = key

		for i in range(len(key)):
					st2 = st2[:int(key[i]) - 1] + st1[i] + st2[int(key[i]):]

		txt2 += st2

		txt2 = txt2.strip(' ')

	return txt2

def getpassword1(msg):

	write('\n')
	pw = raw_input(msg)

	if len(pw) < 1:
		return False

	pw2 = pw

	for i in range(len(pw)):
		pw2 = pw2[:int(pw[i]) - 1] + pw[i] + pw2[int(pw[i]):]

	i = 1

	for k in pw2:
		if int(k) <> i:
			return False
		i += 1

	return pw

def encrypt2(txt, key):

	txt2 = ''

	'''
	for ch in txt:
		txt2 += chr((ord(ch) + ord(key)) % 224 + 31)
	'''
	for ch in txt:
		if s > 31:
			txt2 += chr(ord(ch) - 32 + k) % 224 + 32
			

	return txt2

def decrypt2(txt, key):

	txt2 = ''

	for ch in txt:
		p = ord(ch) - ord(key) - 31
		if p < 0:
			p = 224 - (p * -1) % 224
		txt2 += chr(p)

	return txt2

def getpassword2(msg):

	write('\n')
	k = raw_input(msg)

	if len(k) < 0 or len(k) > 224:
		return False

	return k

def encrypt3(txt, key):

	txt2 = ''
	inx = 0

	for ch in txt:
		txt2 += chr((ord(ch) + ord(key[inx])) % 224 + 31)
		inx = (inx + 1) % len(key)

	return txt2

def decrypt3(txt, key):

	txt2 = ''
	inx = 0

	for ch in txt:
		p = ord(ch) - ord(key[inx]) - 31
		if p < 0:
			p = 224 - (p * -1) % 224
		txt2 += chr(p)
		inx = (inx + 1) % len(key)

	return txt2

def getpassword3(msg):

	write('\n')
	kw = raw_input(msg)

	if len(kw) < 1:
		return False

	return kw

"""==============================================================================
->next function:
	clrscr()
	getkey()
	cursoron()
	cursoroff()
	write()
	pause()
"""
def clrscr():
	write('\033c')
	return

def write(value):

	import sys

	sys.stdout.write(value)

	return

def getkey():
    import termios
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return ord(_getch())

def cursoron():
	write('\033[?25h')
	return

def cursoroff():
	write('\033[?25l')
	return

def pause():
	getkey()
	return

"""==============================================================================
->Entry point
"""
initialization()
show_menu()
finalization()