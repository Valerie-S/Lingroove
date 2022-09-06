from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ChatRoom


# Create views to show a list of rooms
@login_required  # make sure only logged in user can view this
def show_rooms(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def show_room_detail(request, room_id):
    room = ChatRoom.objects.get(room_id=room_id)
    return render(request, 'room/room_detail.html', {'room': room})