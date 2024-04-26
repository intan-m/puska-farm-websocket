from typing import List
from pydantic import BaseModel


# Entity
# Sub Model
class BarPermintaanSusu(BaseModel):
    label: str
    data: int
    backgroundColor: str

class HargaSusu(BaseModel):
    mean: str
    min: str
    max: str

class PieChartItem(BaseModel):
    no: int
    label: str
    bgColor: str
    borderColor: str

class PrediksiProduksi(BaseModel):
    graph: dict
    timestamp: str
    liter_prediction: int

class PrediksiProduksiSusuSegar(BaseModel):
    label: str
    value: int

class ProduksiDistribusi(BaseModel):
    produksi: int
    distribusi: int

class ProduksiDistribusiPerCategory(BaseModel):
    susu_segar_liter: ProduksiDistribusi
    susu_pasteurisasi_liter: ProduksiDistribusi
    kefir_liter: ProduksiDistribusi
    yogurt_liter: ProduksiDistribusi
    keju_kg: ProduksiDistribusi

class ProduksiDistribusiSusu(BaseModel):
    label: str
    value: int


# Main Model
class SusuMasterData(BaseModel):
    prod_dis: ProduksiDistribusiPerCategory
    prediksi_produksi_susu_segar: List[PrediksiProduksiSusuSegar]
    prediksi_produksi: PrediksiProduksi
    pie_prod_per_produk: List[PieChartItem]
    pie_dis_per_produk: List[PieChartItem]
    pro_dis_susu: List[ProduksiDistribusiSusu]
    graph_bar_permintaan_susu: List[BarPermintaanSusu]
    persentase_distribusi_pct: int
    total_pendapatan_idr: str
    harga_susu: HargaSusu

    @classmethod
    def get_dummy(cls) -> "SusuMasterData":
        """
        Temporary Function to get dummy values
        """
        return cls.model_validate(DEFAULT_SUSU_MASTER)


# Dummy Data
DEFAULT_SUSU_MASTER = {
    "prod_dis": {
        "susu_segar_liter": {
            "produksi": 100,
            "distribusi": 50,
        },
        "susu_pasteurisasi_liter": {
            "produksi": 100,
            "distribusi": 50,
        },
        "kefir_liter": {
            "produksi": 100,
            "distribusi": 50,
        },
        "yogurt_liter": {
            "produksi": 100,
            "distribusi": 50,
        },
        "keju_kg": {
            "produksi": 100,
            "distribusi": 50,
        }
    },
    "prediksi_produksi_susu_segar": [
        {
            "label": "2024-04-07",
            "value": 5,
        },
        {
            "label": "2024-04-08",
            "value": 10,
        },
        {
            "label": "2024-04-09",
            "value": 15,
        },
        {
            "label": "2024-04-10",
            "value": 20,
        },
        {
            "label": "2024-04-11",
            "value": 25,
        },
        {
            "label": "2024-04-12",
            "value": 30,
        },
        {
            "label": "2024-04-13",
            "value": 35,
        },
        {
            "label": "2024-04-14",
            "value": 40,
        }
    ],
    "prediksi_produksi": {
        "graph": {},
        "timestamp": "2024-04-15",
        "liter_prediction": 45,
    },
    "pie_prod_per_produk": [
        {
            "no": 1,
            "label": "Susu Segar",
            "bgColor": "#E8C872",
            "borderColor": "#FFFFFF",
        },
        {
            "no": 2,
            "label": "Susu Pasteurisasi",
            "bgColor": "#FFF3CF",
            "borderColor": "#FFFFFF",
        },
        {
            "no": 3,
            "label": "Susu Kefir",
            "bgColor": "#C9D7DD",
            "borderColor": "#FFFFFF",
        },
        {
            "no": 4,
            "label": "Yogurt",
            "bgColor": "#637A9F",
            "borderColor": "#FFFFFF",
        }
    ],
    "pie_dis_per_produk": [
        {
            "no": 1,
            "label": "Susu Segar",
            "bgColor": "#E8C872",
            "borderColor": "#FFFFFF",
        },
        {
            "no": 2,
            "label": "Susu Pasteurisasi",
            "bgColor": "#FFF3CF",
            "borderColor": "#FFFFFF",
        },
        {
            "no": 3,
            "label": "Susu Kefir",
            "bgColor": "#C9D7DD",
            "borderColor": "#FFFFFF",
        },
        {
            "no": 4,
            "label": "Yogurt",
            "bgColor": "#637A9F",
            "borderColor": "#FFFFFF",
        }
    ],
    "pro_dis_susu": [
        {
            "label": "2024-04-07",
            "value": 5,
        },
        {
            "label": "2024-04-08",
            "value": 10,
        },
        {
            "label": "2024-04-09",
            "value": 15,
        },
        {
            "label": "2024-04-10",
            "value": 20,
        },
        {
            "label": "2024-04-11",
            "value": 25,
        },
        {
            "label": "2024-04-12",
            "value": 30,
        },
        {
            "label": "2024-04-13",
            "value": 35,
        },
        {
            "label": "2024-04-14",
            "value": 40,
        }
    ],
    "graph_bar_permintaan_susu": [
        {
            "label": "Senduro Farm",
            "data": 30,
            "backgroundColor": "#E8C872"
        },
        {
            "label": "Mitra F",
            "data": 15,
            "backgroundColor": "#FFF3CF"
        },
        {
            "label": "Konsumen",
            "data": 10,
            "backgroundColor": "#C9D7DD"
        },
    ],
    "persentase_distribusi_pct": 50,
    "total_pendapatan_idr": "Rp 10.000.000,00",
    "harga_susu": {
        "mean": "30.000",
        "min": "10.000",
        "max": "50.000",
    }
}
