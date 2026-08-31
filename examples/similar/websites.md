```py
from tomba.client import Client
from tomba.services.similar import Similar

client = Client()

(
    client.set_key("ta_xxxx").set_secret("")  # Your Key  # Your Secret
)

similar = Similar(client)

result = similar.websites("zapier.com")
```
