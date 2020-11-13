#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from distutils.core import setup

long_description = "It is a method of compensatory aggregation that compares a set of alternatives by identifying weights for each criterion, normalising scores for each criterion and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion"

setup(
  name = 'TOPSIS-Nipun-101803531',
  version = '0.01',
  license='MIT',      
  description = 'A package for python implemetation of TOPSIS method for multiple criteria decision making', 
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Nipun Saraswat',
  author_email = 'nsaraswat_be18@thapar.edu',
  url = 'https://github.com/nipunsaras/assignment6',
  download_url = 'https://github.com/nipunsaras/assignment6/archive/0.01.tar.gz',
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   
  install_requires=[          
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.7',
  ],
)

