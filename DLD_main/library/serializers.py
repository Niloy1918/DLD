from dataclasses import fields
from rest_framework import serializers
from library.models import Accounts


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['email', 'username', 'password', 'password2']

