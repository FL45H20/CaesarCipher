#english alphabets symbols
alpha = ' abcdefghijklmnopqrstuvwxyz012356789.?><"}{+-_)*(*#@$%^&=\\\'.,/~`:;'
key = 3

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
option = raw_input("Please provide whether to code(0) or decipher(1) or bruteforce(2):")

text = raw_input("TEXT: ")

if (option == '0'):
	coded(text)
elif (option == '1'):
	plain(text)
elif (option == '2'):
	brute(text)
else:
	print("Please choose coorect option")
