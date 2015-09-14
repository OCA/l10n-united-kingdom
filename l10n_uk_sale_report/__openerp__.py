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



{
   'name': 'UK customised reports',
   'version': '8.0.1.0.0',
   'category': 'Reporting',
   'description': """
   Customised reports for UK:
    - Sales order / Quotation
    - Account balance / overdue
    - Invoice print 

    These have been migrated from V3.3, V4, V5, V6, V6.1 to V8

   """,
   'author': ['OpusVL', 'Odoo Community Association (OCA)'],
   'website': 'http://opusvl.com',
   'depends': ['account_accountant', 'sale', 'report'],
   'data': [
       'views/reports.xml',
   ],
   'license': 'AGPL-3',
   'installable': True,
   'active': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
