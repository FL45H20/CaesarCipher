# CaesarCipher
Caesar Cipher is a method to encryt and decryt secret message, it is too old and not used nowadays, but this is just for beginners. 

## Working
It has 3 options to encryt, decryt or bruteforce the data, choose 0 to encryt, 1 to decryt and 2 to bruteforce

### Encryt
It works by adding a key to the each letter in the message and hence shifting the letters.

### Decryt
It works by subtracting the key from each letter from the key, hence we are shiting the letters back as we have done during encrytion.

### Bruteforce
It works by starting from each key value of 0 and checking all possibility and subtracting that key from the encryted message and trying to get the message back, so we are checking each key and decryting it and printing the decryted data the meaningful decryted code represents the actual key.

## Use
```
git clone https://github.com/FL45H20/CaesarCipher.git
cd CaesarCipher
python CaesarCipher.py option "msg" key
```
