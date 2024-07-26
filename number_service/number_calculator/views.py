# number_calculator/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import NumberService

number_service = NumberService()

@api_view(['GET'])
def get_numbers(request):
    number_type = request.query_params.get('type')
    if number_type not in ['p', 'f', 'e', 'r']:
        return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

    result = number_service.process_numbers(number_type)
    return Response(result)
