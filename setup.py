import setuptools

__version__ = "0.0.0"
REPO_NAME = "Spark-Foundation-Task-1-Simple-Linear-Regression"
AUTHOR = "Chetand777"
AUTHOR_EMAIL = "chetand777@gmail.com"

setuptools.setup(
  
  name=REPO_NAME,
  version=__version__,
  author=AUTHOR,
  author_email=AUTHOR_EMAIL,
  url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
  project_urls={
    "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues"
  },
  packages=setuptools.find_packages()

)