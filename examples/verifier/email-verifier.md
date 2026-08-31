```py
from tomba.client import Client
from tomba.services.verifier import Verifier

client = Client()

(
    client.set_key("ta_xxxx").set_secret("")  # Your Key  # Your Secret
)

verifier = Verifier(client)

result = verifier.email_verifier("b.mohamed@tomba.io")
```
