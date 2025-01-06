# from dotenv import load_dotenv
from openai import OpenAI
from dataclasses import dataclass

# load_dotenv()


@dataclass
class GeneratingImgStruct:
    keywords: str


def create_img_module(data: GeneratingImgStruct):
    client = OpenAI()
    response = client.images.generate(
        model="dall-e-3",
        prompt=data['keywords'],
        size="1024x1024",
        quality="standard",
        n=1
    )

    return response.data[0].url
