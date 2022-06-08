# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class session(models.Model):
    _name = "open_academy.session"
    _description = 'open_academy.session'

    name = fields.Char(default=lambda self: "session" + str(fields.Date.context_today(self)))
    start_date = fields.Date('Start date', default=lambda self: fields.Date.context_today(self))
    duration = fields.Integer(default=10)
    number_of_seats = fields.Integer(default=10)
    seats_percentage = fields.Float(compute='_compute_percentage', store=True)
    instructor_id = fields.Many2one('res.partner')
    course_id = fields.Many2one('open_academy.course')
    attendee_ids = fields.Many2many('res.partner')
    active = fields.Boolean(default=True)
    # taken_seats = fields.Integer(compute='_compute_percentage', store=True)
    taken_seats = fields.Integer()
    color = fields.Integer()

    # onchange handler
    @api.onchange('taken_seats', 'attendee_ids')
    def _onchange_seats(self):
        # set auto-changing field
        self.taken_seats = len(self.attendee_ids)
        # Can optionally return a warning and domains
        # if self.number_of_seats <= 0:
        #     return {
        #         'warning': {
        #             'title': "Error",
        #             'message': "Too much attendees",
        #         }
        #     }
        #elif self.taken_seats > self.number_of_seats:
        #     return {
        #         'warning': {
        #             'title': "Error",
        #             'message': "Too much attendees",
        #         }
        #     }

    @api.depends('attendee_ids', 'number_of_seats')
    def _compute_percentage(self):
        for record in self:
            # record.taken_seats = len(self.attendees)
            record.seats_percentage = record.taken_seats / self.number_of_seats * 100 if self.number_of_seats != 0 else 100

    @api.constrains('attendees', 'instructor')
    def _check_attendees_count(self):
        for record in self:
            if len(record.attendee_ids) > record.number_of_seats:
                raise ValidationError("Too much attendees")
            if record.instructor_id in record.attendee_ids:
                raise ValidationError("Attendee cant be an Instructor")

        # all records passed the test, don't return anything
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
