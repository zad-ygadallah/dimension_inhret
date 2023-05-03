# -*- coding: utf-8 -*-
# from odoo import http


# class InheritanceSale(http.Controller):
#     @http.route('/inheritance_sale/inheritance_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inheritance_sale/inheritance_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inheritance_sale.listing', {
#             'root': '/inheritance_sale/inheritance_sale',
#             'objects': http.request.env['inheritance_sale.inheritance_sale'].search([]),
#         })

#     @http.route('/inheritance_sale/inheritance_sale/objects/<model("inheritance_sale.inheritance_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inheritance_sale.object', {
#             'object': obj
#         })
