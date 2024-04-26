from typing import List, Type
from pydantic import BaseModel

from src.modules.susu.entity import SusuMasterData
from src.modules.ternak.entity import TernakMasterData


class APIHelper:
    def request(self, url: str, Model: Type[BaseModel]) -> List[BaseModel]:
        # TMP
        data = Model.get_dummy()
        return data