from fastapi import APIRouter, Depends
from api.auth.jwt_bearer import JWTBearer
from routes.admin import router as AdminRouter
from routes.student import router as StudentRouter
from routes.index import router as IndexRouter

token_listener = JWTBearer()

router = APIRouter()
router.include_router(IndexRouter, tags=["Root"])
router.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
router.include_router(StudentRouter, tags=["Students"], prefix="/student", dependencies=[Depends(token_listener)])
