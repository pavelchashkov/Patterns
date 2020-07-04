from typing import Dict, List
import hashlib


class Flyweight:
    '''
    Легковес хранит общую часть состояния (также называемую внутренним
    состоянием), которая принадлежит нескольким реальным бизнес-объектам.
    Легковес принимает оставшуюся часть состояния (внешнее состояние, уникальное
    для каждого объекта) через его параметры метода.
    '''

    def __init__(self, shared_state: List):
        self._shared_state = shared_state

    def operation(self, unique_state: List) -> str:
        pr_unique_state = ', '.join(unique_state)
        return f"Flyweight: [{self}] with [{pr_unique_state}]"

    def __str__(self) -> str:
        return ', '.join(self._shared_state)


class FlyweightFactory:
    '''
    Фабрика Легковесов создает объекты-Легковесы и управляет ими. Она
    обеспечивает правильное разделение легковесов. Когда клиент запрашивает
    легковес, фабрика либо возвращает существующий экземпляр, либо создает
    новый, если он ещё не существует.
    '''
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, flyweight_states: List):
        for state in flyweight_states:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: List) -> str:
        '''
        Возвращает хеш строки Легковеса для данного состояния.
        '''
        hash_object = hashlib.md5("_".join(sorted(state)).encode())
        return hash_object.hexdigest()

    def get_flyweight(self, shared_state: List) -> Flyweight:
        '''
        Возвращает существующий Легковес с заданным состоянием или создает
        новый.
        '''
        key = self.get_key(shared_state)
        if key not in self._flyweights:
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")
        return self._flyweights[key]

    def print_list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        for key, value in self._flyweights.items():
            print(f"   {key} - ({value})")


def add_car_to_police_database(
    factory: FlyweightFactory,
    num: str,
    owner: str,
    brand: str,
    model: str,
    color: str
) -> None:
    print("\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    flyweight.operation([num, owner])


if __name__ == '__main__':
    '''
    Клиентский код обычно создает кучу предварительно заполненных легковесов на
    этапе инициализации приложения.
    '''
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "white"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "black"],
    ])
    factory.print_list_flyweights()
    add_car_to_police_database(
        factory, 'X564FG', 'James Bond', 'BMW', 'X6', 'black')
    factory.print_list_flyweights()
    add_car_to_police_database(
        factory, 'E937DW', 'Ivan Petrov', 'Toyota', 'Camry', 'grey')
    factory.print_list_flyweights()
