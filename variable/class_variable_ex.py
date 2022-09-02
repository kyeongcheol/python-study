'''
@author kcyang
@date 2022.08.29

class 변수 예제
'''

class ClassVariable:

    text = "kcyang"     # 클래스 변수 선언

    def __init__(self):
        ClassVariable.text = "kcyang dev"


if __name__ == '__main__':

    print("class variable {} ".format(ClassVariable.text))  # 클래스 변수 접근
    v = ClassVariable()     # 인스턴스 생성
    print("class variable {} ".format(v.text))      # 클래스 변수 접근
