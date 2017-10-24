# ReplaceMyFood
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

#### PostgrSQL

#### Heroku


### Challenges

#### Static file serving

#### Time Prioritization and Package Usage

#### Finding the Value


### Encryption

#### Database level

#### Database to Server Level

#### Request Level


### Analytics Dashboard

#### Implementation

#### Goals


### Next Steps

#### Better Location Service using the Google Maps API

#### Greater Input Filtering and Error Handling

#### Test Framework and Automated Deployment

#### Self Cert and DNS

#### UI Imporvement

#### External Data Source Integration


