# -*- coding: utf-8 -*-

import requests

from odoo import _, models, fields
from odoo.exceptions import UserError
from werkzeug.urls import url_encode, url_join


class SocialMediaLinkedin(models.Model):
    _name = 'linkedin.pragtech.social.media'
    _description = 'Linkedin Social Pages'
    _rec_name = 'linkedin_media_name'

    # _INSTA_ENDPOINT = 'https://graph.facebook.com'

    linkedin_media_name = fields.Char('Name', readonly=True, required=True, translate=True)
    linkedin_media_description = fields.Char('Description', readonly=True)
    linkedin_media_image = fields.Binary('Image', readonly=True)
    # media_account_ids = fields.One2many('linkedin.pragtech.social.account', 'linkedin_social_media_id',
                                        # string="Linkedin Accounts")
    likedin_media_link_accounts = fields.Boolean('link Your accounts ?', default=True, readonly=True, required=True, )
    linkedin_media_type = fields.Selection([('linkedin', 'Linkedin')], string='Media Type', required=True,
                                        default='linkedin')

    def pragtech_action_linkedin_add_account(self):
        self.ensure_one()
        # print("pragtech_action_add_account=============",self)

        linkedin_client_id = self.env['ir.config_parameter'].sudo().get_param(
            'pragtech_crm_linkedin_leads.linkedin_client_id')
        linkedin_client_secret = self.env['ir.config_parameter'].sudo().get_param(
            'pragtech_crm_linkedin_leads.linkedin_client_secret')
        if linkedin_client_id and linkedin_client_secret:
            return self._add_linkedin_accounts_from_configuration(linkedin_client_id)
        else:
            raise UserError(_(" You are Missing App ID and App Secret."))

    def _add_linkedin_accounts_from_configuration(self, linkedin_client_id):
        get_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        split_base_url = get_base_url.split(':')[0]
        if split_base_url == 'http':
            get_base_url = get_base_url.replace("http", "https")
        else:
            pass
        get_base_linkedin_url = 'https://www.linkedin.com/oauth/v2/authorization%s'
        get_params = {
            'client_id': linkedin_client_id,
            'redirect_uri': url_join(get_base_url, "/social_linkedin_leads/callback"),
            'response_type': 'token',
            'scope': ','.join([
                # 'instagram_basic',
                'rw_ads',
                'r_basicprofile',
                'w_organization_social',
                'w_member_social',
            ])
        }
        return {
            'type': 'ir.actions.act_url',
            'url': get_base_linkedin_url % url_encode(get_params),
            'target': 'new'
        }
