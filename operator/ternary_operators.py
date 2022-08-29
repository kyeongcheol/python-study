'''
@author kcyang
@date 2022.08.29

삼항 연산자 예제
'''

def ternary_oper(flag):

    print("true") if flag else print("false")

if __name__ == '__main__':

    # flag = True
    flag = False
    ternary_oper(flag)