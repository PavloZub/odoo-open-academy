# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'open_academy.course'

    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'Name and description must be different!'),
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),
    ]
    name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible")
    session_ids = fields.One2many('open_academy.session', 'course_id', string="Sessions")
    # , default=lambda self: self.env.user)
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

    #@api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _("%s (copy)") % (self.name)
        return super(Course, self).copy(default)
