# -*- coding: utf-8 -*-
# from odoo import http


# class Eventos(http.Controller):
#     @http.route('/eventos/eventos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eventos/eventos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('eventos.listing', {
#             'root': '/eventos/eventos',
#             'objects': http.request.env['eventos.eventos'].search([]),
#         })

#     @http.route('/eventos/eventos/objects/<model("eventos.eventos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eventos.object', {
#             'object': obj
#         })

