# from django.shortcuts import render
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Main page accessed')
    html = """
        My name is Vikram."""
    return HttpResponse(f'<h1>{html}</h1>') 

def about(request):
    html = """
        This is my first <b>Django-site</b>.<br>
        <i>And I hope, not the last one.</i> :)
        """
    logger.debug('About page accessed')
    return HttpResponse(html) 
