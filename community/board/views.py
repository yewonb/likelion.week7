from .models import Post
from .models import Comment
from .serializers import PostSerializer
from .serializers import CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def post_list(request):
  posts=Post.objects.all()
  serializer=PostSerializer(posts, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)
  
@api_view(['POST'])  
def post_create(request):    
  serializer=PostSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
@api_view(['GET'])
def post_detail(request, pk):
  try:
    post = Post.objects.get(pk=pk)
    serializer=PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)
  except Post.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def post_update(request, pk):
  try:
    post = Post.objects.get(pk=pk)
    serializer=PostSerializer(post, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
  except Post.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def post_delete(request, pk):
  try:
    post = Post.objects.get(pk=pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  except Post.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def comment_list(request, post_id):
  comments = Comment.objects.filter(post=post_id)
  serializer = CommentSerializer(comments, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def comment_create(request, post_id):
  serializer=CommentSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
