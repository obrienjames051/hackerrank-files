cube = lambda x: x**3 # a labda function is the same as defining a function, but for one/short use
def fibonacci(n): #this just computes the fibonacci sequence to the nth term
    a, b = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n)))) # this was used before list comprehensions was added