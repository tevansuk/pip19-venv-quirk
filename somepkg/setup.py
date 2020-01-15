from setuptools import find_packages, setup

setup(
    name="some-package",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    description="Some package",
    long_description="Some package",
    author="Tom Evans",
    author_email="tevans@mintel.com",
    url="http://a.com/b",
)
