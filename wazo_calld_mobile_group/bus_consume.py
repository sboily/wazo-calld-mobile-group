# Copyright 2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import logging

from kombu import binding


logger = logging.getLogger(__name__)


class WP465BusEventHandler():

    def __init__(self, service, bus_consumer):
        self.services = service
        self.bus_consumer = bus_consumer

    def subscribe(self):
        self._on_auth_event('auth_session_created', 'auth.sessions.*.created', self._enable_devstate)
        self._on_auth_event('auth_session_deleted', 'auth.sessions.*.deleted', self._disable_devstate)

    def _on_auth_event(self, event_type, routing_key, callback):
        logger.debug('Added callback on auth event "%s"', event_type)
        self.bus_consumer._queue.bindings.add(binding(self.bus_consumer._exchange, routing_key=routing_key))
        self.bus_consumer._events_pubsub.subscribe(event_type, callback)

    def _enable_devstate(self, event):
        if event['mobile']:
            self.services.enable_devstate(event['user_uuid'])

    def _disable_devstate(self, event):
        # Need a fix to know if the session deleted if mobile or not.
        state = self.services.disable_devstate(event['user_uuid'])
