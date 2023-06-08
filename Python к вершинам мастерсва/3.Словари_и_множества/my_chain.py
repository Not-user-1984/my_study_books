d1  = dict(a=1,b=2)
d2  = dict(a=1,b=2,c=6)
from collections import ChainMap

chain = ChainMap(d1, d2)
print(chain["a"])
print(chain["c"])
# ChainMap полезен при реализации интерпретаторов языков с вложенными областями видимости,
# когда каждая область видимости представлена отдель- ным отображением, в направлении от самого внутреннего к самому внеш-нему. 
# В разделе «Объекты ChainMap» документации по модулю collections
# (https://docs.python.org/3/library/collections.html#collections.ChainMap)
