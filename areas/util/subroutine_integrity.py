from areas.exception import ToolFileError
from areas.config.architectures import ARCHITECTURES

AVAILABLE_TYPES = [
    "int",
    "long",
    "float",
    "double",
    "char",
    "chari",
    # arrays
    "char*",
    "string",
    "array int",
    "array long",
    "array float",
    "array double",
    "array char",
    "array chari"
]

PYTHON_COMPATIBLE_TYPES = {
    "int": [int],
    "long": [int],
    "float": [int, float],
    "double": [int, float],
    "char": [str],
    "chari": [int],
    # arrays
    "char*": [str],
    "string": [str],
    "array int": [list],
    "array long": [list],
    "array float": [list],
    "array double": [list],
    "array char": [list],
    "array chari": [list]
}


def __parse_subroutine_definition(subroutine):
    if "params" not in subroutine:
        raise ToolFileError("No parameters in subroutine definition")

    if "architecture" in subroutine:
        architecture = subroutine["architecture"].lower()

        if architecture not in ARCHITECTURES:
            raise ToolFileError(
                f"Architecture {architecture} is not supported")

    params = subroutine["params"]
    returns = subroutine["return"] or []

    for param in params:
        if param not in AVAILABLE_TYPES:
            raise ToolFileError(f"Parameter type {param} not supported")

    for return_type in returns:
        if return_type not in AVAILABLE_TYPES:
            raise ToolFileError(f"Return type {return_type} not supported")

    return params, returns


def __parse_test(inputs, outputs, params, returns):
    if len(inputs) != len(params):
        raise ToolFileError(
            "Number of inputs does not match number of parameters")

    if len(outputs) != len(returns):
        raise ToolFileError(
            "Number of outputs does not match number of returns")

    for param, input in zip(params, inputs):
        expected_types = PYTHON_COMPATIBLE_TYPES[param]

        matches = [isinstance(input, expected_type)
                   for expected_type in expected_types]

        if not any(matches):
            raise ToolFileError(
                f"Input {input} ({type(output)}) is not of type {expected_types}")

    for return_type, output in zip(returns, outputs):
        expected_types = PYTHON_COMPATIBLE_TYPES[return_type]

        matches = [isinstance(output, expected_type)
                   for expected_type in expected_types]

        if not any(matches):
            raise ToolFileError(
                f"Output {output} ({type(output)}) is not of type {expected_types}")


def __parse_subroutine_tests(tests, params, returns):
    for test in tests:
        if "inputs" not in test:
            raise ToolFileError("No inputs in test suite")

        if "outputs" not in test:
            raise ToolFileError("No outputs in test suite")

        inputs = test["inputs"]
        outputs = test["outputs"]

        __parse_test(inputs, outputs, params, returns)


def parse_subroutine(subroutine, tests):
    params, returns = __parse_subroutine_definition(subroutine)

    __parse_subroutine_tests(tests, params, returns)
