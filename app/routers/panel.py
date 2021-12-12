from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from hashlib import sha256
import requests
import random

from starlette import status
from starlette.responses import JSONResponse

from app.dependencies import templates

router = APIRouter(
    prefix='/panel',
    tags=['panel'],
    responses={404: {'descriptions': 'Not Found'}},
)


@router.get("/", response_class=HTMLResponse)
async def panel(request: Request):
    wallet = sha256('word asd sushka'.encode('utf-8')).hexdigest()
    trs = [{col: ''} for i in range(20) for col in ['from', 'to', 'price']]

    for row in trs:
        row['from'] = wallet
        row['to'] = sha256(f'asd asd {random.randint(1, 200)} ds ds'.encode('utf-8')).hexdigest()
        row['price'] = random.uniform(10.5, 75.5)
    return templates.TemplateResponse("panel.html", {
        "request": request,
        "wallet": {
            "hash": wallet,
            "balance": "0.03123"
        },
        "transactions": trs,
    })


@router.get("/transactions", response_class=HTMLResponse)
async def transactions(request: Request):
    wallet = sha256('word asd sushka'.encode('utf-8')).hexdigest()
    trs = [{col: ''} for i in range(20) for col in ['from', 'to', 'price']]

    for row in trs:
        row['from'] = wallet
        row['to'] = sha256(f'asd asd {random.randint(1, 200)} ds ds'.encode('utf-8')).hexdigest()
        row['price'] = random.uniform(10.5, 75.5)
    return templates.TemplateResponse("transactions.html", {
        "request": request,
        "transactions": trs,
    })
