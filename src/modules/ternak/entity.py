from typing import List, Optional
from pydantic import BaseModel


# Entity
# Sub Model
class TernakPotong(BaseModel):
    total_produksi: Optional[float]
    total_distribusi: Optional[float]
    total_produksi: Optional[float]
    total_distribusi: Optional[float]
    persentase: Optional[float]

class DagingTernak(BaseModel):
    total_produksi: Optional[float]
    total_distribusi: Optional[float]
    total_produksi: Optional[float]
    total_distribusi: Optional[float]
    persentase: Optional[float]

class SusuSegar(BaseModel):
    total_produksi: Optional[float]
    total_distribusi: Optional[float]
    total_produksi: Optional[float]
    total_distribusi: Optional[float]
    persentase: Optional[float]

class ProduksiDistribusiTernakPotong(BaseModel):
    label: str
    produksi: Optional[float]
    distribusi: Optional[float]

class ProduksiDistribusiDagingTernak(BaseModel):
    label: str
    produksi: Optional[float]
    distribusi: Optional[float]

class ProduksiDistribusiSusuSegar(BaseModel):
    label: str
    produksi: Optional[float]
    distribusi: Optional[float]

class SebaranPopulasi(BaseModel):
    region: Optional[str]
    title: str
    populasi: int

class RingkasanPopulasi(BaseModel):
    jumlah_perah_dewasa: int
    jumlah_perah_anakan: int
    jumlah_pedaging_dewasa: int
    jumlah_pedaging_anakan: int

class TablePopulasi(BaseModel):
    wilayah: Optional[str] = None
    perah_dewasa_jantan: int
    perah_dewasa_betina: int
    perah_anakan_jantan: int
    perah_anakan_betina: int
    pedaging_dewasa_jantan: int
    pedaging_dewasa_betina: int
    pedaging_anakan_jantan: int
    pedaging_anakan_betina: int
    total_populasi: int


# Main Model
class TernakMasterData(BaseModel):
    ternak_potong: TernakPotong
    daging_ternak: DagingTernak
    susu_segar: SusuSegar
    pro_dis_ternak_potong: List[ProduksiDistribusiTernakPotong]
    pro_dis_daging_ternak: List[ProduksiDistribusiDagingTernak]
    pro_dis_susu_segar: List[ProduksiDistribusiSusuSegar]
    sebaran_populasi_all: List[SebaranPopulasi]
    ringkasan_populasi: RingkasanPopulasi
    table: List[TablePopulasi]
