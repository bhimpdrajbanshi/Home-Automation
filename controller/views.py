from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Device

# Web dashboard control
def dashboard(request):
    bulb, _ = Device.objects.get_or_create(name="Bulb")
    if request.method == "POST":
        bulb.status = not bulb.status
        bulb.save()
        return redirect('dashboard')
    return render(request, 'dashboard.html', {'bulb': bulb})

# API: Get bulb status (for ESP32 or dashboard)
def get_status(request):
    bulb, _ = Device.objects.get_or_create(name="Bulb")
    return JsonResponse({"status": bulb.status})

# ✅ NEW API: Update bulb status (ESP32 can call this)
@csrf_exempt
def control_bulb(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            status = data.get("status", None)
            if status is None:
                return JsonResponse({"error": "Missing 'status' field"}, status=400)
            bulb, _ = Device.objects.get_or_create(name="Bulb")
            bulb.status = bool(status)
            bulb.save()
            return JsonResponse({"message": "Bulb updated", "status": bulb.status})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "POST only"}, status=405)
