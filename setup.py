# © 2019 Daniel Luque
# License AGPLv3 (http://www.gnu.org/licenses/agpl-3.0-standalone.html)
import setuptools

setuptools.setup(
    name="MyPortfolio",
    version="v2023.4.13",
    license="AGPLv3+",
    description="",
    url="https://github.com/LuqueDaniel/lnmc",
    author="Daniel Luque",
    author_email="danielluque14@gmail.com",
    install_requires=["pelican[markdown]==4.7"],
    extras_require={
        "dev": ["black", "isort", "pre-commit", "pylint", "mypy"],
    },
)
