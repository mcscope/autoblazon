from lark import Lark

parser = Lark(open('blazon.lark'), parser="lalr")

# tinctures
print( parser.parse("azure").pretty() )
# charges
print( parser.parse("azure, a bend or").pretty() )
print( parser.parse("Azure, bend or").pretty() )
print( parser.parse("Azure, bend").pretty() )
# furs
print( parser.parse("Ermine, bend vair").pretty() )
print( parser.parse("Three lions rampant").pretty() )
print( parser.parse("Or, a fesse vair").pretty() )
print( parser.parse("A bend sinister or").pretty() )
# plural charges
print( parser.parse("Three Bends ermine").pretty() )
# recursive charges
print( parser.parse("Five escallops in saltire").pretty() )
print( parser.parse("Or, a cheveron gules").pretty() )

