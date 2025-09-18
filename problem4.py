def palindrome(pal):
    return pal == pal[::-1]

def toBinary(num):
    if num.isDigit():
        return bin(int(num))[2:]
    return None

value = input("Enter a value: ")
pal_num = palindrome(value)
print("Input is a palindrome " + pal_num)

bina = toBinary(value)

if bina:
    print("Binary equivalent: " + bina)
    bina_pal = palindrome(bina)
    print("Binary is a palindrome " + bina_pal)
else:
    print("No binary input")