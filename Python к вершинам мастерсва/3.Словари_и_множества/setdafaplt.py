import re
import sys
import collections
# запуск python setdafaplt.py zen.txt
WORD_RE = re.compile(r'\w+')

# index = {}
index = collections.defaultdict(list)

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            colump_no = match.start() + 1
            location = (line_no, colump_no)
# вариант в тупую
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences


# Эта строка кода добавляет значение location в список значений словаря index,
# связанный с ключом word. Если ключ word еще не существует в словаре, 
# то он создается с пустым списком в качестве значения, затем значение location добавляется в этот список.
# Таким образом, этот код строит индекс слов, сопоставляя каждому слову список местоположений, где оно встречается.
            # index.setdefault(word, []).append(location)

# вариант с defaultdict
            index[word].append(location)

            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences


for word in sorted(index, key=str.upper):
    print(word, index[word])
