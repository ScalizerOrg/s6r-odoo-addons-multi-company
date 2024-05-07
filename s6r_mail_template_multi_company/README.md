Scalizer Mail Template Multi Company
===============

This module adds a code field on mail templates to retrieve templates in multi-company mode.

<br>
<br>

## Usage

Set a code on mail templates from different companies.
Get the company mail template by using the get_by_code function:

```python
mail_template_id = self.env['mail.template'].get_by_code('welcome_email')
```

## Requirements

OCA addon [mail_template_multi_company](https://github.com/OCA/multi-company/tree/16.0/mail_template_multi_company) is required.

## Authors

* Scalizer

## Contributors

* Michel Perrocheau ([Github](https://github.com/myrrkel))

## Maintainers

This module is maintained by [Scalizer](https://www.scalizer.fr).

![Scalizer](./static/description/logo.png)
