import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get('/')
@template()
def index(user: str = 'anon'):

    return {
        'package_count': 2222,
        'release_count': 10,
        'user_count': 333,
        'packages': [
            {'id': 'fastapi', 'summary': "A great web framweork"},
            {'id': 'uvicorn', 'summary': "blablabla"},
            {'id': 'whatever', 'summary': "and so on"},
        ],
        'user_name': user
    }


@router.get('/about')
@template()
def about():
    return {}
