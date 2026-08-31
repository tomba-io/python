```py
from tomba.client import Client
from tomba.services.finder import Finder

client = Client()

(
    client.set_key("ta_xxxx").set_secret("")  # Your Key  # Your Secret
)

finder = Finder(client)

result = finder.linkedin_finder("https://www.linkedin.com/in/alex-maccaw-ab592978")
```
