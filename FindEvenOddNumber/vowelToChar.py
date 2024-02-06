str = input("Enter any string to convert vowels to *")
vowels = 'AEIOUaeiou'
chr = "*"

for i in vowels:
    str= str.replace(i,chr)
print(str)


# vowelsList = ['a','e','i','o','u']
# string_value = input("Enter any string to convert ")
# new_string = ''.join(['*' if letter in vowelsList else letter for letter in string_value])