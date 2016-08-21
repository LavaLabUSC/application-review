from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from .models import application

@csrf_exempt
def index(request):
	resp = {}
	
	# saving annotated applicant if exists
	annotator = request.POST.get('annotator')
	if annotator:
		applicantEmail = request.POST.get('applicantEmail')
		subtApplicants = application.objects.filter(email=applicantEmail)
		subtApplicant = subtApplicants[0]
		subtApplicant.dedicationRating = request.POST.get('determined')
		subtApplicant.resourcefulRating = request.POST.get('resourceful')
		subtApplicant.experienceRating = request.POST.get('experienced')
		subtApplicant.imaginationRating = request.POST.get('imaginative')
		subtApplicant.naughtyRating = request.POST.get('naughty')
		subtApplicant.notes = request.POST.get('final')
		subtApplicant.final = request.POST.get('finalDec')
		subtApplicant.annotator = annotator
		subtApplicant.save()

	# get a new applicant
	newApplicants = application.objects.filter(annotated=False)
	currentApplicant = newApplicants[0]
	
	# save as annotated so no one else can try to edit this person
	currentApplicant.annotated = True
	currentApplicant.save() # TODO: uncomment this in production!

	resp['annotator'] = annotator
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
