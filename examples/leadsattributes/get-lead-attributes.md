```py
from tomba.client import Client
from tomba.services.leads_attributes import LeadsAttributes

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

leads_attributes = LeadsAttributes(client)

result = leads_attributes.get_lead_attributes()
```
