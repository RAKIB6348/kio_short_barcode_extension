# -*- coding: utf-8 -*-
# from odoo import http


# class KioShortBarcodeExtension(http.Controller):
#     @http.route('/kio_short_barcode_extension/kio_short_barcode_extension', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kio_short_barcode_extension/kio_short_barcode_extension/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kio_short_barcode_extension.listing', {
#             'root': '/kio_short_barcode_extension/kio_short_barcode_extension',
#             'objects': http.request.env['kio_short_barcode_extension.kio_short_barcode_extension'].search([]),
#         })

#     @http.route('/kio_short_barcode_extension/kio_short_barcode_extension/objects/<model("kio_short_barcode_extension.kio_short_barcode_extension"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kio_short_barcode_extension.object', {
#             'object': obj
#         })

