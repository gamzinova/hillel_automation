class Employee:
    """
    Class Employee that contain employee's name, last lame, position, salary and years of work.
    """

    def __init__(self, name: str, last_name: str, position: str, salary: float):
        self.__name = name
        self.__last_name = last_name
        self.__position = position
        self.__salary = salary

    @property
    def name(self):
        """
        A method to get the employee's name
        """
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """
        A method to change the employee's name
        """
        if len(new_name):
            self.__name = new_name
        else:
            print("Your name is empty, can not update")

    @property
    def last_name(self):
        """
        A method to get the employee's last name
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, new_last_name: str):
        """
        A method to change the employee's last name
        """
        if len(new_last_name):
            self.__last_name = new_last_name
        else:
            print("Your last name is empty, can not update")

    @property
    def position(self):
        """
        A method to get the employee's position
        """
        return self.__position

    @position.setter
    def position(self, new_position: str):
        """
        A method to change the employee's position
        """
        if len(new_position):
            self.__position = new_position
        else:
            print("Your position is empty, can not update")

    def position_promotion(self, position_promotion: str):
        """
        A method to update the employee's position
        """
        if len(position_promotion):
            self.__position = "".join([position_promotion, " ", self.__position])
        else:
            print("Your position promotion is empty, can not update")

    @property
    def salary(self):
        """
        A method to get the employee's salary
        """
        return self.__salary

    @salary.setter
    def salary(self, new_salary: float):
        """
        A method to change the employee's salary
        """
        if new_salary > self.__salary:
            self.__salary = new_salary
        else:
            print("Unable to set new salary that is lower than the current one")

    @staticmethod
    def calculate_bonus(years_of_work: int):
        """
        A method to calculate the bonus
        """
        if years_of_work < 5:
            return years_of_work * 100
        else:
            return years_of_work * 150

    def salary_raise(self, salary_raise: float):
        """
        A method to raise the employee's salary
        """
        if salary_raise > 1:
            self.__salary = self.__salary + salary_raise
        else:
            print("Unable to add this sum to the salary")


if __name__ == '__main__':
    employee_1 = Employee("Ross", "Geller", "QA", 10000)
    employee_1.position_promotion("Team Lead")
    print(employee_1.position)
    bonus = Employee.calculate_bonus(10)
    print(employee_1.salary + bonus)
    employee_1.salary_raise(-550)
    employee_1.salary_raise(550)
    print(employee_1.salary)
    employee_1.salary = 9000
    print(employee_1.salary)
    employee_1.name = ""
    employee_1.last_name = ""
    employee_1.position = ""
    employee_1.position_promotion("")
