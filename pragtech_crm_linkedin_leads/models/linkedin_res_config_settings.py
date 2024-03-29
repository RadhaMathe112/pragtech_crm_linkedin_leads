# coding: utf-8

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    linkedin_own_account = fields.Boolean("Linkedin Account",
                                          config_parameter='pragtech_crm_linkedin_leads.linkedin_own_account')
    linkedin_client_id = fields.Char("Linkedin App ID",
                            compute='_compute_linkedin_client_id', inverse='_inverse_likedin_app_id')
    linkedin_client_secret = fields.Char("Linkedin App Secret",
                                   compute='_compute_linkedin_client_secret', inverse='_inverse_linkedin_client_secret')

    @api.onchange('linkedin_own_account')
    def _onchange_linkedin_own_account(self):
        if not self.linkedin_own_account:
            self.linkedin_client_id = False
            self.linkedin_client_secret = False

    @api.depends('linkedin_own_account')
    def _compute_linkedin_client_id(self):
        for record in self:
            if self.env.user.has_group('odoo_lead_forms_ad_integration_hub_crm.group_social_manager'):
                record.instagram_app_id = self.env['ir.config_parameter'].sudo().get_param(
                    'pragtech_crm_linkedin_leads.linkedin_client_id')
            else:
                record.linkedin_client_id = None

    def _inverse_likedin_app_id(self):
        for record in self:
            if self.env.user.has_group('odoo_lead_forms_ad_integration_hub_crm.group_social_manager'):
                self.env['ir.config_parameter'].sudo().set_param('pragtech_crm_linkedin_leads.linkedin_client_id',
                                                                 record.linkedin_client_id)

    @api.depends('linkedin_own_account')
    def _compute_linkedin_client_secret(self):
        for record in self:
            if self.env.user.has_group('odoo_lead_forms_ad_integration_hub_crm.group_social_manager'):
                record.instagram_client_secret = self.env['ir.config_parameter'].sudo().get_param(
                    'pragtech_crm_linkedin_leads.linkedin_client_secret')
            else:
                record.linkedin_client_secret = None

    def _inverse_linkedin_client_secret(self):
        for record in self:
            if self.env.user.has_group('odoo_lead_forms_ad_integration_hub_crm.group_social_manager'):
                self.env['ir.config_parameter'].sudo().set_param('pragtech_crm_linkedin_leads.linkedin_client_secret',
                                                                 record.linkedin_client_secret)
