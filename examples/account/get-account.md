```python
from tomba.client import Client
from tomba.services.account import Account

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

account = Account(client)

result = account.get_account()
```
