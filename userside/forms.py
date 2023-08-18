
from django import forms

from userside.models import UserCart


class UserCartForm(forms.Form):
     class Meta:
        models= UserCart
        fields= "__all__"
