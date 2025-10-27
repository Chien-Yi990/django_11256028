from django.http import HttpResponse

def index(request):
    return HttpResponse("""
<pre>
台北商業大學
五專資管科
11256028
簡翊安
</pre>
""")
