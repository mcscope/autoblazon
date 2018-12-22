from lark import Lark

parser = Lark(open('blazon.lark'), parser="lalr")
test_cases = [
    # tinctures
    "azure",
    # charges
    "azure, a bend or",
    "Azure, bend or",
    "Azure, bend",
    "Or, a cheveron gules",
    # furs
    "Ermine, bend vair",
    "Three lions rampant",
    "Or, a fesse vair",
    "A bend sinister or",
    # plural charges
    "Three Bends ermine",
    # charges IN charges
    "Five escallops in saltire",
    # AND clauses
    "Sable, a lion argent and a chief gules",
    # PATTERNED FIELDS
    "Barry argent and azure",
    "Bendy azure and or",
    "Gyronny gules and argent, on an escutcheon argent a cinquefoil azure",
    # Aspect
    "A crowned pomegranate",
]

for test in test_cases:
    print(parser.parse("A crowned pomegranate").pretty()),
