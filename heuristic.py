from lark import Lark
from random import shuffle, seed
import time
seed(time.time())
cyk_parser = Lark(open('blazon.lark'), parser="cyk")
earley_parser = Lark(open('blazon.lark'), parser="earley")

success = 0
total = 0
missed = []
old_successes = set()
new_successes = set()
with open("heuristic_successes.txt", "r") as successes_file:
    old_successes = {line for line in successes_file}
with open("blazons/cambridge_blazons_only.txt") as cambridge_blazons:
    for line in cambridge_blazons:
        total += 1
        try:
            ast = cyk_parser.parse(line)
            success += 1
            new_successes.add(line)
            # print(line)
        except:
            try:
                ast = earley_parser.parse(line)
                success += 1
                new_successes.add(line)
                # print(line)
            except:
                if len(line.split()) < 5:
                    missed.append(f"\t<missed> {line}")

shuffle(missed)
for l in missed[:50]:
    print(l)
print(f"{success} / {total} : {success/total}")

improvements = new_successes - old_successes
regressions = old_successes - new_successes
for line in improvements:
    print(f"Improvement {line}")

for line in regressions:
    print(f"REGRESSION {line}")

with open("heuristic_successes.txt", "w") as outfile:
    for success in new_successes:
        outfile.writelines(new_successes)
