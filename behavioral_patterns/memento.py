from random import sample
from string import ascii_letters, digits
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List


class Memento(ABC):
    '''
    Интерфейс Снимка предоставляет способ извлечения метаданных снимка, таких
    как дата создания или название. Однако он не раскрывает состояние Создателя.
    '''
    @abstractmethod
    def get_state(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str):
        self._state = state
        self._date = str(datetime.now())

    def get_name(self) -> str:
        return f"{self._date} - {self._state[:19]}"

    def get_state(self) -> str:
        return self._state

    def get_date(self) -> str:
        return self._date


class Originator:
    '''
    Создатель содержит некоторое важное состояние, которое может со временем
    меняться. Он также объявляет метод сохранения состояния внутри снимка и
    метод восстановления состояния из него.
    '''

    def __init__(self, state: str):
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        '''
        Бизнес-логика Создателя может повлиять на его внутреннее состояние.
        Поэтому клиент должен выполнить резервное копирование состояния с
        помощью метода save перед запуском методов бизнес-логики.
        '''
        self._state = self._generate_random_string()
        print(f"I`m doing something important ({self._state})")

    def _generate_random_string(self, length: int = 10) -> str:
        return ''.join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento, err: bool) -> None:
        """
        Восстанавливает состояние Создателя из объекта снимка.
        """
        if err:
            raise Exception('TEST')
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Caretaker:
    '''
    Опекун не зависит от класса Конкретного Снимка. Таким образом, он не имеет
    доступа к состоянию создателя, хранящемуся внутри снимка. Он работает со
    всеми снимками через базовый интерфейс Снимка.
    '''

    def __init__(self, originator: Originator):
        self._originator = originator
        self._mementos: List[Memento] = []

    def create_backup(self) -> None:
        self._mementos.append(self._originator.save())

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())

    def undo(self, err: bool = False) -> None:
        if not len(self._mementos):
            print("Empty history")
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento, err)
        except:
            print("I can`t restore state, try restore previous state")
            self.undo()


if __name__ == "__main__":
    originator = Originator("Super-puper")
    caretaker = Caretaker(originator)

    caretaker.create_backup()
    originator.do_something()

    caretaker.create_backup()
    originator.do_something()

    print('')
    caretaker.show_history()

    print('')
    print("Client: Now, let's rollback!")
    caretaker.undo(err=True)

    print("Client: Once more!")
    caretaker.undo()
    