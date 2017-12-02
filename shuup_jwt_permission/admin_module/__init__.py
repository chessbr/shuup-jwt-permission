# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from shuup.admin.base import AdminModule, MenuEntry
from shuup.admin.menu import SETTINGS_MENU_CATEGORY
from shuup.admin.utils.permissions import (
    get_default_model_permissions,
    get_permissions_from_urls
)
from shuup.admin.utils.urls import derive_model_url, get_edit_and_list_urls
from shuup_jwt_permission.models import APIApplication


class APIApplicationAccessAdminModule(AdminModule):
    name = _("API Application Access")
    breadcrumbs_menu_entry = MenuEntry(name, url="shuup_admin:api_application.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^api_application",
            view_template="shuup_jwt_permission.admin_module.views.APIApplication%sView",
            name_template="api_application.%s",
            permissions=get_default_model_permissions(APIApplication)
        )

    def get_menu_category_icons(self):
        return {self.name: "fa fa-server"}

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("API Applications"), icon="fa fa-server",
                url="shuup_admin:api_application.list",
                category=SETTINGS_MENU_CATEGORY,
                subcategory="other_settings",
                ordering=10,
                aliases=[_("Show API Applications")]
            )
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(APIApplication)

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(APIApplication, "shuup_admin:api_application", object, kind)
