import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="enviro",
    version="0.0.1",
    author="Gustavo Ghioldi",
    author_email="gustavo.ghioldir@benefit.com.ar",
    description="Envio variables helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gustavoghioldi/enviro",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)