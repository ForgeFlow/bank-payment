from odoo import models


class BankPaymentLine(models.Model):
    _inherit = "bank.payment.line"

    def _is_missing_bank_account(self):
        self.ensure_one()
        return not self.partner_bank_id
