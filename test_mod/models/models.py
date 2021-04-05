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
class TestSale(models.Model):
    _inherit = "sale.order"

    # Allows us to notate and store who refered the customer to the company.
    customer_ref = fields.Char()
    
    # This field allows the customer to select their level of subsciption. 
    # The first string of each tuple is what is used in the code, and the second string of each tuple is what is displayed client-side.
    customer_tier = fields.Selection([('silver', 'Silver'), ('gold', 'Gold'), ('platinum', 'Platinum'), ('diamond', 'Diamond')])
        
    
    # Displays a quote that varies depending on the chosen level.
    customer_tier_quote = fields.Char(compute='_compute_tier_quote')

    @api.depends('customer_tier') 
    # Draws the value from what was selected in the customer tier field.
    # Make sure to use the first string from each tuple when looking for the right response from each selection.
    def _compute_tier_quote(self):
        if customer_tier == 'silver':
            return 'Your quote is $10.00'
        if customer_tier == 'gold':
            return 'Your quote is $20.00'
        if customer_tier == 'platinum':
            return 'Your quote is $30.00'
        if customer_tier == 'diamond':
            return 'Your quote is $40.00'
        else:
            return 'Select a tier to learn your quote.'


class test_debt(models.Model):
    _inherit = "res.partner"

    customer_debt = fields.Char()  