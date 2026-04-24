from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends
from models.base import get_session

SessionDep = Annotated[Session, Depends(get_session)]
