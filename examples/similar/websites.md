```py
from tomba.client import Client
from tomba.services.similar import Similar

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

similar = Similar(client)

result = similar.websites('zapier.com')
```
