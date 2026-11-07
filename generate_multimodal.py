import requests  # requests is a popular Python library for making HTTP requests. It simplifies the process of sending HTTP requests and handling responses, making it easier to interact with web APIs.
import base64  # base64 is used to encode the image data into a format that can be sent over HTTP

# load image
with open('sample_image.jpg', 'rb') as image_file:

    # 1. read its contents (binary)
    image_data = image_file.read()

    # 2. turn binary into base64
    base64_image_data = base64.b64encode(image_data)

    # 3. encode to utf-8
    base64_image_string = base64_image_data.decode('utf-8')


api_endpoint = 'http://localhost:11434/api/generate'

data = {
    'model': 'ornith-1.5:9b',
    'stream': False,
    'prompt': 'Describe the image provided',
    'images': [base64_image_string]
}

response = requests.post(api_endpoint, json=data)

if response.status_code == 200:
    response_data = response.json()
    print(response_data['response'])

else:
    print('Failed to get response from Ollama API')
