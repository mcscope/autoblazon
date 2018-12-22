from lark import Lark

earley_parser = Lark(open('blazon.lark'), parser="earley")
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
    "Three running greyhounds or",
    "A crowned demi-falcon",
    "Vairy or and gules",
    "Sable, a fesse checky argent and azure between three bezants",
    "Quarterly gules and or, a bend sable",
    "Or, a fesse azure and over all a bend gules",
    "Quarterly with a crescent for difference on the fesse point: 1 and 4, Argent, a fesse between six annulets gules; 2 and 3, Morrow",
    "Quarterly: 1 and 4, Gules, a saltire or surmounted by another vert, a crescent or for difference in chief"
    # "; 2 and 3, Ermine, two bars sable each with three fusils or"
]

for test in test_cases:
    print(earley_parser.parse(test).pretty()),
