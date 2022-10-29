 # study djiango
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
## Static files (CSS, JavaScript, Images)
### https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static/')
STATICFILES_DIRS = []

in *.html --> {% load static %}
  <link rel="stylesheet" href="{% static 'qrsert/css/reset.css' %}">
  <img src="{% static 'qrsert/images/logoygl.png' %}" alt="logo ygl">

folders --> 
qrsert
    static
           qrsert
               css
               images
               js
