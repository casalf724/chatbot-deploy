# How to modify Chatbot with Flask and Jinja2 templates

This file is to deploy the chatbot I created from this [this](https://github.com/python-engineer/pytorch-chatbot) tutorial with Flask and JavaScript.

There are 2 deployment options:
- Deploy within Flask app with jinja2 template
- Serve only the Flask prediction API. The used html and javascript files can be included in any Frontend application (with only a slight modification) and can run completely separate from the Flask App then.

## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ git clone https://github.com/python-engineer/chatbot-deployment.git
$ cd chatbot-deployment
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
Modify `intents.json` with different intents and responses for your Chatbot

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.

$ (venv) python chat.py
```

```
Run 
$ (venv) pip install flask-cors

This will install the Flask with cors to run the front end with jinja2 templates.
Then run the app and open the web page to see the UI.

$ (venv) python app.py

```

Now for deployment set up  in render.

## Here is a Tutorial for future reference
[![Alt text](https://img.youtube.com/vi/a37BL0stIuM/hqdefault.jpg)](https://youtu.be/a37BL0stIuM)  
[https://youtu.be/a37BL0stIuM](https://youtu.be/a37BL0stIuM)

## Note
The video demonstrates the first approach using jinja2 templates within the Flask app. Only slight modifications are needed to run the frontend separately. 

For the alternative option use the frontend code for a standalone frontend application in the [standalone-frontend](/standalone-frontend) folder.

## Credits:
This repo was used for the frontend code:
https://github.com/hitchcliff/front-end-chatjs
