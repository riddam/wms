from ..containers import container
import inspect

containers_types = []


def search_containers():
    """
    search available container types inherited from container class
    :return:
    """
    parent = container.Container
    for i in dir(container):
        child = getattr(container, i)
        if child is parent:
            continue
        if inspect.isclass(child) and issubclass(child, parent):
            containers_types.append(child)


search_containers()
