from django.shortcuts import render
from rest_framework.response import Response
from api.models import User, Todo
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from api.serializers.todo import TodoListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
import logging


logger = logging.getLogger(__name__)

class ListTodoAPI(APIView):
    '''
        GET Request:
            - Return a list of all tasks in the todo table.
    '''

    authentication_classes = [BasicAuthentication] 
    permission_classes = [IsAuthenticated] 
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo_list.html'

    def get(self, request, format=None):
        try:
            todo = Todo.objects.all()
            logger.info(f"User {request.user} accessed the task list.")
            return Response({"todo": todo}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching task list: {str(e)}", exc_info=True)
            return render(request, "error.html", status=status.HTTP_404_NOT_FOUND)


class DetailTodoApi(APIView):
    '''
        GET (PK) Request:
            - Returns a matching task in the todo table.
    '''
    authentication_classes = [BasicAuthentication] 
    permission_classes = [IsAuthenticated] 
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'detail_todo.html'

    def get(self, request,  pk=None, format=None):
        '''
            Return a single todo'
        '''
        try:
            todo = Todo.objects.get(id=pk)
            logger.info(f"User {request.user} accessed task ID {pk}.")
            return Response({"todo": todo}, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            logger.error(f"User {request.user} tried to access a non-existent task ID {pk}.")
            return render(request, "error.html", status=status.HTTP_404_NOT_FOUND)



class CreateToDoAPI(APIView):
    '''
        POST: Create Task and store it in the todo table
        
    '''
    authentication_classes = [BasicAuthentication] 
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        return render(request, 'create_todo.html')

    def post(self, request):
        try:
            user = request.user

            data = request.POST.copy() #make it mutable
            data['user'] = user.id
            serializer = TodoListSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return render(request, "success.html", {"data": serializer.data, "msg": "Task created successfully"}, status=status.HTTP_201_CREATED)
            return render(request, 'create_todo.html', {'errors': serializer.errors})
        except Exception as e:
            logger.error(f"Task not created: {request.user}: {str(e)}", exc_info=True)
            return render(request, "error.html", status=status.HTTP_404_NOT_FOUND)


class UpdateDeleteToDoApi(APIView):
    '''
        Works for Updation and Deletion of Tasks
    '''
    authentication_classes = [BasicAuthentication] 
    permission_classes = [IsAuthenticated] 
    
    def put(self, request, pk=None):
        try:
            todo = Todo.objects.get(id=pk)
            serializer = TodoListSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"todo": serializer.data, "msg": "Task Updated"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Todo.DoesNotExist:
            logger.error(f"Task not found, requested by {request.user}", exc_info=True)
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk, format=None):
        try:
            user = request.user.id
            todo = Todo.objects.get(id=pk)
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            logger.error(f"Task not found, requested by {request.user}", exc_info=True)
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
    