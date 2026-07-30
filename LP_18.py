# DES Key Generation (Simplified)

shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

key = input("Enter 56-bit binary key: ")

left = key[:28]
right = key[28:]

for i in range(16):
    s = shifts[i]

    left = left[s:] + left[:s]
    right = right[s:] + right[:s]

    subkey = left[:24] + right[:24]

    print(f"K{i+1}: {subkey}")
