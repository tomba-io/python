```py
from tomba.client import Client
from tomba.services.keys import Keys

client = Client()

(
    client.set_key("ta_xxxx").set_secret("")  # Your Key  # Your Secret
)

keys = Keys(client)

result = keys.delete_key("")
```
