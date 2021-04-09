# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class PlantVarieties(models.Model):
    _name = "plant.varieties"
    _description = "Types of cannabis plants"

    name = fields.Char(string='Name', required=True)
    genus = fields.Selection([
        ('indica', 'Indica'),
        ('sativa', 'Sativa'),
        ('ruderalis', 'Ruderalis'),
    ], required=True, default='indica')
    thc = fields.Float(string='THC', required=True)
    note = fields.Text(string='Description')
