from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer, LoginSerializer
from .models import User, Device, Keazy
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)


class AssociateKeazyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        device_id = request.data.get('device_id')
        try:
            device = Device.objects.get(device_id=device_id)
        except Device.DoesNotExist:
            return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)

        keazy = Keazy.objects.create(user=request.user, device=device)
        return Response({'message': 'Keazy associated successfully'}, status=status.HTTP_201_CREATED)

class OpenDeviceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        device_id = request.data.get('device_id')
        try:
            keazy = Keazy.objects.get(user=request.user, device__device_id=device_id)
        except Keazy.DoesNotExist:
            return Response({'error': 'Device not associated with this user'}, status=status.HTTP_404_NOT_FOUND)

        # Simulate sending open command to the device
        # Here you would implement the actual logic to send the command to the Raspberry Pi
        # For this example, we just return a success message
        return Response({'message': f'Device {device_id} opened successfully'}, status=status.HTTP_200_OK)