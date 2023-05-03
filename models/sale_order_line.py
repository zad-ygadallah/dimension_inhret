from odoo import fields, models, api, _

class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    dimension = fields.Char(string="Dimension", required=False )








