from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import pipeline
from fastapi.staticfiles import StaticFiles
app = FastAPI()

templates = Jinja2Templates(directory="templates")


app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/")
async def predict_sentiment(text: str = Form(...)):
    sentiment_analysis = pipeline("sentiment-analysis")
    result = sentiment_analysis(text)
    return {"text": text, "sentiment": result[0]["label"], "confidence": result[0]["score"]}
