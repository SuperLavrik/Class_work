
class A:
    def __init__(self):
        self.attr1 =  "attrA"
    def foo(self):
        print ("i'm foo (A)")
    pass

class B(A):

    def __init__(self):
        super().__init__()
        self.attr2 = "attrB"
    def foo(self):
        print ("i'm foo (B)")

class C(A):

    def __init__(self):
        super().__init__()
        self.attr3 = "attrC"
    def foo(self):
        print ("i'm foo (C)")

class D(B,C):

    def __init__(self):
        super().__init__()
        self.attr4 = "attrD"
    def foo(self):
        print ("i'm foo (D)")


b = B()
b.foo()
print(b.attr1)
print(b.attr2)

print (D.mro())

