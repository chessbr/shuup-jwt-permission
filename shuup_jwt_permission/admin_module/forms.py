# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.models import ModelForm
from django.utils.translation import gettext_lazy as _

from shuup.admin.form_part import FormPart, TemplatedFormDef
from shuup_jwt_permission.models import APIApplication, APIApplicationPermission
from rest_jwt_permission.scopes import get_all_permission_providers_scopes, APIScope


class APIApplicationForm(ModelForm):
    class Meta:
        model = APIApplication
        exclude = ("identifier",)

    def __init__(self, *args, **kwargs):
        super(APIApplicationForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields["key"] = forms.CharField(
                initial=self.instance.key,
                help_text=_("Auto generated"),
                required=False,
                widget=forms.TextInput(
                    attrs={
                        "readonly": "readonly",
                        "placeholder": _("Auto generated key")
                    }
                )
            )


class APIApplicationFormPart(FormPart):
    priority = -1000  # Show this first, no matter what

    def get_form_defs(self):
        yield TemplatedFormDef(
            "base",
            APIApplicationForm,
            template_name="shuup_jwt_permission/admin/edit_base.jinja",
            required=True,
            kwargs={"instance": self.object}
        )

    def form_valid(self, form_group):
        self.object = form_group["base"].save()
        return self.object



class ApplicationPermissionForm(forms.Form):
    api_view_prefix = "apiview__"

    def __init__(self, *args, **kwargs):
        super(ApplicationPermissionForm, self).__init__(*args, **kwargs)
        scopes = get_all_permission_providers_scopes()

        api_scopes = {}

        # group api endpoint scopes for now
        for scope in scopes:
            if isinstance(scope, APIScope):
                if not scope.view_class.__name__ in api_scopes:
                    api_scopes[scope.view_class.__name__] = []
                api_scopes[scope.view_class.__name__].append(scope)
            else:
                self.fields[scope.identifier] = forms.BooleanField(
                    required=False,
                    label=scope.get_description(),
                    help_text=str(scope),
                )

        # now add fields for api endpoints
        for viewset, scopes in api_scopes.items():
            choices = [
                (scope.identifier, "{}: {}".format(scope.method.upper(), scope.path)) for scope in scopes
            ]
            self.fields["{}{}".format(self.api_view_prefix, viewset)] = forms.MultipleChoiceField(
                required=False,
                label=viewset,
                help_text="Module: {}".format(scopes[0].view_class.__module__),
                choices=choices
            )


class APIApplicationPermissionFormPart(FormPart):
    priority = 1

    def get_form_defs(self):
        yield TemplatedFormDef(
            "permissions",
            ApplicationPermissionForm,
            template_name="shuup_jwt_permission/admin/edit_permissions.jinja",
            required=True
        )

    def form_valid(self, form_group):
        form_group["permissions"].save()
        return self.object
