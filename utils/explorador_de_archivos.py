# python utils/explorador_de_archivos.py
from pathlib import Path
from collections import Counter, defaultdict
import json


pages = Path("pages")

def get_pages():
    return pages.glob("**/*.rst")
# print(Counter(page.suffix for page in pages.glob("**/*") if page.is_file()))
# Counter({'.rst': 878})

def get_lines(page):
    with open(page,"r") as f:
        return sum(1 for _ in f)


# Counter({2: 134, 14: 21, 3: 19, 6: 19, 5: 18, 11: 16, 7: 14, 4: 14, 8: 13, 13: 13, 10: 11, 9: 10, 12: 6})
# page_sizes = Counter(n for p in get_pages() if (n := get_lines(p)) < 15)
# print(page_sizes)        
d = defaultdict(list)

for page in get_pages():
    n = get_lines(page)
    if n < 15:
        d[n].append(page)

ordenado = {i:d[i] for i in sorted(d)}
# print(json.dumps(d,default=str,indent=2))
with open("utils/lineas.json","w+") as f:
    json.dump(ordenado, f, default=str, indent=2)


