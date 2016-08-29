from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required

# csv handling
import csv
# from djqscsv import render_to_csv_response

# models
from .models import application

@csrf_exempt
@login_required
def index(request):
	resp = {}
	
	# saving annotated applicant if exists
	emailLookup = request.GET.get('email')
	annotator = request.POST.get('annotator')
	other = request.GET.get('other')
	developer = request.GET.get('developer')
	designer = request.GET.get('designer')
	product = request.GET.get('product')

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
	if developer is not None:
		newApplicants = application.objects.filter(annotated=False,developer=True)
	elif emailLookup is not None:
		newApplicants = application.objects.filter(email=emailLookup)
	elif designer is not None:
		newApplicants = application.objects.filter(annotated=False,designer=True)
	elif product is not None:
		newApplicants = application.objects.filter(annotated=False,product=True)
	elif other is not None:
		newApplicants = application.objects.filter(annotated=False,other=True)
	else:
		newApplicants = application.objects.filter(annotated=False)
	currentApplicant = newApplicants[0]
	
	# save as annotated so no one else can try to edit this person
	currentApplicant.annotated = True
	# currentApplicant.save() # TODO: uncomment this in production!

	resp['roleView'] = "Role: "
	if currentApplicant.developer:
		resp['roleView'] += "Developer "
	if currentApplicant.designer:
		resp['roleView'] += "Designer "
	if currentApplicant.product:
		resp['roleView'] += "Product "
	if currentApplicant.other:
		resp['roleView'] += "Other "

	if annotator is not None:
		resp['annotator'] = annotator
	resp['fullName'] = currentApplicant.fullName
	resp['email'] = currentApplicant.email
	resp['uscId'] = currentApplicant.uscId
	resp['major'] = currentApplicant.major
	resp['minor'] = currentApplicant.minor
	resp['gradYear'] = currentApplicant.gradYear
	resp['available'] = currentApplicant.available
	resp['developer'] = currentApplicant.developer
	resp['designer'] = currentApplicant.designer
	resp['product'] = currentApplicant.product
	resp['other'] = currentApplicant.other
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
	resp['dedicationRating'] = currentApplicant.dedicationRating
	resp['resourcefulRating'] = currentApplicant.resourcefulRating
	resp['experienceRating'] = currentApplicant.experienceRating
	resp['imaginationRating'] = currentApplicant.imaginationRating
	resp['naughtyRating'] = currentApplicant.naughtyRating
	resp['notes'] = currentApplicant.notes
	resp['final'] = currentApplicant.final

	return render(request,'index.html',resp)

@csrf_exempt
@login_required
def all(request):
	resp = {}
	# for getting and displaying all applicants by type
	
	resp['applicants'] = []

	newApplicants = application.objects.all()
	
	for each in newApplicants:
		singleApplicant = {}
		singleApplicant['fullName'] = each.fullName
		singleApplicant['email'] = each.email
		singleApplicant['major'] = each.major
		singleApplicant['gradYear'] = each.gradYear
		singleApplicant['roleView'] = ""
		if each.developer:
			singleApplicant['roleView'] += "Developer "
		if each.designer:
			singleApplicant['roleView'] += "Designer "
		if each.product:
			singleApplicant['roleView'] += "Product "
		if each.other:
			singleApplicant['roleView'] += "Other "
		resp['applicants'].append(singleApplicant)
		print(singleApplicant['fullName'])

	return render(request,'all.html',resp)

@csrf_exempt
@login_required
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


# @csrf_exempt
# @login_required
# def downloadCSV(request):
# 	allApplications = application.objects.all().values('fullName', 'email', 'uscId', 'major', 'minor', 'gradYear', 'available', 'developer', 'designer', 'product', 'other', 'otherRole', 'desiredOutcome', 'contribution', 'recentProj', 'dailyProb', 'excitingTech', 'devToolsSoft', 'devToolsHard', 'designTools', 'otherTools', 'resume', 'portfolio', 'whatWork', 'otherOrg', 'referral', 'joke', 'annotated', 'dedicationRating', 'resourcefulRating', 'experienceRating', 'imaginationRating', 'naughtyRating', 'notes', 'annotator', 'final')
# 	return render_to_csv_response(allApplications)
