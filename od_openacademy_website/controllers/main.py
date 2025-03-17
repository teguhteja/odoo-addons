from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

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
    
    @http.route('/odoodiscussions/classes4', auth='public', website=True)
    def odoodiscussions_classes(self, **kwargs):
        courses = request.env['od_openacademy.course'].search([])
        values = {
            "message": "Hello Odoo Discussions 4",
            "courses": courses
        }
        return request.render('od_openacademy_website.odoodiscussions_classes4', values)
    
    @http.route('/odoodiscussions/classes5', auth='public', website=True)
    def odoodiscussions_classes(self, **kwargs):
        courses = request.env['od_openacademy.course'].search([])
        values = {
            "message": "Hello Odoo Discussions 5",
            "courses": courses
        }
        return request.render('od_openacademy_website.odoodiscussions_classes5', values)
    
    @http.route('/odoodiscussions/<string:name>', auth='public', website=True, type='http')  
    def display_name(self, name):
        return "This is Odoo Discussions with Name: %s" % name
    
    @http.route('/odoodiscussions/<int:my_id>', auth='public', website=True, type='http')  
    def display_id(self, my_id):
        return "This is Odoo Discussions with ID: %s" % my_id

    @http.route('/odoodiscussions/classes7', auth='public', website=True, type='http')
    def odoodiscussions_classes(self, **kwargs):
        courses = request.env['od_openacademy.course'].sudo().search([])
        values = {
            "message": "Hello Odoo Discussions 5",
            "courses": courses
        }
        return request.render('od_openacademy_website.odoodiscussions_classes7', values)

    @http.route("/odoodiscussions/<model('od_openacademy.course'):course>", 
                auth='public', website=True, type='http')
    def display_name(self, course):
        template = "od_openacademy_website.odoodiscussions_courses"
        return request.render(template, {'course': course})
    
    
class CustomerPortalDiscussions(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values['course_count'] = request.env['od_openacademy.course'].search_count([])
        return values