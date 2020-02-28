#for cmd line args
import sys

#english alphabets symbols
alpha = ' abcdefghijklmnopqrstuvwxyz012356789.?><"}{+-_)*(*#@$%^&=\\\'.,/~`:;'
key = int(sys.argv[1])

#function for coding
def coded(text):
	code = ''

	for char in text:
		code = code + alpha[(alpha.find(char.lower()) + key) % len(alpha)]

	print("CODE: ", code)

#function for decode
def plain(text):
	decipher= ''

	for char in text:
		decipher = decipher + alpha[(alpha.find(char.lower()) - key) % len(alpha)]
	print("PLAIN: ", decipher)

#function to bryteforce each key
def brute(text):
	decipher  = ''

	for k in range(len(alpha)):
		for char in text:
                	decipher = decipher + alpha[(alpha.find(char.lower()) - k) % len(alpha)]
		print("KEY: ", k, "DECODE: ", decipher)
		decipher = ''

#user part
option = sys.argv[2]

text = sys.argv[3]

if (option == '0'):
	coded(text)
elif (option == '1'):
	plain(text)
elif (option == '2'):
	brute(text)
else:
	print("Please choose coorect option")
