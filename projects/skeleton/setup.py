try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    description="My Project",
    author="My Name",
    url="URL to get it at.",
    download_url="Where to download it.",
    author_email="My email.",
    version="0.1",
    name="My Project",
    install_requires=["nose"],
    packages=["NAME"],
    scripts=[]
)