from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask,jsonify
import requests
app = Flask(__name__)
# Define your API endpoint
API_ENDPOINT = "https://devapi.beyondchats.com/api/get_message_with_source"  
# Load the model
model = SentenceTransformer('bert-base-nli-mean-tokens')
## function to find the simillarty and semantic search between  context and resposne
def text_similarity_model(context, response):
    context_embedding = model.encode(context)
    response_embedding = model.encode(response)
    similarity = cosine_similarity([context_embedding], [response_embedding])[0][0]
    return similarity

##api_data 
def get_all_citation(api_data):
    dataset = api_data['data']
    list_dataset = dataset['data']
    citations = []
    for di in list_dataset:
        response = di['response']
        sources = di['source']
        matching_sources = []
        for source in sources:
            similarity_score = text_similarity_model(source['context'], response)
            if similarity_score > 0.7:
                matching_sources.append({'id': source['id'], 'link': source['link']})
        citations.append(matching_sources)

    return citations
#when input_format is dict with response and source are key 
def get_citations_input_format(input_format):
  response=input_format['response']
  sources=input_format['source']
  citations = []
  for source in sources:
    matching_sources=[]
    similarity_score = text_similarity_model(source['context'], response)
    
    if similarity_score > 0.7:
      matching_sources.append({'id': source['id'], 'link': source['link']})
  citations.append(matching_sources)
  return citations
def fetch_data():
    response = requests.get(API_ENDPOINT) 
    data = response.json()
    return data

#Fetch data from the API  and get citations
api_data = fetch_data()

@app.route('/')
def root():
    return {"message":"Welcome to BeyondChats"}
@app.route('/get_citations_api_data', methods=['GET'])
def get_citations_input_format():
    data = fetch_data()
    citations = get_all_citation(data)
    return jsonify(citations)


## if user gives input then as mentioned exmaple in the assignment ex: {"response":"value","source":"list_value"} this is format you need to pass
@app.route('/process', methods=['POST'])
def process():
    input_data = requests.json  # Getting JSON data from POST request
    if input_data:
        result = get_citations_input_format(input_data)
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'No input_data provided'}), 400
if __name__ == '__main__':
    app.run(debug=True)


