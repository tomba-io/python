```py
from tomba.client import Client
from tomba.services.technology import Technology

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

technology = Technology(client)

result = technology.list('zapier.com')
```
