import re

print("=" * 50)
print("      MINI COMPILER - IF ELSE")
print("=" * 50)

source = input("Masukkan kode:\n")

# =========================
# LEXICAL ANALYSIS
# =========================

token_specification = [

    ('IF', r'if'),
    ('ELSE', r'else'),

    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),

    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),

    ('ASSIGN', r'='),
    ('OPERATOR', r'>|<|==|!=|>=|<='),

    ('SEMICOLON', r';'),

    ('IDENTIFIER', r'[A-Za-z_]\w*'),

    ('SKIP', r'[ \t\n]+'),

    ('MISMATCH', r'.')

]

tok_regex = '|'.join(
    '(?P<%s>%s)' % pair
    for pair in token_specification
)

print("\n===== LEXICAL ANALYSIS =====")

tokens = []

for mo in re.finditer(tok_regex, source):

    kind = mo.lastgroup
    value = mo.group()

    if kind == "SKIP":
        continue

    elif kind == "MISMATCH":
        print("Karakter tidak dikenali:", value)

    else:

        tokens.append((kind, value))
        print(f"{kind:12} : {value}")

# =========================
# SYNTAX ANALYSIS (AST)
# =========================

print("\n===== SYNTAX ANALYSIS =====")

try:
    # Mengambil bagian kondisi
    condition = []

    i = 0

    while tokens[i][0] != "LPAREN":
        i += 1

    i += 1

    while tokens[i][0] != "RPAREN":
        condition.append(tokens[i][1])
        i += 1

    # Mengambil statement THEN
    then_stmt = []

    while tokens[i][0] != "LBRACE":
        i += 1

    i += 1

    while tokens[i][0] != "RBRACE":
        then_stmt.append(tokens[i][1])
        i += 1

    # Mengambil statement ELSE
    else_stmt = []

    while tokens[i][0] != "LBRACE":
        i += 1

    i += 1

    while tokens[i][0] != "RBRACE":
        else_stmt.append(tokens[i][1])
        i += 1

    print("IF")
    print("├── Condition")

    print("│   ├──", condition[0])
    print("│   ├──", condition[1])
    print("│   └──", condition[2])

    print("├── THEN")
    print("│   └──", " ".join(then_stmt))

    print("└── ELSE")
    print("    └──", " ".join(else_stmt))

except Exception as e:
    print("Syntax Error!")
    print(e)

# =========================
# SEMANTIC ANALYSIS
# =========================

print("\n===== SEMANTIC ANALYSIS =====")

# Variabel yang dianggap sudah dideklarasikan
declared_variables = {"a", "b", "c"}

# Ambil semua identifier
identifiers = set()

for token in tokens:
    if token[0] == "IDENTIFIER":
        identifiers.add(token[1])

error = False

for var in identifiers:
    if var not in declared_variables:
        print(f"Semantic Error : Variabel '{var}' belum dideklarasikan.")
        error = True

if not error:
    print("Semantic Check : SUCCESS")

# =========================
# THREE ADDRESS CODE (TAC)
# =========================

print("\n===== THREE ADDRESS CODE =====")

lhs_then = then_stmt[0]
rhs_then = then_stmt[2]

lhs_else = else_stmt[0]
rhs_else = else_stmt[2]

print(f"if {condition[0]} {condition[1]} {condition[2]} goto L1")
print("goto L2")
print()

print("L1:")
print(f"{lhs_then} = {rhs_then}")
print("goto L3")
print()

print("L2:")
print(f"{lhs_else} = {rhs_else}")
print()

print("L3:")
print("END")