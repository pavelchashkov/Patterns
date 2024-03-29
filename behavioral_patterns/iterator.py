from collections.abc import Iterable, Iterator
from typing import List, Any

'''
Для создания итератора в Python есть два абстрактных класса из встроенного
модуля collections - Iterable, Iterator. Нужно реализовать метод __iter__() в
итерируемом объекте (списке), а метод __next__() в итераторе.
'''


class AlphabeticalOrderIterator(Iterator):
    '''
    Конкретные Итераторы реализуют различные алгоритмы обхода. Эти классы
    постоянно хранят текущее положение обхода.
    '''

    '''
    Атрибут _position хранит текущее положение обхода. У итератора может быть
    множество других полей для хранения состояния итерации, особенно когда он
    должен работать с определённым типом коллекции.
    '''
    _position: int = None

    '''
    Aтрибут _reverse указывает направление обхода.
    '''
    _reverse: bool = False

    def __init__(self, collection: 'WordCollection', reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        '''
        Метод __next __() должен вернуть следующий элемент в последовательности.
        При достижении конца коллекции и в последующих вызовах должно вызываться
        исключение StopIteration.
        '''
        try:
            value = self._collection[self._position]
        except IndexError:
            raise StopIteration()
        else:
            self._position += -1 if self._reverse else 1
        return value


class WordCollection(Iterable):
    '''
    Конкретные Коллекции предоставляют один или несколько методов для получения
    новых экземпляров итератора, совместимых с классом коллекции.
    '''

    def __init__(self, words: List[Any] = []):
        self._collection = words

    def add_item(self, item: str) -> None:
        self._collection.append(item)

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, reverse=True)


if __name__ == "__main__":
    '''
    Клиентский код может знать или не знать о Конкретном Итераторе или классах
    Коллекций, в зависимости от уровня косвенности, который вы хотите
    сохранить в своей программе.
    '''
    collection = WordCollection()
    collection.add_item('First')
    collection.add_item('Second')
    collection.add_item('Third')

    print(', '.join(collection))
    print(', '.join(collection.get_reverse_iterator()))