from setuptools import setup, setuptools

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='ConstraintModels',
    url='https://github.com/christopher-inegbedion/ConstraintModels',
    author='Christopher E. Inegbedion',
    author_email='eromoseleinegbe@gmail.com',
    # Needed to actually package something
    packages=setuptools.find_packages(),
    # Needed for dependencies
    # install_requires=['arrow'],
    # *strongly* suggested for sharing
    version='0.0.0',
    # description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
)
