from abc import ABC, abstractmethod


class Product(ABC):
    """
    Интерфейс Продукта объявляет операции, которые должны выполнять все конкретные продукты.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Конкретные Продукты предоставляют различные реализации интерфейса Продукта.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "Result of the ConcreteProduct1"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "Result of the ConcreteProduct2"


class Creator(ABC):
    """
    Класс Создатель объявляет фабричный метод, который должен возвращать объект
    класса Продукт. Подклассы Создателя обычно предоставляют реализацию этого
    метода.
    """

    @abstractmethod
    def factory_method(self):
        """
        Создатель может также обеспечить реализацию фабричного метода по умолчанию.
        """
        pass

    def some_operation(self):
        """
        Несмотря на название, основная обязанность Создателя не заключается в создании продуктов. 
        Обычно он содержит некоторую базовую бизнес-логику, которая основана на объектах Продуктов,
        возвращаемых фабричным методом. Подклассы могут косвенно изменять эту бизнес-логику, 
        переопределяя фабричный метод и возвращая из него другой тип продукта.
        """
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


"""
Конкретные Создатели переопределяют фабричный метод для того, чтобы изменить тип результирующего продукта.
"""


class ConcreteCreator1(Creator):
    def factory_method(self) -> ConcreteProduct1:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> ConcreteProduct2:
        return ConcreteProduct2()


def client_code(creator: Creator) -> None:
    """
    Клиентский код работает с экземпляром конкретного создателя, хотя и через
    его базовый интерфейс. Пока клиент продолжает работать с создателем через
    базовый интерфейс можно передать ему любой подкласс создателя.
    """
    result_operation = creator.some_operation()
    print(
        f"Client: I'm not aware of the creator's class, but it still works\n"
        f"{result_operation}",
        end=''
    )

if __name__ == '__main__':
    print("App: Work with the ConcreteCreator1")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Work with the ConcreteCreator2")
    client_code(ConcreteCreator2())