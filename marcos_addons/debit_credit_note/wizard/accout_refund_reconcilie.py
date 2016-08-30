# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013-2015 Marcos Organizador de Negocios SRL http://marcos.do
#    Write by Eneldo Serrata (eneldo@marcos.do)
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
#
##############################################################################
from openerp import models, api, fields


class PrintLabel(models.TransientModel):
    _name = "marcos.credit.apply"

    invoice_ids = fields.Many2one("account.invoice", "Facturas pedientes", required=True)
    # date_invoice = fields.Datetime(related="invoice_ids.date_invoice", string="Fecha")
    partner_id = fields.Many2one(related="invoice_ids.partner_id", string="A nombre de:")
    amount_total = fields.Float(related="invoice_ids.amount_total", string="Facturado")
    residual = fields.Float(related="invoice_ids.residual", string="Balance")

    # @api.one
    # def apply_credit(self):
    #     pass