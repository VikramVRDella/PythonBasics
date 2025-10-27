from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app=FastAPI()

@app.get("/",response_class=HTMLResponse)
def home():
    html="""
    <html>
        <head>
            <title>
                FastAPI using HTML
            </title>
        </head>
        <body>
            <p> This is the page made of HTML and FastAPI </p>
        <body>
    </html>
    """
    return html