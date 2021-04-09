# -*- coding: utf-8 -*-
# from odoo import http


# class MikeModule/(http.Controller):
#     @http.route('/mike_module//mike_module//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mike_module//mike_module//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mike_module/.listing', {
#             'root': '/mike_module//mike_module/',
#             'objects': http.request.env['mike_module/.mike_module/'].search([]),
#         })

#     @http.route('/mike_module//mike_module//objects/<model("mike_module/.mike_module/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mike_module/.object', {
#             'object': obj
#         })
