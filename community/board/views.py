from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, PostDetailSerializer
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
    post = serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def post_detail(request, pk):
  try:
    post = Post.objects.get(pk=pk)
    serializer=PostDetailSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)
  except Post.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def post_update(request, pk):
  try:
    post = Post.objects.get(pk=pk)
    serializer=PostSerializer(post, data=request.data)
    if serializer.is_valid():
      updated_post = serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
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
  try:
    post=Post.objects.get(id=post_id)
  except Post.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  comments = post.comments.all()
  serializer = CommentSerializer(comments, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def comment_create(request, post_id):
  try:
    post = Post.objects.get(id = post_id)
  except Post.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  serializer=CommentSerializer(data=request.data)
  if serializer.is_valid():
    comment = serializer.save(post = post)
    return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
