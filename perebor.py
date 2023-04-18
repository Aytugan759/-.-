def f(x):
    return 5*x**2-5+31*abs(x-5)
N = 23
x = [0]*(N+2)
a = -1
b = 6
x[0] = a
x[N+1] = b
for i in range(1, N+1):
    x[i] = a+(b-a)*i/(N+1)
print(x)
f_min = f(x[1])
j = 1
for i in range(2, N+1):
    if f(x[i]) < f_min:
        f_min = f(x[i])
        j = i
print(j, f(x[j]), x[j])
x_ = (x[j-1]+x[j+1])/2
print('x* = ',x_)
print('fact toch = ', abs(x_-3.1))

def dihot():
    def f(x):
        return 5 * x ** 2 - 5 + 31 * abs(x - 5)

    a = -1
    b = 6
    N = 23
    xa = a
    xb = b
    k = N // 2
    d = (b - a) / (2 ** (k))

    for i in range(k):
        x1 = (a + xb) / 2 - d
        x2 = (xa + b) / 2 + d

        if f(x1) <= f(x2):
            xb = x2
        else:
            xa = x1
    x_ = (xa + xb) / 2
    l = (b - a) / (2 ** (k)) + d * (2 ** k - 1) / (2 ** (k - 1))
    print('x*=', x_, 'дельта = ', d, ' теоретическая погрешность = ', l / 2, " фактическая погрешность = ",
          abs(x_ - 3.1))