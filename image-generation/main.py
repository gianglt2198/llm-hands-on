from openai import OpenAI
from IPython import display

client = OpenAI()

response = client.images.generate(
    model="dall-e-2",
    prompt="a white siamese cat", ## change prompt as needed
    size="1024x1024",
    # quality="standard",
    n=1,
)

url = response.data[0].url
display.Image(url=url, width=512)

response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat", ## change prompt as needed
    size="1024x1024",
    quality="standard",
    n=1,
)

url = response.data[0].url
display.Image(url=url, width=512)