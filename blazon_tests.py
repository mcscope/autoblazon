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
    "Three bends ermine",
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
    "Gules, three escutcheons argent each charged with a cinquefoil",
    "Azure, a cheveron ermine cotised or between three martlets argent",
    "Azure, a sword and key in saltire or and on a chief or three lozenges gules",
    "Argent, three saltires engrailed sable with a crescent gules for difference",
    "Azure, three stags tripping or",
    "Per fesse sable and argent, a lion counterchanged",
    "Argent, a fret gules, on a canton gules a lion passant or all in a border engrailed sable",
    # Quartering is so hard!
    "Quarterly gules and or, a bend sable",
    "Or, a fesse azure and over all a bend gules",
    "Sable, a cheveron between three leopards' faces or",
    "Per fesse embattled, three falcons counterchanged",
    "Or, three piles gules, on a canton argent a griffin sable",
    "A cheveron between ten crosses crosslet",
    " Or, on a fesse between two cheverons sable three crosses crosslet or",
    "A fesse between three crosses crosslet fitchy",
    # expanding vocaublary
    "On a fesse between three saltires three lions' heads erased",
    "Gules, a double-headed eagle between three fleurs-delys argent",
    " lion between three crosses formy",
    "On a canton an owl",
    "Sable, three escallops and a border engrailed sable",
    "Barry argent and azure, three roundels gules in chief, a label ermine",
    "Argent, a lion gules crowned or",
    "Argent, a stag's head erased gules",
    "Argent, a fesse wavy and in chief three crescents gules",
    "Sable, a fesse ermine and in chief three crosses formy fitchy argent",
    "Three bears' heads erased and muzzled, a chief",
    "Barry wavy argent and azure",
    "Argent, a bend azure, in chief an annulet gules", 
    "Gules, a fesse of three lozenges between three lions' heads erased or",
    "A fesse between three crosses crosslet fitchy",
    "Quarterly per fesse indented argent and gules",
    # Proper names, here we care about case
    "Beacham",
    "Quarterly: 1, Lancaster; 2, Angoulême; 3, Guienne; 4, Butler quartering Rochfort; 5, Brotherton; 6, Warenne",
    "Quarterly of six: 1, Luxemburg; 2, Baux; 3, Cyprus; 4, Orsini; 5, St",
    "Per cheveron sable and ermine, in chief two boars' heads or",
    "Azure, on a chief or three martlets gules",
    "Gules, three cushions ermine",
    "Or ermined sable, a lion sable collared argent, on a canton vert a garb or",

    # subcase - crusily with cross aspects
    "Azure crusily fitchy, two barbels erect addorsed or",
    "Azure crusily of crosslets, three herrings argent",


    "lion",
    "A fesse between three voided lozenges",
    "Azure, three escallops argent, on a chief gules a fleur-de-lys between two mullets or",
    "Per fesse indented, in chief three mullets and in base a crescent",
    "Argent, a fesse indented gules and or and in chief three trefoils sable",
    "Azure, ten estoiles or",
    "Sable semy of cinquefoils, a lion argent",
    "Azure flory, a lion argent",
    # FROM SCA site!
    "Argent, on a bend between a mullet and a lozenge sable, an annulet between two roundels argent, on a chief wavy sable a sword argent",

    "Sable, two stags combatant argent, collared with coronets and chained and attired or"
    # "Quarterly with a crescent for difference on the fesse point: 1 and 4, Argent, a fesse between six annulets gules; 2 and 3, Morrow",
    # "Quarterly per pale indented or and azure, with an eagle displayed or on the blue, over all on a bend azure a fret between two martlets or"
    # "Quarterly: 1 and 4, Gules, a saltire or surmounted by another vert, a crescent or for difference in chief"
    # "; 2 and 3, Ermine, two bars sable each with three fusils or"
]

for test in test_cases:
    print (test)
    tree = earley_parser.parse(test)
    print(tree.pretty())
