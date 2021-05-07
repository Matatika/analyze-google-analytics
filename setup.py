from setuptools import setup, find_packages

setup(
    name="matatika-datasets-google-analytics",
    version="0.1.0",
    description="Meltano project file bundle of Matatika datasets for Google Analytics",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/*.yaml"
        ]
    },
)
