def simp13m(a, h, n, f):
    sum = f(a)
    for i in range(1, n, 2):
            sum += 4 * f(a+i*h) + 2 * f(a+(i+1)*h)
    sum += 4 * f(a+(n-1)*h) + f(a+n*h) 
    return h * sum / 3
