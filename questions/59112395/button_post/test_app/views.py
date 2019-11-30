from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from test_app.models import characterTable

def addCharacter(sUserID, sPlayerName, sRace, sPlayerClass, sStr, sCon, sDex, sInt, sWis, sCha):
    print(sRace)
    # c = characterTable()
    # c.userID=sUserID
    # c.playerName = sPlayerName
    # #... rest of fields go here
    # c.save()


# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        userID = 'testUser'
        addCharacter(
            userID,
            str(request.POST.get('characterName')),
            str(request.POST.get('race')),
            str(request.POST.get('class')),
            str(request.POST.get('strength')),
            str(request.POST.get('dexterity')),
            str(request.POST.get('constitution')),
            str(request.POST.get('intelligence')),
            str(request.POST.get('wisdom')),
            str(request.POST.get('charisma'))
        )

        return render(request, self.template_name, {})

class AboutPageView(TemplateView):
    template_name = "about.html"
