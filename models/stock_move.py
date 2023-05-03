from odoo import fields, models, api, _

class StockMove(models.Model):

    _inherit = 'stock.move'

    dimension = fields.Char(string="Dimension",required=False)
    # dimension = fields.Char(string="Dimension", required=False, related='sale_line_id.dimension')


