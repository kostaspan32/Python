x = float(input('Posa lefta exete? : '))

maximum = x

y = float(input('How much money do you have? : '))

if y > x:
    maximum = y

z = float(input('Wie viel Geld haβt du? : '))

if z > maximum:
    maximum = z

print(maximum)
