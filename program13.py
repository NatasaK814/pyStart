
import requests

#take the latest randomness
my_request = requests.get('https://drand.cloudflare.com/public/latest').text
my_randomness = my_request[31:95]
doubles = []

#divide hexadecimal characters into pairs, then numbers modulo 80
for i in range (0, len(my_randomness), 2):
    decodedNumber=my_randomness[i]+my_randomness[i+1]
    decodedNumber = int(decodedNumber, 16) % 80
    doubles.append(decodedNumber)

#take the winning numbers of kino
first_request = requests.get('https://api.opap.gr/draws/v3.0/1100/last-result-and-active').text
first_request = first_request.split(',')
first_number = first_request[11].split('[')[-1]
last_number = first_request[30].split(']')[0]

#add kino numbers in a list
numbers = []
numbers.append(int(first_number))
for num in first_request[12:29]:
    numbers.append(int(num))
numbers.append(int(last_number))

#compare with kino numbers
similar = []
count = 0
for ranNumber in doubles:
    for kino in numbers:
        if kino == ranNumber:
            count += 1
            similar.append(kino)
            break


print("Similar Numbers found from random generated hex with the KINO results where :" , count)
print("Βelow are the numbers we found:")
for n in similar:
    print (n)