import logging
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from datetime import datetime

# Inisialisasi logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# Add FastAPI
app = FastAPI()

router = APIRouter(prefix="/v1")

# Definisikan model data untuk request body
class Numbers(BaseModel):
    a: int
    b: int

# Endpoint untuk melakukan penjumlahan dengan method POST
@router.post("/add")
def add_numbers(numbers: Numbers):
    result = int(numbers.a + numbers.b)
    logger.info(f"Hit to /v1/add at {datetime.now()}")
    return {"result": result}

# Endpoint untuk menguji pangkat dua dengan method GET
@router.get("/testing/{angka}")
async def test(angka: int):
    answer = {'PangkatDua': float(angka**2)} 
    return answer

app.include_router(router)