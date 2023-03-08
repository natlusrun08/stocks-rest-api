from django.shortcuts import render

# Create your views here.
from rest_framework import views
from rest_framework.response import Response
import pandas as pd
import yfinance as yf

class InstitutionalHoldersAPIView(views.APIView):
    def get(self, request, ticker):
        apple = yf.Ticker(ticker)
        holders = apple.get_institutional_holders()
        df = pd.DataFrame(holders)
        return Response(df.to_dict())
