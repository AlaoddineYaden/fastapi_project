from typing import List

from starlette.requests import Request

from services import package_service, user_service
from viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.package_count: int = package_service.package_count()
        self.release_count: int = package_service.release_count()
        self.user_count: int = user_service.user_count()
        self.packages: List = package_service.latest_packages(limit=5)
# {
#         'package_count': 39_987,
#         'release_count': 26829983,
#         'user_count': 128_828,
#         'packages': [
#             {'id': 'fastapi', 'summary':'python framework'},
#             {'id': 'react js', 'summary': 'js framework'},
#             {'id': 'flutter', 'summary': 'dart framework'}
#         ]
#     }
