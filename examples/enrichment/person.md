```py
from tomba.client import Client
from tomba.services.enrichment import Enrichment

client = Client()

(
    client.set_key("ta_xxxx").set_secret("")  # Your Key  # Your Secret
)

enrichment = Enrichment(client)

result = enrichment.person("john.doe@zapier.com")
```
