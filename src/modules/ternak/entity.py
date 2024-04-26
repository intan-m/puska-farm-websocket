from typing import List, Tuple
from pydantic import BaseModel


# Entity
# Sub Model
class TernakPotong(BaseModel):
    produksi: int
    distribusi: int
    persentase: float

class DagingTernak(BaseModel):
    produksi: int
    distribusi: int
    persentase: float

class SusuSegar(BaseModel):
    produksi: int
    distribusi: int
    persentase: float

class ProduksiDistribusiTernakPotong(BaseModel):
    label: str
    value: int

class ProduksiDistribusiDagingTernak(BaseModel):
    label: str
    value: int

class ProduksiDistribusiSusuSegar(BaseModel):
    label: str
    value: int

class SebaranPopulasi(BaseModel):
    coord: Tuple[float, float]
    title: str

class JumlahPerahDewasa(BaseModel):
    produksi: float
    distribusi: float

class JumlahPerahAnakan(BaseModel):
    produksi: float
    distribusi: float

class JumlahPedagingDewasa(BaseModel):
    produksi: float
    distribusi: float

class JumlahPedagingAnakan(BaseModel):
    produksi: float
    distribusi: float

class RingkasanPopulasi(BaseModel):
    jumlah_perah_dewasa: JumlahPerahDewasa
    jumlah_perah_anakan: JumlahPerahAnakan
    jumlah_pedaging_dewasa: JumlahPedagingDewasa
    jumlah_pedaging_anakan: JumlahPedagingAnakan

class TablePopulasi(BaseModel):
    wilayah: str
    perah_dewasa_jantan: int
    perah_dewasa_betina: int
    perah_anakan_jantan: int
    perah_anakan_betina: int
    pedaging_dewasa_jantan: int
    pedaging_dewasa_betina: int
    pedaging_anakan_jantan: int
    pedaging_anakan_betina: int


# Main Model
class TernakMasterData(BaseModel):
    ternak_potong: TernakPotong
    daging_ternak: DagingTernak
    susu_segar: SusuSegar
    pro_dis_ternak_potong: List[ProduksiDistribusiTernakPotong]
    pro_dis_daging_ternak: List[ProduksiDistribusiDagingTernak]
    pro_dis_susu_segar: List[ProduksiDistribusiSusuSegar]
    sebaran_populasi: List[SebaranPopulasi]
    ringkasan_populasi: RingkasanPopulasi
    table: List[TablePopulasi]

    @classmethod
    def get_dummy(cls) -> "TernakMasterData":
        """
        Temporary Function to get dummy values
        """
        return cls.model_validate(DEFAULT_TERNAK_MASTER)


# Dummy Data
DEFAULT_TERNAK_MASTER = {
    "ternak_potong": {
        "produksi": 100,
        "distribusi": 50,
        "persentase": 0.5,
    },
    "daging_ternak": {
        "produksi": 100,
        "distribusi": 50,
        "persentase": 0.5,
    },
    "susu_segar": {
        "produksi": 100,
        "distribusi": 50,
        "persentase": 0.5,
    },
    "pro_dis_ternak_potong": [
        {
            "label": "2024-04-09",
            "value": 10,
        },
        {
            "label": "2024-04-10",
            "value": 15,
        },
        {
            "label": "2024-04-11",
            "value": 10,
        },
        {
            "label": "2024-04-12",
            "value": 15,
        },
        {
            "label": "2024-04-13",
            "value": 20,
        },
        {
            "label": "2024-04-14",
            "value": 25,
        },
        {
            "label": "2024-04-15",
            "value": 30,
        }
    ],
    "pro_dis_daging_ternak": [
        {
            "label": "2024-04-09",
            "value": 10,
        },
        {
            "label": "2024-04-10",
            "value": 15,
        },
        {
            "label": "2024-04-11",
            "value": 10,
        },
        {
            "label": "2024-04-12",
            "value": 15,
        },
        {
            "label": "2024-04-13",
            "value": 20,
        },
        {
            "label": "2024-04-14",
            "value": 25,
        },
        {
            "label": "2024-04-15",
            "value": 30,
        }
    ],
    "pro_dis_susu_segar": [
        {
            "label": "2024-04-09",
            "value": 10,
        },
        {
            "label": "2024-04-10",
            "value": 15,
        },
        {
            "label": "2024-04-11",
            "value": 10,
        },
        {
            "label": "2024-04-12",
            "value": 15,
        },
        {
            "label": "2024-04-13",
            "value": 20,
        },
        {
            "label": "2024-04-14",
            "value": 25,
        },
        {
            "label": "2024-04-15",
            "value": 30,
        }
    ],
    "sebaran_populasi": [
        {
            "coord": [113.05174600354292, -8.174366742801373],
            "title": "XYZ Farm",
        },
        {
            "coord": [113.14806663017885, -7.982891293213635],
            "title": "ABC Farm",
        }
    ],
    "ringkasan_populasi": {
        "jumlah_perah_dewasa": {
            "produksi": 100,
            "distribusi": 100,
        },
        "jumlah_perah_anakan": {
            "produksi": 100,
            "distribusi": 100,
        },
        "jumlah_pedaging_dewasa": {
            "produksi": 100,
            "distribusi": 100,
        },
        "jumlah_pedaging_anakan": {
            "produksi": 100,
            "distribusi": 100,
        },
    },
    "table": [
        {
            "wilayah": "LUMAJANG",
            "perah_dewasa_jantan": 10,
            "perah_dewasa_betina": 10,
            "perah_anakan_jantan": 10,
            "perah_anakan_betina": 10,
            "pedaging_dewasa_jantan": 10,
            "pedaging_dewasa_betina": 10,
            "pedaging_anakan_jantan": 10,
            "pedaging_anakan_betina": 10,
        },
        {
            "wilayah": "MALANG",
            "perah_dewasa_jantan": 10,
            "perah_dewasa_betina": 10,
            "perah_anakan_jantan": 10,
            "perah_anakan_betina": 10,
            "pedaging_dewasa_jantan": 10,
            "pedaging_dewasa_betina": 10,
            "pedaging_anakan_jantan": 10,
            "pedaging_anakan_betina": 10,
        },
    ]
}
