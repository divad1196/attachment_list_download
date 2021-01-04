# -*- coding: utf-8 -*-

from odoo import models

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    def action_download_zip(self):
        """
            you can return an attachment to download from any action by returning this function call
            def somefunction(self):
                ...
                return attachment_ids.action_download_zip()
        """
        if len(self) == 1:
            return {
                'type': 'ir.actions.act_url',
                'target': 'self',
                'url': "/web/content/{id}?download=true".format(
                    id=self.id,
                ),
            }
        if self:
            return {
                'type': 'ir.actions.act_url',
                'target': 'self',
                'url': "/document/zip?zip_name={zip_name}&file_ids={ids}".format(
                    zip_name="attachments.zip",
                    ids=",".join(str(id) for id in self.ids),
                ),
            }
