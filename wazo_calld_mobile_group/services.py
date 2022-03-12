# Copyright 2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import logging

logger = logging.getLogger(__name__)


class WP465Service():

    def __init__(self, amid):
        self.amid = amid

    def enable_devstate(self, uuid):
        self.amid.action('setVar', {
            'Variable': f"DEVICE_STATE(Custom:{uuid})",
            'Value': 'NOT_INUSE'
        })

    def disable_devstate(self, uuid):
        endpoint = self._get_endpoint(uuid)
        self.amid.action('setVar', {
            'Variable': f"DEVICE_STATE(Custom:{uuid})",
            'Value': 'UNAVAILABLE'
        })
