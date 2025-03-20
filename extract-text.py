from wetro import Wetrocloud
from decouple import config
import time

# Initialize the main client and access modules
client = Wetrocloud(api_key=config("WETROCLOUD_API_KEY"))
wetro_client = client.tools

image_url_list = [
    "https://i.imgflip.com/74kzm0.jpg",
    "https://i.imgflip.com/6krvw4.jpg",
    "https://i.pinimg.com/736x/1e/ae/c7/1eaec746640620f5acfdd03d84980480.jpg",
    "https://i.redd.it/j86wxtvtqsp71.jpg",
    "https://www.meme-arsenal.com/memes/352a38807aa3a1ca67c6b7bec8eb5559.jpg",
]

def process_image(image_url):
    return wetro_client.image_to_text(
        image_url=image_url,
        request_query="What text is shown in this image? display only the text in your response."
    )

# Process each image with delay
for image_url in image_url_list:
    result = process_image(image_url)
    print(result.response)
    print("\n")
    time.sleep(1)  # Wait for 1 second before next iteration



