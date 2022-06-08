# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner']
    _description = 'Partners'
    instructor = fields.Boolean(string='instructor')
    teacher_category_id = fields.Many2one('open_academy.teacher_category')
    session_partners_ids = fields.Many2many(comodel_name='res.partner', relation='session_partners_ids',
                                       column1='partner_id', column2='instructor_id')
