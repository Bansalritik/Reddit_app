# Reddit_app
A web application that allows user to login to their reddit account and fetches all the allowed data, It shows the only shows the link posts of all the subreddits you have joined, the top authors who have shared most of the links and also the top domains in all the posts.<br>
 ``If you want to have a demo of the web app you can`` [click here](https://pure-reaches-41056.herokuapp.com/)
 
### Approach:
A model is defined that contains all the attributes stored in the SQLite table. The model contains all the structure that stores the data that will be needed to use up in the webapp. 
A wrapper called ``praw`` has been used here which takes an instatnce connected to the reddit id as soon as the client logins to reddit and then used the saame to fetch data by defining different scopes. The data is stored in the database which is then fetched according to the needs and shown to the client by using HTML, CSS for the frontend integrated with the backend.
   
### Steps to run:
    Requirements:
               Any platform that is capable of running django(used PyCharm here).
    Commands:
              Installation Commands:
                               pip install -r requirements.txt
              Running Commands:
                               Migrating Models(database):
                                            python manage.py makemigrations
                                            python manage.py migrate
                               Local Host Run:
                                            python manage.py runserver

To get connected to reddit by python is used the ``praw wrapper`` which makes it easier to connect and use reddit using python. Go to [www.reddit.com/prefs/apps](www.reddit.com/prefs/apps) and create an app and then used the generated CLIENT_ID and the CLIENT_SECRET to create an instance. Fill out the REDIRECT_URI as the Uri you want to be redirected to after recieving the token -

      Redditt = praw.Reddit(  client_id="CLIENT_ID",
                              client_secret="CLIENT_SECRET",
                              redirect_uri="REDIRECT_URI",
                              user_agent="USER_AGENT"   )


Here , You can create a ``superuser`` that you can have access to using:
      Run:
          python manage.py createsuperuser
      Now enter the credentials you want and have access to it using
          URL: (localhost)/admin/
          usrename: USERNAME
          password: USERPASSWORD
      
### Result:
    As the app starts running it takes the client to the login page and asks for the permissions.
    Then the data is fetched and the SQLite database is updated with the client's data.
    The data is then fetched from the database and displayed accordingly using HTML and CSS.

## SAMPLE IMAGES:
<div class="ui small images">
  <img src=https://github.com/Bansalritik/Reddit_app/blob/master/redditsaver/static/images/Screenshot%20(395).png width=400px>
  <img src= https://github.com/Bansalritik/Reddit_app/blob/master/redditsaver/static/images/Screenshot%20(394).png width=400px>
</div>
<div>
 <div>
  <img src = https://github.com/Bansalritik/Reddit_app/blob/master/redditsaver/static/images/Screenshot%20(395).png width=400px>
 </div>
 <div>
  <img src = https://github.com/Bansalritik/Reddit_app/blob/master/redditsaver/static/images/Screenshot%20(394).png width=400px>
 </div>
</div>
 


## Tech-Stack:
             HTML, CSS, Python, SQLite, Django


## Credits

     Created and Developed By: Ritik Bansal
     Contact Email: ritik.4545@gmail.com
   
   
   
   
   
   
