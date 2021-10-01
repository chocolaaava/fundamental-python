# nested while 

a = 1
while a < 5:
    b = 0
    while b < a:
        print("*", end="")
        b = b+1
    print()
    a = a+1     


"""
penjelasan nested while:
apakah 1 < 5 ? True
apakah 0 < 1 ? True 
"""

# nested for in

for a in range(1,5):
    for b in range(1,5):
        c = a*b
        print(c, end=" ")
    print()