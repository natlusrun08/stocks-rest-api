from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
import pandas as pd
import yfinance as yf

class InstitutionalHoldersAPIView(APIView):
    def get(self, request, symbol):
        holders = InstitutionalHolder.objects.filter(symbol=symbol)
        serializer = InstitutionalHolderSerializer(holders, many=True)
        return Response(serializer.data)

