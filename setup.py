from setuptools import setup, find_packages

setup(name='donkeypart_moving_square_sim',
      version='0.1',
      description='Library for donkeycar custom hat, the sombrero.',
      long_description="no long description given",
      url='https://github.com/autorope/donkeypart_sombrero',
      author='Will Roscoe',
      author_email='wroscoe@gmail.com',
      license='MIT',

      #NOTE: The url install method works in the recent version of pip but will not work if moved to pypi.
      install_requires=['numpy',
                        ],
      extras_require={'dev': ['pytest-cov']},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='selfdriving cars donkeycar diyrobocars datastore',
      packages=['donkeypart_moving_square_sim'],
      )
