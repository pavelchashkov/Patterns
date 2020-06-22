from abc import ABC, abstractmethod, abstractproperty


class Product():
    """
    Имеет смысл использовать паттерн Строитель только тогда, когда ваши продукты
    достаточно сложны и требуют обширной конфигурации.

    В отличие от других порождающих паттернов, различные конкретные строители
    могут производить несвязанные продукты. Другими словами, результаты
    различных строителей могут не всегда следовать одному и тому же интерфейсу.
    """

    def __init__(self):
        self.parts = []

    def add_part(self, part: any) -> None:
        self.parts.append(part)

    def show_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}")


class Builder(ABC):
    """
    Интерфейс Строителя объявляет создающие методы для различных частей объектов
    Продуктов.
    """
    @abstractproperty
    def product(self):
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder(Builder):
    """
    Классы Конкретного Строителя следуют интерфейсу Строителя и предоставляют
    конкретные реализации шагов построения. Ваша программа может иметь несколько
    вариантов Строителей, реализованных по-разному.
    """

    def __init__(self):
        self._product = None
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
        """
        Конкретные Строители должны предоставить свои собственные методы
        получения результатов. Это связано с тем, что различные типы строителей
        могут создавать совершенно разные продукты с разными интерфейсами.
        Поэтому такие методы не могут быть объявлены в базовом интерфейсе
        Строителя (по крайней мере, в статически типизированном языке
        программирования).

        Как правило, после возвращения конечного результата клиенту, экземпляр
        строителя должен быть готов к началу производства следующего продукта.
        Поэтому обычной практикой является вызов метода сброса в конце тела
        метода getProduct. Однако такое поведение не является обязательным, вы
        можете заставить своих строителей ждать явного запроса на сброс из кода
        клиента, прежде чем избавиться от предыдущего результата.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add_part('PartA')

    def produce_part_b(self) -> None:
        self._product.add_part('PartB')

    def produce_part_c(self) -> None:
        self._product.add_part('PartC')


class Director():
    """
    Директор отвечает только за выполнение шагов построения в определённой
    последовательности. Это полезно при производстве продуктов в определённом
    порядке или особой конфигурации. Строго говоря, класс Директор необязателен,
    так как клиент может напрямую управлять строителями.
    """

    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        Директор работает с любым экземпляром строителя, который передаётся ему
        клиентским кодом. Таким образом, клиентский код может изменить конечный
        тип вновь собираемого продукта.
        """
        self._builder = builder

    """
    Директор может строить несколько вариаций продукта, используя одинаковые
    шаги построения.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == '__main__':
    builder = ConcreteBuilder()
    director = Director()

    director.builder = builder
    
    print("Minimal product configuration:")
    director.build_minimal_viable_product()
    builder.product.show_parts()

    print("")

    print("Full product configuration:")
    director.build_full_featured_product()
    builder.product.show_parts()

    print("")

    # Паттерн Строитель можно использовать без класса Директор.
    print("Custom product configuration:")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.show_parts()