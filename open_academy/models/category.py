# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TeacherCategory(models.Model):
    _name = "open_academy.teacher_category"
    _description = 'Teacher category'

    name = fields.Char()
