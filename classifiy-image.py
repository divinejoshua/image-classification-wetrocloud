from wetro import Wetrocloud
from decouple import config
import time

# Initialize the main client and access modules
client = Wetrocloud(api_key=config("WETROCLOUD_API_KEY"))
wetro_client = client.tools

image_url_list = [
    "https://images.unsplash.com/photo-1511884642898-4c92249e20b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
    "https://images.unsplash.com/photo-1494500764479-0c8f2919a3d8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
    "https://images.unsplash.com/photo-1434725039720-aaad6dd32dfe?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1642&q=80",
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
]

def process_image(image_url):
    return wetro_client.image_to_text(
        image_url=image_url,
        request_query="Describe what you see in this image."
    )

# Process each image with delay
for image_url in image_url_list:
    result = process_image(image_url)
    print(result.response)
    print("\n")
    time.sleep(1)  # Wait for 1 second before next iteration
