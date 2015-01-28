INSTALLATION
============
1. Clone the repository and copy it to `/var/www/`
2. Copy `local-settings.py` from `conf-files` to `communityapp` directory as 
`local_settings.py` and set values as required.
3. Install the GNU/Linux requirements
4. Install the python django requirements
5. Setup database as mentioned below
6. Copy the `httpd.conf` from `conf-files` to `/etc/apache2` directory
7. Copy the `000-default.conf` from conf-files to 
`/etc/apache2/sites-available/`
7. Restart `apache` and server will be running on port 80 :)
## GNU/Linux requirements
```bash
$ sudo apt-get install binutils git postgresql-server-dev-9.3 
postgresql-9.3-postgis-2.1 python-dev python-setuptools
postgis gdal-bin
```
## Python Django requirements
In-order to install django requirements, `python-pip` package needs to be
installed first. 
```bash
$ sudo easy_install pip
```
`requirements.txt` could be found inside the root directory of this 
repository
```bash
$ sudo pip install -r requirements.txt
```
## Setting up DB
Change the password of the postgresql db. The same $PASSWORD should be 
updated in the copied `local_settings.py` file in `communityapp` directory
```bash
$ sudo -u postgres psql -c "ALTER USER postgres PASSWORD '$PASSWORD';"
```
Create DB `communityapp`
```bash
$ sudo -u postgres psql createdb communityapp
```
Enable GIS to the database
```bash
$ sudo -u postgres psql -d communityapp -c "create extension postgis;"
```
## Possible Issues
1. Invalid command `WSGIScriptAlias`, perhaps misspelled or defined by a 
module not included in the server configuration.
This is because `WSGI` module is not loaded into `apache2`. Add the 
following line to `/etc/apache2/mods-available/wsgi.load`
`LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so` and create
a symlink to the file in `/etc/apache2/mods-enabled`. Don't forget to 
restart apache :).
