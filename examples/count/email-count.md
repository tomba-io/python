from tomba.client import Client
from tomba.services.count import Count

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

count = Count(client)

result = count.email_count('tomba.io')
