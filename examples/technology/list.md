```py
from tomba.client import Client
from tomba.services.technology import Technology

client = Client()

(
    client.set_key("ta_xxxx").set_secret("")  # Your Key  # Your Secret
)

technology = Technology(client)

result = technology.list("zapier.com")
```
