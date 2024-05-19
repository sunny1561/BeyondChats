install the necessary package to use the llm (large language model)
pip install sentence-transformers
pip install flask
pip install requests






also for the input format to pass into get_citations_input_format function you need 
to post some json format for instance
response = "Yes, we offer online delivery services through major platforms like Swiggy and Zomato. You can also reserve a table directly from our website if you are planning to have breakfast!"
source = [
  {
    "id": "71",
    "context": "Order online Thank you for your trust in us! We are available on all major platforms like zomato, swiggy. You can also order directly from our website",
    "link": "https://orders.brikoven.com"
  },
  {
    "id": "75",
    "context": "Do you give franchise if the brand No, we currently don't offer franchise opportunities for BrikOven! Although do feel free to drop in an email at theteam@brikoven. com so we can get in touch with you at a later stage if we do decide to give out franchisees''",
    "link": ""
  },
  {
    "id": "8",
    "context": "Breakfast Reservations\r For Breakfast, we recommend making reservations in advance. Reservation is only available through our website",
    "link": "https://www.brikoven.com/reservations"
  },
]

# Create the dictionary with the response as the key and sources as the value
input_format= {"response":response,"source": source}











