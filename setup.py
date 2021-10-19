import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'tomba',
  version = '1.0.0',
  license='Apache-2.0',
  description = 'Tomba.io is an Email Finder for B2B sales and email marketing',
  long_description=long_description,
  author = 'Tomba technology web service LLC',
  author_email = 'info@tomba.io',
  maintainer = 'Mohamed Ben rebia',
  maintainer_email = 'b.mohamed@tomba.io',
  url = 'https://tomba.io',
  keywords = ['email', 'Email Finder', 'Email Verifier', 'B2B', 'Email marketing'],
  install_requires=[
          'requests',
      ],
  packages=setuptools.find_packages(),
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Environment :: Web Environment',
    'Topic :: Software Development',
    'License :: OSI Approved :: ',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  include_package_data=True,
  zip_safe=False,
)
