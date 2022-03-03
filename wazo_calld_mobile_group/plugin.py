# Copyright 2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_amid_client import Client as AmidClient

from .services import WP465Service
from .bus_consume import WP465BusEventHandler


class Plugin():

    def load(self, dependencies):
        config = dependencies['config']
        token_changed_subscribe = dependencies['token_changed_subscribe']
        bus_consumer = dependencies['bus_consumer']

        amid_client = AmidClient(**config['amid'])
        token_changed_subscribe(amid_client.set_token)
        wp465_service = WP465Service(amid_client)

        wp465_bus_event_handler = WP465BusEventHandler(wp465_service, bus_consumer)
        wp465_bus_event_handler.subscribe()
