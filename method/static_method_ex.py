class StaticMethod:

    cnt = 10  # class 변수

    def __init__(self, a):
        self.a = a

    @staticmethod
    def add(a):
        print(a + StaticMethod.cnt)

if __name__ == '__main__':
    StaticMethod.add(1)