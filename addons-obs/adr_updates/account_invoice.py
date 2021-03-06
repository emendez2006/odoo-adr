# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
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
# dd
##############################################################################

from openerp.osv import fields, osv, expression, orm

class account_invoice(osv.osv):

    _inherit = "account.invoice"

    _columns = {
        #'internal_sequence_number': fields.related('move_id', 'internal_sequence_number', type='char', readonly=True, size=64, relation='account.move', store=True, string='Numero de Factura'),
        'external_source': fields.boolean('Fuente externa'),
        'external_source_state': fields.selection([('draft', 'Borrador'), ('closed', 'Cerrada')],
                                                  "Estado fuente externa"),
        'processed': fields.boolean('Procesada?'),
        'payment_journal_id': fields.many2one('account.journal', 'Metodo de pago externo'),

	}

account_invoice()
