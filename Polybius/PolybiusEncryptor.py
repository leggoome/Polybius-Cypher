# Made by Leggoome, 5/13/2025
# square is just the polybius checkerboard
square = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

# Function to actually decode it
def decoder(tst):
    pairs = len(tst) // 2
    output = ""
    for i in range(pairs):
        row = int(tst[i * 2]) - 1
        col = int(tst[i * 2 + 1]) - 1
        output += square[row][col]
    return output

# Function to encode a message
def encoder(msg):
    msg = msg.upper().replace("J", "I")
    output = ""
    for char in msg:
        if char == " ":
            output += "  "
            continue
        found = False  # Flag to track if the character is found
        for row in range(5):
            for col in range(5):
                if square[row][col] == char:
                    output += f"{row + 1}{col + 1} "
                    found = True
                    break
            if found:
                break
        if not found:
            return "Invalid Character, Try again"  # Return if any character is invalid
    return output.strip()

input_str = input("Enter the message to encode: ")
sentence = encoder(input_str)
print(sentence)
