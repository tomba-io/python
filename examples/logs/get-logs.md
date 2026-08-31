```py
from tomba.client import Client
from tomba.services.logs import Logs

client = Client()

(
    client.set_key("ta_xxxx").set_secret("")  # Your Key  # Your Secret
)

logs = Logs(client)

result = logs.get_logs()
```
