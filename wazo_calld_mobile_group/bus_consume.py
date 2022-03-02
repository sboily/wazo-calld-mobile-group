# -*- coding: utf-8 -*-
# Copyright 2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging


logger = logging.getLogger(__name__)


class WP465BusEventHandler(object):

    def __init__(self, service, bus_consumer):
        self.services = service
        self.bus_consumer = bus_consumer

    def subscribe(self, bus_consumer):
        self._on_auth_event('auth_session_created', self._enable_devstate)
        self._on_auth_event('auth_session_delete', self._disable_devstate)

    def _on_auth_event(self, event_type, callback):
        logger.debug('Added callback on auth event "%s"', event_type)
        self.bus_consumer._queue.bindings.add(binding(self.bus_consumer._exchange, routing_key='auth.{}'.format(event_type)))
        self.bus_consumer._events_pubsub.subscribe(event_type, callback)

    def _enable_devstate(self, event):
            state = self.services.enable_devstate(uuid)

    def _disable_devstate(self, event):
            state = self.services.disable_devstate(uuid)
