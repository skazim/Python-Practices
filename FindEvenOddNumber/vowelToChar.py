str = input("Enter any string to convert vowels to *")
vowels = 'AEIOUaeiou'
chr = "*"

for i in vowels:
    str = str.replace(i,chr)


print(str)