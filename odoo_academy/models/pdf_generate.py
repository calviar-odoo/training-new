# -*- coding:utf-8 -*-
from odoo import models,fields,api
class AccountMovePdf(models.Model):
    _inherit = 'account.move'
    pdf_invoice = fields.Binary(string = 'PDF', required = True, default=lambda self: self.action_invoice_print()) # Llamamos a la función pdf_generator

    @api.model
    
    
    def action_get_attachment(self):
        pdf = self.env.ref('account.move..report_id').render_qweb_pdf(self.ids)
        b64_pdf = base64.b64encode(pdf[0])
        # save pdf as attachment
        name = "My Attachment"
        return self.env['ir.attachment'].create({
            'name': name,
            'type': 'binary',
            'datas': b64_pdf,
            'datas_fname': name + '.pdf',
            'store_fname': name,
            'res_model': self._name,
            'res_id': self.id,
            'mimetype': 'application/x-pdf'
        })
    
    
    def action_invoice_print(self):
        invoices = self.env['account.move'].search([('move_type', '=', 'out_invoice')])
        for invoice in invoices:
            self.pdf_invoice = self.env.ref('account.account_invoices_without_payment').report_action(self)
            
            
   