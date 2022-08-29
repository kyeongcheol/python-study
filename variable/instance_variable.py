'''
@author kcyang
@date 2022.08.29

instance 변수 예제
'''
class InstacneVariable :

    ## 인스턴스 메서드
    def __init__(self, text):
        self.text = text    ## 인스턴스 변수 선언

    def print_instace(self):
        print("instance variable {}".format(self.text))

if __name__ == '__main__':
    a = InstacneVariable("===kcyang===")
    b = InstacneVariable("===kcyang abc===")
    a.print_instace()
    b.print_instace()

