class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print('Доход сотрудника: ' + str(self._income['wage'] + self._income['bonus'])+'$')


a = Position('Mark', 'Ivanov', 'HR', 3400, 600)
a.get_full_name()
a.get_total_income()
b=Position('Sam','Lui', 'SMM', 3800, 400)
b.get_full_name()
b.get_total_income()
