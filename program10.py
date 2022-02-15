# apt install python3-pip
# pip3 install bitarray

#from bitstring import BitArray
import binascii
import bitarray 

ba = bitarray.bitarray()
bitlist = []
numberlist=[]

#take the binary and only 2 first + 2 lasts bits
def modifyChar(char):
    bitar = bitarray.bitarray()
    bitar.frombytes(char.encode('utf-8'))
    byte = str(bitar)
    byte = byte[11:-2]
    temp =[byte[0], byte[1], byte[-2], byte[-1]]
    return temp


#function to convert an array of integers to a decimal number
def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))


#seperate every 16bits 
def makeNumberlist():
    bitsb=[]
    count = 0
    for bit in bitlist:
        bitsb.append(bit)
        count+=1
        if count == 16:
            numberlist.append(binatodeci(bitsb))
            bitsb=[]
            count = 0


def even():
    totalNumbers = len(numberlist)
    evenNumbers = 0
    for number in numberlist:
        if number%2 == 0:
            evenNumbers+=1
    return evenNumbers/totalNumbers*100
            

def mod3():
    totalNumbers = len(numberlist)
    numbers3 = 0
    for number in numberlist:
        if number%3 == 0:
            numbers3+=1
    return numbers3/totalNumbers*100
    

def mod5():
    totalNumbers = len(numberlist)
    numbers5 = 0
    for number in numberlist:
        if number%5 == 0:
            numbers5+=1
    return numbers5/totalNumbers*100


def mod7():
    totalNumbers = len(numberlist)
    numbers7 = 0
    for number in numberlist:
        if number%7 == 0:
            numbers7+=1
    return numbers7/totalNumbers*100

    
# open a file and read it using ASCII encoding
file = open('two_cities_ascii.txt', mode='r', encoding='ascii').read()


for char in file:
    #editing each byte according to the given instructions
    temp = modifyChar(char)
    for i in range(0, len(temp)):
        bitlist.append(int(temp[i]))

makeNumberlist()

print("Even numbers :" , even() , "%")

print("Multiple of 3 :" , mod3() , "%")

print("Multiple of 5 :" , mod5() , "%")

print("Multiple of 7 :" , mod7() , "%")