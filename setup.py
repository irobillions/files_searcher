from setuptools import setup, find_packages

setup(
    name="file_searcher",
    version="1.0.0",
    description="Un outil de recherche de fichiers avancé avec exportation vers Excel et journalisation",
    author="Christ Bouka",
    author_email="christbouka14@yahoo.fr",
    url="https://github.com/irobillions/file_searcher",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=[
        "openpyxl==3.0.10",
    ],
    entry_points={
        'console_scripts': [
            'file_searcher=ui.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
