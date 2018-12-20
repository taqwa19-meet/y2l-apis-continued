from flask import Flask, render_template, request
import requests, json
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='62c59b4eb52547238acda6225d9bd908')
model = app.public_models.general_model
model.model_version = 'aa7f35c01e0642fda5cf400f543e7c40'

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
    image_url = request.form['url-input']
    # At this point you have the image_url value from the front end
    # Your job now is to send this information to the Clarifai API
    # and read the result, make sure that you read and understand the
    # example we covered in the slides! 

    # YOUR CODE HERE!
    
    headers = {'Authorization': 'Key 62c59b4eb52547238acda6225d9bd908'}
    api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url_": image_url
          }
        }
      }
    ]}
    response = model.predict([ClImage(url=image_url)])

    # response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response_dict = json.loads(response.content)
    response_dict["outputs"][0]["data"]["concepts"]




    return render_template('home.html', results=response_dict)

if __name__ == '__main__':
    app.run(debug=True)