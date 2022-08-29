'''
@author kcyang
@date 2022.08.29

public 접근 제한자
'''
class Public:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print("name {}".format(self.name))

    def get_age(self):
        print("age {}".format(self.age))

if __name__ == '__main__':
    p = Public('양경철', '33')
    p.get_name()
    p.get_age()