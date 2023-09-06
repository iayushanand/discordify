from setuptools import setup

setup(
    include_package_data=True,
    name="discordify",
    version="0.0.1",
    author="Ayu Itz",
    author_email="icontactayu@gmail.com",
    description="A Python package to retrieve detailed Spotify album images for Discord integration.",
    long_description=open("Readme.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iayushanand/discordify",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    keywords="discord spotify spotify-wrapper image",
    packages=["discordify"],
    install_requires=[
        "discord.py==2.3.2",
        "pillow==10.0.0",
        "cbvx==0.1.0",
    ],
    python_requires=">=3.6",
    package_data={"discordify":['font/spotify.ttf']}
)
