# what will the following code print?

def f():
    print("Entering f()\nRaising the exception")
    raise Exception("Error Message")
    print("f() complete")

def g():
    print("Entering g()")
    f()
    print("g() complete")

def h():
    print("Entering h()")
    g()
    print("h() complete")

def j():
    print("Entering j()")
    try:
        h()
    except:
        print("Exception caught")
    print("j() complete")

j()