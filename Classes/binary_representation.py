from stack import Stack
modulos = Stack()
def get_binary_representation(number):
    if number == 0:
        return None
    x = number % 2
    modulos.push(x)
    get_binary_representation(number//2)


def print_binary_representation(number):
    binary_representation = []
    for _ in range(len(modulos.array)):
        binary_representation.append(modulos.pop())
    return binary_representation


get_binary_representation(135)
print(print_binary_representation(135))



