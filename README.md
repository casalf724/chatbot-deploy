# Chatbot Deployment with Flask and Jinja2 templates

This file is to deploy the chatbot I created from this [this](https://github.com/python-engineer/pytorch-chatbot) tutorial with Flask and JavaScript.

The chatbot is trained on the content from the Scrun Guide on the Scrum (Agile) franework for Project management. It incorporates content from the Scrum Guide, provided by SCRUM.org, covering theory, values, team roles, events, and artifacts.

It uses intents with tags for each topic area such as philosophy, values, scrum events, etc. This is intended as a primer or study aid for scrum certification tests or as reference guide to assist in learning Scrum.


## Initial Setup:
This repo currently contains all files.

Create a virtual environment
```
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```

Run the following command to test it in the console.

```
$ (venv) python chat.py
```

Install Flask-cors. This will install the Flask with cors to run the front end with jinja2 templates.

```
$ (venv) pip install flask-cors
```

Then run the app and open the web page to see the UI.

```
$ (venv) python app.py
```

Now for deployment set up in render.



## Credits:

This repo was used for the frontend code:
https://github.com/hitchcliff/front-end-chatjs
