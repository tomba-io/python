```py
from tomba.client import Client
from tomba.services.account import Account

client = Client()

(
    client.set_key("ta_xxxx").set_secret("")  # Your Key  # Your Secret
)

account = Account(client)

result = account.get_account()
```
