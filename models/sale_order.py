from odoo import fields, models, api, _

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for move in self.mapped('picking_ids.move_lines'):
            sale_order_line = move.sale_line_id
            if sale_order_line:
                sale_order_line.dimension = move.custom_dimension or sale_order_line.dimension
        return res

    # def action_confirm(self):
    #     res = super(SaleOrder, self).action_confirm()
    #     for move in self.mapped('picking_ids.move_lines'):
    #         sale_order_line = move.sale_line_id
    #         if sale_order_line:
    #             move.dimension = sale_order_line.dimension
    #     return res



    #
