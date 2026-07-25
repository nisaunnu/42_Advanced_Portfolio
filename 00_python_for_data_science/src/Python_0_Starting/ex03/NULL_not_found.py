def NULL_not_found(object: any) -> int:

    object_type = type(object)

    if object_type is type(None):
        print(f"Nothing: {object} {object_type}")
        return 0

    if object_type is float and object != object:
        print(f"Cheese: {object} {object_type}")
        return 0

    if object_type is int and object == 0:
        print(f"Zero: {object} {object_type}")
        return 0

    if object_type is str and object == "":
        print(f"Empty: {object_type}")
        return 0

    if object_type is bool and object is False:
        print(f"Fake: {object} {object_type}")
        return 0

    print("Type not Found")
    return 1
