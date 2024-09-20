from flask import Flask, redirect, url_for, request, render_template, session
#uses render_template in a while, when we want to return our HTML.

import requests, os, uuid, json
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__) # app will be our core application. We'll use it when we register our routes in the next step.

# By using @app.route, we indicate the route we want to create.
@app.route('/', methods=['GET']) 
def index():
	return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
	#Reads the values from the form
	original_text = request.form['text']
	target_language = request.form['language']

	# Loads the values from .env
	key = os.environ['KEY']
	endpoint = os.environ['ENDPOINT']
	location = os.environ['LOCATION']

	# Indicate that we want to transalate and the API version (3.0) and the target language
	path = '/translate?api-version=3.0'
	# Adding the target language parameter
	target_language_parameter = '&to=' + target_language
	# Create the full URL
	constructed_url = endpoint + path + target_language_parameter

	# Set up the header information, which includes our subscription key
	headers = {
		'Ocp-Apim-Subscription-Key': key,
		'Ocp-Apim-Subscription-Region': location,
		'Content-type': 'application/json',
		'X-ClientTraceId': str(uuid.uuid4())
	}

	# Create the body of the request with the text to be translated
	body = [{ 'text': original_text }]

	# Make the call using post
	translator_request = requests.post(constructed_url, headers=headers, json=body)

	# Retrieve the JSON response
	translator_response = translator_request.json()

	# Retrieve the translation
	translated_text = translator_response[0]['translations'][0]['text']

	# Call render template, passing the translated text,
	# original text, and target language to the template
	return render_template(
		'results.html',
		translated_text=translated_text,
		original_text=original_text,
		target_language=target_language

		)


# Here's what the code does:
'''
1. Reads the text the user entered and the language they selected on the form
2. Reads the environmental variables we created earlier from our .env file
3. Creates the necessary path to call the Translator service, which includes the target language (the source language is automatically detected)
4. Creates the header information, which includes the key for the Translator service, the location of the service, and an arbitrary ID for the translation
5. Creates the body of the request, which includes the text we want to translate
6. Calls post on requests to call the Translator service
7. Retrieves the JSON response from the server, which includes the translated text
8. Retrieves the translated text (see the following note)
9. Calls render_template to display the response page

'''






