class InstanceMethod:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 인스턴스 메서드
    def print_info(self):
        print(self.name, ',', self.age)

    # 인스턴스 메서드
    def call_print_info(self):
        self.print_info()

if __name__ == '__main__':
    instance_method = InstanceMethod('양경철', '33')
    instance_method.print_info()
    instance_method.call_print_info()