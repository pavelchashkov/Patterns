from abc import ABC, abstractmethod


class Receiver:
    '''
    Классы Получателей содержат некую важную бизнес-логику. Они умеют выполнять
    все виды операций, связанных с выполнением запроса. Фактически, любой класс
    может выступать Получателем.
    '''

    def do_something(self, mes: str):
        print(f"Receiver: Working on ({mes})")

    def do_something_else(self, mes: str):
        print(f"Receiver: Also working on ({mes})")


class Command(ABC):
    '''
    Интерфейс Команды объявляет метод для выполнения команд.
    '''

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    '''
    Некоторые команды способны выполнять простые операции самостоятельно.
    '''

    def __init__(self, payload: str):
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: execute -> {self._payload}")


class ComplexCommand(Command):
    '''
    Но есть и команды, которые делегируют более сложные операции другим
    объектам, называемым «получателями».
    '''

    def __init__(self, receiver: Receiver, mes_a: str, mes_b: str):
        '''
        Сложные команды могут принимать один или несколько объектов-получателей
        вместе с любыми данными о контексте через конструктор.
        '''
        self._receiver = receiver
        self._mes_a = mes_a
        self._mes_b = mes_b

    def execute(self) -> None:
        print("ComplexCommand")
        self._receiver.do_something(self._mes_a)
        self._receiver.do_something_else(self._mes_b)


class Invoker:
    '''
    Отправитель связан с одной или несколькими командами. Он отправляет запрос
    команде.
    '''
    _on_start: Command = None
    _on_finish: Command = None

    def set_command_on_start(self, command: Command) -> None:
        self._on_start = command

    def set_command_on_finish(self, command: Command) -> None:
        self._on_finish = command

    def do_something_important(self) -> None:
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    command_a = SimpleCommand('Say hi')
    
    receiver = Receiver()
    command_b = ComplexCommand(receiver, 'Say start', 'Say finish')

    invoker = Invoker()
    invoker.set_command_on_start(command_a)
    invoker.set_command_on_finish(command_b)
    invoker.do_something_important()