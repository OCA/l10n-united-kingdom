.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================
l10n_uk_sale_report
===================

Odoo module to introduce UK format on reports, that can fit in standard window envelopes in the UK.

Installation
============

To install this module, you need to:
* Clone it to your addons directory
* Restart Odoo service

Configuration
=============

No configuration needed

Usage
=====

Sales Orders
* From print drop down menu, option available to print the sales order in UK format
* *Print* button defaults to UK format on printing

Invoices
* From print drop down menu, option available to print the sales order in UK format
* *Print* button defaults to UK format on printing

Customers
* From print drop down menu, option available to print account statements in UK format.

Known issues / Roadmap
======================

TODO: *Send by Email* button needs to default to UK format.
Manual Workaround -> Technical features flag on for your user. Refresh and go to *Settings > Technical > Emails > Templates*. Open up *Sales Order - Send by Email*, edit. Go to *Advanced Settings* tab and choose *Sales Order (UK format)* from the list of options on *Optional report to print and attach*.


TODO: *Send by Email* button needs to default to UK format.
Manual Workaround -> Technical features flag on for your user. Refresh and go to *Settings > Technical > Emails > Templates*. Open up *Invoice - Send by Email*, edit. Go to *Advanced Settings* tab and choose *Invoice (UK format)* from the list of options on *Optional report to print and attach*.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/{l10n-united-kingdom}/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/{l10n-united-kingdom}/issues/new?body=module:%20{l10n_uk_sale_report}%Aversion:%20{1.0}%0A%0A**Steps%20to%reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
=======

Contributors
------------

* Nuria Arranz-Velazquez <nuria@opusvl.com>
* Colin Newell <colin@opusvl.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
