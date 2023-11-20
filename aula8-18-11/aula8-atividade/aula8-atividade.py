'''
Recriar todos estes metodos de array na mão:
'''
# Clear
# Count
# Index
# Copy
# Insert
# Pop (delete last)
# Pop (delete return by index)
# Len

names = ["john", "michael", "carlos"]
names2 = ["john", "michael", "carlos"]

def Clear(array):

    del array [:]
    return array

print(Clear(names))

def Count(array):

    elementsQuantity = 0

    while len(array) > 0:
        
        elementsQuantity += 1

        if elementsQuantity == len(array):
            break

    return elementsQuantity

print(Count(names2))