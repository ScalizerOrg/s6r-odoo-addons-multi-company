# Copyright 2025 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models, _
from odoo.tools.image import image_data_uri


class ResCompany(models.Model):
    _inherit = 'res.company'
    
    mail_catchall_domain = fields.Char()
