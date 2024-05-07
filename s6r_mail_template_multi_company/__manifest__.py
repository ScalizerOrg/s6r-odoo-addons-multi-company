# Copyright 2024 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Scalizer Mail Template Multi Company',
    'version': '16.0.1.0.0',
    'author': 'Scalizer',
    'website': 'https://www.scalizer.fr',
    'summary': "Retrieve templates by code in multi-company mode",
    'sequence': 0,
    'license': 'AGPL-3',
    'depends': [
        'mail_template_multi_company',  # OCA/multi-company
    ],
    'category': 'Generic Modules/Scalizer',
    'complexity': 'easy',
    'description': '''
This module adds a code field on mail templates to retrieve templates in multi-company mode.
    ''',
    'qweb': [
    ],
    'demo': [
    ],
    'images': [
    ],
    'data': [
        'views/mail_template.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
