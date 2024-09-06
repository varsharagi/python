#Aryan has two strings S and T containing lowercase alphabets. His student Ram has been asked to encode the string in the following manner.
#Ram should think a positive number K that may transform S into T by shifting each character of S to the right of K positions.
#For example, if K = 1
#Alphabet
#a
#za
#1
#19
#26
#Encoded Alphabet b Similarly,
#If K = 2 then a is shifted to the right of 2 positions, it will become C.If K3 then x is shifted to the right of 3 positions, it will become
#a.
#Submit Feedback
#News for you Grenfell Tower: I...
#b
#C
#C
#d
#e
#Z
#d
#QSeil

#Code:
def find_shift_amount(s, t):
    # Check if the lengths of the strings are different
    if len(s) != len(t):
        return -1  # Return -1 if lengths differ

    # Calculate the shift amount K
    for i in range(len(s)):
        shift = (ord(t[i]) - ord(s[i])) % 26
        if i == 0:
            k = shift
        elif k != shift:
            return -1  # Return -1 if no consistent shift K can be found
    
    return k

def encode_string(s, k):
    encoded = []
    for char in s:
        # Shift character by K positions and wrap around the alphabet
        new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        encoded.append(new_char)
    return ''.join(encoded)

def main():
    # Read strings S and T from user input
    s = input("Enter the first string (S): ")
    t = input("Enter the second string (T): ")
    
    # Find the shift amount K
    k = find_shift_amount(s, t)
    
    if k == -1:
        print("No consistent shift K found")
    else:
        print(f"The shift amount K is: {k}")
        # Encode string S with the found shift amount K
        encoded_s = encode_string(s, k)
        print(f"Encoded string: {encoded_s}")

# This ensures the script runs only when it's executed directly
if __name__ == "__main__":
    main()
