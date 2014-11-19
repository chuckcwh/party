from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from partyApp.api.permissions import IsOwnerOrReadOnly
from partyApp.api.serializers import PartySerializer, ProfileSerializer
from partyApp.models import Party, Profile


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    # filter_fields = ('', 'first_name', 'last_name',)
    # search_fields = ('first_name', 'last_name', 'about',)
    # ordering_fields = ('first_name', 'last_name',)
    # ordering = ('-date_joined',)


# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     filter_fields = ('owner__username', 'follower__username')
#     permission_classes = (IsOwnerOrReadOnly,)
#     # ordering = ('-created_time',)
#
#     def pre_save(self, obj):
#         obj.owner = self.request.user
#
#     def get_queryset(self):
#         queryset = Project.objects.all()
#         username = self.request.QUERY_PARAMS.get('username', None)
#         if username is not None: # Optionally filters against 'username' query param
#             queryset = queryset.filter(owner__username=username)
#         return queryset
#
#     @detail_route(methods=['post'])
#     def follow(self, request, pk):
#         project = Project.objects.get(pk=pk)
#         follower_id = request.DATA.get('follower', None)
#         project.follower.add(follower_id)
#         return Response(status=status.HTTP_200_OK)
#
#     @detail_route(methods=['post'])
#     def followMe(self, request, pk):
#         project = Project.objects.get(pk=pk)
#         project.follower.add(request.user.id)
#         return Response(status=status.HTTP_200_OK)