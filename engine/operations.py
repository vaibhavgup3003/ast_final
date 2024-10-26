def ast_and(op1: bool, op2: bool) -> bool:
    return op1 and op2


def ast_or(op1: bool, op2: bool) -> bool:
    return op1 or op2


def ast_gt(op1: int | float, op2: int | float) -> bool:
    return op1 > op2


def ast_gte(op1: int | float, op2: int | float) -> bool:
    return op1 >= op2


def ast_lt(op1: int | float, op2: int | float) -> bool:
    return op1 < op2


def ast_lte(op1: int | float, op2: int | float) -> bool:
    return op1 <= op2


def ast_eq(op1: int | float | str, op2: int | float | str) -> bool:
    return op1 == op2

func_map: dict = {
    "AND": ast_and,
    "OR": ast_or,
    ">": ast_gt,
    ">=": ast_gte,
    "<": ast_lt,
    "<=": ast_lte,
    "=": ast_eq,
}
