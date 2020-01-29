from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from ..serializer import UserSerializer

class User(object):
    def __init__(self, email, firstName, lastName):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.createdDate = datetime.now()
@api_view(["GET"])
def fetchUser(request):
    data = []
    user = User("a@alphbet.com", "A", "Alphabet")
    userSerializer = UserSerializer.UserSerializer(user)
    data.append(userSerializer.data)

    user = User("b@alphbet.com", "B", "Alphabet")
    userSerializer = UserSerializer.UserSerializer(user)
    data.append(userSerializer.data)

    return Response({
        'status' : 200,
        'data' : data
    })
