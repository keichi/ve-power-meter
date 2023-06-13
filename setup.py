from setuptools import setup


setup(name="ve-power-meter",
      version="0.1.0",
      description="Power meeasurement tool for the NEC Vector Engine",
      url="http://github.com/keichi/ve-power-meter",
      author="Keichi Takahashi",
      author_email="hello@keichi.dev",
      license="MIT",
      packages=["ve_power_meter"],
      entry_points={
        "console_scripts": [
          "ve-power-meter = ve_power_meter:main"
        ]
      })
