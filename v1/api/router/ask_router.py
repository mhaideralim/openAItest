from fastapi import FastAPI, Request, APIRouter, HTTPException
from fastapi.params import Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import openai
import os

from starlette.staticfiles import StaticFiles

from v1.api.database.connection import database
from v1.api.database.model import Input, User

# Initialize FastAPI
router = APIRouter()

# Initialize OpenAI API
openai.api_key = "<YOUR OPENAI API KEY HERE>"

# Initialize templates
templates = Jinja2Templates(directory="v1/api/frontend")


# Define route for root page
@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("ask_anything.html", {"request": request})


# Define route for handling form submission
@router.post("/")
async def process_input(input_text: str = Form(...)):
    try:  # Define your OpenAI API request parameters
        print(input_text)
        database.insert_one(input_text)
        prompt = f"What is {input_text}?"
        model_engine = "text-davinci-002"
        max_tokens = 100
        temperature = 0.5

        # Call the OpenAI API with the input text
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )

        # Extract the response text from the OpenAI API response
        output_text = response.choices[0].text

        # Save the input and output text to MongoDB database
        # YOUR CODE HERE

        # Return the response to the HTML page
        return output_text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
