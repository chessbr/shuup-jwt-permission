# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.transaction import atomic

from shuup.admin.form_part import FormPartsViewMixin, SaveFormPartsMixin
from shuup.admin.utils.views import CreateOrUpdateView
from shuup_jwt_permission.admin_module.forms import APIApplicationFormPart, APIApplicationPermissionFormPart
from shuup_jwt_permission.models import APIApplication


class APIApplicationEditView(SaveFormPartsMixin, FormPartsViewMixin, CreateOrUpdateView):
    model = APIApplication
    context_object_name = "api_application"
    template_name = "shuup_jwt_permission/admin/edit.jinja"
    base_form_part_classes = [
        APIApplicationFormPart,
        APIApplicationPermissionFormPart
    ]

    @atomic
    def form_valid(self, form):
        return self.save_form_parts(form)
