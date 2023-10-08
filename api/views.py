from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = [
    {
        "name": "Bekpolat Normurodov Ergash O'g'li",
        "card":[
            "8600 8790 6789 5482"
        ]
    }
]
    return Response(person)