from types import ModuleType
import inspect


TUTORIAL_URL = "https://docs.python.org/3/library/typing.html"

HELP_MESSAGE = (
    f"We would like this functions to be typed."
    f"If you are not familiar with adding type hints in "
    f"functions, you can look at functions already typed in"
    f"the codebase. \n"
    f"If you don't want to type your function, you can add it "
    f"to the TODO list of functions to type (also known as exception_list)."
    f"You can also look at this tutorial: "
    f"{TUTORIAL_URL}.\n"
)


def ensure_api_is_typed(
    objects_to_check: list,
    exception_list: list,
    init_only: bool = False,
    additional_message: str = "",
):
    if not init_only:
        raise NotImplementedError(
            "The code to check other methods than __init__ is not implemented yet."
        )
    api = API(objects_to_check, exception_list, additional_message)
    api.check()


class API:
    def __init__(self, objects_to_check, exception_list, additional_message):
        self.objects_to_check = objects_to_check
        self.exception_list = exception_list
        self.additional_message = additional_message

    def check(self):
        for object_ in self.objects_to_check:
            self.check_api_of_object(object_)

    def check_api_of_object(self, object_):
        if isinstance(object_, ModuleType):
            for attribute in get_attributes(object_):
                self.check_api_of_object(attribute)
        if inspect.isclass(object_):
            self.check_function_is_typed(object_.__init__, class_=object_)
        if inspect.isfunction(object_):
            self.check_function_is_typed(object_)

    def check_function_is_typed(self, func, class_=None):
        """ If class_ is not None, func is the __init__ of the class."""
        if class_ is None:
            if func in self.exception_list:
                return
        else:
            if class_ in self.exception_list:
                return
        check_function_is_typed(func, class_, self.additional_message)


def check_function_is_typed(func, class_, additional_message):
    signature = inspect.signature(func)
    for parameter_name, parameter in signature.parameters.items():
        if parameter.annotation != inspect.Signature.empty:
            continue
        if parameter_name in ("args", "kwargs", "self"):
            continue
        if class_ is None:
            function_name = func.__name__
        else:
            function_name = class_.__name__ + ".__init__"
        raise NotTypedError(
            f"The function '{function_name}' has not complete type annotations "
            f"in its signature (it's missing the type hint for '{parameter_name}'). "
            f"{HELP_MESSAGE} \n{additional_message}"
        )

    if class_ is None:
        if signature.return_annotation != inspect.Signature.empty:
            return
        raise NotTypedError(
            f"The function {func.__name__} has no return type. Please add one. \n"
            f"{HELP_MESSAGE} \n{additional_message}"
        )


def get_attributes(module):
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        yield attr


class NotTypedError(Exception):
    pass
