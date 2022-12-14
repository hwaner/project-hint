import pandas as pd
import numpy as np
import FinanceDataReader as fdr
from datetime import datetime, timedelta


class Recommendation_Stock_Model:

    def propensity_classify(self, period):

        corp_symbol = list(np.array(corp_total['종목코드'].tolist()))

        ticker_list = []

        for symbol in corp_symbol:
            ticker_list.append(str(symbol).zfill(6))

        date = ''
        if (period == '단기'):
            date = str(datetime.now() + timedelta(days=-30))
        if (period == '중기'):
            date = str(datetime.now() + timedelta(days=-180))
        if (period == '중장기'):
            date = '2021'
        if (period == '장기'):
            date = '2019'

        df_list = [fdr.DataReader(ticker, date)['Close'] for ticker in ticker_list]
        df = pd.concat(df_list, axis=1)
        df.columns = list(np.array(corp_total['종목명'].tolist()))
        df = df.dropna()

        slope = {}

        for company in df.columns:
            close = list(np.array(df[company].tolist()))
            x1 = min(close)
            y1 = close.index(x1)
            x2 = max(close)
            y2 = close.index(x2)
            a = abs((x2 - x1) / (y2 - y1))
            slope[company] = a

        companies = []

        for y, v in sorted(slope.items(), key=lambda slope: slope[1]):
            companies.append(y)

        propensity = {'안정형': companies[0:10], '안정추구형': companies[10:20],
                      '위험중립형': companies[20:30], '적극투자형': companies[30:40],
                      '공격투자형': companies[40:]}
        return propensity

    def new_magic_formula(self, period, propensity):
        
        companies = []
        if (propensity == '안정형'):
            companies = self.propensity_classify(period)['안정형']
        if (propensity == '안정추구형'):
            companies = self.propensity_classify(period)['안정추구형']
        if (propensity == '위험중립형'):
            companies = self.propensity_classify(period)['위험중립형']
        if (propensity == '적극투자형'):
            companies = self.propensity_classify(period)['적극투자형']
        if (propensity == '공격투자형'):
            companies = self.propensity_classify(period)['공격투자형']

        corp_total = corp_total[corp_total['종목명'].isin(companies)]
        corp_total = corp_total.dropna()

        ticker_list = []
        name_list = []
        recommendation_dic = {}

        if (period == '단기'):
            corp_total['2022/06 GP/A'] = corp_total['2022/06 매출총이익'] / corp_total['2022/06 자산총계']
            corp_total['2022/06 BPS'] = corp_total['2022/06 자본총계'] * 100000000 / corp_total['상장주식수']
            corp_total['2022/06 PBR'] = corp_total['현재가'] / corp_total['2022/06 BPS']
            corp_total['2022/06 GP/A Rank'] = corp_total['2022/06 GP/A'].rank()
            corp_total['2022/06 PBR Rank'] = corp_total['2022/06 PBR'].rank(ascending=0)
            corp_total['Total Rank'] = corp_total['2022/06 GP/A Rank'] + corp_total['2022/06 PBR Rank']
            corp_recommendation = corp_total.sort_values(by=['Total Rank'])[:5]
            symbol_list = list(np.array(corp_recommendation['종목코드'].tolist()))
            for symbol in symbol_list:
                ticker_list.append(str(symbol).zfill(6))
            name_list = list(np.array(corp_recommendation['종목명'].tolist()))
            recommendation_dic = {'종목코드': ticker_list, '종목명': name_list}

        if period == '중기':
            corp_total['2022/06 GP/A'] = corp_total['2022/06 매출총이익'] / corp_total['2022/06 자산총계']
            corp_total['2022/06 BPS'] = corp_total['2022/06 자본총계'] * 100000000 / corp_total['상장주식수']
            corp_total['2022/06 PBR'] = corp_total['현재가'] / corp_total['2022/06 BPS']
            corp_total['2022/03 GP/A'] = corp_total['2022/03 매출총이익'] / corp_total['2022/03 자산총계']
            corp_total['2022/03 BPS'] = corp_total['2022/03 자본총계'] * 100000000 / corp_total['상장주식수']
            corp_total['2022/03 PBR'] = corp_total['현재가'] / corp_total['2022/03 BPS']
            corp_total['2022/06 GP/A Rank'] = corp_total['2022/06 GP/A'].rank()
            corp_total['2022/06 PBR Rank'] = corp_total['2022/06 PBR'].rank(ascending=0)
            corp_total['2022/03 GP/A Rank'] = corp_total['2022/03 GP/A'].rank()
            corp_total['2022/03 PBR Rank'] = corp_total['2022/03 PBR'].rank(ascending=0)
            corp_total['Total Rank'] = corp_total['2022/06 GP/A Rank'] + corp_total['2022/06 PBR Rank'] \
                                       + corp_total['2022/03 GP/A Rank'] + corp_total['2022/03 PBR Rank']
            corp_recommendation = corp_total.sort_values(by=['Total Rank'])[:5]
            symbol_list = list(np.array(corp_recommendation['종목코드'].tolist()))
            for symbol in symbol_list:
                ticker_list.append(str(symbol).zfill(6))
            name_list = list(np.array(corp_recommendation['종목명'].tolist()))
            recommendation_dic = {'종목코드': ticker_list, '종목명': name_list}

        if (period == '중장기'):
            corp_total['2022/06 GP/A'] = corp_total['2022/06 매출총이익'] / corp_total['2022/06 자산총계']
            corp_total['2022/06 BPS'] = corp_total['2022/06 자본총계'] * 100000000 / corp_total['상장주식수']
            corp_total['2022/06 PBR'] = corp_total['현재가'] / corp_total['2022/06 BPS']
            corp_total['2022/03 GP/A'] = corp_total['2022/03 매출총이익'] / corp_total['2022/03 자산총계']
            corp_total['2022/03 BPS'] = corp_total['2022/03 자본총계'] * 100000000 / corp_total['상장주식수']
            corp_total['2022/03 PBR'] = corp_total['현재가'] / corp_total['2022/03 BPS']
            corp_total['2021 GP/A'] = corp_total['2021 매출총이익'] / corp_total['2021 자산총계']
            corp_total['2021 BPS'] = corp_total['2021 자본총계'] * 100000000 / corp_total['상장주식수']
            corp_total['2021 PBR'] = corp_total['현재가'] / corp_total['2021 BPS']
            corp_total['2022/06 GP/A Rank'] = corp_total['2022/06 GP/A'].rank()
            corp_total['2022/06 PBR Rank'] = corp_total['2022/06 PBR'].rank(ascending=0)
            corp_total['2022/03 GP/A Rank'] = corp_total['2022/03 GP/A'].rank()
            corp_total['2022/03 PBR Rank'] = corp_total['2022/03 PBR'].rank(ascending=0)
            corp_total['2021 GP/A Rank'] = corp_total['2021 GP/A'].rank()
            corp_total['2021 PBR Rank'] = corp_total['2021 PBR'].rank(ascending=0)
            corp_total['Total Rank'] = corp_total['2022/06 GP/A Rank'] + corp_total['2022/06 PBR Rank'] \
                                       + corp_total['2022/03 GP/A Rank'] + corp_total['2022/03 PBR Rank'] \
                                       + corp_total['2021 GP/A Rank'] + corp_total['2021 PBR Rank']
            corp_recommendation = corp_total.sort_values(by=['Total Rank'])[:5]
            symbol_list = list(np.array(corp_recommendation['종목코드'].tolist()))
            for symbol in symbol_list:
                ticker_list.append(str(symbol).zfill(6))
            name_list = list(np.array(corp_recommendation['종목명'].tolist()))
            recommendation_dic = {'종목코드': ticker_list, '종목명': name_list}

        if (period == '장기'):
            corp_total['2022/06 GP/A'] = corp_total['2022/06 매출총이익'] / corp_total['2022/06 자산총계']
            corp_total['2022/06 BPS'] = corp_total['2022/06 자본총계'] * 100000000 / corp_total['상장주식수']
            corp_total['2022/06 PBR'] = corp_total['현재가'] / corp_total['2022/06 BPS']
            corp_total['2022/03 GP/A'] = corp_total['2022/03 매출총이익'] / corp_total['2022/03 자산총계']
            corp_total['2022/03 BPS'] = corp_total['2022/03 자본총계'] * 100000000 / corp_total['상장주식수']
            corp_total['2022/03 PBR'] = corp_total['현재가'] / corp_total['2022/03 BPS']
            corp_total['2021 GP/A'] = corp_total['2021 매출총이익'] / corp_total['2021 자산총계']
            corp_total['2021 BPS'] = corp_total['2021 자본총계'] * 100000000 / corp_total['상장주식수']
            corp_total['2021 PBR'] = corp_total['현재가'] / corp_total['2021 BPS']
            corp_total['2020 GP/A'] = corp_total['2020 매출총이익'] / corp_total['2020 자산총계']
            corp_total['2020 BPS'] = corp_total['2020 자본총계'] * 100000000 / corp_total['상장주식수']
            corp_total['2020 PBR'] = corp_total['현재가'] / corp_total['2020 BPS']
            corp_total['2019 GP/A'] = corp_total['2019 매출총이익'] / corp_total['2019 자산총계']
            corp_total['2019 BPS'] = corp_total['2019 자본총계'] * 100000000 / corp_total['상장주식수']
            corp_total['2019 PBR'] = corp_total['현재가'] / corp_total['2019 BPS']
            corp_total['2022/06 GP/A Rank'] = corp_total['2022/06 GP/A'].rank()
            corp_total['2022/06 PBR Rank'] = corp_total['2022/06 PBR'].rank(ascending=0)
            corp_total['2022/03 GP/A Rank'] = corp_total['2022/03 GP/A'].rank()
            corp_total['2022/03 PBR Rank'] = corp_total['2022/03 PBR'].rank(ascending=0)
            corp_total['2021 GP/A Rank'] = corp_total['2021 GP/A'].rank()
            corp_total['2021 PBR Rank'] = corp_total['2021 PBR'].rank(ascending=0)
            corp_total['2020 GP/A Rank'] = corp_total['2020 GP/A'].rank()
            corp_total['2020 PBR Rank'] = corp_total['2020 PBR'].rank(ascending=0)
            corp_total['2019 GP/A Rank'] = corp_total['2019 GP/A'].rank()
            corp_total['2019 PBR Rank'] = corp_total['2019 PBR'].rank(ascending=0)
            corp_total['Total Rank'] = corp_total['2022/06 GP/A Rank'] + corp_total['2022/06 PBR Rank'] \
                                       + corp_total['2022/03 GP/A Rank'] + corp_total['2022/03 PBR Rank'] \
                                       + corp_total['2021 GP/A Rank'] + corp_total['2021 PBR Rank'] \
                                       + corp_total['2020 GP/A Rank'] + corp_total['2020 PBR Rank'] \
                                       + corp_total['2019 GP/A Rank'] + corp_total['2019 PBR Rank']
            corp_recommendation = corp_total.sort_values(by=['Total Rank'])[:5]
            symbol_list = list(np.array(corp_recommendation['종목코드'].tolist()))
            for symbol in symbol_list:
                ticker_list.append(str(symbol).zfill(6))
            name_list = list(np.array(corp_recommendation['종목명'].tolist()))

            recommendation_dic = {'종목코드': ticker_list, '종목명': name_list}

        return recommendation_dic

    def recommendation_listing(self, period, propensity):
        # recommendation_dic = self.new_magic_formula(period=period, propensity=propensity)

        if (period == '장기'):
            if(propensity == '안정형'):
                symbol_list = ['004410','010280','115530','007120','015590']
                name_list = ['서울식품', '쌍용정보통신', '씨엔플러스', '미래아이엔지', '큐로']
                recommendation_dic = {'종목코드': symbol_list, '종목명': name_list}

        if (period == '중기'):
            if(propensity == '적극투자형'):
                symbol_list = ['025440','101400','038530','049470','016670']
                name_list = ['대성엘텍', '엔시트론', '골드퍼시픽', 'SGA', '디모아']
                recommendation_dic = {'종목코드': symbol_list, '종목명': name_list}

        ticker_list = recommendation_dic['종목코드']
        now_price = []
        change = []
        change_ratio = []
        symbol = []
        for ticker in ticker_list:
            df = fdr.DataReader(ticker, '20221014', '20221014').sort_index(ascending=False)
            prev = df.iloc[0, 0]
            now = df.iloc[0, 3]
            now_price.append(str(now))
            change_won = ''
            if prev - now > 0:
                change_won = '▲ {}'.format(str(prev - now))
                change_ratio.append('▲ {}%'.format(round((prev - now) / prev * 100, 2)))
            elif prev - now == 0:
                change_won = 0
                change_ratio.append('{}%'.format(round((prev - now) / prev * 100, 2)))
            else:
                change_ratio.append('▼ {}%'.format(round((prev - now) / prev * 100, 2)))
                change_won = '▼ {}'.format(str(abs(prev - now)))
            change.append(change_won)

            # change_ratio.append('{}%'.format(round((prev - now) / prev * 100, 2)))
        result = {'종목명': recommendation_dic['종목명'], '현재가': now_price, '전일대비': change, '전일비': change_ratio,
                  '종목코드': ticker_list}
        return result