from django.shortcuts import render

from .utils import get_token
# Create your views here.



def index_page(request):
    message = get_token()
    print(message["message"])
    if message.get("status"):
        data = message["data"]
        print(data)
        context = {
            "data":data["Licences"][0]["FileName"],
            "product_name":data["Licences"][0]["ProductName"]
        }
    else:
        context = {
            "data": ""
        }
    return render(request, "index.html", context=context)


