from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Note
from .serializers import NoteSerializer


# Create your views here.
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_note(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    new_Note = NoteSerializer(data=request.data)
    if new_Note.is_valid():
        new_Note.save()
        dataResponse = {
            "msg": "Created Successfully",
            "Note": new_Note.data
        }
        return Response(dataResponse)
    else:
        print(new_Note.errors)
        dataResponse = {"msg": "couldn't create a note"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)



# display note
@api_view(['GET'])
def list_Note(request: Request):
    notes = Note.objects.all()
    dataResponse = {
        "msg": "List of All notes",
        "note": NoteSerializer(instance=notes, many=True).data
    }
    return Response(dataResponse)

#update note
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_note(request : Request, note_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    note = Note.objects.get(id=note_id)
    updated_note = NoteSerializer(instance=note, data=request.data)
    if updated_note.is_valid():
        updated_note.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_note.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)



# delete note
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_note(request: Request, note_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    note = Note.objects.get(id=note_id)
    note.delete()
    return Response({"msg" : "Deleted Successfully"})