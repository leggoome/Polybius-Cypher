# Polybius Cipher Program

def polybiusCipher(s):
    for char in s:
        if char == ' ':
            continue  # skip spaces
        row = int((ord(char) - ord('a')) / 5) + 1
        col = ((ord(char) - ord('a')) % 5) + 1

        if char == 'k':
            row = row - 1
            col = 5 - col + 1
        elif ord(char) >= ord('j'):
            if col == 1:
                col = 6
                row = row - 1
            col = col - 1

        print(row, col, end='', sep='')

if __name__ == "__main__":
    user_input = input("Enter message to encrypt: ").lower()
    print("You entered:", user_input)
    polybiusCipher(user_input)
