# Copyright 2024 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).

from odoo import api, models, fields
from odoo.osv import expression


class MailTemplate(models.Model):
    _inherit = 'mail.template'

    code = fields.Char()

    @api.model
    def get_by_code(self, code):
        template_id = self.search([('code', '=', code),
                                   ('company_id', '=', self.env.company.id)], limit=1)
        if not template_id:
            template_id = self.search([('code', '=', code),
                                       ('company_id', '=', False)], limit=1)
        return template_id
