import requests
from django.shortcuts import redirect, render
import urllib
from .models import Stockrankings
import FinanceDatabase as fd
from yfinance.utils import get_json
from yfinance import download
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
# def stockdb():
#     # symbolname list화
#     stocks = fd.select_equities(
#         country='United States', industry='Advertising Agencies')
#     for symbol in stocks:
#         fundamental = get_json( "https://finance.yahoo.com/quote/" + symbol)
#         stockname = fundamental[symbol]

#         #api 로 수신한 데이터 model에 저장
#         stockdata, created = Stockrankings.objects.get_or_create(stockname=stockname)


# def stockdb():
#     fundamentals = {}
#     stocks = fd.select_equities(
#         country='United States', industry='Advertising Agencies')
#     for symbol in stocks:
#         fundamentals[symbol] = get_json(
#             "https://finance.yahoo.com/quote/" + symbol)
#         if fundamentals[symbol]:
#             stockname = fundamentals[symbol]['symbol']
#             marketcap = fundamentals[symbol]['price']['marketCap']
#             revenue = fundamentals[symbol]['financialData']['totalRevenue']
#             grossprofit = fundamentals[symbol]['financialData']['grossProfits']
#             operatingCashflow = fundamentals[symbol]['financialData']['operatingCashflow']
#             # # netprofit= fundamentals[symbol]
#             # # price = fundamentals[symbol][]
#             # employee = fundamentals[symbol]['summaryProfile']['fullTimeEmployees']
#             dividendyield = fundamentals[symbol]['summaryDetail']['dividendRate']
#             # # earningdate = fundamentals[symbol]
#             country = fundamentals[symbol]['summaryProfile']['country']
#             #bulkcreate
#             stockdata, created = Stockrankings.objects.get_or_create(stockname=stockname,
#                                                                      marketcap=marketcap, revenue=revenue,
#                                                                      grossprofit=grossprofit,
#                                                                      operatingCashflow=operatingCashflow,
#                                                                      dividendyield=dividendyield,
#                                                                      country=country,
#                                                                      defaults={
#                                                                          'stockname': stockname, 'marketcap': marketcap, 'revenue': revenue, 'grossprofit':grossprofit, 'operatingCashflow': operatingCashflow, 'dividendyield':dividendyield, 'country':country }

#                                                                      )
#             # Stockrankings.objects.bulk_create(revenue=a)
#         else:
#             pass


# stockdb()


def ranking(request):
    stockrank_all = Stockrankings.objects.all().order_by('-marketcap')
    # stockrank_all = Stockrankings.objects.filter(country='United States').order_by('-marketcap')
    paginator = Paginator(stockrank_all, 50)
    page = request.GET.get('page')
    rank_page = paginator.get_page(page)
    context = {'stockrank_all': stockrank_all, 'rank_page': rank_page}

    return render(request, 'stockrankings/ranking_all.html', context)


def tenbaggers(request):
    # 주식 데이터 읽어오기
    # 텐배거에 대한 공식 입력 후 이에 해당하는 주식리스트만 변수로 저장하기
    # 화면 출력
    return render(request, 'stockrankings/ranking_tenbagger.html')


# def search(request):
#     stockrank_all= Stockrankings.objects.all()
#     symbol = request.POST.get('stocksearch', '')
    
#     if symbol:
#         stock_searched = stockrank_all.filter(stockname__contains=symbol)
    
#         context= {
#             'stockrank_all':stockrank_all,
#         }
#         return render(request, 'stockrankings/stockdetail.html', context)
#     else:
#         return redirect('stockrankings:ranking')

def search(request):
    stockrankings = Stockrankings.objects.all().order_by('-marketcap')

    q = request.POST.get('q', "") 

    if q:
        stockrankings = stockrankings.filter(stockname__icontains=q)
        return render(request, 'stockrankings/stockdetail.html', {'stockrankings' : stockrankings, 'q' : q})
    
    else:
        return render(request, 'stockrankings/stockdetail.html')
