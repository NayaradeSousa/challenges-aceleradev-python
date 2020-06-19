from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter


@api_view(['POST'])
def lambda_function(request):
    if request.method == 'POST':
        data = request.data.get('question')

        answer = []
        for items, num in Counter(data).most_common():
            answer.extend([items] * num)
    return Response({'solution': answer})
