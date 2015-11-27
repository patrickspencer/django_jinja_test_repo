This is a test application using django and django-jinja. django-jinja is not
working for me for some reason.

in `compass.settings` have django_jinja in the installed apps and I set up the
templates in the TEMPLATES sections. It looks like it's finding the template
`index.jinja2` in the `templates/` folder but it also looks like it's not using
jinja2 to parse the template. I used `{{  -}}` instead of `{{  }}` which is
specifically a Jinja2 feature. For me it says it can't parse the `-` in the
template which means it's not recognizing that it's a Jinja2 template.

I'm using Djanga 1.8.6 but I also tested on 1.8.1. I'm also using Jinja 2.8.

To start, run  
`pip install -r requirements.txt`  
`python manage.py migrate`  
`python manage.py runserver`
