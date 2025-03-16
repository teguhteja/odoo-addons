from odoo import http

class OdooDiscussions(http.Controller):

    @http.route('/odoodiscussions/courses', auth='public', website=True)
    def display_data(self, **kwargs):
        return "<h1>This is Odoo Discussions<h1>"
    
    @http.route('/odoodiscussions/sessions', auth='public', website=True)
    def display_sessions(self, **kwargs):
        return "This is Odoo Discussions Sessions"