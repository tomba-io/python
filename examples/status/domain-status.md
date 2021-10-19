from tomba.client import Client
from tomba.services.status import Status

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

status = Status(client)

result = status.domain_status('gmail.com')
