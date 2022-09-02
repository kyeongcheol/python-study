def __except_ex():

    try:
        array = [1,2,3,4,5]
        # print(array[8])     # 예외 발생
        print(array[1])
    except:
        print("error !! index out of bounds")
        print("program still alive")

    else:
        print("not error !!")

    print("program end")
if __name__=='__main__':
    __except_ex()