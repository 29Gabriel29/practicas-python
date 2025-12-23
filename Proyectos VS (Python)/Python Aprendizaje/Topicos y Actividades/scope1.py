"""
c = 10
a = 20

print(globals())

def suma(a, b):
    r = a + b
    print(locals())

print(suma(40, 60))

def func1():
    print(c)

print(func1())


# Utilizo global para poder modificar la variable global "c"

def ac():
    global c
    c += 1
ac()
ac()
print(c)
"""
def func2():
    c = 0
    
    def func3():
        nonlocal c
        c += 1
        a = 0
    func3()
    print(c)

func2()
func2()
func2()
