# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class test_mod(models.Model):
#     _name = 'test_mod.test_mod'
#     _description = 'test_mod.test_mod'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class test_mod(models.Model):
    _inherit = "sale.order"

    customer_ref = fields.Char()
