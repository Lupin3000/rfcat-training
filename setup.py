from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='srfc',
      version='0.0.7',
      description='very simple wrapper for rfcat',
      long_description="file:README.rst",
      long_description_content_type='text/x-rst',
      url='https://github.com/Lupin3000/rfcat-training',
      author='Steffen Lorenz',
      author_email='steffenlorenz@hotmail.de',
      license='MIT',
      packages=find_packages(include=['srfcat', 'srfcat.*']),
      include_package_data=True)
