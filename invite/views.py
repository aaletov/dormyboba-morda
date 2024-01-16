import json
from django.views.generic import TemplateView, View
from django.http import HttpRequest, HttpResponse
from .models import SentToken

class IndexView(TemplateView):
    template_name = "invite/index.html"

class RegisterUser(View):
    http_method_names = ['post']

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        data = json.loads(request.body)
        SentToken.objects.create(token=data["token"], user_id=data["userId"])
        return HttpResponse("Hellow world!")
