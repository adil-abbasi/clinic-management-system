from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.opd_visit import (
    OPDVisitCreate,
    OPDVisitResponse
)

from app.schemas.opd import TokenSlipResponse

from app.services.opd_service import OPDService

router = APIRouter(
    prefix="/opd",
    tags=["OPD"]
)


@router.post(
    "/generate-token",
    response_model=OPDVisitResponse
)
def generate_token(
    opd_data: OPDVisitCreate,
    db: Session = Depends(get_db)
):

    visit, error = OPDService.generate_token(
        db,
        opd_data
    )

    if error:
        raise HTTPException(
            status_code=404,
            detail=error
        )

    return visit


@router.get(
    "/token/{visit_id}",
    response_model=TokenSlipResponse
)
def print_token(
    visit_id: int,
    db: Session = Depends(get_db)
):

    slip = OPDService.get_token_slip(
        db,
        visit_id
    )

    if not slip:
        raise HTTPException(
            status_code=404,
            detail="Token not found"
        )

    return slip