# -*- coding: utf-8 -*-
# from odoo import http


# class PragtechCrmLinkedinLeads(http.Controller):
#     @http.route('/pragtech_crm_linkedin_leads/pragtech_crm_linkedin_leads', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pragtech_crm_linkedin_leads/pragtech_crm_linkedin_leads/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pragtech_crm_linkedin_leads.listing', {
#             'root': '/pragtech_crm_linkedin_leads/pragtech_crm_linkedin_leads',
#             'objects': http.request.env['pragtech_crm_linkedin_leads.pragtech_crm_linkedin_leads'].search([]),
#         })

#     @http.route('/pragtech_crm_linkedin_leads/pragtech_crm_linkedin_leads/objects/<model("pragtech_crm_linkedin_leads.pragtech_crm_linkedin_leads"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pragtech_crm_linkedin_leads.object', {
#             'object': obj
#         })

