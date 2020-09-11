# Query string parser

query string parser like php


### Quick start

First, install package

```
pip3 install query-string-parser
```

include in your project

```python
from queryStringParser import parser
```

Parse query string

```python
dict_query = parser.parse("foo[]=bar+foo&foo[]=baz&biz[name]=gino&biz[name]=pino&caz=33&paz[]=ggu")

print(dict_query)
```
