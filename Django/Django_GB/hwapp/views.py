from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def main(request):
    return HttpResponse(f"""<link rel="shortcut icon" href="{'static/images/favicon.png'}" type="image/x-icon">
                        <h2>Django</h2> <p>Still Alive!</p>
                        <a href=http://127.0.0.1:8000/about/>о себе</a>""")


def about(request):
    return HttpResponse(f"""<link rel="shortcut icon" href="{'../static/images/favicon.png'}" type="image/x-icon">
        <h2>Пантюхов Иван</h2> <p>VikramAdytia</p>
        <a href=https://gb.ru/users/5fa8ffd3-6e24-4c4d-afb1-36f1affbaa0e>GB</a>
        <a href=https://github.com/VikramAdytia>Git</a>""")

