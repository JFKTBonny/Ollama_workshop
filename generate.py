import requests

api_endpoint = 'http://localhost:11434/api/generate'

data = {
    'model': 'gpt-oss:20b',
    'stream': False,
    'prompt': 'Act as a translator machine.use an entire sentence to translate this to Spanish: car'
}

response = requests.post(api_endpoint, json=data)

if response.status_code == 200:
    response_data = response.json()
    print(response_data['response'])

else:
    print('Failed to get response from Ollama API')
