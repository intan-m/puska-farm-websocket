from typing import Optional, List, Union
from pydantic import BaseModel

# Entity
# Sub Model
class SusuSegar(BaseModel):
    distribusi: Optional[float]
    produksi: Optional[float]

class SusuPasteurisasi(BaseModel):
    distribusi: Optional[float]
    produksi: Optional[float]

class SusuKefir(BaseModel):
    distribusi: Optional[float]
    produksi: Optional[float]

class Yogurt(BaseModel):
    distribusi: Optional[float]
    produksi: Optional[float]

class Keju(BaseModel):
    distribusi: Optional[float]
    produksi: Optional[float]

class PrediksiValue(BaseModel):
    label: str
    actual: Optional[float]
    predict: Optional[float]

class PersentaseProduksi(BaseModel):
    susu_segar: float
    susu_pasteurisasi: float
    susu_kefir: float
    yogurt: float

class PersentaseDistribusi(BaseModel):
    susu_segar: float
    susu_pasteurisasi: float
    susu_kefir: float
    yogurt: float

class ProduksiDistribusiSusuSegar(BaseModel):
    label: str
    produksi: int
    distribusi: int

class PermintaanSusuSegarPerMitra(BaseModel):
    label: str
    value: Optional[float]

class HargaSusu(BaseModel):
    minimum: Optional[int]
    maximum: Optional[int]
    rata_rata: Optional[float]


# Main Model
class SusuMasterData(BaseModel):
    susu_segar: SusuSegar
    susu_pasteurisasi: SusuPasteurisasi
    susu_kefir: SusuKefir
    yogurt: Yogurt
    keju: Keju
    prediksi: List[PrediksiValue]
    persentase_produksi: PersentaseProduksi
    persentase_distribusi: PersentaseDistribusi
    prod_dis_susu_segar: List[ProduksiDistribusiSusuSegar]
    permintaan_susu_segar_dari_mitra_all: List[PermintaanSusuSegarPerMitra]
    total_persentase_distribusi: float
    total_pendapatan: int
    harga_susu: HargaSusu
