# © 2019 Daniel Luque
# License AGPLv3 (http://www.gnu.org/licenses/agpl-3.0-standalone.html)
import setuptools

setuptools.setup(
    name="MyPortfolio",
    version="v2021.5.1",
    license="AGPLv3+",
    description="",
    url="https://github.com/LuqueDaniel/lnmc",
    author="Daniel Luque",
    author_email="danielluque14@gmail.com",
    install_requires=["pelican[markdown]==4.5.0"],
    extras_require={
        "dev": ["black", "isort>=5.6", "pre-commit"],
    },
)
