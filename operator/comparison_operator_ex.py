'''
@author kcyang
@date 2022.08.29

비교 연산자 예제
'''

def equal_comparison_oper():

    a = 10000
    b = 10000

    if a == b:
        print("equal ==")
    else:
        print("not equal")

def identity_comparison_oper():

    a = 10000
    b = 10000

    if a is b:
        print("object a {}".format(id(a)))
        print("object b {}".format(id(b)))
        print("object equal")
    else:
        print("object a {}".format(id(a)))
        print("object b {}".format(id(b)))
        print("not object equal")


if __name__ == '__main__':
    equal_comparison_oper()
    identity_comparison_oper()