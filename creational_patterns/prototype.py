import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self) -> 'SomeComponent':
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo={}) -> 'SomeComponent':
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)
        return new

    def __str__(self):
        return f"{self.some_int}, {self.some_list_of_objects}, {self.some_circular_ref}"


if __name__ == '__main__':
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(56, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    copy_component = copy.copy(component)
    copy_component.some_list_of_objects.append("another object")
    print(f"component     : {component}")
    print(f"copy_component: {copy_component}")
    component.some_list_of_objects[1].add(4)
    print(f"component     : {component}")
    print(f"copy_component: {copy_component}")

    print("")

    print(
        f"id(copy_component.some_circular_ref.parent): "
        f"{id(copy_component.some_circular_ref.parent)}"
    )
    print(
        f"id(copy_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(copy_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )

    print("")

    deepcopy_component = copy.deepcopy(component)
    deepcopy_component.some_list_of_objects.append("another object")
    print(f"component         : {component}")
    print(f"deepcopy_component: {deepcopy_component}")
    component.some_list_of_objects[1].add(10)
    print(f"component         : {component}")
    print(f"deepcopy_component: {deepcopy_component}")

    print("")

    print(
        f"id(deepcopy_component.some_circular_ref.parent): "
        f"{id(deepcopy_component.some_circular_ref.parent)}"
    )
    print(
        f"id(deepcopy_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deepcopy_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )