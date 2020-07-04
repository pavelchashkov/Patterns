class SubsystemA:
    '''
    Подсистема может принимать запросы либо от фасада, либо от клиента напрямую.
    В любом случае, для Подсистемы Фасад – это ещё один клиент, и он не является
    частью Подсистемы.
    '''

    def operation_a(self) -> str:
        return "SubsystemA operation_a"

    def operation_b(self) -> str:
        return "SubsystemA operation_b"


class SubsystemB:
    '''
    Некоторые фасады могут работать с разными подсистемами одновременно.
    '''

    def operation_c(self) -> str:
        return "SubsystemB operation_c"

    def operation_d(self) -> str:
        return "SubsystemB operation_d"


class Facade:
    '''
    Класс Фасада предоставляет простой интерфейс для сложной логики одной или
    нескольких подсистем. Фасад делегирует запросы клиентов соответствующим
    объектам внутри подсистемы. Фасад также отвечает за управление их жизненным
    циклом. Все это защищает клиента от нежелательной сложности подсистемы.
    '''

    def __init__(self, subsystem_a: SubsystemA, subsystem_b: SubsystemB):
        self._subsystem_1 = subsystem_a or SubsystemA()
        self._subsystem_2 = subsystem_b or SubsystemB()

    def operation(self) -> str:
        results = [
            "Facade initializes subsystems:",
            self._subsystem_1.operation_a(),
            self._subsystem_1.operation_b(),
            "Facade orders subsystems to perform the action:",
            self._subsystem_2.operation_c(),
            self._subsystem_2.operation_d(),
        ]
        return '\n'.join(results)


def client_code(facade: Facade) -> None:
    '''
    Клиентский код работает со сложными подсистемами через простой интерфейс,
    предоставляемый Фасадом. Когда фасад управляет жизненным циклом подсистемы,
    клиент может даже не знать о существовании подсистемы. Такой подход
    позволяет держать сложность под контролем.
    '''
    print(facade.operation())


if __name__ == '__main__':
    # В клиентском коде могут быть уже созданы некоторые объекты подсистемы. В
    # этом случае может оказаться целесообразным инициализировать Фасад с этими
    # объектами вместо того, чтобы позволить Фасаду создавать новые экземпляры.
    s1 = SubsystemA()
    print(s1.operation_a())
    s2 = SubsystemB()
    print(s2.operation_d())
    
    print('')

    f = Facade(s1, s2)
    client_code(f)
