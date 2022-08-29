'''
@author kcyang
@date 2022.08.29

protected 접근 제한자
'''
class Protected:

    def __init__(self, name, age):
        # protected variable
        self._name = name
        self._age = age

    # protected method
    def _get_name(self):
        print("name {}".format(self._name))

    def _get_age(self):
        print("age {}".format(self._age))

class SubClass(Protected):

    def __init__(self, name, age):
         Protected.__init__(self, name, age)

    def details(self):
        self._get_name()
        self._get_age()

if __name__ == '__main__':
    s = SubClass('양경철', '33')
    s.details()