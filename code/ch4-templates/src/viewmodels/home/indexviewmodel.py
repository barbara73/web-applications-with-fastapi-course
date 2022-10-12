from typing import List

from starlette.requests import Request

from src.viewmodels.shared.viewmodel import ViewModelBase
from src.services import option_service


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.options: List = option_service.get_options()


# {
#
#         'options': [
#             {'id': 'Create Order Table', 'summary': "Create an order table (from postgres)"},
#             {'id': 'Settings', 'summary': "Choose the options for your download"},
#
#         ]
#     }