# quick_django_db

## Initial build

Change directory to root project directory, the directory containing the README, requirements, and gitignore files.  Execute the following to build the database.

'''bash
build\initial_build.bat
'''

During the build, you will be prompted for a username, email, and password.  This will be the user information for a superuser in the Django admin portal.

## Using the Admin Portal

Open a Command Prompt window, navigate to `quick_django_db\quick_django_db` directory (the directory containing manage.py), and execute

'''bash
python manage.py runserver 127.0.0.1:8000
'''

This will broadcast the admin portal on your own computer.  Under these settings it is not accessible by any other machines.  In your browser, navigate to `127.0.0.1:8000/admin/` and log in with the credentials set during build.  

If you forget your credentials and can't log in, you can create another superuser with the commands

'''bash
python manage.py createsuperuser
'''

The build will also initialize the server on the local host.

## Making changes to the databases

Table definitions are contained in the `quick_django_db\qdb\models.py` file in the form of Django `Model` classes.  

'''python
class <ClassName>(models.Model):
    <field_name> = models.<Django model>(parameters)

    class Meta:
        db_table = '<table_name>'
        ordering = ["<field_name>","<field_name>"]
        verbose_name = '<Verbose description - singular>'
        verbose_name_plural = '<Verbose description - plural>'

    # Fields displayed in admin portal record list view
    def admin_list_display(self):
        return ['<field_name>', '<field_name>','<field_name>']
'''

In order for the data to appear in the admin portal, you must register the relevant Class in the quick_django_db settings file.  Open `quick_django_db\quick_django_db\settings.py` and add the `<ClassName?` from the definition above as a string to the list `REGISTERED_CLASSES`.

Open a Command Prompt window, navigate to `quick_django_db\quick_django_db` directory (the directory containing manage.py), and execute

'''bash
python manage.py makemigrations
python manage.py migrate
'''

All Classes in the models.py file will be in the database, as long as you run the `makemigrations` and `migrate` commands.  Only the tables associated to the Classes listed in `REGISTERED_CLASSES` will be in the admin portal.
