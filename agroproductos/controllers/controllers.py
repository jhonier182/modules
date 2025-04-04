# -*- coding: utf-8 -*-
# from odoo import http


# class Agroproductos(http.Controller):
#     @http.route('/agroproductos/agroproductos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agroproductos/agroproductos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agroproductos.listing', {
#             'root': '/agroproductos/agroproductos',
#             'objects': http.request.env['agroproductos.agroproductos'].search([]),
#         })

#     @http.route('/agroproductos/agroproductos/objects/<model("agroproductos.agroproductos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agroproductos.object', {
#             'object': obj
#         })

