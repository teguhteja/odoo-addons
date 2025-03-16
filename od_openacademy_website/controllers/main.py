from odoo import http
from odoo.http import request

class OdooDiscussions(http.Controller):

    @http.route('/odoodiscussions/courses', auth='public', website=True)
    def display_data(self, **kwargs):
        return "<h1>This is Odoo Discussions<h1>"
    
    @http.route('/odoodiscussions/sessions', auth='public', website=True)
    def display_sessions(self, **kwargs):
        return "This is Odoo Discussions Sessions"
    
    @http.route('/odoodiscussions/classes', auth='public', website=True)
    def display_classes(self, **kwargs):
        template = 'od_openacademy_website.odoodiscussions_classes'
        return request.render(template)
