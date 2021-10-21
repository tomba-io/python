```python
from tomba.client import Client
from tomba.services.logs import Logs

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

logs = Logs(client)

result = logs.get_logs()
```
