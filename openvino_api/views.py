import os

from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

from openvino_api.app import main
from openvino_api.settings import BASE_DIR


@csrf_exempt
def StartApp(request):
    if request.method == 'POST':
        image = request.FILES['file']
        type = request.POST['optradio']
        if type == 'TEXT':
            model = "/models/text-detection-0004.xml"

        elif type == 'CAR_META':
            model = "/models/vehicle-attributes-recognition-barrier-0039.xml"

        elif type == 'POSE':
            model = "/models/human-pose-estimation-0001.xml"
            
        elif type== 'PEDESTRIAN':
            model="/models/person-detection-retail-0013.xml"
        else:
            return render(request, "home.html")
        fs = FileSystemStorage()
        img = fs.save(image.name, image)
        res = main(img, type, model)
        request.session['picture'] = res
        return redirect('/feedback')
    return render(request, "home.html")


@csrf_exempt
def feedback(request):
    previous_url = request.META.get('HTTP_REFERER')
    if previous_url is None:
        return redirect('/')
    if request.method == 'POST':
        message = request.POST['message']
        message = str(message)
        feedback_file_path = str(BASE_DIR) + "/static/" + str('feedback.txt'),
        if not feedback_file_path:
            os.mknod(feedback_file_path)
        feedback = open("static/feedback.txt", "a+")
        feedback.write(message + "\n\n")
        feedback.close()
        return redirect('/')
    picture = request.session.get('picture')
    return render(request, "feedback.html", {"picture": picture})
