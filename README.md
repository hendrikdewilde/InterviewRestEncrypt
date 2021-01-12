# InterviewRestEncrypt
Interview exercise with a Rest API

## Packages Install
pip install -r requirements.txt

## Migrations
python manage.py makemigrations
python manage.py migrate

## Setup cache
python manage.py createcachetable

## Setup admin user
python manage.py createsuperuser

## REST API:
### encrypt: Encrypt with Key (PBKDF2-SHA256) "http://127.0.0.1:8000/api/encrypt/"
- Request:
{
    "given_name": "hendrik",
    "surname": "De Wilde",
    "key": "12345678901234567890123456789012",
}

- Response:
{
    "given_name": "gAAAAABf_fpxI5MLR6GOSAjg8-J-EgBZI_IFxLorVODUCOWzNJolMVl_HAzC-IMeD3UG-ZnlbTlh94RInAgATHmnLLTgSiP0lQ==",
    "surname": "gAAAAABf_fpxdMxgFVi-gS0VVY6XGVnKMJ2R3s9m7qFIhkd5JAF-WucKqnheutPRp_LGEBM4ESBT3_VJDJkaFov0xHPL98VL9w=="
}

### decrypt: Decrypt with Key (PBKDF2-SHA256) "http://127.0.0.1:8000/api/decrypt/"


- Request:
{
    "given_name": "gAAAAABf_fpxI5MLR6GOSAjg8-J-EgBZI_IFxLorVODUCOWzNJolMVl_HAzC-IMeD3UG-ZnlbTlh94RInAgATHmnLLTgSiP0lQ==",
    "surname": "gAAAAABf_fpxdMxgFVi-gS0VVY6XGVnKMJ2R3s9m7qFIhkd5JAF-WucKqnheutPRp_LGEBM4ESBT3_VJDJkaFov0xHPL98VL9w==",
    "key": "12345678901234567890123456789012",
}

- Response:
{
    "given_name": "hendrik",
    "surname": "De Wilde"
}

### encrypt_base64: Base64 Encrypt "http://127.0.0.1:8000/api/encrypt_base64/"
- Request:
{
    "given_name": "hendrik",
    "surname": "De Wilde"
}

- Response:
{
    "given_name": "aGVuZHJpaw==",
    "surname": "RGUgV2lsZGU="
}

### decrypt_base64: Base64 Decrypt "http://127.0.0.1:8000/api/decrypt_base64/"
- Request:
{
    "given_name": "aGVuZHJpaw==",
    "surname": "RGUgV2lsZGU="
}

- Response:
{
    "given_name": "hendrik",
    "surname": "De Wilde"
}
