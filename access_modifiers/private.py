'''
@author kcyang
@date 2022.08.29

private 접근 제한자
'''
class Private:

    def __init__(self, age=1):
        self.__age = age    # private variable
    
    # private method
    def __get_age(self):
        return self.__age

    def __get_public_age__(self):       # __ 로 시작하는 method 끝에 __ 를 추가하면 public 과 동일하게 작동
        return self.__get_age()


if __name__ == '__main__':
    p = Private()
    p.__age = 33        ## Private Member 이므로 반영 되지 않음

    # print(p.__get_age)      ## Private Method 접근 불가
    print(p.__get_public_age__())
    