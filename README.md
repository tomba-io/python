# [<img src="https://app.tomba.io/tomba/f250de39816043cfc8f5578fa078a79e.svg" alt="Tomba" width="25"/>](https://tomba.io/) Tomba Email Finder Python Client Library

This is the official Python client library for the [Tomba.io](https://tomba.io.io) Email Finder API,
allowing you to:

- [Domain Search.](https://developer.tomba.io/#domain-search) (Search emails are based on the website You give one domain name and it returns all the email addresses found on the internet.)
- [Email Finder](https://developer.tomba.io/#email-finder) (This API endpoint generates or retrieves the most likely email address from a domain name, a first name and a last name..)
- [Email Verifier.](https://developer.tomba.io/#email-verifier) (checks the deliverability of a given email address, verifies if it has been found in our database, and returns their sources.)
- [Email Sources](https://developer.tomba.io/#email-sources) (Find email address source somewhere on the web .)
- [Company Domain autocomplete](https://developer.tomba.io/#autocomplete) (Company Autocomplete is an API that lets you auto-complete company names and retreive logo and domain information.)

# Getting Started

You'll need an Tomba API access token, which you can get by signing up for a free account at https://app.tomba.io/auth/register

The free plan is limited to 25 search request and 50 verification a month,  To enable all the data fields and additional request volumes see https://tomba.io/pricing.

## Installation

To install via [PyPI](https://pypi.org/):

```bash
pip install tomba-io
```

## Usage

### Domain Search

get email addresses found on the internet.

```python
from tomba.client import Client
from tomba.services.domain import Domain

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

domain = Domain(client)

result = domain.domain_search('stripe.com')

```

### Email Finder

Find the verified email address of any professional.

```python
from tomba.client import Client
from tomba.services.finder import Finder

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

finder = Finder(client)

result = finder.email_finder('stripe.com', 'Moskoz', 'Dustin')

```

### Email Verifier

Verify the validity of any professional email address with the most complete email checker.

```python
from tomba.client import Client
from tomba.services.verifier import Verifier

client = Client()

(client
  .set_key('ta_xxxx') # Your Key
  .set_secret('') # Your Secret
)

verifier = Verifier(client)

result = verifier.email_verifier('b.mohamed@tomba.io')

```

## Examples

Sample codes under **examples/** folder.

## Documentation

See the [official documentation](https://ipfinder.io/docs).

### Other Libraries

There are official Tomba Email Finder client libraries available for many languages including PHP, Python, Go, Java, Ruby, and many popular frameworks such as Django, Rails and Laravel. There are also many third party libraries and integrations available for our API.

https://developer.tomba.io/#introduction-libraries

### About Tomba

Founded in 2020, Tomba prides itself on being the most reliable, accurate, and in-depth source of Email address data available anywhere. We process terabytes of data to produce our Email finder API, company.


[![image](https://avatars.githubusercontent.com/u/67979591?s=200&v=4)](https://tomba.io/)

## Contribution

1. Fork it (<https://github.com/tomba-io/go/fork>)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## License

Please see the [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0.html) file for more information.
