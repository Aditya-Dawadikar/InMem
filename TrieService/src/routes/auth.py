from fastapi import APIRouter
from auth.ServiceAccount import ServiceAccount

router = APIRouter(
    tags = ["Authentication"]
)

@router.get('/test')
def test_endpoint():
    sa = ServiceAccount("test_db_01")
    return sa.generateCredentials()