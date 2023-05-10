# api/resity_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import RegistationCenterAdmin, Owner, Car, RegistationDoc
from django.contrib.auth.models import User
from .serializers import RegistationCenterAdminSerializer, OwnerSerializer, CarSerializer, RegistationDocSerializer, AdminSerializer

class RegistationCenterAdminApiViewAll(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all center
        '''
        centers = RegistationCenterAdmin.objects.all()
        serializer = RegistationCenterAdminSerializer(centers, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create new center
        '''
        data = {
            'center_name': request.data.get('center_name'), 
            'area': request.data.get('area'), 
            'city': request.data.get('city')
        }
        serializer = RegistationCenterAdminSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class RegistationCenterAdminApiViewInstance(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, center_id, *args, **kwargs):
        '''
        List all center
        '''
        try:
            center = RegistationCenterAdmin.objects.filter(id = center_id)
            serializer = RegistationCenterAdminSerializer(center, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except:
            return Response(
                {
                    'message': 'can not find center',
                    'keyError': 'center_id'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

    # 2. Update
    def put(self, request, center_id, *args, **kwargs):
        '''
        Updates the center item with given center_id if exists
        '''
        center = RegistationCenterAdmin.objects.get(id = center_id)
        if not center:
            return Response(
                {
                    'message': 'can not find center',
                    'keyError': 'center_id'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'center_name': request.data.get('center_name'), 
            'area': request.data.get('area'), 
            'city': request.data.get('city')
        }
        serializer = RegistationCenterAdminSerializer(instance = center, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. Delete
    def delete(self, request, center_id, *args, **kwargs):
        '''
        Deletes the center item with given center_id if exists
        '''
        center = RegistationCenterAdmin.objects.get(id = center_id)
        if not center:
            return Response(
                {
                    'message': 'can not find center',
                    'keyError': 'center_id'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        center.delete()
        return Response(
            {
                "message": "successfully"
            },
            status=status.HTTP_200_OK
        )

class OwnerApiViewAll(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all owner
        '''
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create new owner
        '''
        data = {
            'fullname': request.data.get('fullname'),
            'password': request.data.get('password'), 
            'email': request.data.get('email'), 
            'phone': request.data.get('phone'),
            'indenty': request.data.get('indenty'),
            'birthday': request.data.get('birthday'),
            'accommodation': request.data.get('accommodation'),
            'place_of_birth': request.data.get('place_of_birth')
        }
        serializer = OwnerSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OwnerApiViewInstance(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, owner_id, *args, **kwargs):
        '''
        List all owner
        '''
        try:
            owner = Owner.objects.filter(id = owner_id)
            serializer = OwnerSerializer(owner, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except:
            return Response(
                {
                    'message': 'can not find owner',
                    'keyError': 'owner_id'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

    # 2. Update
    def put(self, request, owner_id, *args, **kwargs):
        '''
        Updates the owner item with given owner_id if exists
        '''
        owner = Owner.objects.get(id = owner_id)
        if not owner:
            return Response(
                {
                    'message': 'can not find owner',
                    'keyError': 'owner_id'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'fullname': request.data.get('fullname'),
            'password': request.data.get('password'), 
            'email': request.data.get('email'), 
            'phone': request.data.get('phone'),
            'indenty': request.data.get('indenty'),
            'birthday': request.data.get('birthday'),
            'accommodation': request.data.get('accommodation'),
            'place_of_birth': request.data.get('place_of_birth')
        }
        serializer = OwnerSerializer(instance = owner, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. Delete
    def delete(self, request, owner_id, *args, **kwargs):
        '''
        Deletes the owner item with given owner_id if exists
        '''
        owner = Owner.objects.get(id = owner_id)
        if not owner:
            return Response(
                {
                    'message': 'can not find owner',
                    'keyError': 'owner_id'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        owner.delete()
        return Response(
            {
                "message": "successfully"
            },
            status=status.HTTP_200_OK
        )

class CarApiViewAll(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all center
        '''
        centers = Car.objects.all()
        serializer = CarSerializer(centers, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create new center
        '''
        data = {
            'center_name': request.data.get('center_name'), 
            'area': request.data.get('area'), 
            'city': request.data.get('city')
        }
        serializer = CarSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CarApiViewInstance(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, center_id, *args, **kwargs):
        '''
        List all center
        '''
        try:
            center = Car.objects.filter(id = center_id)
            serializer = CarSerializer(center, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except:
            return Response(
                {
                    'message': 'can not find center',
                    'keyError': 'center_id'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

    # 2. Update
    def put(self, request, center_id, *args, **kwargs):
        '''
        Updates the center item with given center_id if exists
        '''
        center = Car.objects.get(id = center_id)
        if not center:
            return Response(
                {
                    'message': 'can not find center',
                    'keyError': 'center_id'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'center_name': request.data.get('center_name'), 
            'area': request.data.get('area'), 
            'city': request.data.get('city')
        }
        serializer = CarSerializer(instance = center, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. Delete
    def delete(self, request, center_id, *args, **kwargs):
        '''
        Deletes the center item with given center_id if exists
        '''
        center = Car.objects.get(id = center_id)
        if not center:
            return Response(
                {
                    'message': 'can not find center',
                    'keyError': 'center_id'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        center.delete()
        return Response(
            {
                "message": "successfully"
            },
            status=status.HTTP_200_OK
        )

class RegistationDocApiViewAll(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all center
        '''
        centers = RegistationDoc.objects.all()
        serializer = RegistationDocSerializer(centers, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create new center
        '''
        data = {
            'center_name': request.data.get('center_name'), 
            'area': request.data.get('area'), 
            'city': request.data.get('city')
        }
        serializer = RegistationDocSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class RegistationDocApiViewInstance(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, center_id, *args, **kwargs):
        '''
        List all center
        '''
        try:
            center = RegistationDoc.objects.filter(id = center_id)
            serializer = RegistationDocSerializer(center, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except:
            return Response(
                {
                    'message': 'can not find center',
                    'keyError': 'center_id'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

    # 2. Update
    def put(self, request, center_id, *args, **kwargs):
        '''
        Updates the center item with given center_id if exists
        '''
        center = RegistationDoc.objects.get(id = center_id)
        if not center:
            return Response(
                {
                    'message': 'can not find center',
                    'keyError': 'center_id'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'center_name': request.data.get('center_name'), 
            'area': request.data.get('area'), 
            'city': request.data.get('city')
        }
        serializer = RegistationDocSerializer(instance = center, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. Delete
    def delete(self, request, center_id, *args, **kwargs):
        '''
        Deletes the center item with given center_id if exists
        '''
        center = RegistationDoc.objects.get(id = center_id)
        if not center:
            return Response(
                {
                    'message': 'can not find center',
                    'keyError': 'center_id'
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        center.delete()
        return Response(
            {
                "message": "successfully"
            },
            status=status.HTTP_200_OK
        )

class AdminApiViewAll(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, admin_id, *args, **kwargs):
        '''
        List all center
        '''
        centers = Admin.objects.filter(id = admin_id)
        serializer = AdminSerializer(centers, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create new center
        '''
        data = {
            'center_name': request.data.get('center_name'), 
            'area': request.data.get('area'), 
            'city': request.data.get('city')
        }
        serializer = AdminSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)