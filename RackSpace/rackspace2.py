import os
import numpy as py
from collections import Counter

input_file = 'easylist.txt'
domain_split = '@'

with open(input_file, encoding="utf8", errors='ignore') as f:

    for line in f:
        if domain_split in line:
            lines = [line.rstrip('\n').split('@')[-1] for line in f]

        else:
            lines = [line.rstrip('\n') for line in f]

print(lines)
tld_map = (Counter(lines))

for domain, count in tld_map.items():
    print(domain, ":", count)
