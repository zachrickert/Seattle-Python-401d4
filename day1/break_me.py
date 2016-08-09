import random


def name_error():
    print(undefined_var)


def type_error():
    integer = 42
    print(integer[0])


def attribute_error():
    integer = 43
    integer.append(3)


def error_selector():
    error_list = [name_error, type_error, attribute_error]
    error_list[random.randint(0, 2)]()


def call_function():
    # import pdb; pdb.set_trace()
    error_selector()

call_function()

# def sytax_error():
#     this is a systax error function.
