```py
from tomba.client import Client
from tomba.services.leads_lists import LeadsLists

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

leads_lists = LeadsLists(client)

result = leads_lists.delete_list_id('[LIST_ID]')
```
