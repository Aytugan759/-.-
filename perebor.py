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
print('teor toch =', (b-a)/(N+1))