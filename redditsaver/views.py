from django.http import HttpResponse
from django.shortcuts import render, redirect
from prawcore import ResponseException
from django.db.models import Count
import praw
from .models import Reddit_Data


# Persisting all the data

def Index(request):
    # Trying to get the code sent here by praw wrapper
    try:
        Code = request.GET['code']  # This is coming back correctly
    except:
        return redirect('/')

    # Creating an instace of the reddit
    Redditt = praw.Reddit(client_id="CLIENT_ID",
                          client_secret="CLIENT_SECRET",
                          redirect_uri="REDIRECT_URL",
                          user_agent="USER_AGENT")

    # Authorizing the instance
    Redditt.auth.authorize(Code)
    Name = Redditt.user.me()

    # Acquiring the list of all the subreddits joined
    Subscribed = list(Redditt.user.subreddits(limit=None))
    for Sub in Subscribed:
        SubRedditt = Redditt.subreddit(str(Sub))
        New_Redd = SubRedditt.new(limit=None)

    # Going through all the subreeddits and its posts and saving the data
        for Submission in New_Redd:
            if not Reddit_Data.objects.filter(Reddit_Id=Submission.id, Reddit_Username=str(Name)).exists():
                temp = False
                Author_Name = ''
                if(not Submission.selftext):
                    print(Submission.selftext)
                    temp = True
                if Submission.author is not None:
                    Author_Name = Submission.author.name

                # Saving the data in sqlite
                Reddit_Data.objects.create(Reddit_Id=Submission.id, Reddit_Title=Submission.title,
                                           Reddit_Comments=Submission.num_comments, Reddit_Username=str(Name),
                                           Reddit_Score=Submission.score, Reddit_Domain=Submission.domain,
                                           Reddit_User=Author_Name, Reddit_Subred=str(Sub), Reddit_Body=Submission.url,
                                           Reddit_Link=temp)

    # Filtering the data and saving in various objects
    Data = Reddit_Data.objects.filter(Reddit_Link=True)
    Users = Reddit_Data.objects.filter(Reddit_Username=str(Name)).values('Reddit_User').annotate(total=Count('Reddit_User')).order_by('-total')[:3]
    Domains = Reddit_Data.objects.filter(Reddit_Username=str(Name)).values('Reddit_Domain').annotate(total=Count('Reddit_Domain')).order_by('-total')[:3]
    Context = {
        'Datas': Data,
        'Users': Users,
        'Domains': Domains,
        'UserName': str(Name)
    }
    # if Data.count()is 0 and Users.count() is 0 and Domains.count() is 0:
    #     return render(request, 'empty.html',Context)
    return render(request, 'redditpage.html', Context)

# Runs initially
def Reddit(request):
    # instance of reddit
    Redditt = praw.Reddit(client_id="CLIENT_ID",
                          client_secret="CLIENT_SECRET",
                          redirect_uri="REDIRECT_URL",
                          user_agent="USER_AGENT")

    # getting the authorization token
    return redirect(Redditt.auth.url(['identity, history, '
                                      'modlog, modposts, modwiki, mysubreddits,read,'
                                      ' save, ''subscribe, wikiread'], "...", "temporary"))

