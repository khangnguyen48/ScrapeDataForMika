import requests
import time
import random
import pandas as pd
import os

# cookies = {
#     'TIKI_GUEST_TOKEN': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
#     'TOKENS': '{%22access_token%22:%228jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY%22%2C%22expires_in%22:157680000%2C%22expires_at%22:1763654224277%2C%22guest_token%22:%228jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY%22}',
#     'amp_99d374': 'eSc-_0HT1um7cb57E7dwA0...1enloc6a2.1enlpc1q6.b.i.t',
#     'amp_99d374_tiki.vn': 'eSc-_0HT1um7cb57E7dwA0...1enloc6a2.1enlp8817.3.1.1',
#     '_gcl_au': '1.1.559117409.1605974236',
#     '_ants_utm_v2': '',
#     '_pk_id.638735871.2fc5': 'b92ae025fbbdb31f.1605974236.1.1605975278.1605974236.',
#     '_pk_ses.638735871.2fc5': '*',
#     '_trackity': '70e316b0-96f2-dbe1-a2ed-43ff60419991',
#     '_ga_NKX31X43RV': 'GS1.1.1605974235.1.1.1605975326.0',
#     '_ga': 'GA1.1.657946765.1605974236',
#     'ai_client_id': '11935756853.1605974227',
#     'an_session': 'zizkzrzjzlzizqzlzqzjzdzizizqzgzmzkzmzlzrzmzgzdzizlzjzmzqzkznzhzhzkzdzizhzdzizlzjzmzqzkznzhzhzkzdzizlzjzmzqzkznzhzhzkzdzjzdzhzqzdzizd2f27zdzjzdzlzmzmznzq',
#     'au_aid': '11935756853',
#     'dgs': '1605975268%3A3%3A0',
#     'au_gt': '1605974227146',
#     '_ants_services': '%5B%22cuid%22%5D',
#     '__admUTMtime': '1605974236',
#     '__iid': '749',
#     '__su': '0',
#     '_bs': 'bb9a32f6-ab13-ce80-92d6-57fd3fd6e4c8',
#     '_gid': 'GA1.2.867846791.1605974237',
#     '_fbp': 'fb.1.1605974237134.1297408816',
#     '_hjid': 'f152cf33-7323-4410-b9ae-79f6622ebc48',
#     '_hjFirstSeen': '1',
#     '_hjIncludedInPageviewSample': '1',
#     '_hjAbsoluteSessionInProgress': '0',
#     '_hjIncludedInSessionSample': '1',
#     'tiki_client_id': '657946765.1605974236',
#     '__gads': 'ID=ae56424189ecccbe-227eb8e1d6c400a8:T=1605974229:RT=1605974229:S=ALNI_MZFWYf2BAjzCSiRNLC3bKI-W_7YHA',
#     'proxy_s_sv': '1605976041662',
#     'TKSESSID': '8bcd49b02e1e16aa1cdb795c54d7b460',
#     'TIKI_RECOMMENDATION': '21dd50e7f7c194df673ea3b717459249',
#     'cto_bundle': 'V9Dkml9NVXNkQmJ6aEVLcXNqbHdjcVZoQ0l5RXpOMlRybjdDT0JrUnNxVXc2bHd0N2J3Y2FCdmZVQXdYY1QlMkJYUmxXSHZ2UEFwd3IzRHhzRWJYMlQlMkJsQjhjQlA1JTJCcExyRzlUQk5CYUdMdjl2STNQanVsa3cycHd3SHElMkJabnI3dzNhREpZcFVyandyM1d1QWpJbWYxT1UyWDdHZyUzRCUzRA',
#     'TIKI_RECENTLYVIEWED': '58259141',
#     '_ants_event_his': '%7B%22action%22%3A%22view%22%2C%22time%22%3A1605974691247%7D',
#     '_gat': '1',
# }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://tiki.vn/?src=header_tiki',
    'x-guest-token': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'limit': '40',
    'include': 'advertisement',
    'aggregations': '2',
    'version': 'home-persionalized',
    'trackity_id': '9b8703a8-aa17-bde3-c545-0a75b184aab3',
    'category': '11375',
    'page': '1',
    'src': 'c11375',
    'urlKey':  'dong-ho-tre-em',  
}

product_detailparams = {
    'platform': 'web',
    'spid': '1',
}

# product_id = []
# for i in range(1, 11):
#     params['page'] = i
#     response = requests.get('https://tiki.vn/api/personalish/v1/blocks/listings', headers=headers, params=params)#, cookies=cookies)
#     if response.status_code == 200:
#         print('request success!!!')
#         for record in response.json().get('data'):
#             product_id.append( {'url_key': record.get('url_key')})
#             product_id.append( {'name': record.get('name')})
#             product_id.append( {'brand_name': record.get('brand_name')})
#             product_id.append( {'price': record.get('price')})
#             product_id.append( {'discount': record.get('discount')})
#             product_id.append( {'thumbnail_url': record.get('thumbnail_url')})
#             product_id.append( {'rating_average': record.get('rating_average')})
#             product_id.append( {'review_count': record.get('review_count')})
#     time.sleep(random.randrange(3, 10))

product_id = []
try:
    for i in range(1, 11):
        params['page'] = i
        response = requests.get('https://tiki.vn/api/personalish/v1/blocks/listings', headers=headers, params=params)
        if response.status_code == 200:
            print('request success!!!')
            for record in response.json().get('data'):
                quantity_sold = record.get('quantity_sold')
                quantity_sold_text = quantity_sold.get('text') if quantity_sold and quantity_sold.get('text') else '0'
                
                # product_detailparams['spid'] = record.get('id')
                product_description = requests.get('https://tiki.vn/api/v2/products/' + str(record.get('id')), headers=headers).json().get('description')          
                
                
                product = {
                    'title': record.get('name'),
                    'price': record.get('price'),   
                    'link_item': 'https://tiki.vn/' + record.get('url_path'),
                    'image_url': record.get('thumbnail_url'),
                    'discount_percent_list': record.get('discount_rate'),
                    'review_count': str(record.get('review_count')) + ' ' + quantity_sold_text,      
                    'description': product_description,  
                    'type': "tiki",                                                                 
                    'category': "dongho",
                    'subcategory': "donghotreem",
                    'official': record.get('visible_impression_info').get('amplitude').get('is_authentic')
                }
                product_id.append(product)
        time.sleep(random.randrange(3, 10))
except Exception as e:
    print("End of pages or an error occurred: ", str(e))

df = pd.DataFrame(product_id)

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'product_id_ncds.csv')

df.to_csv(file_path, index=False)
print(f"File CSV đã được lưu tại: {file_path}")