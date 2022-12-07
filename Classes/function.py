class Polynomial:
    def __init__(self, *coeff):
        self.coeff = [c for c in coeff]

    def __str__(self):
        st = []
        for i in range(len(self.coeff)):
            st.append(f'{self.coeff[i]}*x^{len(self.coeff) - 1 - i}')
        return " + ".join(st)

    def __call__(self, x):
        res = 0
        for i in range(len(self.coeff)):
            res += self.coeff[i] * x ** (len(self.coeff) - 1 - i)
        return res


p = Polynomial(5, 1, 2)
print(p)
print(p(2))

