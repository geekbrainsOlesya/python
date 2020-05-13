class DivisionByNull(Exception):
    def __init__(self,txt):
        self.txt=txt

    @staticmethod
    def divide_by_null():
        try:
            divident=int(input('divident: '))
            divider=int(input('divider: '))
            if divider==0:
                raise DivisionByNull('Деление на ноль!')
        except DivisionByNull as div:
            return div
        else:
            return divident / divider


print(DivisionByNull.divide_by_null())





