# -*- coding: utf-8 -*-
import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = "shuup_jwt_permission"
    provides = {
        "admin_module": [
            "shuup_jwt_permission.admin_module:APIApplicationAccessAdminModule"
        ]
    }
