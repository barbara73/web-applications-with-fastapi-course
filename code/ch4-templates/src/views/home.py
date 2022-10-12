import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from src.viewmodels.home.indexviewmodel import IndexViewModel

router = fastapi.APIRouter()


@router.get('/')
@template()
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()
    # return {
    #
    #     'options': [
    #         {'id': 'Create Order Table', 'summary': "Create an order table (from postgres)"},
    #         {'id': 'Settings', 'summary': "Choose the options for your download"},
    #
    #     ]
    # }


@router.get('/about')
@template()
def about():
    return {}
