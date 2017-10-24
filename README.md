# ReplaceMyFood
Demo: [ReplaceMyFood](https://replace-my-food.herokuapp.com/)
## What is ReplaceMyFood?
Living in Waterloo, Ontario I see an enormous number of small food and produce vendors either at markets
in Waterloo, Kitchener, or Saint Jacobs. On the other hand, most of the food that I consume on a day to day
basis (along with most students) is mass produced and imported. I want to use
ReplaceMyFood for twp purposes. The first is to give food vendors a place to
make themselves known and show what local, seasonal produce can replace
the imported and out of season produce. The second reason is to identify and
prove a demand for local products. By trapping the location and searches of
buyers, we can analyze what producst should be produced and sold where.

This does not even apply to the traditional idea of seasonal produce. With the growth
of greenhouse and hydroponic technology, in season means more than just root
vegetables and apples in the fall and canned fruits in the winter.
The accessibility of the data will enable consumers to replace their food
and the analytics dashboard will show potential farmers, both traditional and
not, that there is a market for their current and potential products and where
it might be.

Vendors can add their information to the application along with the market that
they sell their products at. They can also add their products and its seasonal availability.
If they should wish, they can also remove themselves from the system. This
all occurs from the /vendor url which is linked to from the landing page.
Buyers can access information about produce and markets from the /buyer
url which is accessible from the home page. Here a buyer can enter a product
to find local, seasonal alternatives which have been crowd sourced. They can
also enter their location to see vendors nearby.

## Documentation
### Useful Links For Development
* Django: The framework that ReplaceMyFood is built on
    * [Django Documentation](https://docs.djangoproject.com/en/1.11/)
* PostgreSQL: The database used in the production system. Extendability allows for easy addition of database level encryption
    * [PostgreSQL Documentation](https://www.postgresql.org/docs/)
* Django control-center: The add-on to allow the simple creation of widget based dashboards for data analytics
    * [Django Control-center Documentation](https://django-controlcenter.readthedocs.io/en/latest/)
* Django-pgcrypto: Package for integrating encryption at the database layer into postgresql
    * [Django-pgcrypto Documentation](https://django-pgcrypto.readthedocs.io/en/latest/)
* Python-decouple: Increase security and easy of deployment by moving installation unique variables from the code base to an environment file
    * [Python-decouple Documentation](https://pypi.python.org/pypi/python-decouple)
### Local Setup
0. (Optional but highly recommended) Setup a [Virtualenv](https://virtualenv.pypa.io/en/stable/) and then cd into it and activate it (see link for details)
1. Git clone the project
2. Install dependencies with pip from the root of the project
```
pip install -r requirements.txt
```
3. Copy the .env.dist file to a .env file and replace the default values
4. If using PostegreSQL, follow the link above for installation instructions
5. From the project root run the database migrations
```
python manage.py migrate
```
6. Generate a super admin user by running
```
python manage.py createsuperuser
```
7. Run the development server with
```
python manage.py runserver
```
### Development Notes
* Any time a change is made to the models file then a migration must be created and run by executing the following
```
python manage.py makemigration
python manage.py migrate
```
* Currently everything is sitting in the app project. As this grows it
should be factored out for greater reusability
* All of the dashboard functionality is in a single file at the project root
* views.py contains the logic of the routes, models.py contains the data structure and connections, and the root directory
templates contains all of the templates which all inherit from base.html to give basic bootstrap styling
* When looking at the database, the personal information of vendors is
stored behind an encryption layer. The use of this can be seen in models.py. Any further
personal information entered should follow this pattern.

## Reflections

### Tools and Framework

#### Django
I chose Django for this project for several reasons. The first reason is
that it provides a large amount of the functionality required for a web
application with minimal configuration. The admin functionality allows for
manipulation of models and database entries as soon as the models have
been defined and migrated. There is also a great range of tools in the
manage.py toolbox such as a development server that listens for changes
and an analyzer for sql migrations. From a prototyping and rapid devlopment
viewpoint this is optimal as the development focus can just be
the business logic implementation.

In terms of databases, I initially developed on sqlite for its ease of setup
but switched to PostgreSQL at a later stage due to its greater extensability,
especially in terms of encryption modules.

#### Heroku
I used Heroku to host the application. This decision was made for several reasons.
The first was for the security benefits which will be discussed later and the second
was for simplicity. Heroku provides a very streamlined deployment process
useing one git push command and requires very little reconfiguring of the application.
While the free tier does "sleep" and "wake", it is still an optimal solution
for secure and simple hosting with little required effort. It also includes
a PostgreSQL module which is used.

### Challenges

#### Static file serving
When working locally in development mode everything functioned normally
initially, but when moving to a more secure, production setup with debugging
turned off, the serving of static files become unpredictable and complicated.
I first noticed this when testing production mode locally and noticed that all
of the css had disappeared. I turned to the internet and found about 15 solutions
to this problem almost all of which where different. To solve this problem
I looked down to the officially supported documentation for a starting point
both for Heroku and for Django to see some starting points which allowed
me to ignore most of the user supplied solutions. The problem ended up being
with the recommended static file engine and its requirement that there
be a directory called statics in the project root. Creating that and committing
it solved this particular problem.

This problem relates to the general challenge I faced of moving from a development
setup to a production setup. Out of the box, Django is not configured to run
in a production environment. Through a process of research and trial and error
I learned that things like production environment variable configuration,
Gunicorn setup (production server) and static files must be handled in differently in
a production environment.

#### Time Prioritization and Package Usage
Due to midterm season I have had to prioritize my time well. As with any
project, and any prototype project in particular, I attempted to use external
packages whenever possible to avoid reinventing the wheel. I also was careful with
my choosing in order to pick the best tool and package for the job.

An example of this was the choice to use PostegreSQL in order to take advantage
of its extensibility. After some research I noticed that MySQL and SQLite both allow
for encryption but that there was no built in package to handle it. Either
would require added development and work on the server. As the project was being built
quickly, this would take time and necessary security precautions could be overlooked
so using a stable package with the right SQL Database for the task was the right decision.

Other examples of this was using built a built in dashboard package for Django
as well as the built in admin functionality for django.

#### Finding the Value Proposition
While this project originated from a personal interest in how we can increase
local and sustainable farming, I struggled to see what the value proposition was.
Small farmers do not have the money to pay for advertising and they are the only ones
where the value proposition came from. I began, however, to think of how anyone could
become a small scale farmer if they had a greenhouse and or a hydroponic system.
I recalled learning about The Netherlands' enormous food export due to their use of
greenhouses and how we could replicate that on a smaller scale in sub-urban and rural
areas in Canada. The real value, I realized, of ReplaceMyFood would be to see
where the demand for food and food item replacements could be found and use that
to grow a new industry.

### Encryption
I will provide an overview from the bottom up of how a production encryption
system is integrated into ReplaceMyFood to protect vendor data.

#### Database level
In a typical database, data is stored as is. This is fine if there is an absolute
guarantee that no malicious attacker will gain access to the database. This should
be the goal but can never be perfectly achieved. To combat this, I have implemented
a field level encryption for specific sensitive data in the database. The data is scrambled
and unscrambled by the system when it is written and read but remains in an unreadable state
when sitting in the database. Note that this still has the issue that an attacker
who gains access to the code on the production server will be able to see how this encryption
is performed and then manually decrypt and data they would like.


#### Database to Server Level
The data also must be passed between the server and the database. As this is
a prototype project there is no need to built this encryption on your own.
This would be done by holding a key in the database and in the server and then locking
and unlocking any data that passes between the two so that it cannot be intercepted.
By using Heroku for the hosting I have avoided having to handle this issue as
it is done automatically and at a security level I could not implement on a short
time scale on my own.

#### Server Level
Notice that there was one vulnerability at the database level which is handled at
the server level. All of the code and production is secured by Heroku's own
two factor authentication which is required to deploy any code. This forces all changes to
come from me and any access to be limited to me. Any sensitive data such as
encryption keys is also stored directly in Heroku to avoid allowing a malicious attacker to
view it on, for example, Github.

#### Request Level
In the same way that the server to database encryption is handled by Heroku,
so to is the server to browser communication. Any data passed from the website to
the browser or the reverse will use Heroku's (and by extension Salesforce's) certificate
and keys to encrypt it. This process is called https and means that any data sent
from a browser (including names and phone numbers) are not visible of an attacker
is able to intercept a message.


### Analytics Dashboard

#### Implementation
The implementation of the analytics dashboard is quite simple. The
goal right now is just to be able to see the current state of the application
as well as the most popular queries. I used an addon to Django that
allowed for widgets to be configured and placed in a sub-route of the admin
panel. I included a model called a Query that is logged in the database every time a user
searches for a product which includes their location and the time.

The nice aspect of this implementation is that the dashboard can easily be
extended by adding more widgets and the Query object can be modified to include
more data as it can be captured.

#### Goals
The goal of the analytics dashboard is to see what food people are searching
for and when along with where the suppliers are located. This will,
hopefully identify where a greater demand is as well as where the greatest
interest in local products is. It currently only shows a small subset of the potential data.
These limitations and potential improvements will be described in the Next Steps section.

### Next Steps

#### Better Location Service using the Google Maps API
Currently, all of the location data requested and stored relies on users entering
their city and in markets entering their address correctly. It also limits
searches for "near me" at a city level. Google maps provides an api which allows for
distance queries as well as the ability to extract a large amount of data from an address entry.
I would like to integrate this, along with location services, to better track the location of
buyers and sellers and to provide a more tailored experience to users.

#### Greater Input Filtering and Error Handling
Currently, if a vendor mis-spells a name then it will create a duplicate entry for
either the market or the product with the mis-spelled name. This is fine for a prototype
but I would like to add the ability to select an existing entry or add a new one. There are also
a large number of combinations of data that can be entered. The most common invalid ones
are currently scanned for but a robust input scanning and backend to front-end error
message system should be implemented to replace the rudimentary one.

#### Test Framework and Automated Deployment
Django provides a built in test framework. It is not currently used but could easily be
implemented to test that that the correct views are returned given every combinatin of data entered.
Once this is complete then a build and deployment process could be implemented
so that every commit, tests are run and if successful then the new version
would be deployed to production.

#### UI Improvement
The UI is currently a basic, no frills, static html application. It does have
some basic bootstrap styling applied but this is a very basic improvement. I would
like to build this out to use a modern front end framework such as react. The benefit of react is that
it could be integrated at specific points where it is useful while
still taking advantage of Django's built in template engine. This would give the
application a modern appearance.

#### External Data Source Integration
There is an enormous amount of data on seasonality of food, regional demographics,
existing vendors and markets as well as regional preferences. If these could be integrated
both in to the client application as well as the analytics page then a better product could
be provided and more insight could be generated.

#### User Accounts For Vendors
Right now the only user accounts that are used are the built in admin accounts.
Any time a vendor wants to changed their info then they enter their name and validate the change with
their phone number. If an actual account existed then this process could be more securely replaced.

#### More Models and More Relationships
Right now, buyers can search for product replacements and markets but cannot see what is sold at each market.
I would like to create Link objects that link products to Vendors in order to show whether
a replacement product is available nearby. I would also like to show more
info about markets and vendors by including hours and days open. Lastly, currently the
Vendors each have one Market which could be unrealistic. I would like to create
a many to many relationship that more accurately models real life.


