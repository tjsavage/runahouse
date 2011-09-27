from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

import hmac, hashlib

def login(request):
	return HttpResponseRedirect('http://www.stanford.edu/~tjsavage/cgi-bin/webauth/?next=%s' % settings.AUTH_URL)
	
def authenticate(request):
	hmac_obj = hmac.new("i48S(Se8fh29&#(#gfs83&gd8f@&#", request.GET['username'], hashlib.md5)
	if hmac_obj.hexdigest() == request.GET['hash']:
		return HttpResponse("Success!")
	else:
		return HttpResponse("Failure: username %s, hash %s, digest %s" % (request.GET['username'], request.GET["hash"], hmac_obj.hexdigest()))