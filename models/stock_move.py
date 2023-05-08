from odoo import fields, models, api, _


class StockMove(models.Model):
    _inherit = 'stock.move'


    dimension = fields.Char(string="Dimension",  store=True, readonly=False, )




    # def _create_stock_moves(self, picking):
    #     res = super(StockMove, self)._create_stock_moves(picking)
    #     for line in self.order_line.filtered(lambda l: l.product_id.type in ('consu', 'product')):
    #         move = res.filtered(lambda m: m.sale_line_id == line)
    #         if move:
    #             move.dimension = line.dimension  # Copy the dimension from the sale order line to the move
    #     return res

    # @api.model
    # def _prepare_procurement_values(self, group_id=False):
    #     res = super(StockMove, self)._prepare_procurement_values(group_id=group_id)
    #     for line in self.order_line.filtered(lambda l: l.product_id.type in ('consu', 'product')):
    #
    # values.update = {
    #     'sale_line_id': line.id,
    #     'dimension': line.dimension,  # Add the new field to the procurement values
    # }
    #
    # res[line] = values
    # return res


