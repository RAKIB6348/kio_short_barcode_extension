# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    kio_short_barcode = fields.Char(
        string='Barcode',
        compute='_compute_kio_short_barcode',
        store=True,
        readonly=True,
    )

    @api.depends('barcode')
    def _compute_kio_short_barcode(self):
        for product in self:
            barcode = product.barcode or ''
            product.kio_short_barcode = barcode[-7:] if barcode else ''


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    kio_short_barcode = fields.Char(
        string='Barcode',
        related='product_id.kio_short_barcode',
        readonly=True,
    )

