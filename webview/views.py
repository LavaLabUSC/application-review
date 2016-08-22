from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
import csv

from .models import application

@csrf_exempt
@login_required
def index(request):
	resp = {}
	
	# saving annotated applicant if exists
	annotator = request.POST.get('annotator')
	if annotator:
		applicantEmail = request.POST.get('applicantEmail')
		subtApplicants = application.objects.filter(email=applicantEmail)
		subtApplicant = subtApplicants[0]
		try:
			subtApplicant.dedicationRating = int(request.POST.get('determined'))
		except:
			print("the annotator skipped something!")
		try:
			subtApplicant.resourcefulRating = int(request.POST.get('resourceful'))
		except:
			print("the annotator skipped something!")
		try:
			subtApplicant.experienceRating = int(request.POST.get('experienced'))
		except:
			print("the annotator skipped something!")
		try:
			subtApplicant.imaginationRating = int(request.POST.get('imaginative'))
		except:
			print("the annotator skipped something!")
		try:
			subtApplicant.naughtyRating = int(request.POST.get('naughty'))
		except:
			print("the annotator skipped something!")
		try:
			subtApplicant.notes = request.POST.get('final')
		except:
			print("the annotator skipped something!")
		try:
			subtApplicant.final = request.POST.get('finalDec')
		except:
			print("the annotator skipped something!")
		try:
			subtApplicant.annotator = annotator
		except:
			print("the annotator skipped something!")
		subtApplicant.save()

	# get a new applicant
	newApplicants = application.objects.filter(annotated=False)
	currentApplicant = newApplicants[0]
	
	# save as annotated so no one else can try to edit this person
	currentApplicant.annotated = True
	currentApplicant.save() # TODO: uncomment this in production!

	if annotator is not None:
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


def uploadCSV(request):
	
	# application.objects.all().delete()

	reader = [
	]
	
	for each in reader:
		roles = each[8] + "," + each[9] + "," + each[10] + "," + each[11]
		singleApplicant = application(fullName=each[1],email=each[2],uscId=each[3],major=each[4],minor=each[5],gradYear=each[6],available=each[7],roles=roles,otherRole=each[12],desiredOutcome=each[13],contribution=each[14],recentProj=each[15],dailyProb=each[16],excitingTech=each[17],devToolsSoft=each[18],devToolsHard=each[19],designTools=each[20],otherTools=each[21],resume=each[22],portfolio=each[23],whatWork=each[24],otherOrg=each[25],referral=each[26],joke=each[27])
		singleApplicant.save()
		print(each[1])

	return HttpResponse("Completed.")
