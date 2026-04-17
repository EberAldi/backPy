from rest_framework.decorators import api_view
from rest_framework.response import Response
import bcrypt
from .models import User

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'message': 'Usuario no encontrado'}, status=404)

    if not bcrypt.checkpw(password.encode(), user.password.encode()):
        return Response({'message': 'Contraseña incorrecta'}, status=401)

    return Response({
        'message': 'Login exitoso',
        'user': {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
    })