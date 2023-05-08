from odoo import fields, models, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    dimension = fields.Char(string="Dimension", required=False, )


    # this method that pass data from sale order line to stock
    @api.model
    def _prepare_procurement_values(self, group_id=False):
        res = super(SaleOrderLine, self)._prepare_procurement_values(group_id=group_id)
        res.update({'dimension': self.dimension})
        return res

   #this function pass data from stock.move to invoice
    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res.update({
            'dimension': self.move_ids.dimension

        })

        return res


class Stock_Rule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id,
                               values):
        move_values = super()._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin,
                                                     company_id, values)
        if values.get('dimension'):
            move_values['dimension'] = values['dimension']
        return move_values
