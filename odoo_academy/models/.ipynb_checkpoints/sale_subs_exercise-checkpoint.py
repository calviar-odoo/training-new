# -*- coding:utf-8 -*-
import logging
import datetime
import traceback

from ast import literal_eval
from collections import Counter
from dateutil.relativedelta import relativedelta
from uuid import uuid4

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression
from odoo.tools import format_date, float_compare
from odoo.tools.float_utils import float_is_zero

INTERVAL_FACTOR = {
    'daily': 30.0,
    'weekly': 30.0 / 7.0,
    'monthly': 1.0,
    'yearly': 1.0 / 12.0,
}

PERIODS = {'daily': 'days', 'weekly': 'weeks', 'monthly': 'months', 'yearly': 'years'}    

class SubsExercise(models.Model):
    _inherit = 'sale.subscription'
    
    def _prepare_invoice_extra_line(self, fiscal_position, date_start=False, date_stop=False):
        #company = self.env.company or line.analytic_account_id.company_id
        #tax_ids = line.product_id.taxes_id.filtered(lambda t: t.company_id == company)
        #price_unit = line.price_unit
        #if fiscal_position and tax_ids:
            #tax_ids = self.env['account.fiscal.position'].browse(fiscal_position).map_tax(tax_ids)
            #price_unit = self.env['account.tax']._fix_tax_included_price_company(line.price_unit, line.product_id.taxes_id, tax_ids, self.company_id)
        return {
            'name': 'NuevoProducto',
            'subscription_id': 10,
            'price_unit': 10,
            'discount': 10,
            'quantity': 10,
            'product_uom_id': 10,
            'product_id': 10,
            'tax_ids': [(6, 0, 1)],
            'analytic_account_id': 10,
            'analytic_tag_ids': [(6, 0, 1)],
            'subscription_start_date': date_start,
            'subscription_end_date': date_stop,
        }
    
    def _prepare_invoice_lines(self, fiscal_position):
        self.ensure_one()
        revenue_date_start = self.recurring_next_date
        revenue_date_stop = revenue_date_start + relativedelta(**{PERIODS[self.recurring_rule_type]: self.recurring_interval}) - relativedelta(days=1)
        return [((0, 0, self._prepare_invoice_extra_line(fiscal_position, revenue_date_start, revenue_date_stop))),
            ((0, 0, self._prepare_invoice_line(line, fiscal_position, revenue_date_start, revenue_date_stop)) for line in self.recurring_invoice_line_ids)]
    
  #  (0, 0, self._prepare_invoice_extra_line(line, fiscal_position, revenue_date_start, revenue_date_stop)),


#return [(0, 0, self._prepare_invoice_line(line, fiscal_position, revenue_date_start, revenue_date_stop)) for line in self.recurring_invoice_line_ids]