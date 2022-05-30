# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Fast API Modules
import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

STATIC_PATH = os.path.join(BASE_DIR, 'static')

app = FastAPI(root_path='/')

app.mount('/static', StaticFiles(directory=STATIC_PATH), name='static')
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    try:
        return templates.TemplateResponse('home.html', {'request': request})
    except:
        return templates.TemplateResponse('page-404.html',{'request':request})

@app.get('/{path}', response_class=HTMLResponse)
async def app_path(path:str, request: Request):
    try:
        return templates.TemplateResponse(path + '.html', {'request': request})
    except:
        return templates.TemplateResponse('page-404.html',{'request':request})

