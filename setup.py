from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='srfc',
      version='0.0.1',
      description='simple rfcat wrapper',
      long_description=readme(),
      url='https://softwaretester.info',
      author='Steffen Lorenz',
      author_email='steffenlorenz@hotmail.de',
      license='MIT',
      packages=['srfcat'],
      include_package_data=True)
