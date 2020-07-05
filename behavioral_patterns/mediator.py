from abc import ABC, abstractmethod


class Mediator(ABC):
    '''
    Интерфейс Посредника предоставляет метод, используемый компонентами для
    уведомления посредника о различных событиях. Посредник может реагировать на
    эти события и передавать исполнение другим компонентам.
    '''

    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass


class BaseComponent:
    '''
    Базовый Компонент обеспечивает базовую функциональность хранения экземпляра
    посредника внутри объектов компонентов.
    '''

    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator


'''
Конкретные Компоненты реализуют различную функциональность. Они не зависят от
других компонентов. Они также не зависят от каких-либо конкретных классов
посредников.
'''


class ConcreteComponentA(BaseComponent):
    def do_a(self) -> None:
        print("ConcreteComponentA: do_a")
        self.mediator.notify(self, "a")

    def do_b(self) -> None:
        print("ConcreteComponentA: do_b")
        self.mediator.notify(self, "b")


class ConcreteComponentB(BaseComponent):
    def do_c(self) -> None:
        print("ConcreteComponentB: do_c")
        self.mediator.notify(self, "c")

    def do_d(self) -> None:
        print("ConcreteComponentB: do_d")
        self.mediator.notify(self, "d")


class ConcreteMediator(Mediator):
    def __init__(self, component1: ConcreteComponentA, component2: ConcreteComponentB):
        self._component1 = component1
        self._component2 = component2
        self._component1.mediator = self
        self._component2.mediator = self

    def notify(self, sender: BaseComponent, event: str) -> None:
        if event == 'a':
            print("Mediator reacts on 'a' and triggers following operations:")
            self._component2.do_c()
        if event == 'c':
            print("Mediator reacts on 'c' and triggers following operations:")
            self._component1.do_b()
            self._component2.do_d()
        if event == 'd':
            print("Mediator reacts on 'd' and triggers following operations:")
            self._component1.do_b()


if __name__ == "__main__":
    c1 = ConcreteComponentA()
    c2 = ConcreteComponentB()
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation 'a'")
    c1.do_a()

    print('')

    print("Client triggers operation 'd'")
    c2.do_d()
