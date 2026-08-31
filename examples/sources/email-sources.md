```py
from tomba.client import Client
from tomba.services.sources import Sources

client = Client()

(
    client.set_key("ta_xxxx").set_secret("")  # Your Key  # Your Secret
)

sources = Sources(client)

result = sources.email_sources("b.mohamed@tomba.io")
```
