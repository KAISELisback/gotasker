from pydantic import BaseModel, StringConstraints
from typing import Annotated, Optional

class AtributosTarefa(BaseModel):
    tarefa_id: Optional[int] = None
    titulo: Annotated[str, StringConstraints(min_length=1, max_length=80)]
    descricao: Annotated[str, StringConstraints(min_length=1, max_length=255)]

