class Company:
    """
    Class Company that contain name, industry, employees, headquarter, product and services.
    """

    def __init__(self, name: str, industry: set, employees: int, headquarter: str, product: set, service: set):
        self.__name = name
        self.__industry = industry
        self.__employees = employees
        self.__headquarter = headquarter
        self.__product = product
        self.__service = service

    @property
    def name(self):
        """
        A method to get the company's name
        """
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """
        A method to change the company's name
        """
        if len(new_name):
            self.__name = new_name
        else:
            print("Your name is empty, can not update")

    @property
    def industry(self):
        """
        A method to get the company's industry
        """
        return self.__industry

    @industry.setter
    def industry(self, new_industry: str):
        """
        A method to update the company's industry
        """
        if new_industry in self.__industry:
            print(f"{new_industry} can not be added")
        elif not len(new_industry):
            print("Your new industry is empty, can not update it")
        else:
            self.industry.add(new_industry)

    @property
    def employees(self):
        """
        A method to get the company's number of employees
        """
        return self.__employees

    @employees.setter
    def employees(self, new_employees_number: int):
        """
        A method to update company's employees number
        """
        if new_employees_number > -1:
            self.__employees = new_employees_number
        else:
            print("The number of employees can not be negative")

    def add_employee(self, new_employee_number: int = 1):
        """
        A method to add the number of employees to the existing one
        """
        if new_employee_number > -1:
            self.__employees += new_employee_number
        else:
            print("The number of employees can not be negative")

    @property
    def headquarter(self):
        """
        A method to get the headquarters
        """
        return self.__headquarter

    @headquarter.setter
    def headquarter(self, new_headquarter: str):
        """
        A method to update the headquarters location
        """
        if len(new_headquarter):
            self.__headquarter = new_headquarter
        else:
            print("Your headquarter name is empty, can not update")

    @property
    def product(self):
        """
        A method to get the company's product
        """
        return self.__product

    @product.setter
    def product(self, new_product: str):
        """
        A method to update the company's product
        """
        if new_product in self.__product:
            print(f"{new_product} can not be added")
        elif not len(new_product):
            print("Your new product is empty can not update it")
        else:
            self.__product.add(new_product)

    def remove_product(self, product_to_remove: str):
        """
        A method to remove the company's product
        """
        if product_to_remove in self.__product:
            self.__product.remove(product_to_remove)
        else:
            print(f"{product_to_remove} can not be removed")

    @property
    def service(self):
        """
        A method to get the company's service
        """
        return self.__service

    @service.setter
    def service(self, new_service: str):
        """
        A method to update the company's service
        """
        if new_service in self.__service:
            print(f"{new_service} can not be added")
        elif not len(new_service):
            print("Your new service is empty can not update it ")
        else:
            self.__service.add(new_service)

    def remove_service(self, service_to_remove: str):
        """
        A method to remove the company's service
        """
        if service_to_remove in self.__service:
            self.__service.remove(service_to_remove)
        else:
            print(f"{service_to_remove} can not be removed")


if __name__ == '__main__':
    my_company = Company("Apple", {"Consumer electronics"}, 153000, "California",
                         {"IPhone", "AirPods", "IPad"}, {"AppStore", "Apple Music"})
    my_company.name = "Apple Computers Inc."
    print(my_company.name)
    my_company.industry = "Consumer electronics"
    my_company.industry = "Software service"
    print(my_company.industry)
    my_company.employees = 154000
    print(my_company.employees)
    my_company.add_employee(10)
    my_company.add_employee(-1000)
    print(my_company.employees)
    my_company.headquarter = "1 Apple Park Way, Cupertino, California, USA"
    print(my_company.headquarter)
    my_company.product = "IPhone"
    my_company.remove_product("TEST")
    my_company.product = "Macintosh"
    print(my_company.product)
    my_company.service = "Apple Music"
    my_company.remove_service("Apple Music")
    print(my_company.service)
    my_company.service = "Apple TV+"
    print(my_company.service)
    print("+++++++++")
    my_company.name = ""
    my_company.industry = ""
    my_company.headquarter = ""
    my_company.product = ""
    my_company.service = ""
