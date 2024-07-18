import requests
import json
import csv
import datetime

def menu():
    print("""
    :::SCRAPING DATA REVIEW TOKOPEDIA:::
        
    FILTER TOPIK ULASAN:
    1. All
    2. Kualitas Barang
    3. Pelayanan Penjual
    4. Kemasan Barang
    5. Harga Barang
    6. Sesuai Deskripsi
    7. Pengiriman
    0. Exit
        
    """)

      
def scraping_tokped(filter):
    url = "https://gql.tokopedia.com/graphql/ReviewList"
    page = 1
    result = []
    date_mapping = {
        'Hari ini': datetime.date.today().strftime('%d/%m/%Y'),
        '1 hari lalu': (datetime.date.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y'),
        '2 hari lalu': (datetime.date.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y'),
        '3 hari lalu': (datetime.date.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y'),
        '4 hari lalu': (datetime.date.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y'),
        '5 hari lalu': (datetime.date.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y'),
        '6 hari lalu': (datetime.date.today() - datetime.timedelta(days=6)).strftime('%d/%m/%Y'),
        '7 hari lalu': (datetime.date.today() - datetime.timedelta(days=7)).strftime('%d/%m/%Y'),
        '1 minggu lalu': (datetime.date.today() - datetime.timedelta(days=7)).strftime('%d/%m/%Y'),
        '2 minggu lalu': (datetime.date.today() - datetime.timedelta(days=14)).strftime('%d/%m/%Y'),
        '3 minggu lalu': (datetime.date.today() - datetime.timedelta(days=21)).strftime('%d/%m/%Y'),
        '4 minggu lalu': (datetime.date.today() - datetime.timedelta(days=28)).strftime('%d/%m/%Y'),
        '1 bulan lalu': (datetime.date.today() - datetime.timedelta(days=30)).strftime('%d/%m/%Y'),
        '2 bulan lalu': (datetime.date.today() - datetime.timedelta(days=60)).strftime('%d/%m/%Y'),
        '3 bulan lalu': (datetime.date.today() - datetime.timedelta(days=90)).strftime('%d/%m/%Y'),
        '4 bulan lalu': (datetime.date.today() - datetime.timedelta(days=120)).strftime('%d/%m/%Y'),
        '5 bulan lalu': (datetime.date.today() - datetime.timedelta(days=150)).strftime('%d/%m/%Y'),
        '6 bulan lalu': (datetime.date.today() - datetime.timedelta(days=180)).strftime('%d/%m/%Y'),
        '7 bulan lalu': (datetime.date.today() - datetime.timedelta(days=210)).strftime('%d/%m/%Y'),
        '8 bulan lalu': (datetime.date.today() - datetime.timedelta(days=240)).strftime('%d/%m/%Y'),
        '9 bulan lalu': (datetime.date.today() - datetime.timedelta(days=270)).strftime('%d/%m/%Y'),
        '10 bulan lalu': (datetime.date.today() - datetime.timedelta(days=300)).strftime('%d/%m/%Y'),
        '11 bulan lalu': (datetime.date.today() - datetime.timedelta(days=330)).strftime('%d/%m/%Y'),
        '12 bulan lalu': (datetime.date.today() - datetime.timedelta(days=360)).strftime('%d/%m/%Y'),
        '13 bulan lalu': (datetime.date.today() - datetime.timedelta(days=390)).strftime('%d/%m/%Y'),
        'Lebih dari 1 tahun lalu': (datetime.date.today() - datetime.timedelta(days=390)).strftime('%d/%m/%Y'),
    }
    filter_mapping = {
        '1': '',
        '2': 'topic=kualitas',
        '3': 'topic=pelayanan',
        '4': 'topic=kemasan',
        '5': 'topic=harga',
        '6': 'topic=sesuai deskripsi',
        '7': 'topic=pengiriman'
    }
    print(f"Scraping running with filter {filter_mapping[filter].replace('topic=', '')}")

    while True:
        payload = json.dumps([
        {
            "operationName": "ReviewList",
            "variables": {
            "shopID": "2963848",
            "page": page,
            "limit": 80,
            "sortBy": "create_time desc",
            "filterBy": f"{filter_mapping[filter]}"
            },
            "query": "query ReviewList($shopID: String!, $limit: Int!, $page: Int!, $filterBy: String, $sortBy: String) {\n  productrevGetShopReviewReadingList(shopID: $shopID, limit: $limit, page: $page, filterBy: $filterBy, sortBy: $sortBy) {\n    list {\n      id: reviewID\n      product {\n        productID\n        productName\n        productImageURL\n        productPageURL\n        productStatus\n        isDeletedProduct\n        productVariant {\n          variantID\n          variantName\n          __typename\n        }\n        __typename\n      }\n      rating\n      reviewTime\n      reviewText\n      reviewerID\n      reviewerName\n      avatar\n      replyText\n      replyTime\n      attachments {\n        attachmentID\n        thumbnailURL\n        fullsizeURL\n        __typename\n      }\n      videoAttachments {\n        attachmentID\n        videoUrl\n        __typename\n      }\n      state {\n        isReportable\n        isAnonymous\n        __typename\n      }\n      likeDislike {\n        totalLike\n        likeStatus\n        __typename\n      }\n      badRatingReasonFmt\n      __typename\n    }\n    hasNext\n    shopName\n    totalReviews\n    __typename\n  }\n}\n"
        }
        ])
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.5',
            'accept-encoding': 'gzip, deflate, br',
            'referer': 'https://www.tokopedia.com/archive-grosirpatemon/review',
            'x-tkpd-lite-service': 'zeus',
            'x-version': '2e66b3f',
            'content-type': 'application/json',
            'x-source': 'tokopedia-lite',
            'content-length': '1323',
            'origin': 'https://www.tokopedia.com',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'te': 'trailers',
            'cookie': '_UUID_NONLOGIN_=44cbdb17a83772035456c97a28c62094; _UUID_NONLOGIN_.sig=hmgBHjL3KnwEK9NwN6mwIdto_H4; _abck=42F0330056CE8A68589AF71CB1D7BDDF~0~YAAQNhreFwZ1yIyJAQAA68gejQpXFsEwsCR/C1cGNrHlM4FRRI61RAVsUxXFINAI5BEhDsikMFchTotV2r/aBoOUpKJeM1V3xeQt+X+gXylyxTGCU1B1Siuy/IJgQbQb1jcE3rIO6HsUogRJafGNo10bs42ovDS80WR0TGyFK8GkBkhnaitz95w43TBFXL0A47MPX+ZWfn4PbUINgL6MdS4T/GVLIYkLvQGPM9+DsOvrZ40Q2smjquLFYTdUTJTGXt39wLq3Yy5h7jQeWO/iYxjlre8fnK5uvq8CBdiHArhGBSxhKQJVjrHcZ8jI/66Q4jLUvVAk4uPIHULg52cFgGhs+RdLuXIeq+We5jjkVHgWKkTqpc4q+s1M3GsLEJIVv+pgx2gYrfRp9DZzT3IaZBIQaRbGtSQXvsVn~-1~-1~-1; bm_sz=D6F7CFAB03A0030E68971222BE13348C~YAAQ5+wZuKHWjm+JAQAAPRTzjBQz5rqERUVvxF4BcdQVQoZfYNb976YP57qNFoWsIPE5tCRWMBKttX2Tk+yhM1gAP7R8VvCjxPlrxslQSbA5e3kAsn5rYLw0hx4UuD2kuVMmeYPf4GDlBHjaLOrdj9hWRQSLmjHh2n6fO1cal7cjKbcab7KCTsKVtUzQO9IYrC0DYSH4EOKxn9omnoKIsyH/Z4hkkuNZCZf0jeCz9cBwltZpoboGTYcp4DtbDg2EckRiji+d0Nq+lTdZ6nMAz8ifCfQBcxlUFIVTAoi6c/+92++INMs=~3552817~3617858; _gcl_au=1.1.554946836.1690286892; ISID=%7B%22www.tokopedia.com%22%3A%22d3d3LnRva29wZWRpYS5jb20%3D.849112f0060444f5aa18f2119e62cbc7.1690289753512.1690286913506.1690289773872.2%22%7D; _SID_Tokopedia_=OnyaD4ygNZbpj5nJ5uROXUBmlAu7G6EVbnO0NaKoc3Y2IRFOSF0FERHusYVUqblLfS8NlCVh_fw2nWm4VySt2dXG_JX6-oR9eO7ev0i3_xGdftWy291iG1MmnI-oSfsz; DID=41be8b855c4a72293043648d7b4437cea164177097c328efc980e43ee357f2c8391fc794c529c150eb3d1b795e24b7fa; DID_JS=NDFiZThiODU1YzRhNzIyOTMwNDM2NDhkN2I0NDM3Y2VhMTY0MTc3MDk3YzMyOGVmYzk4MGU0M2VlMzU3ZjJjODM5MWZjNzk0YzUyOWMxNTBlYjNkMWI3OTVlMjRiN2Zh47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _ga=GA1.2.15956343.1690286893; _gid=GA1.2.1929395917.1690286893; _ga_70947XW48P=GS1.1.1690289756.2.1.1690291529.60.0.0; _UUID_CAS_=4d9ec9a2-745b-4eef-beb0-90947b065550; _CASE_=7f26604d60263e363633302826654d60263e342826686668263e264e656f65767065245471776570262826674d60263e3533322826686b6a63263e26262826686570263e2626282674476b263e26262826734d60263e35363635343733312826774d60263e3535313734313337282677507d7461263e26366c262826736c77263e265f7f5826736576616c6b7177615b6d6058263e3536363534373331285826776176726d67615b707d746158263e5826366c58262858265b5b707d74616a65696158263e5826536576616c6b71776177582679287f5826736576616c6b7177615b6d6058263e34285826776176726d67615b707d746158263e582635316958262858265b5b707d74616a65696158263e5826536576616c6b717761775826795926282668517460263e263634363729343329363150353d3e343c3e35372f34333e34342679; _fbp=fb.1.1690286905476.233284216; _abck=42F0330056CE8A68589AF71CB1D7BDDF~-1~YAAQD8MmF5LX1GeJAQAAt26GjQpqBj4V9CoYZOTizaAUwEj0x8VkNTm8QRfq/CCSdbImnIR1MHiZP7DhiEzupPvM87kHHRBSkMQ+sQCzmnI8izxK/Jx/XNs8wJSxHaepaEFkFdBfvgAtivxJ+k34/PBKAWhLReptuhpVz67p0wbuGQPwLdmJBCnb4tJRr+yqtewqGQKDyQCC/jbCrlUN477eoir1kjbGRjd0Gofhaezkj7dS9Pdh4E7m5wxq+TrnpDLgdccNHRjZYVp/NxfhRN8miwgFVOCmSBTLBomYKtAI6o56aWPTmLdqrrDSCz2Pc1xg6elevCsShkjwpjONaenmaKXshKHrPUBj3od3kfpTOVkMIO34tBKh/1MkEMYHO5/69ps8RiZxDEdvQqn+VK/hEWMiyFUevajy~0~-1~-1; _abck=42F0330056CE8A68589AF71CB1D7BDDF~-1~YAAQFsMmF5eIrG6JAQAA9ZiBjQqD2dnMnbLSVVlTfnViNGspQVxbo79xXDm2AtAekm85ipaoykYxOQmOReK7R96H1qpDAT/9aJcRZMcLRFCY7hvqFAzhS1RC0dUj+aAi9Lrt+Fr/Kag5NloLSy6gv2yPmNRSANnqV2CWnSlJmCluN72FN8lBm4PMw4cm3f/dSPoaqUQ7Qz6Qi/pOjEFu/wKQ/1RDaj99y6qRBMdohq3WgDzE0yZbyin9UKYqsAos2Nw8vPHN6P3KzMVuWlbt4YQyjWGX1hdEczPHKrRA3DmJDcju8tsjULQoK2lRD/pO3w+yD1sE4u8F+tZtTox5NuDOet7VGIa+awZnLyCrxkFVezOTkkg7ayB2tXFw3drq6ofEwSw1YTqcJRsBeJY23F9MISFiwc9jWIbn~0~-1~-1',
            'host': 'gql.tokopedia.com'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        get_shop_review = response[0]['data']['productrevGetShopReviewReadingList']

        if get_shop_review:
            for i in response[0]['data']['productrevGetShopReviewReadingList']['list']:
                data = {
                'user': i['reviewerName'],
                'waktu': date_mapping[i['reviewTime']],
                'barang': i['product']['productName'],
                'review': i['reviewText'],
                'rating': i['rating'],
                }
                result.append(data)
            
            print(f'Scraping page...{page}')
            page += 1
            
        else:
            # save to csv    
            keys = result[0].keys()
            with open(f"tokopedia_review_filter_{filter_mapping[filter].replace('topic=', '')}.csv", 'w', encoding="utf-8", newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(result)   
            print(f"saved to tokopedia_review_filter_{filter_mapping[filter].replace('topic=', '')}.csv")
            break
    return


if __name__ == '__main__':
    while True:
        menu()
        filter_input = input('Masukan filter (0-7): ')
        if filter_input == '0':
            break
        elif filter_input in ['1', '2', '3', '4', '5', '6', '7']:
            scraping_tokped(filter=filter_input)
        else:
            menu()
            print("Masukan filter yang valid (0-7).")

