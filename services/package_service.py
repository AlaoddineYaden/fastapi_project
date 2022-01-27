import datetime
from typing import List, Optional

from data.package import Package
from data.release import Release


def package_count() -> int:
    return 39_987


def release_count() -> int:
    return 26829983


def latest_packages(limit: int = 5) -> List:
    return [
               {'id': 'fastapi', 'summary': 'python framework'},
               {'id': 'react js', 'summary': 'js framework'},
               {'id': 'flutter', 'summary': 'dart framework'}
           ][:limit]


def get_packages_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name, "framework", "is a framework for python called fastapi", "https://fastapi.tiangolo.com", "MIT",
        "alaoddine"
    )
    return package


def get_latest_release_for_package(package_name) -> Optional[Release]:
    return Release("1.2.0", datetime.datetime.now())
