from setuptools import setup

setup(name='g9led',
      version=0.1,
      description="G9(X) led color changer.",
      author="Jean Schurger",
      author_email='jean@schurger.org',
      packages=['g9led'],
      install_requires=["pyusb"],
      license='GPLv3',
      entry_points="""
[console_scripts]
g9led = g9led:main
""")
