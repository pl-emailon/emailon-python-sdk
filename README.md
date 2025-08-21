Emailon Python SDK
================

This repository contains the Python SDK for Emailon System
You'll find proper example on how to manage lists, subscribers, campaigns, templates and more.

### Install
You can either download latest version of the code or you can install it via pip as follows:  
`pip install emailon`
Then follow the instructions from `examples/api_config.py` file.

### Python packaging reference    
1. https://packaging.python.org/tutorials/packaging-projects/  
2. https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments  

### Example config
from emailon.base import Base
from emailon.config import Config

def setup():
    # configuration api object
    config = Config({
        'api_url': 'https://system.emailon.pl/api',
        'public_key': 'XX',
        'private_key': 'XX',
        'charset': 'utf-8'
    })

    # now inject the configuration and we are ready to make api calls
    Base.set_config(config)

### Please make sure you have all needed files at the main directory of your project (setup_api.py)
