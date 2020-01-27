from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def fetchUser(request):
    return Response({
        'status' : 200,
        'message' : "hello"
    })
