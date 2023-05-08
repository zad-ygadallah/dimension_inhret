from odoo import fields, models, api, _


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    dimension = fields.Char(string="Dimension", store=True, readonly=False, )



