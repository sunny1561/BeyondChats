##run this function first to ensure the model is working
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('bert-base-nli-mean-tokens')
def text_similarity_model(context, response):
    context_embedding = model.encode(context)
    response_embedding = model.encode(response)
    similarity = cosine_similarity([context_embedding], [response_embedding])[0][0]
    return similarity
res="Yes, we offer online delivery services through major platforms like Swiggy and Zomato. You can also reserve a table directly from our website if you are planning to have breakfast!"
cont="Order online Thank you for your trust in us! We are available on all     major platforms like zomato, swiggy. You can also order directly from our website"

print(text_similarity_model(cont,res))






##pip install sentence_transfomer
