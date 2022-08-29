class ClassMethod:

    cnt = 0     # 클래스 변수

    def __init__(self):
        ClassMethod.cnt += 1

    @classmethod
    def print_count(cls):
        print('{} 명 생성되었습니다.'.format(cls.cnt))

    @classmethod
    def create(cls):
        # 클래스 메서드 내부에서 cls() 로 현재 클래스의 인스턴스 생성
        # cls() = ClassMethod()
        c = cls()
        return c

if __name__ == '__main__':

    #c = ClassMethod()
    print(ClassMethod.create())
    ClassMethod.print_count()
