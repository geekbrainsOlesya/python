class NumbersOnly(Exception):
    def __init__(self,txt):
        self.txt=txt

    @staticmethod
    def nums_or_not():

        ls=[]

        while True:
            try:
                num=input('Введите число или Enter для выхода: ')
                if num=='':
                    return ' '.join(ls)
                if not num.isdigit():
                    raise NumbersOnly('Вы ввели не число!')
            except NumbersOnly as nums:
                print(nums)
            else:
                ls.append(num)


print(NumbersOnly.nums_or_not())
