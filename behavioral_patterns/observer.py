from abc import ABC, abstractmethod
from typing import List
from random import randrange


class Observer(ABC):
    """
    Интерфейс Наблюдателя объявляет метод уведомления, который издатели
    используют для оповещения своих подписчиков.
    """
    @abstractmethod
    def update(self, subject: 'Subject') -> None:
        pass


class Subject(ABC):
    """
    Интферфейс издателя объявляет набор методов для управлениями подписчиками.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    """
    Издатель владеет некоторым важным состоянием и оповещает наблюдателей о его
    изменениях.
    """

    state: int = None
    """
    Для удобства в этой переменной хранится состояние Издателя, необходимое всем
    подписчикам.
    """

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            print(f"Attache observer {observer}")
            self._observers.append(observer)
        else:
            print(f"{observer} are already in list subscribsers")

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Detache observer {observer}")
        else:
            print(f"{observer} are not in list subscribers")

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_busines_logic(self):
        print("Some busines logic of ConcreteSubject")
        self.state = randrange(0, 10)
        self.notify()


"""
Конкретные Наблюдатели реагируют на обновления, выпущенные Издателем, к которому
они прикреплены.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject):
        print(f"ConcreteObserverA get notify with subject state {subject.state}")
        if subject.state > 5:
            print("AAA action > 5")
        else:
            print("AAA another action")

    def __str__(self) -> str:
        return 'ConcreteObserverA'

class ConcreteObserverB(Observer):
    def update(self, subject: Subject):
        print(f"ConcreteObserverB get notify with subject state {subject.state}")
        if subject.state < 5:
            print("BBB action < 5")
        else:
            print("BBB another action")

    def __str__(self) -> str:
        return 'ConcreteObserverB'

if __name__ == "__main__":
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()
    print('')
    subject.attach(observer_a)
    subject.some_busines_logic()
    print('')
    subject.attach(observer_a)
    subject.attach(observer_b)
    subject.some_busines_logic()
    print('')
    subject.attach(observer_b)
    subject.detach(observer_a)
    subject.some_busines_logic()
    print('')
    subject.detach(observer_a)
    subject.detach(observer_b)
    subject.some_busines_logic()
    print('')
    subject.detach(observer_b)
    subject.some_busines_logic()