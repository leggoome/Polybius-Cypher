#Made by Leggoome, 12/17/2024
#Decode is just the polybius checkerboard
decode = [
['A', 'B', 'C', 'D', 'E'],
['F', 'G', 'H', 'I', 'K'],
['L', 'M', 'N', 'O', 'P'],
['Q', 'R', 'S', 'T', 'U'],
['V', 'W', 'X', 'Y', 'Z']
]

# Function to actually decode it
def decoder(tst):
    pairs = int(len(tst)/2)
    output = ""
    for i in range(pairs):
        row = int(tst[i*2])-1
        col = int(tst[i*2 + 1])-1
        output = output + decode[row][col]
    return(output)

#Add your encoded string here

input_str = input("Enter the encoded message: ")
message = int(input_str)  # Remove spaces from the input
sentence = ""
words = input_str.split()
for w in words:
    sentence = sentence + " " + decoder(w)
    
print(sentence)