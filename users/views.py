from django.shortcuts import render, redirect
from controller.models import Device
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, logout, login
User = get_user_model()


# Create your views here.
def dashboard(request):
    bulb, _ = Device.objects.get_or_create(name="Bulb")
    if request.method == "POST":
        bulb.status = not bulb.status
        bulb.save()
        return redirect('dashboard')  
    return render(request, 'dashboard.html', {'bulb': bulb})



# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            return redirect('dashboard')
        else: 
            error = 'Invalid username or password.'
            return render(request, 'login.html', {'error': error})
        
    # Redirect already logged-in users
    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login') 


from django.http import StreamingHttpResponse
from django.shortcuts import render
import cv2

# Replace this with your iPhone IP Camera URL
CAMERA_URL = "http://192.168.18.18:8080/video"

def index(request):
    """Render the main page"""
    return render(request, 'live.html')


def generate_frames():
    """Continuously capture frames from IP camera"""
    camera = cv2.VideoCapture(CAMERA_URL)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def video_feed(request):
    """Return live stream"""
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
