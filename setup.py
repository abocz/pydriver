from setuptools import setup

setup(name='pydriver',
      version='0.1',
      description='',
      url='http://github.com/dmcneil/pydriver',
      author='Derek McNeil',
      author_email='derek.mcneil90@gmail.com',
      license='MIT',
      packages=['pydriver'],
      install_requires=[
          'selenium',
          'polling'
      ],
      zip_safe=False)

