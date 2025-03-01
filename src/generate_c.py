import snippet_functions as snf
import sys, csv
from random import randint

number_of_files = int(sys.argv[1])

snippet_types = {
    0: snf.ari_snippet,
    1: snf.if_ari_snippet,
    2: snf.for_ari_snippet,
    3: snf.if_if_ari_snippet,
    4: snf.if_for_ari_snippet,
    5: snf.for_if_ari_snippet,
    6: snf.for_for_ari_snippet
}

data = open("data.csv", 'w')
writer = csv.writer(data)
writer.writerow(['snippet_type'])

for filenum in range(number_of_files):
    with open(f"c_files/{filenum}.c", 'w') as file:
        snippet_type = randint(0,6)
        file.write(snippet_types[snippet_type]())
        writer.writerow([snippet_type])

data.close()


