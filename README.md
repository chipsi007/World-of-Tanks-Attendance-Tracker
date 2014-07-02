World of Tanks CW Attendance Tracker
====================================

This web application helps a clan keep track of the clan war
attendance of its players and with gold payouts.

Dependencies
------------

* Python 2.7+
* Various Python libraries (See requirements.txt)
  These can be installed via "pip install -r requirements.txt"

Python 2.6 probably works too.

Deployment
----------

As a Python WSGI application, this web application can be deployed in
various ways.
See the Flask documentation (http://flask.pocoo.org/docs/deploying/) for
further information.

Configuration
-------------

* Copy `whyattend/config.py` to `local_config.py` and adjust the settings.
* Put your clan's logo into `whyattend/static/img/clanicons`.
* Replace `whyattend/static/img/header.jpg` with an image of your choice.
* Copy `alembic.ini.template` to `alembic.ini` and set `sqlalchemy.url` to the same value as `DATABASE_URI`
  in `local_config.py`

After deployment, the initial database schema should be generated by
running `python initdb.py` from the shell.

Make sure the `replay_blob` column in the generated replay table is large enough to hold
WoT replay files. In MySQL, for example, the default BLOB type can only store
around 64 kB. This can be changed by running the SQL statement
`ALTER TABLE replay MODIFY replay_blob LONGBLOB`, for example. Additionally, MySQL
defines a `max_allowed_packet` size in `my.cnf`, which might have to be increased.

The clan member roles can be synchronized with Wargaming's server by
opening `/sync-players/<clanid>/?API_KEY=<configured API KEY>`

`config.API_TOKEN` is used to authenticate your application instance with the Wargaming API.
Tokens can be generated on the Wargaming Developer Partner program website, e.g.
[https://eu.wargaming.net/developers/](https://eu.wargaming.net/developers/)

`config.API_KEY` should be set to something random and secret, so only you
can trigger the synchronization.

This can be automated by a cron script, e.g:

    #!/bin/bash
    # Synchronize WHY members
    curl "http://myserver.com/sync-players/500014725?API_KEY=<configured API KEY>"

Database Migration
------------------

When the data model is changed, existing database will have to be migrated to reflect the model changes.
For database migration we use [Alembic](http://alembic.readthedocs.org/). After updating to the latest source code,
make sure to run `alembic upgrade head`, which will issue the necessary SQL statements and bring the database
up to date.

For developers: When making changes to the data model in `model.py`, you should create an Alembic migration file and
check it into version control along the code changes.

Development
-----------

For developing the builtin development HTTP server is sufficient. To install the required dependencies
simply run the following commands (assuming a bash shell and `virtualenv` using Python 2.7)

    cd topleveldir
    virtualenv devenv
    source devenv/bin/activate
    pip install -r requirements.txt
    python server.py

which will start a web server listening on port 5000. The development server will automatically
restart when it detects changes to the code.

Deployment Example
------------------

Example 1:

apache2 + mod_wsgi

Follow the instructions from example 2 to install a virtual Python environment
and use the provided `wsgi_app.wsgi` file as example.

The apache2 virtual host configuration could look like this:

    WSGIDaemonProcess clanwars processes=1 threads=5
    WSGIProcessGroup clanwars
    WSGIScriptAlias /clanwars /var/www/clanwars/wsgi_app.wsgi

    Alias /clanwars/static/ /var/www/clanwars/whyattend/static/
    <Directory /var/www/clanwars/whyattend/static>
        Order allow,deny
        Allow from all
    </Directory>

Example 2:

Tornado + Reverse Proxy (nginx/apache2)

On Debian 7 you'd have to do the following:

Adjust the settings in `whyattend/config.py` Then:

    > apt-get install python python-pip python-virtualenv
    > virtualenv ./myenv
    > source ./myenv/bin/activate
    > pip install -r requirements.txt
    > pip install tornado

To start the server (here: Tornado):

    > source ./myenv/bin/activate
    > python runtornado.py

This will start a Tornado server listening on port 5001. It
is recommended to let Tornado listen only on localhost and put
it behind a web server such as nginx or apache.
