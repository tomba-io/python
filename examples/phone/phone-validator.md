```py
from tomba.client import Client
from tomba.services.phone import Phone

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

phone = Phone(client)

result = phone.validator('+14158586273')
```
