import os
import urllib.request
import json
from duckduckgo_images_api import search


# Search for images
results = search("powdery mildew on soy")

# Create a folder to save the images
if not os.path.exists("images"):
    os.makedirs("images")

# Download the images and save their URLs
downloaded_images = []
cont = 0
for i, image in enumerate(results["results"]):
    image_url = image["image"]
    image_ext = image_url.split(".")[-1]
    image_path = f"images/image_{cont}.{image_ext}"
    if image_url not in downloaded_images:
        # response = urllib.request.urlopen(image_url)
        # img = response.read()
        # with open(image_path, "wb") as f:
        #     f.write(img)
        downloaded_images.append(image_url)
        print(f"Image {i} saved at {image_path}")
        cont+=1
    else:
        print(f"Image {i} already downloaded")
        

# Save the URLs of the downloaded images
with open("downloaded_images_urls.txt", "w") as f:
    for url in downloaded_images:
        f.write(f"{url}\n")
