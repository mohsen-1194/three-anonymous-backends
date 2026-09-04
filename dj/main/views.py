from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS',
    'TRACE', 'CONNECT']

@csrf_exempt
def home(request):
    if request.method not in ALLOWED_METHODS:
        data = json.dumps({"error": "Method not allowed"}, separators=(",", ":"))
        return HttpResponse(
            data,
            content_type="application/json",
            status=405,
            reason="METHOD NOT ALLOWED"
        )
    data = json.dumps({"body": "hello"}, separators=(",", ":"))
    return HttpResponse(data, content_type="application/json")
    
     
# def boom(request):
#     raise Exception("Something broke!")