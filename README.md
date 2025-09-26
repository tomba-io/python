# [<img src="https://tomba.io/logo.svg" alt="Tomba" width="25"/>](https://tomba.io/) Tomba Email Finder Python Client Library

This is the official Python client library for the [Tomba.io](https://tomba.io) Email Finder API,
allowing you to:

-   [Domain Search](https://tomba.io/domain-search) (Search emails are based on the website You give one domain name and it returns all the email addresses found on the internet.)
-   [Email Finder](https://tomba.io/email-finder) (This API endpoint generates or retrieves the most likely email address from a domain name, a first name and a last name..)
-   [Author Finder](https://tomba.io/author-finder) (Instantly discover the email addresses of article authors.)
-   [Linkedin Finder](https://tomba.io/author-finder) (The Linkedin lets you find the current job title, company, location and social profiles of the person behind the linkedin URL.)
-   [Email Verifier](https://tomba.io/email-verifier) (checks the deliverability of a given email address, verifies if it has been found in our database, and returns their sources.)
-   [Email Enrichment.](https://tomba.io/enrichment) (Locate and include data in your emails.)

# Getting Started

You'll need an Tomba API access token, which you can get by signing up for a free account at [https://app.tomba.io/auth/register](https://app.tomba.io/auth/register)

The free plan is limited to 25 search request and 50 verification a month, To enable all the data fields and additional request volumes see [https://tomba.io/pricing](https://tomba.io/pricing).

## Requirements

-   Python 3.5+
-   `requests` library

## Installation

To install via [PyPI](https://pypi.org/project/tomba-io/):

```bash
pip install tomba-io
```

## Quick Start

```py
from tomba.client import Client

client = Client()
client.set_key('YOUR_KEY').set_secret('YOUR_SECRET')
```

## Usage

### Domain Search

```py
from tomba.services.domain import Domain

domain = Domain(client)
result = domain.domain_search('stripe.com')
print(result)
```

### Email Finder

```py
from tomba.services.finder import Finder

finder = Finder(client)
result = finder.email_finder('tomba.io', 'Mohamed', 'Ben rebia')
print(result)
```

### Email Verifier

```py
from tomba.services.verifier import Verifier

verifier = Verifier(client)
result = verifier.email_verifier('b.mohamed@tomba.io')
print(result)
```

## Examples

Sample codes under [**examples/**](/examples/) folder.

## Error Handling

All errors raise `TombaException`:

```py
from tomba.exception import TombaException

try:
    result = domain.domain_search('stripe.com')
except TombaException as e:
    print(f"Error: {e.message} (code: {e.code})")
```

## Documentation

See the [official documentation](https://docs.tomba.io/introduction).

### Other Libraries

There are official Tomba Email Finder client libraries available for many languages including PHP, Python, Go, Java, Ruby, and many popular frameworks such as Django, Rails and Laravel. There are also many third party libraries and integrations available for our API.

[https://docs.tomba.io/libraries](https://docs.tomba.io/libraries)

### About Tomba

Founded in 2021, Tomba prides itself on being the most reliable, accurate, and in-depth source of Email address data available anywhere. We process terabytes of data to produce our Email finder API, company.

[![image](https://avatars.githubusercontent.com/u/67979591?s=200&v=4)](https://tomba.io/)

## Contribution

1. Fork it (<https://github.com/tomba-io/python/fork>)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## License

Please see the [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0.html) file for more information.
