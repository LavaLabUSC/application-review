from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from .models import application

@csrf_exempt
def index(request):
	resp = {}
	
	# get a new applicant
	newApplicants = application.objects.filter(annotated=False)
	currentApplicant = newApplicants[0]
	
	# save as annotated so no one else can try to edit this person
	currentApplicant.annotated = True
	currentApplicant.save()

	# saving annotated applicant
		# if not annotator in request.session:
		# 	request.session['annotator'] = request.POST.get('offset')
		# resp['annotator'] = request.session['annotator']

	return render(request,'index.html',resp)
