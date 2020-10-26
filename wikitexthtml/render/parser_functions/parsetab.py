# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = "3.10"

_lr_method = "LALR"

_lr_signature = "leftLOGIC_ORleftLOGIC_ANDleftEQUALNOT_EQUALLTGTLTEGTEnonassocROUNDleftPLUSMINUSleftMULTIPLYDIVIDEMODULOleftPOWERnonassocUNARYnonassocBINARY_UNARYCONST DIVIDE EQUAL FLOAT GT GTE LOGIC_AND LOGIC_OR LPAREN LT LTE MINUS MODULO MULTIPLY NOT_EQUAL NUMBER PLUS POWER ROUND RPAREN UNARYexpr : LPAREN expr RPARENexpr : NUMBERexpr : FLOATexpr : CONSTexpr : PLUS expr %prec BINARY_UNARYexpr : MINUS expr %prec BINARY_UNARYexpr : UNARY exprexpr : expr POWER exprexpr : expr MULTIPLY exprexpr : expr DIVIDE exprexpr : expr MODULO exprexpr : expr PLUS exprexpr : expr MINUS exprexpr : expr ROUND exprexpr : expr EQUAL exprexpr : expr NOT_EQUAL exprexpr : expr LT exprexpr : expr GT exprexpr : expr LTE exprexpr : expr GTE exprexpr : expr LOGIC_AND exprexpr : expr LOGIC_OR expr"

_lr_action_items = {
    "LPAREN": (
        [
            0,
            2,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
        ],
        [
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
        ],
    ),
    "NUMBER": (
        [
            0,
            2,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
        ],
        [
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
        ],
    ),
    "FLOAT": (
        [
            0,
            2,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
        ],
        [
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
        ],
    ),
    "CONST": (
        [
            0,
            2,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
        ],
        [
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
        ],
    ),
    "PLUS": (
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            6,
            13,
            6,
            -2,
            -3,
            -4,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            13,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            13,
            13,
            13,
            13,
            13,
            13,
            13,
            13,
            13,
            -1,
        ],
    ),
    "MINUS": (
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            7,
            14,
            7,
            -2,
            -3,
            -4,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            14,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            14,
            14,
            14,
            14,
            14,
            14,
            14,
            14,
            14,
            -1,
        ],
    ),
    "UNARY": (
        [
            0,
            2,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
        ],
        [
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
            8,
        ],
    ),
    "$end": (
        [
            1,
            3,
            4,
            5,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            0,
            -2,
            -3,
            -4,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            -14,
            -15,
            -16,
            -17,
            -18,
            -19,
            -20,
            -21,
            -22,
            -1,
        ],
    ),
    "POWER": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            9,
            -2,
            -3,
            -4,
            9,
            -5,
            -6,
            -7,
            -8,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            -1,
        ],
    ),
    "MULTIPLY": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            10,
            -2,
            -3,
            -4,
            10,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            -1,
        ],
    ),
    "DIVIDE": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            11,
            -2,
            -3,
            -4,
            11,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            -1,
        ],
    ),
    "MODULO": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            12,
            -2,
            -3,
            -4,
            12,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            12,
            12,
            12,
            12,
            12,
            12,
            12,
            12,
            12,
            12,
            12,
            -1,
        ],
    ),
    "ROUND": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            15,
            -2,
            -3,
            -4,
            15,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            None,
            15,
            15,
            15,
            15,
            15,
            15,
            15,
            15,
            -1,
        ],
    ),
    "EQUAL": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            16,
            -2,
            -3,
            -4,
            16,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            -14,
            -15,
            -16,
            -17,
            -18,
            -19,
            -20,
            16,
            16,
            -1,
        ],
    ),
    "NOT_EQUAL": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            17,
            -2,
            -3,
            -4,
            17,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            -14,
            -15,
            -16,
            -17,
            -18,
            -19,
            -20,
            17,
            17,
            -1,
        ],
    ),
    "LT": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            18,
            -2,
            -3,
            -4,
            18,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            -14,
            -15,
            -16,
            -17,
            -18,
            -19,
            -20,
            18,
            18,
            -1,
        ],
    ),
    "GT": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            19,
            -2,
            -3,
            -4,
            19,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            -14,
            -15,
            -16,
            -17,
            -18,
            -19,
            -20,
            19,
            19,
            -1,
        ],
    ),
    "LTE": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            20,
            -2,
            -3,
            -4,
            20,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            -14,
            -15,
            -16,
            -17,
            -18,
            -19,
            -20,
            20,
            20,
            -1,
        ],
    ),
    "GTE": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            21,
            -2,
            -3,
            -4,
            21,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            -14,
            -15,
            -16,
            -17,
            -18,
            -19,
            -20,
            21,
            21,
            -1,
        ],
    ),
    "LOGIC_AND": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            22,
            -2,
            -3,
            -4,
            22,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            -14,
            -15,
            -16,
            -17,
            -18,
            -19,
            -20,
            -21,
            22,
            -1,
        ],
    ),
    "LOGIC_OR": (
        [
            1,
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            23,
            -2,
            -3,
            -4,
            23,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            -14,
            -15,
            -16,
            -17,
            -18,
            -19,
            -20,
            -21,
            -22,
            -1,
        ],
    ),
    "RPAREN": (
        [
            3,
            4,
            5,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
        ],
        [
            -2,
            -3,
            -4,
            43,
            -5,
            -6,
            -7,
            -8,
            -9,
            -10,
            -11,
            -12,
            -13,
            -14,
            -15,
            -16,
            -17,
            -18,
            -19,
            -20,
            -21,
            -22,
            -1,
        ],
    ),
}

