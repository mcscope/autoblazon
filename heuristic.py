from lark import Lark
from collections import Counter
parser = Lark(open('blazon.lark'), parser="lalr")

success = 0
total = 0
missed_counter = Counter()
with open("blazons/cambridge_blazons_only.txt") as cambridge_blazons:
    for line in cambridge_blazons:
        total += 1
        try:
            ast = parser.parse(line)
            success += 1
            print(line)
        except:
            missed_counter.update(line.split())
            if len(line.split()) < 5:
                print(f"\t<missed> {line}")
            continue
print(f"{success} / {total} : {success/total}")
print(f"{missed_counter.most_common(10)}")
