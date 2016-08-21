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
	# currentApplicant.save() # TODO: uncomment this in production!

	# saving annotated applicant
		# if not annotator in request.session:
		# 	request.session['annotator'] = request.POST.get('offset')
		# resp['annotator'] = request.session['annotator']

	resp['fullName'] = currentApplicant.fullName
	resp['email'] = currentApplicant.email
	resp['uscId'] = currentApplicant.uscId
	resp['major'] = currentApplicant.major
	resp['minor'] = currentApplicant.minor
	resp['gradYear'] = currentApplicant.gradYear
	resp['available'] = currentApplicant.available
	resp['roles'] = currentApplicant.roles
	resp['otherRole'] = currentApplicant.otherRole
	resp['desiredOutcome'] = currentApplicant.desiredOutcome
	resp['contribution'] = currentApplicant.contribution
	resp['recentProj'] = currentApplicant.recentProj
	resp['dailyProb'] = currentApplicant.dailyProb
	resp['excitingTech'] = currentApplicant.excitingTech
	resp['devToolsSoft'] = currentApplicant.devToolsSoft
	resp['devToolsHard'] = currentApplicant.devToolsHard
	resp['designTools'] = currentApplicant.designTools
	resp['otherTools'] = currentApplicant.otherTools
	resp['resume'] = currentApplicant.resume
	resp['portfolio'] = currentApplicant.portfolio
	resp['whatWork'] = currentApplicant.whatWork
	resp['otherOrg'] = currentApplicant.otherOrg
	resp['referral'] = currentApplicant.referral
	resp['joke'] = currentApplicant.joke

	return render(request,'index.html',resp)
