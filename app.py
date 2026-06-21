from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from live_whisper import trascrivi_audio
from concierge import rispondi

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"stato": "Pronto"}
    )


@app.post("/parla", response_class=HTMLResponse)
def parla(request: Request):

    testo = trascrivi_audio()   # registrazione + whisper

    risposta = rispondi(testo)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "stato": "Elaborato",
            "domanda": testo,
            "risposta": risposta
        }
    )