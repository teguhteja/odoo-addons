from odoo import http
from odoo.http import request

class OdooDiscussions(http.Controller):

    @http.route('/odoodiscussions/courses', auth='public', website=True)
    def display_data(self, **kwargs):
        return "<h1>This is Odoo Discussions<h1>"
    
    @http.route('/odoodiscussions/sessions', auth='public', website=True)
    def display_sessions(self, **kwargs):
        return "This is Odoo Discussions Sessions"
    
    @http.route('/odoodiscussions/classes1', auth='public', website=True)
    def display_classes1(self, **kwargs):
        template = 'od_openacademy_website.odoodiscussions_classes1'
        return request.render(template)

    @http.route('/odoodiscussions/classes2', auth='public', website=True)
    def odoodiscussions_classes2(self, **kwargs):
        values = {
            "message": "Hello Odoo Discussions",
        }
        return request.render('od_openacademy_website.odoodiscussions_classes2', values)
    
    @http.route('/odoodiscussions/classes3', auth='public', website=True)
    def odoodiscussions_classes(self, **kwargs):
        courses = request.env['od_openacademy.course'].search([])
        values = {
            "message": "Hello Odoo Discussions 3",
            "courses": courses
        }
        return request.render('od_openacademy_website.odoodiscussions_classes3', values)