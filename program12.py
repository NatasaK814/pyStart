
import requests

currentRound = 0
mybitarray = []

#make the url for every round - previous round
def makeURI(round):
    url="https://drand.cloudflare.com/public/"
    new_round = int(round) - 1
    currentRound = new_round
    subdomain = str(new_round)
    return url+subdomain

#take the randomness, convert to binary, add it to the list
def keepRandomness(randomness):
    bitakia = bin(int(randomness, 16)).zfill(8)[2:] #removing the "0b" from the beginning
    for bit in bitakia:
        mybitarray.append(int(bit))
    return bitakia

#Round number 100 - last randomness
first_request = requests.get('https://drand.cloudflare.com/public/latest').text
#first_round = first_request[9:16]
#first_randomness = first_request[31:95]
my_request= first_request.split(',')
find_round = my_request[0].split(':')
first_round = find_round[1]
find_random = my_request[1].split(':')
find_random = find_random[1].split('"')
first_randomness = find_random[-2]
currentRound = first_round

#While loop to take the rest 99
count = 99
while count != 0:
    new_request = requests.get(makeURI(currentRound)).text
    current_randomness = new_request[31:95]
    keepRandomness(current_randomness)
    count -=1

#Now we must find the longest 0s and 1s
ones = 0
zeroes = 0
max1 = 0
max0 = 0

for bit in mybitarray:
    if bit == 1:
        zeroes = 0
        ones+=1
        if ones > max1:
            max1 = ones
    else:
        ones=0
        zeroes+=1
        if zeroes > max0:
            max0 = zeroes

print("Total bits in bitArray: ", len(mybitarray) , " bits")
print("Length of the longest 1s' sequence " , max1, " bits!")
print("Length of the longest 0s' sequence " , max0, " bits!")