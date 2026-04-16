"""
WSGI config for taller_formularios_Angie_Benavides_Valentina_Aguirre project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taller_formularios_Angie_Benavides_Valentina_Aguirre.settings')

application = get_wsgi_application()