_lr_action = {}
for _k, _v in _lr_action_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_action:
            _lr_action[_x] = {}
        _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {
    "expr": (
        [
            0,
            2,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
        ],
        [
            1,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
        ],
    ),
}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_goto:
            _lr_goto[_x] = {}
        _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
    ("S' -> expr", "S'", 1, None, None, None),
    ("expr -> LPAREN expr RPAREN", "expr", 3, "p_parens", "helpers.py", 120),
    ("expr -> NUMBER", "expr", 1, "p_number", "helpers.py", 125),
    ("expr -> FLOAT", "expr", 1, "p_float", "helpers.py", 130),
    ("expr -> CONST", "expr", 1, "p_const", "helpers.py", 135),
    ("expr -> PLUS expr", "expr", 2, "p_unary_plus", "helpers.py", 140),
    ("expr -> MINUS expr", "expr", 2, "p_unary_minus", "helpers.py", 145),
    ("expr -> UNARY expr", "expr", 2, "p_unary", "helpers.py", 150),
    ("expr -> expr POWER expr", "expr", 3, "p_power", "helpers.py", 155),
    ("expr -> expr MULTIPLY expr", "expr", 3, "p_multiply", "helpers.py", 160),
    ("expr -> expr DIVIDE expr", "expr", 3, "p_divide", "helpers.py", 165),
    ("expr -> expr MODULO expr", "expr", 3, "p_modulo", "helpers.py", 172),
    ("expr -> expr PLUS expr", "expr", 3, "p_plus", "helpers.py", 177),
    ("expr -> expr MINUS expr", "expr", 3, "p_minus", "helpers.py", 182),
    ("expr -> expr ROUND expr", "expr", 3, "p_round", "helpers.py", 187),
    ("expr -> expr EQUAL expr", "expr", 3, "p_equal", "helpers.py", 192),
    ("expr -> expr NOT_EQUAL expr", "expr", 3, "p_not_equal", "helpers.py", 197),
    ("expr -> expr LT expr", "expr", 3, "p_less_than", "helpers.py", 202),
    ("expr -> expr GT expr", "expr", 3, "p_greater_than", "helpers.py", 207),
    ("expr -> expr LTE expr", "expr", 3, "p_less_than_equal", "helpers.py", 212),
    ("expr -> expr GTE expr", "expr", 3, "p_greater_than_equal", "helpers.py", 217),
    ("expr -> expr LOGIC_AND expr", "expr", 3, "p_logic_and", "helpers.py", 222),
    ("expr -> expr LOGIC_OR expr", "expr", 3, "p_logic_or", "helpers.py", 227),
]