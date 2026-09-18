def filter_objects(objects, predicate):
    return list(filter(predicate, objects))


def transform_objects(objects, operation):
    return list(map(operation, objects))


def sort_objects(objects, key_function):
    return sorted(objects, key=key_function)


def average(values):
    if not values:
        return 0
    return sum(values) / len(values)