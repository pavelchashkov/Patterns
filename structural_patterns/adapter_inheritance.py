class Target:
    """
    Целевой класс объявляет интерфейс, с которым может работать клиентский код.
    """

    def request(self) -> str:
        return "Target: default target behaviour"


class Adaptee:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
    некоторой доработке, прежде чем клиентский код сможет его использовать.
    """

    def specific_quest(self) -> str:
        return "eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом благодаря множественному наследованию.
    """

    def request(self) -> str:
        return f"Adapter (TRANSLATE): {self.specific_quest()[::-1]}"


def client_code(target: Target) -> None:
    """
    Клиентский код поддерживает все классы, использующие интерфейс Target.
    """
    print(target.request())


if __name__ == '__main__':
    target = Target()
    client_code(target)
    adapter = Adapter()
    client_code(adapter)
