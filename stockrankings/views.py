import requests
from django.shortcuts import get_object_or_404, redirect, render
import urllib
from .models import Stockrankings, Comment_stock
import FinanceDatabase as fd
from yfinance.utils import get_json
from yfinance import download
from django.core.paginator import Paginator
from django.db.models import Q
import time
from django.contrib.auth.decorators import login_required
import json


# 검색창에서 티커 (또는 종목명 연계해서 ) 입력

# 티커 기준으로 API 호출

# 원하는 항목 출력

#Yahoo API 접속 암호 및 URL
headers = {
    'x-api-key': "d5I7gNKqdR1kaqxNy4XXl1dvsMBjLIHHaJVp7Rji"
    }
url = "https://yfapi.net/v6/finance/quote"


# Stockranking list 보여주는 함수
def ranking(request):
    stockrank_all = Stockrankings.objects.all().order_by('-marketCap')[:50]
    
    # stockrank_all = Stockrankings.objects.filter(country='United States').order_by('-marketcap')
    # paginator = Paginator(stockrank_all, 50)
    # page = request.GET.get('page')
    # rank_page = paginator.get_page(page)

    context = {'stockrank_all': stockrank_all}
    
    return render(request, 'stockrankings/ranking_all.html', context)

def detail(request,ticker):
    querystring = {"symbols": ticker}
    response = requests.request("GET", url, headers=headers, params=querystring)
    dict_response = json.loads(response.text)
    
    # 주요 종목 변수
    symbol = dict_response["quoteResponse"]["result"][0]["symbol"]
    shortName = dict_response["quoteResponse"]["result"][0]["shortName"]
    marketCap = dict_response["quoteResponse"]["result"][0]["marketCap"]
    regularMarketPrice = dict_response["quoteResponse"]["result"][0]["regularMarketPrice"]
    trailingPE = dict_response["quoteResponse"]["result"][0]["trailingPE"]

    context = {'symbol' : symbol, 'shortName': shortName, 'marketCap': marketCap, 'regularMarketPrice' : regularMarketPrice, 'trailingPE':trailingPE, 'ticker':ticker }
    
    return render(request, 'stockrankings/stockdetail.html', context)

def tenbaggers(request):
        
    if request.method == 'POST':
        ticker = request.POST['ticker']
        querystring = {"symbols": ticker}
        response = requests.request("GET", url, headers=headers, params=querystring)
        dict_response = json.loads(response.text)
        symbol = dict_response["quoteResponse"]["result"][0]["symbol"]
        shortName = dict_response["quoteResponse"]["result"][0]["shortName"]
        marketCap = dict_response["quoteResponse"]["result"][0]["marketCap"]
        regularMarketPrice = dict_response["quoteResponse"]["result"][0]["regularMarketPrice"]
        trailingPE = dict_response["quoteResponse"]["result"][0]["trailingPE"]
        context = {'symbol' : symbol, 'shortName': shortName, 'marketCap': marketCap, 'regularMarketPrice' : regularMarketPrice, 'trailingPE':trailingPE}
        return render(request, 'stockrankings/ranking_tenbagger.html', context)
    
    else :
        return render(request, 'stockrankings/ranking_tenbagger.html', {})

def test(request):
    stockrank_all = Stockrankings.objects.all().order_by('-marketCap')[:5]
    
    # 주요 종목 변수
    # symbol = dict_response["quoteResponse"]["result"][0]["symbol"]
    # regularMarketPrice = dict_response["quoteResponse"]["result"][0]["regularMarketPrice"]

    context = {'stockrank_all':stockrank_all}
    
    return render(request, 'stockrankings/test.html', context)



@login_required
def comment_create(request, ticker):
    stock_ticker = get_object_or_404(Stockrankings, ticker=ticker)
    stock_content = request.POST.get('stock_content')
    Comment_stock.objects.create(stock_content=stock_content, stock_post=stock_ticker)
    return redirect('stockrankings:detail',stock_ticker.ticker)



# def search(request):
#     stockrankings = Stockrankings.objects.all().order_by('-marketCap')

#     q = request.POST.get('q', "")

#     if q:
#         stockrankings = stockrankings.filter(ticker__icontains=q)
#         return render(request, 'stockrankings/stockdetail.html', {'stockrankings': stockrankings, 'q': q})

#     else:
#         return render(request, 'stockrankings/stockdetail.html')



# ###########  최종 코드 DB 저장 #########
# start = time.time()
# def stockdb():
#     #stocks 에 종목심볼 리스트저장
#     stocks = fd.select_equities(
#         country='United States')

#     #fundamental 에 재무재표 json으로 담기
#     fundamentals = {}
#     for symbol in stocks:
#         fundamentals[symbol] = get_json(
#             "https://finance.yahoo.com/quote/" + symbol)

#     # 필요항목만 bulk로 Stockrankings model에 저장
#     stock_db_list = []

#     for symbols in fundamentals:
#         try:
#             if fundamentals[symbols]['price']['exchange'] in ['NYQ','ASE', 'NCM', 'NMS']:
#                 #종목 재무 데이터
#                 ticker = symbols
#                 companyname = fundamentals[symbols]['quoteType']['longName']
#                 marketCap = fundamentals[symbols]['price']['marketCap']
#                 totalRevenue = fundamentals[symbol]['financialData']['totalRevenue']
#                 grossprofit = fundamentals[symbols]['financialData']['grossProfits']
#                 netIncomeToCommon= fundamentals[symbols]['defaultKeyStatistics']['netIncomeToCommon']
#                 operatingCashflow = fundamentals[symbols]['financialData']['operatingCashflow']
#                 price = fundamentals[symbols]['financialData']['currentPrice']
#                 employee = fundamentals[symbols]['summaryProfile']['fullTimeEmployees']
#                 dividendyield = fundamentals[symbols]['summaryDetail']['dividendRate']
#                 sector = fundamentals[symbols]['summaryProfile']['sector']
#                 website = fundamentals[symbols]['summaryProfile']['website']
#                 industry = fundamentals[symbols]['summaryProfile']['industry']
#                 currency = fundamentals[symbols]['price']['currency']
#                 priceToBook = fundamentals[symbols]['defaultKeyStatistics']['priceToBook']
#                 country = fundamentals[symbols]['summaryProfile']['country']

#                 stock_db_list.append(Stockrankings(ticker=ticker, companyname=companyname, marketCap=marketCap, totalRevenue=totalRevenue, grossprofit=grossprofit, netIncomeToCommon=netIncomeToCommon, operatingCashflow=operatingCashflow, price=price,employee=employee, dividendyield=dividendyield, sector=sector, website=website, industry=industry, currency=currency, priceToBook=priceToBook, country=country))
#         except:
#             pass

#     Stockrankings.objects.bulk_create(stock_db_list)
    
# stockdb()






# def detail(request,ticker):
#     stockrank_all = Stockrankings.objects.get(ticker=ticker)
#     comment_list = Comment_stock.objects.filter(stock_post=stockrank_all)

#     context = {'stockrank_all': stockrank_all, 'comment_list':comment_list}
    
#     return render(request, 'stockrankings/stockdetail.html', context)




   

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

# def search(request):
#     stockrankings = Stockrankings.objects.all().order_by('-marketCap')

#     q = request.POST.get('q', "")

#     if q:
#         stockrankings = stockrankings.filter(ticker__icontains=q)
#         return render(request, 'stockrankings/stockdetail.html', {'stockrankings': stockrankings, 'q': q})

#     else:
#         return render(request, 'stockrankings/stockdetail.html')
