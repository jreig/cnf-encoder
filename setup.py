import setuptools

setuptools.setup(
    author_email="joan.reig27@gmail.com",
    author="Joan Reig",
    classifiers=["Intended Audience :: Developers"],
    description="CNF encoder of propositional formulas using Tseytin transformation.",
    keywords="cnf encoder sat tseytin tseitin",
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    name="cnfencoder",
    packages=setuptools.find_packages(),
    test_require=['nose'],
    test_suit='nose.collector',
    url="https://github.com/jreig/cnf-encoder",
    version="0.1"
)
