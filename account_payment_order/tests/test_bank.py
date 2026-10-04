# © 2017 Creu Blanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.exceptions import ValidationError

from odoo.addons.base.tests.common import BaseCommon


class TestBank(BaseCommon):
    _test_user_groups = ("base.group_partner_manager",)

    def test_bank(self):
        partner_bank = self.env["res.partner.bank"].create(
            {
                "account_number": "FR66 1212 1212 1212 1212 1212 121",
                "bank_name": "Fiducial Banque",
                "bank_bic": "FIDCFR21XXX",
                "partner_id": self.partner.id,
            }
        )
        with self.assertRaises(ValidationError):
            partner_bank.bank_bic = "TEST"
