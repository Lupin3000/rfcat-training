from setuptools import setup, find_packages


setup(name='srfc',
      version='0.0.8',
      description='very simple wrapper for rfcat',
      long_description_content_type='text/x-rst',
      url='https://github.com/Lupin3000/rfcat-training',
      author='Steffen Lorenz',
      author_email='steffenlorenz@hotmail.de',
      license='MIT',
      packages=find_packages(include=['srfcat', 'srfcat.*']),
      include_package_data=True)
