from django.shortcuts import render
from library.models import Accounts
from rest_framework import generics
from library.serializers import AccountsSerializer
# Create your views here.
class AccountsList(generics.ListCreateAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

class AccountsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accounts
    serializer_class = AccountsSerializer