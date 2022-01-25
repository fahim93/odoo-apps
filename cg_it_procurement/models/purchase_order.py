# -*- coding: utf-8 -*-

from odoo import models, fields, api
from num2words import num2words


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    subject = fields.Char('Subject')

    def amount_in_word(self):
        print(num2words(self.amount_total))
        return num2words(self.amount_total)