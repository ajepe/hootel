# Copyright 2018 Alexandre Díaz <dev@redneboa.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Hotel Channel Connector',
    'version': '1.0',
    'author': "Alexandre Díaz <dev@redneboa.es>",
    'website': 'https://www.eiqui.com',
    'category': 'hotel/connector',
    'summary': "Hotel Channel Connector Base",
    'description': "Hotel Channel Connector Base",
    'depends': [
        'hotel',
        'connector',
    ],
    'external_dependencies': {
        'python': ['xmlrpc']
    },
    'data': [
        'data/cron_jobs.xml',
        'wizard/wubook_installer.xml',
        'wizard/wubook_import_plan_prices.xml',
        'wizard/wubook_import_plan_restrictions.xml',
        'wizard/wubook_import_availability.xml',
        'views/general.xml',
        'views/res_config_views.xml',
        'views/inherited_hotel_reservation_views.xml',
        'views/inherited_hotel_virtual_room_views.xml',
        'views/inherited_hotel_virtual_room_availability_views.xml',
        'views/inherited_hotel_folio_views.xml',
        'views/inherited_product_pricelist_views.xml',
        'views/inherited_product_pricelist_item_views.xml',
        'views/inherited_reservation_restriction_views.xml',
        'views/inherited_reservation_restriction_item_views.xml',
        'views/inherited_res_partner_views.xml',
        'views/wubook_channel_info_views.xml',
        'views/wubook_issue_views.xml',
        'data/menus.xml',
        'data/sequences.xml',
        'security/ir.model.access.csv',
        'security/wubook_security.xml',
        # 'views/res_config.xml'
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}