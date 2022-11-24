

    clone the repository
    run: npm install, this will install the required frontend packages
    run: npm run build, this will make the production react build folder
    run: python3 -m venv venv
    then activate the virtual environment
    run: pip install -r requirements.txt
    in settings.py, under DATABASES, set the PASSWORD field to your database password
    in settings.py, under EMAIL_HOST_USER, set your email that you are using
    in settings.py, under EMAIL_HOST_PASSWORD, set your app password you are using
    in contacts/views.py, under the send_mail function, input the email you are using
