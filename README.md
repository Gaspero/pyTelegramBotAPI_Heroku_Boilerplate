# Yet another template for Telegram bot on Heroku

### Key features:
* Webhook setup out of the box - via plugging extention in app `TelebotWrapper()` and `NgrokListener()` for local development support
* Full local development support via `heroku local web` cli command and local `.env` file to Flask config (to emulate env vaiables provided in Heroku)
* Clean folder structure - one file with message handlers - thats all you need
* Application factory pattern + cli commands
* Pipenv for easy dependency management and Heroku env setup
* `app.json` for bootstraping project in Heroku
