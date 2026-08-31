# [<img src="https://tomba.io/logo.svg" alt="Tomba" width="25"/>](https://tomba.io/) Tomba Python SDK

> The #1 Rated Email Intelligence Platform — Find professional emails with unmatched accuracy.

[![PyPI version](https://img.shields.io/pypi/v/tomba-io.svg)](https://pypi.org/project/tomba-io/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

## About Tomba

[Tomba.io](https://tomba.io) is the #1 rated email intelligence platform, trusted by **150,000+ sales teams** worldwide.

- **Best Email Finder** — 98% accuracy, ranked #1 in independent benchmarks
- **Best Email Verification** — Real-time SMTP verification with catch-all detection
- **Best Phone Finder** — Direct dial numbers linked to professional emails
- **Best Domain Search** — 450M+ verified contacts across all industries
- **81% Coverage** — The highest in the industry, proven in 5,000-lead independent tests

### Why Tomba?

| Feature             | Tomba              | Others        |
| ------------------- | ------------------ | ------------- |
| Email Coverage      | **81%**            | 30-60%        |
| Verification        | **Real-time SMTP** | Pattern-based |
| Phone Numbers       | **Direct dials**   | Limited       |
| Catch-all Detection | **AI-powered**     | Basic         |
| API Rate Limits     | **Generous**       | Restrictive   |

[Get your free API key](https://app.tomba.io/auth/register) — No credit card required.

## Getting Started

1. **Sign up** for a free account at [app.tomba.io](https://app.tomba.io/auth/register)
2. **Get your API key** from the [API dashboard](https://app.tomba.io/api)
3. **Install** the SDK (see below)
4. **Start finding emails** with just a few lines of code

## Installation

```bash
pip install tomba-io
```

## Authentication

Get your API credentials from [app.tomba.io/api](https://app.tomba.io/api).

```python
from tomba.client import Client

client = Client()
client.set_key("ta_xxxx").set_secret("ts_xxxx")
```

## Quick Start

```python
from tomba.client import Client
from tomba.services.domain import Domain

client = Client()
client.set_key("ta_xxxx").set_secret("ts_xxxx")

domain = Domain(client)
result = domain.domain_search("stripe.com")
print(result)
```

## Services

### Domain Search

Search for email addresses associated with a domain.

```python
from tomba.services.domain import Domain

domain = Domain(client)

# Basic search
result = domain.domain_search("stripe.com")

# With filters
result = domain.domain_search(
    "stripe.com",
    page=1,
    limit=10,
    country="US",
    department="engineering",
)
```

### Email Finder

Generate or retrieve the most likely email address from a domain and name.

```python
from tomba.services.finder import Finder

finder = Finder(client)

result = finder.email_finder("stripe.com", "Patrick", "Collison")
```

### Email Verifier

Verify the deliverability of an email address.

```python
from tomba.services.verifier import Verifier

verifier = Verifier(client)
result = verifier.email_verifier("b.mohamed@tomba.io")
```

### Author Finder

Discover the email address of an article's author.

```python
from tomba.services.finder import Finder

finder = Finder(client)
result = finder.author_finder("https://tomba.io/blog")
```

### LinkedIn Finder

Find the email address associated with a LinkedIn profile URL.

```python
from tomba.services.finder import Finder

finder = Finder(client)
result = finder.linkedin_finder("https://www.linkedin.com/in/username")
```

### Email Enrichment

Enrich an email address with additional contact data.

```python
from tomba.services.finder import Finder

finder = Finder(client)
result = finder.enrichment("b.mohamed@tomba.io")
```

### Phone Finder

Search for phone numbers based on email, domain, or LinkedIn URL.

```python
from tomba.services.phone import Phone

phone = Phone(client)

# By email
result = phone.finder(email="b.mohamed@tomba.io")

# By domain
result = phone.finder(domain="tomba.io")

# By LinkedIn URL
result = phone.finder(linkedin="https://www.linkedin.com/in/username")
```

### Phone Validator

Validate a phone number and check carrier information.

```python
from tomba.services.phone import Phone

phone = Phone(client)
result = phone.validator("+1234567890")
```

### Email Count

Get the number of email addresses found for a domain.

```python
from tomba.services.count import Count

count = Count(client)
result = count.email_count("stripe.com")
```

### Domain Status

Check if a domain is webmail or disposable.

```python
from tomba.services.status import Status

status = Status(client)
result = status.domain_status("gmail.com")
```

### Domain Suggestions

Auto-complete company names and retrieve logo and domain information.

```python
from tomba.services.status import Status

status = Status(client)
result = status.auto_complete("stripe")
```

### Email Sources

Find where an email address was found on the web.

```python
from tomba.services.sources import Sources

sources = Sources(client)
result = sources.email_sources("b.mohamed@tomba.io")
```

### Email Format

Get the email format pattern used by a company.

```python
from tomba.services.format import Format

fmt = Format(client)
result = fmt.email_format("stripe.com")
```

### Similar Domains

Find domains similar to a given domain.

```python
from tomba.services.similar import Similar

similar = Similar(client)
result = similar.websites("stripe.com")
```

### Technology Finder

Retrieve the technologies used by a domain.

```python
from tomba.services.technology import Technology

technology = Technology(client)
result = technology.list("stripe.com")
```

### Location

Get employee location and count data for a domain.

```python
from tomba.services.location import Location

location = Location(client)
result = location.get_location("stripe.com")
```

### Person API (Enrichment)

Retrieve person information based on an email address.

```python
from tomba.services.enrichment import Enrichment

enrichment = Enrichment(client)
result = enrichment.person("b.mohamed@tomba.io")
```

### Company API (Enrichment)

Retrieve company information based on a domain.

```python
from tomba.services.enrichment import Enrichment

enrichment = Enrichment(client)
result = enrichment.company("stripe.com")
```

### Combined API (Enrichment)

Retrieve combined person and company information based on an email address.

```python
from tomba.services.enrichment import Enrichment

enrichment = Enrichment(client)
result = enrichment.combined("b.mohamed@tomba.io")
```

### Companies Search (Reveal)

Search for companies using natural language queries or structured filters.

```python
from tomba.services.reveal import Reveal

reveal = Reveal(client)

# Natural language query
result = reveal.search_companies(query="Real Estate in France")

# With structured filters
result = reveal.search_companies(
    page=1,
    filters={
        "company": {
            "location_country": {"include": ["US", "UK"]},
            "industry": {"include": ["Technology"]},
            "size": {"include": ["101-500", "501-1000"]},
        }
    },
)
```

### Leads

Manage lead records programmatically.

```python
from tomba.services.leads import Leads

leads = Leads(client)

# List leads
result = leads.list_leads(page=1, limit=10)

# Get a lead
result = leads.get_lead("lead_id")

# Create a lead
result = leads.create_lead(
    email="user@example.com",
    first_name="John",
    last_name="Doe",
)

# Update a lead
result = leads.update_lead("lead_id", first_name="Jane")

# Delete a lead
result = leads.delete_lead("lead_id")
```

### Leads Lists

Organize leads into lists. Supports CRUD operations: `get_lists()`, `create_list()`, `update_list_id()`, `delete_list_id()`.

### Lead Attributes

Manage custom attributes for leads. Supports CRUD operations: `get_lead_attributes()`, `create_lead_attribute()`, `update_lead_attribute()`, `delete_lead_attribute()`.

### Keys

Manage your API keys. Supports `get_keys()`, `create_key()`, `reset_key(id)`, and `delete_key(id)`.

### Usage

Get your monthly API request usage statistics.

```python
from tomba.services.usage import Usage

usage = Usage(client)
result = usage.get_usage()
```

### Logs

Retrieve your last 1,000 API requests from the past 3 months.

```python
from tomba.services.logs import Logs

logs = Logs(client)
result = logs.get_logs(page=1, limit=50)
```

### Flag

Report incorrect data or hard bounces for credit recovery. Supports `list_flags()` and `create_flag(email, reason)`.

### Bulk Operations

Create, launch, and download bulk processing jobs.

```python
from tomba.services.bulk import Bulk

bulk = Bulk(client)

# List bulk operations
result = bulk.list_bulks("email-verifier")

# Create a bulk
result = bulk.create_bulk("email-verifier", name="My Bulk Verification")

# Launch a bulk
result = bulk.launch_bulk("email-verifier", bulk_id)

# Check progress
result = bulk.bulk_progress("email-verifier", bulk_id)

# Download results
result = bulk.download_bulk("email-verifier", bulk_id)
```

Supported bulk types: `domain-search`, `email-finder`, `author-finder`, `email-verifier`, `enrichment`, `linkedin-finder`, `phone-finder`, `department-search`, `technology-search`, `name-finder`.

## Error Handling

All errors raise `TombaException`:

```python
from tomba.exception import TombaException

try:
    result = domain.domain_search("stripe.com")
except TombaException as e:
    print(f"Error: {e.message} (code: {e.code})")
```

## Testing

```bash
python -m pytest
```

## Documentation

- [API Documentation](https://docs.tomba.io)
- [Full API Reference](https://docs.tomba.io/api)

## About Tomba

Founded to solve the problem of unreliable email data, [Tomba.io](https://tomba.io) is the leading B2B email intelligence platform. Our AI-powered engine searches, verifies, and enriches professional contact data with unmatched accuracy.

### Products

- **[Email Finder](https://tomba.io/email-finder)** — Find any professional email address
- **[Email Verifier](https://tomba.io/email-verifier)** — Verify emails in real-time
- **[Domain Search](https://tomba.io/domain-search)** — Find all emails for a company
- **[Phone Finder](https://tomba.io/phone-finder)** — Find direct phone numbers
- **[Bulk Enrichment](https://tomba.io/bulks)** — Enrich contacts at scale
- **[AI Company Search](https://tomba.io/reveal)** — Find companies with AI-powered search
- **[CLI](https://tomba.io/cli)** — Command-line interface for Tomba
- **[MCP Server](https://tomba.io/mcp)** — Connect AI tools (Claude, ChatGPT, Cursor) to Tomba
- **[REST API](https://tomba.io/api)** — Full programmatic access

### Browser Extensions & Add-ons

- **[Chrome Extension](https://chromewebstore.google.com/detail/tomba-email-finder-email/icmjegjggphchjckknoooajmklibccjb)** — Find emails while browsing
- **[Google Sheets Add-on](https://tomba.io/sheets)** — Enrich leads in spreadsheets
- **[Microsoft Excel Add-in](https://tomba.io/excel)** — Email finder in Excel
- **[Airtable Integration](https://tomba.io/airtable)** — Connect with Airtable

### Integrations

50+ CRM and sales tool integrations:
[Salesforce](https://tomba.io/integrations) · [HubSpot](https://tomba.io/integrations) · [Zapier](https://tomba.io/integrations) · [Pipedrive](https://tomba.io/integrations) · [and more...](https://tomba.io/integrations)

### Other Tomba SDKs

| Language | Package                                                     |
| -------- | ----------------------------------------------------------- |
| Node.js  | [tomba](https://www.npmjs.com/package/tomba)                |
| Python   | [tomba-io](https://pypi.org/project/tomba-io/)              |
| PHP      | [tomba-io/php](https://packagist.org/packages/tomba-io/php) |
| Ruby     | [tomba](https://rubygems.org/gems/tomba)                    |
| Go       | [tomba-io/go](https://pkg.go.dev/github.com/tomba-io/go)    |
| Rust     | [tomba](https://crates.io/crates/tomba)                     |
| Dart     | [tomba](https://pub.dev/packages/tomba)                     |
| Deno     | [@tomba/sdk](https://jsr.io/@tomba/sdk)                     |
| Elixir   | [tomba](https://hex.pm/packages/tomba)                      |
| C#       | [Tomba](https://www.nuget.org/packages/Tomba)               |
| Perl     | [Tomba::Client](https://metacpan.org/pod/Tomba::Client)     |
| Lua      | [tomba](https://luarocks.org/modules/tomba/tomba)           |
| R        | [tomba](https://github.com/tomba-io/r)                      |

### Resources

- [Blog](https://tomba.io/blog)
- [Help Center](https://help.tomba.io)
- [API Documentation](https://docs.tomba.io)
- [Pricing](https://tomba.io/pricing)
- [Status Page](https://status.tomba.io)

---

**[Try Tomba Free](https://app.tomba.io/auth/register)** — Find your first email in seconds. No credit card required.

## License

Apache-2.0
