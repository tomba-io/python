```python
from tomba.client import Client
from tomba.services.usage import Usage

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

usage = Usage(client)

result = usage.get_usage()
```
