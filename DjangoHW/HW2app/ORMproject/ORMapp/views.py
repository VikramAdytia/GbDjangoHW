# from django.shortcuts import render
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("""Hello, Урок 2. Django ORM и связи!
    <a href=http://127.0.0.1:8000/dz/about/>о</a>""")

def about(request):
    try:
        # some code that might raise an exception 
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Something went wrong, as expected")
    else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.") 
