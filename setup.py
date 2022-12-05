from setuptools import setup, find_packages

setup(
    name="analyze-google-analytics",
    version="0.4.1",
    description="Meltano project file bundle of Matatika datasets for Google Analytics",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/tap-google-analytics/*.yml"
        ]
    },
)
