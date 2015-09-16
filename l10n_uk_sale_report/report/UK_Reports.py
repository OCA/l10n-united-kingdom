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


## Sales order
from openerp.report import report_sxw
import time
 
class order(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(order, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
        })
 
report_sxw.report_sxw(
	'report.sale.UK_SalesOrder.2', 
	'sale.order', 
    'addons/l10n_uk_sale_report/report/UK_sale_print_order.rml', 
	parser=order, header="external"
)

## Invoice
from openerp.report import report_sxw

class account_invoice(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(account_invoice, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
        })

report_sxw.report_sxw(
    'report.account.UK_Invoice.2',
    'account.invoice',
    'addons/l10n_uk_sale_report/report/UK_account_print_invoice.rml',
    parser=account_invoice
)

## Statement
from openerp.report import report_sxw

class Overdue(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(Overdue, self).__init__(cr, uid, name, context=context)
        self.localcontext.update( {
            'time': time,
            'adr_get': self._adr_get,
            'getLines': self._lines_get,
            'tel_get': self._tel_get,
            'message': self._message,
        })
        self.context = context
    def _adr_get(self, partner, type):
        res = []
        result = {
                  'name': partner.name,
                  'street': partner.street,
                  'street2': partner.street2,
                  'city': partner.city,
                  'zip': partner.zip,
                  'state_id': partner.state_id and partner.state_id.name or '',
                  'country_id': partner.country_id and partner.country_id.name or '',
                 }
        res.append(result)
        return res

    def _tel_get(self,partner):
        if not partner:
            return False
        res_partner = self.pool['res.partner']
        addresses = res_partner.address_get(self.cr, self.uid, [partner.id], ['invoice'])
        adr_id = addresses and addresses['invoice'] or False
        if adr_id:
            adr=res_partner.read(self.cr, self.uid, [adr_id])[0]
            return adr['phone']
        else:
            return partner.phone or False
        return False

    def _lines_get(self, partner):
        moveline_obj = self.pool['account.move.line']
        movelines = moveline_obj.search(self.cr, self.uid,
                [('partner_id', '=', partner.id),
                    ('account_id.type', 'in', ['receivable', 'payable']),
                    ('state', '<>', 'draft'), ('reconcile_id', '=', False)])
        movelines = moveline_obj.browse(self.cr, self.uid, movelines)
        return movelines

    def _message(self, obj, company):
        company_pool = self.pool['res.company']
        message = company_pool.browse(self.cr, self.uid, company.id, {'lang':obj.lang}).overdue_msg
        return message

report_sxw.report_sxw(
    'report.account.UK_Statement.2', 
    'res.partner',
    'addons/l10n_uk_sale_report/report/UK_account_print_overdue.rml', 
    parser=Overdue
)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
