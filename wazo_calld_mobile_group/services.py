# Copyright 2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import logging

logger = logging.getLogger(__name__)


class WP465Service():

    def __init__(self, amid):
        self.amid = amid

    def enable_devstate(self, uuid):
        endpoint = self._get_endpoint(uuid)
        self.amid.action('DialplanExtensionAdd', {
            'Context': 'usersharedlines',
            'Priority': 'hint',
            'Extension': uuid,
            'Application': f"Custom:{uuid}&{endpoint}",
            'Replace': 'yes'
        })

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

    def _get_endpoint(self, uuid):
        endpoint = self.amid.action('ExtensionState', {
            'Context': 'usersharedlines',
            'Exten': uuid,
        })

        interfaces = endpoint[0]['Hint'].split('pjsip')
        return "&".join([match for match in interfaces if "pjsip" in match])
