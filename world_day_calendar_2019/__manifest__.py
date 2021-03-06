# -*- coding: utf-8 -*-
# Copyright 2019 Demodoo IT Solutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "World Day Calendar 2019",
    'version': '11.0.1.0.0',
    'summary': """This module loads the World Day calendar 2019 into the calendar.event model. It uses our calendar_event_base module.""",
    'category': 'Extra Tools',
    'author': 'Demodoo IT Solutions',
    'website': "https://demodoo.blogspot.com",
    'depends': [
        'calendar_event_base',
    ],
    'data': [
        'data/world_day_type.xml',
        'data/world_day_calendar.xml',
    ],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
}
