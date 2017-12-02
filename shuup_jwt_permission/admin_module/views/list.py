# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from shuup.admin.utils.picotable import Column, TextFilter
from shuup.admin.utils.views import PicotableListView
from shuup_jwt_permission.models import APIApplication


class APIApplicationListView(PicotableListView):
    model = APIApplication
    default_columns = [
        Column(
            "name",
            _("Name"),
            sort_field="name",
            display="name",
            filter_config=TextFilter(
                filter_field="name",
                placeholder=_("Filter by name...")
            )
        ),
        Column("enabled", _("Enabled"))
    ]
