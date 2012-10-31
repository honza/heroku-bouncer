Heroku bouncer
==============

If you are on the free plan and only using one web dyno, Heroku will actually
turn it off after one hour of inactivity.  Then, on the next request the app
needs to be woken up.  This can take a few seconds.

Heroku bouncer is a Heroku bot that will ping one or more of your Heroku apps
once every hour to make sure that your app stays online.

Installation
------------

```
$ git clone git://github.com/honza/heroku-bouncer.git
$ cd heroku-bouncer
$ ... create heroku app
$ heroku config:set URLS="http://google.com,http://honza.ca" INTERVAL=30
$ git push heroku master
$ heroku scale bouncer=1
```

Settings
--------

```
URLS     --- comma separated list of urls to hit
INTERVAL --- number of minutes between hits (default: 55)
```

License
-------

BSD, short and sweet.
