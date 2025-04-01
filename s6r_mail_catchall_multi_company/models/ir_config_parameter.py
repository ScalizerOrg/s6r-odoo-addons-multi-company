# Copyright 2025 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).
from odoo import api, fields, models
from odoo.tools import ormcache


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'
    company_id = fields.Many2one('res.company', "Company")

    @api.model
    def _get_param(self, key):
        if key == 'mail.catchall.domain':

            company_id = self.env.company.id
            if self.env.context.get("force_config_parameter_company"):
                company_id = self.env.context["force_config_parameter_company"].id
            if company_id:
                self.flush_model(["key", "value"])
                query = '''SELECT c.id, c.mail_catchall_domain, 
        p.mail_catchall_domain as parent_mail_catchall_domain
        FROM res_company as c LEFT JOIN res_company as p on c.parent_id = p.id
        WHERE c.id = %s'''
                self.env.cr.execute(query, [company_id])
                result = self.env.cr.fetchone()
                mail_catchall_domain = result and result[1] or result and result[2] or ''
                return mail_catchall_domain or super()._get_param(key)

        return super(IrConfigParameter, self)._get_param(key)
