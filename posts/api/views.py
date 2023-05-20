
from posts.models import Post
from posts.api.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer( posts , many = True )
    return Response(serializer.data)

@api_view(['POST'])
def addPost(request):
    data = request.data
    post = Post.objects.create(
        title = data['title'],
        content = data['content']
    )
    serializer = PostSerializer(post , many = False)
    return Response(serializer.data)

@api_view(['UPDATE'])
def updatePost(request):
    data = request.data
    post = Post.objects.get(id = data['id'])
    serializer = PostSerializer(instance = post, data = data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PATCH'])
def getPost(request):
    data = request.data
    post = Post.objects.get(id = data['id'])
    serializer = PostSerializer(post , many = False)
    return Response(serializer.data)

