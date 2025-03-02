from django.utils.translation import gettext as _

from extras.forms import CustomFieldModelFilterForm
from tenancy.models import *
from tenancy.forms import ContactModelFilterForm
from utilities.forms import DynamicModelMultipleChoiceField, TagFilterField

__all__ = (
    'ContactFilterForm',
    'ContactGroupFilterForm',
    'ContactRoleFilterForm',
    'TenantFilterForm',
    'TenantGroupFilterForm',
)


#
# Tenants
#

class TenantGroupFilterForm(CustomFieldModelFilterForm):
    model = TenantGroup
    parent_id = DynamicModelMultipleChoiceField(
        queryset=TenantGroup.objects.all(),
        required=False,
        label=_('Parent group')
    )
    tag = TagFilterField(model)


class TenantFilterForm(ContactModelFilterForm, CustomFieldModelFilterForm):
    model = Tenant
    field_groups = (
        ('q', 'tag'),
        ('group_id',),
        ('contact', 'contact_role')
    )
    group_id = DynamicModelMultipleChoiceField(
        queryset=TenantGroup.objects.all(),
        required=False,
        null_option='None',
        label=_('Group')
    )
    tag = TagFilterField(model)


#
# Contacts
#

class ContactGroupFilterForm(CustomFieldModelFilterForm):
    model = ContactGroup
    parent_id = DynamicModelMultipleChoiceField(
        queryset=ContactGroup.objects.all(),
        required=False,
        label=_('Parent group')
    )
    tag = TagFilterField(model)


class ContactRoleFilterForm(CustomFieldModelFilterForm):
    model = ContactRole
    tag = TagFilterField(model)


class ContactFilterForm(CustomFieldModelFilterForm):
    model = Contact
    field_groups = (
        ('q', 'tag'),
        ('group_id',),
    )
    group_id = DynamicModelMultipleChoiceField(
        queryset=ContactGroup.objects.all(),
        required=False,
        null_option='None',
        label=_('Group')
    )
    tag = TagFilterField(model)
