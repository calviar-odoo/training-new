# -*- coding: utf-8 -*-

from odoo import models,fields, api

class Spaceship(models.Model):
    
    _name = 'odoospace.spaceship'
    _description = 'Spaceships Description'
    
    spaceship_name = fields.Char(string='Spaceship Name', required=True)
    description = fields.Text(string='Description'),
    population = fields.Integer(string='Limit Population')