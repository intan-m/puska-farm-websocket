from kink import di

from src.helper.api import APIHelper

from src.modules.susu.repository import SusuBIRepository, SusuDWHRepository, SusuETLRepository
from src.modules.susu.usecase import SusuUsecase
from src.modules.susu.handler import SusuHandler

from src.modules.ternak.repository import TernakBIRepository, TernakDWHRepository, TernakETLRepository
from src.modules.ternak.usecase import TernakUsecase
from src.modules.ternak.handler import TernakHandler


# Repository
class Repository:
    susu_dwh_repo: SusuDWHRepository
    susu_bi_repo: SusuBIRepository
    susu_etl_repo: SusuETLRepository
    ternak_dwh_repo: TernakDWHRepository
    ternak_bi_repo: TernakBIRepository
    ternak_etl_repo: TernakETLRepository

    def __init__(self, api_h: APIHelper, api_urls: dict):
        self.susu_dwh_repo = SusuDWHRepository(api_h, api_urls["dwh-susu"])
        self.susu_bi_repo = SusuBIRepository()
        self.susu_etl_repo = SusuETLRepository()
        self.ternak_dwh_repo = TernakDWHRepository(api_h, api_urls["dwh-susu"])
        self.ternak_bi_repo = TernakBIRepository()
        self.ternak_etl_repo = TernakETLRepository()


# Usecase
class Usecase:
    susu_usecase: SusuUsecase
    ternak_usecase: TernakUsecase

    def __init__(self, repo: Repository):
        self.susu_usecase = SusuUsecase(repo.susu_dwh_repo, repo.susu_bi_repo, repo.susu_etl_repo)
        self.ternak_usecase = TernakUsecase(repo.ternak_dwh_repo, repo.ternak_bi_repo, repo.ternak_etl_repo)


def bootstrap_di():
    API_URLS = {
        "dwh-susu": "",
        "dwh-ternak": "",
    }

    api_h = APIHelper()

    repo = Repository(api_h, API_URLS)
    usecase = Usecase(repo)

    di[SusuHandler] = SusuHandler(usecase.susu_usecase)
    di[TernakHandler] = TernakHandler(usecase.ternak_usecase)
