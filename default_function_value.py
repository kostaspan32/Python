def print_name(name, surname, second_name='', second_surname='', details=False):
    if second_name != '':
        second_name = '-' + second_name
    if details:
        print(f"First name: {name}{second_name}")

        print(f'Surname: {surname} {second_surname}')

    else:
        print(f"{name}{second_name} {surname} {second_surname}")


print_name('Konstantinos', 'Panagiotopoulos','Marios', 'Aggelakas', details = True)

for i in range(10):
    print('=', end='')

def f(par1, par2, par3=0, par4=0):
    print(f"\n{par1} {par2} {par3} {par4}")

f(1, 2)
f(1, 2, 3, 4)
f(1, 2, 3)