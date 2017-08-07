# Django Slack-Invite App

A barebones Django app for automating the invite process for Slack that can easily be deployed to Heroku.

The easiest way to deploy the application is by using the Heroku button below. If you would like to customize the appearances or functionality of your Slack invite app please clone the repository and modify away! 

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

This project was inspired by the outsideris JavaScript [Slack Invite Automation](https://github.com/outsideris/slack-invite-automation) app.

## Settings
You can modify the variables found in `settings.cfg` or manually set environment variables. This project supports the utilization of `virtualenv` and `virtualenvwrapper` environments for development, testing and production.


### `settings.cfg`
Modify the setting in `settings.cfg` as needed:

* SLACK\_TEAM: Your teams Slack name
* SLACK\_URL: Your Slack team url (ex: django-slackinvite.slack.com)
* SLACK\_TOKEN: Your access token for Slack (see Issue Token)

### Environment Variables and Heroku
It is posible for Heroku to utilize predifined envrionment variable in a `.env` file for local deployment. For more information on constructing a `.env` file see the official Heroku documentation: [Set up your local environment variables](https://devcenter.heroku.com/articles/heroku-local#set-up-your-local-environment-variables)

For deployed Heroku applications, set or modify environment variables using the Heroku CLI or in the Heroku Dashboard:

`$ heroku config:set SLACK_TEAM="Your Team Name"`

### Environment Variables and `virtualenv` and `virtualenvwrapper`
This application supports the use of isolated python envrionments using `virtualenv` and `virtualenvwrapper`. When utilizing `virtualenvwrapper` local envrionment variables cane be set in the `postactive` script. For more information on `virtualenv` and `virtualenvwrapper` see the official documentation:

* [virtualenv](https://virtualenv.pypa.io/en/stable/)
* [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/index.html)

For more details regarding setting up the Django Slack-Invite App with `virtualenv` and `virtualenvwrapper`, please see our official documentaion:

* [Django Slack-Invite App Official Documentation](link)

## Run
First the applicaiton needs to be configured to run locally. Once the app has been verified to run locally, it can easily be deployed to Heroku.

### Running locally

Make sure that you have Python properly installed. Also, install the Heroku Toolbelt. It is also highly recommended that you install the application from within a `virtualenv`. 


```
$ git clone https://github.com/sanchagrins/SlackInvite.git
$ cd SlackInvite
```
After cloning the repository, modify `settings.cfg` as noted above. Then install the required Python packages within your virtual environment and launch your local app.

```
$ pip install -r requirements.txt
$ heroku local
```

You can access [http://localhost:5000](http://localhost:5000)

![Invite Page](./screenshots/invite-page.png)

### Deploying to Heroku
```
$ heroku create
$ git push heroku master

$ heroku open
```
## Documentation
For more information about using the Django Slack-Invite web app, see the official documentation:

* [Django Slack-Invite Official Documentation](link)
