import fastapi
import fastapi_chameleon
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.packages.detailsviewmodel import DetailsViewModel

router = fastapi.APIRouter()


@router.get('/project/{package_name}')
@template(template_file='packages/details.pt')
def index(package_name: str, request: Request):
    vm = DetailsViewModel(package_name, request)
    return vm.to_dict()
