# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pragtech_crm_linkedin_leads(models.Model):
#     _name = 'pragtech_crm_linkedin_leads.pragtech_crm_linkedin_leads'
#     _description = 'pragtech_crm_linkedin_leads.pragtech_crm_linkedin_leads'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

