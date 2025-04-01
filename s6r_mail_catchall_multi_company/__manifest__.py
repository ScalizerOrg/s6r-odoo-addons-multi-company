# Copyright 2025 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Scalizer Mail Catchall Multi Company',
    'version': '16.0.1.0.0',
    'author': 'Scalizer',
    'website': 'https://www.scalizer.fr',
    'summary': "Mail catchall domains in multi-company mode",
    'sequence': 0,
    'license': 'LGPL-3',
    'depends': [
    ],
    'category': 'Generic Modules/Scalizer',
    'complexity': 'easy',
    'description': '''
This module adds a field on companies to retrieve catchall domain in multi-company mode.
    ''',
    'qweb': [
    ],
    'demo': [
    ],
    'images': [
    ],
    'data': [
        'views/res_company_views.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
