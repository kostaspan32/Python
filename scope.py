def outer():
    x = 4
    def inner():
        x = 3
        print(f'Inner x = {str(x)}')

    print(f'Outer x = {str(x)}')
    inner()



x = 2
outer()
print(f'Global x = {str(x)}')
