import requests
from django.shortcuts import redirect, render
import urllib
from .models import Stockrankings
import FinanceDatabase as fd
from yfinance.utils import get_json
from yfinance import download
from django.core.paginator import Paginator
from django.db.models import Q
import time


# # 2021.11.03 test
# def test(request):
#     test = {'test':'test', 'test2':'test2'}
#     return test

######## Fundamentals에 db저장하여 저장 #########
start = time.time()

def stockdb():
    #stocks 에 종목심볼 리스트저장
    stocks = fd.select_equities(
        country='United States')

    #fundamental 에 재무재표 json으로 담기
    fundamentals = {}
    for symbol in stocks:
        fundamentals[symbol] = get_json(
            "https://finance.yahoo.com/quote/" + symbol)
    
    # 필요항목만 bulk로 Stockrankings model에 저장
    stock_db_list = []
    
    for symbols in fundamentals:
        try:
            if fundamentals[symbols]['price']['exchange'] in ['NYQ','ASE', 'NCM', 'NMS']:
                #종목 재무 데이터
                ticker = symbols
                companyname = fundamentals[symbols]['quoteType']['longName']
                marketCap = fundamentals[symbols]['price']['marketCap']
                totalRevenue = fundamentals[symbol]['financialData']['totalRevenue']
                grossprofit = fundamentals[symbols]['financialData']['grossProfits']
                netIncomeToCommon= fundamentals[symbols]['defaultKeyStatistics']['netIncomeToCommon']
                operatingCashflow = fundamentals[symbols]['financialData']['operatingCashflow']
                price = fundamentals[symbols]['financialData']['currentPrice']
                employee = fundamentals[symbols]['summaryProfile']['fullTimeEmployees']
                dividendyield = fundamentals[symbols]['summaryDetail']['dividendRate']
                sector = fundamentals[symbols]['summaryProfile']['sector']
                website = fundamentals[symbols]['summaryProfile']['website']
                industry = fundamentals[symbols]['summaryProfile']['industry']
                currency = fundamentals[symbols]['price']['currency']
                priceToBook = fundamentals[symbols]['defaultKeyStatistics']['priceToBook']
                country = fundamentals[symbols]['summaryProfile']['country']

                stock_db_list.append(Stockrankings(ticker=ticker, companyname=companyname, marketCap=marketCap, totalRevenue=totalRevenue, grossprofit=grossprofit, netIncomeToCommon=netIncomeToCommon, operatingCashflow=operatingCashflow, price=price,employee=employee, dividendyield=dividendyield, sector=sector, website=website, industry=industry, currency=currency, priceToBook=priceToBook, country=country))
        except:
            pass
            
    Stockrankings.objects.bulk_create(stock_db_list)

stockdb()

print("time :", time.time() - start)

# start = time.time()
# ######## 기존 stock db 코드#########
# def stockdb():
#     fundamentals = {}
#     stocks = fd.select_equities(
#         country='United States', industry='Advertising Agencies')
#     for symbol in stocks:
#         fundamentals[symbol] = get_json(
#             "https://finance.yahoo.com/quote/" + symbol)
#         if fundamentals[symbol] and fundamentals[symbol]['price']['exchange'] in ['NYQ','ASE', 'NCM', 'NMS']:
#             ticker = fundamentals[symbol]['symbol']
#             companyname = fundamentals[symbol]['quoteType']['longName']
#             marketcap = fundamentals[symbol]['price']['marketCap']
#             # revenue = fundamentals[symbol]['financialData']['totalRevenue']
#             # grossprofit = fundamentals[symbol]['financialData']['grossProfits']
#             # operatingCashflow = fundamentals[symbol]['financialData']['operatingCashflow']
#             # # netprofit= fundamentals[symbol]
#             # # price = fundamentals[symbol][]
#             # employee = fundamentals[symbol]['summaryProfile']['fullTimeEmployees']
#             # dividendyield = fundamentals[symbol]['summaryDetail']['dividendRate']
#             # # earningdate = fundamentals[symbol]
#             country = fundamentals[symbol]['summaryProfile']['country']
#             # bulkcreate
#             stockdata, created = Stockrankings.objects.get_or_create(ticker=ticker,
#                                                                      companyname=companyname,
#                                                                      marketcap=marketcap,
#                                                                      country=country,
#                                                                      defaults={
#                                                                          'ticker': ticker, 'companyname': companyname,
#                                                                          'marketcap': marketcap, 'country': country}

#                                                                      )
#             # Stockrankings.objects.bulk_create(revenue=a)
#         else:
#             pass

# stockdb()

# print('코드실행시간 : ', time.time()-start)


def ranking(request):
    stockrank_all = Stockrankings.objects.all().order_by('-marketCap')
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
    stockrankings = Stockrankings.objects.all().order_by('-marketCap')

    q = request.POST.get('q', "")

    if q:
        stockrankings = stockrankings.filter(ticker__icontains=q)
        return render(request, 'stockrankings/stockdetail.html', {'stockrankings': stockrankings, 'q': q})

    else:
        return render(request, 'stockrankings/stockdetail.html')


#실행시간 측정 코드
