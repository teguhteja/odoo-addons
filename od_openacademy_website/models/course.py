from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = 'od_openacademy.course'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Open Academy Course"

    name = fields.Char(string="Title", required=True, translate=True)
    code = fields.Char(string="Code", copy=False, required=True, default="New", readonly=True)
    description = fields.Text(string="Description")
    course_date = fields.Date(string="Date", required=True, tracking=True)
    responsible_id = fields.Many2one('res.users', ondelete='set null', tracking=True, string="Responsible")
    session_ids = fields.One2many('od_openacademy.session', 'course_id', string="Sessions")
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancel', 'Cancel'),
    ], string="Status", required=True, default='draft', tracking=True)

    company_info = fields.Char(string="Company Info", company_dependent=True)
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    tag_ids = fields.Many2many('openacademy.course.tag', string="Tags")

class Session(models.Model):
    _name = 'od_openacademy.session'
    _description = 'Open Academy Session'

    name = fields.Char(string="Session Title", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    duration = fields.Float(string="Duration", required=True)
    seats = fields.Integer(string="Number of Seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('od_openacademy.course', string="Course", required=True, ondelete='cascade')
    
class CourseTag(models.Model):
    _name = 'openacademy.course.tag'
    _description = 'Course Tag'

    name = fields.Char(string="Tag Name", required=True)