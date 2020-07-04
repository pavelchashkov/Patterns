from abc import ABC, abstractmethod
from typing import Optional, Any

class Handler(ABC):
    '''
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    '''

    @abstractmethod
    def set_next(self, handler: 'Handler') -> 'Handler':
        pass

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler is not None:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'banana':
            return f"Monkey: I`m eating {request}"
        return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'nut':
            return f"Squirrel: I`m eating {request}"
        return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == 'meat':
            return f"Dog: I`m eating {request}"
        return super().handle(request)


def client_code(handler: Handler):
    '''
    Обычно клиентский код приспособлен для работы с единственным обработчиком. В
    большинстве случаев клиенту даже неизвестно, что этот обработчик является
    частью цепочки.
    '''

    for food in ('nut', 'banana', 'meat', 'coffe'):
        print(f"Client: Who wants a {food}?")
        result = handler.handle(food)
        if result is not None:
            print(f"  {result}")
        else:
            print(f"  Food {food} was left untouched.")

if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # Клиент должен иметь возможность отправлять запрос любому обработчику, а не
    # только первому в цепочке.
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)