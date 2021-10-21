```python
from tomba.client import Client
from tomba.services.keys import Keys

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

keys = Keys(client)

result = keys.create_key()
```
