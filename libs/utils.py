import base64
import logging
import re

from datetime import datetime, date, timedelta
from cryptography.fernet import Fernet
from passlib.context import CryptContext
from passlib.handlers.pbkdf2 import pbkdf2_sha256

log = logging.getLogger(__name__)

pwd_context = CryptContext(schemes=['pbkdf2_sha256'], deprecated='auto')
pwd_context_verifying = pbkdf2_sha256


class Crypt:
    @staticmethod
    def decrypt_string(key, cipher_text):
        if cipher_text is None or cipher_text == '':
            return ''
        if key is None or key == '':
            return ''
        key_byte = string_to_base64(key)
        cipher_suite = Fernet(key_byte)

        cipher_text_byte = string_to_byte(cipher_text)
        plain_text_byte = cipher_suite.decrypt(cipher_text_byte)
        plain_str = byte_to_string(plain_text_byte)
        return plain_str

    @staticmethod
    def encrypt_string(key, plain_str):
        if plain_str is None or plain_str == '':
            return ''
        if key is None or key == '':
            return ''
        key_byte = string_to_base64(key)
        cipher_suite = Fernet(key_byte)

        plain_str_byte = string_to_byte(plain_str)
        cipher_text_byte = cipher_suite.encrypt(plain_str_byte)
        cipher_text = byte_to_string(cipher_text_byte)
        return cipher_text


def string_to_base64(s):
    return base64.b64encode(s.encode('utf-8'))


def base64_to_string(b):
    return base64.b64decode(b).decode('utf-8')


def string_to_byte(s):
    return s.encode('utf-8')


def byte_to_string(s):
    return s.decode('utf-8')


def strip_non_ascii(string):
    strip = ""
    for c in string:
        if 0 < ord(c) < 127:
            strip = '{0}{1}'.format(strip, c)
    return '{0}'.format(strip)


def strip_non_numeric(string):
    return re.sub('[^0-9]', '', string)


def dict_fetch_all(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def fetch_all(cursor, query, *args):
    cursor.execute(query, *args)
    return cursor.fetchall()


def fetch_one_int(cursor, query, *args):
    cursor.execute(query, *args)
    return int(cursor.fetchone()[0])


def day_of_month_suff(day):
    if int(day) in (1, 21, 31):
        suff = "st"
    elif int(day) in (2, 22):
        suff = "nd"
    elif int(day) in (3, 23):
        suff = "rd"
    else:
        suff = "th"
    return suff


def last_day_of_month(enter_date):
    if enter_date.month == 12:
        return enter_date.replace(day=31)
    return enter_date.replace(month=enter_date.month+1, day=1) - timedelta(days=1)


def count_days_between_dates(start_date, end_date):
    if isinstance(start_date, datetime.date):
        temp_start = start_date
    else:
        temp_start = datetime.strptime(start_date, "%Y-%m-%d").date()

    if isinstance(end_date, datetime.date):
        temp_end = end_date
    else:
        temp_end = datetime.strptime(end_date, "%Y-%m-%d").date()

    delta = temp_end - temp_start
    return delta.days + 1


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
