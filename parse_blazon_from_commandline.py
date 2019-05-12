from lark import Lark
import sys
earley_parser = Lark(open('blazon.lark'), parser="earley")

print(sys.argv[1])
blazon = sys.argv[1]
if not blazon:
    raise Exception("give me a blazon in quotes")
tree = earley_parser.parse(blazon)
print(tree.pretty())


