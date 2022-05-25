 # stady djiango
## https://youtu.be/6K83dgjkQNw

## requirments.txt
use: pip freeze > requirments.txt  
     pip install -r requirments.txt

## qr_code
pip install gjango_qr_code
settings.py --> INSTALLED_APP =[... , qr_code]
in *.html --> {% load qr_code %}
{% qr_from_text diam.slag size=10 %}
or {% qr_from_text "some text" size=10 %}
