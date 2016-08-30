# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Author: Naresh Soni
#    Copyright 2015 Cozy Business Solutions Pvt.Ltd
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'ADR Scripts',
    'version' : '1.0',
    'category': 'General',
    'author': 'Ernesto Mendez',
    'website': 'https://www.nowebsitefornow.com',
    'description': '''
    ''',
    'depends' : ['base', 'account'],
    'data' : [
        # 'adr_script.xml',
        'adr_script_cron.xml',
        #'views/report_invoice_extra.xml',
    ],
    'installable': True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: