import logging
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone

# Inisialisasi logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


app = APIRouter(prefix="/v1")

# Definisikan model data untuk request body
class Numbers(BaseModel):
    a: int
    b: int

# Endpoint untuk melakukan penjumlahan dengan method POST
@app.post("/add")
def add_numbers(numbers: Numbers):
    result = numbers.a + numbers.b

    
    #jakarta_zone = timezone(timedelta(hours=7))
    #jakarta_time = datetime.now(jakarta_zone)

    logger.info(f"Hit to /v1/add at {datetime.now()}")
    return {"result": result}
