```py
from tomba.client import Client
from tomba.services.phone import Phone

client = Client()

(
    client.set_key("ta_xxxx").set_secret("")  # Your Key  # Your Secret
)

phone = Phone(client)

result = phone.finder("******@zapier.com")
```
