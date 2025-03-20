from wetro import Wetrocloud
from decouple import config

# Initialize the main client and access modules
client = Wetrocloud(api_key=config("WETROCLOUD_API_KEY"))
rag_client = client.rag
tools_client = client.tools

# Extract text from an image and answer questions about it
ocr_response = tools_client.image_to_text(
    image_url="https://images.unsplash.com/photo-1511884642898-4c92249e20b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
    request_query="What in this image?"
)
print(ocr_response)