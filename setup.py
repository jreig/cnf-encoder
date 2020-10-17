import setuptools

setuptools.setup(
  name="cnf-encoder",
  version="0.0.1a",
  author="Joan Reig",
  author_email="joan.reig27@gmail.com",
  keywords="cnf encoder sat tseytin tseitin",
  description="CNF encoder of propositional formulas using Tseytin transformation.",
  long_description=open("README.md").read(),
  long_description_content_type="text/markdown",
  packages=setuptools.find_packages(),
  license="MIT",
  url="https://github.com/jreig/cnf-encoder",
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
  ],
)
