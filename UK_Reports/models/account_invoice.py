# -*- coding: utf-8 -*-

##############################################################################
#
# UK Report Template
# Copyright (C) 2015 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api

class uk_report_account_invoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def invoice_print(self):
        """ Print the invoice and mark it as sent, so that we can see more
            easily the next step of the workflow
        """
	self.sent = True
        self.ensure_one()
        return self.env['report'].get_action(self, 'account.UK_Invoice')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
