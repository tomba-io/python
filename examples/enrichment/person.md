```py
from tomba.client import Client
from tomba.services.enrichment import Enrichment

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

enrichment = Enrichment(client)

result = enrichment.person('john.doe@zapier.com')
```
