# -*- coding: utf-8 -*-
###############################################################################
#
#    BroadTech IT Solutions Pvt Ltd
#    Copyright (C) 2018 BroadTech IT Solutions Pvt Ltd 
#    (<http://broadtech-innovations.com>).
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################


{
    'name': 'Clinica Doctor Datas',
    'version': '1.42',
    'license': 'Other proprietary',
    'category': 'custom',
    'description': """
     Clinica Doctor Datas
    """,
    'author' : 'BroadTech IT Solutions Pvt Ltd',
    'website' : 'http://www.broadtech-innovations.com',
    'depends': [
        'base','contacts','l10n_co_res_partner','product', 'l10n_co_tax_extension','account'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/doctor_sequence.xml',
        'data/doctor_surgical_technologist_element.xml',
        'wizard/create_health_professional_view.xml',
        'report/clinica_visualizer_report_template.xml',
        'report/clinica_visualizer_report.xml',
        'views/doctor_details_view.xml',
        'views/clinica_text_template_view.xml',
        'views/res_partner_view.xml',
        'views/doctor_product_view.xml',
        'views/doctor_attentions_view.xml',
        'views/quirurgic_sheet_view.xml',
        'views/nurse_sheet_view.xml',
        'views/doctor_calendar_view.xml',
        'views/anhestesic_registry_view.xml',
        'views/post_anhestesic_care_view.xml',
        'views/plastic_surgery_sheet_view.xml',
        'views/medical_evolution_view.xml',
        'views/doctor_epicrisis_view.xml',
        'views/quirurgical_check_list_view.xml',
        'views/clinica_record_list_visualizer_view.xml',
        'views/account_invoice_view.xml',
        'views/doctor_surgical_technologist.xml'
    ],
    'demo': [
    ],
    'test': [
    ],
    "external_dependencies": { # python pip packages
    #     'python': ['suds', 'dateutil'],
    },
    'installable': True,
    'auto_install': False,
 }


# vim:expandtab:smartindent:tabstop=2:softtabstop=2:shiftwidth=2: