from setuptools import setup

reqs = [
    "loguru>=0.6.0",
    "picamera"
]

test_pkgs = ["pytest", "coverage", "coverage-badge"]
develop_pkgs = ["jupyter"]

setup(
    name="xcampy",
    packages=["xcampy"],
    package_dir={"": "src"},
    version="0.0.1",
    python_requires=">3.7",
    description="Python package for RPi camera interface and functions.",
    url="https://github.com/neumj/xcampy",
    install_requires=reqs,
    extras_require={"develop": develop_pkgs, "test": test_pkgs},
    include_package_data=True,
    entry_points={"console_scripts": ["CLI_NAME = xcampy.xcampy_cli:start"]},
)
