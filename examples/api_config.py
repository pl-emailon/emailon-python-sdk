from emailon.base import Base
from emailon.config import Config


def setup():
    """
    Notes:
    If SSL present on the webhost, the api can be accessed via SSL as well (https://...).
    A self signed SSL certificate will work just fine.
    If the Emailon powered website doesn't use clean urls,
    make sure your apiUrl has the index.php part of url included, i.e:
    http://www.emailon-powered-website.tld/api/index.php
    :return:
    """

    # configuration object
    config = Config({
        'api_url': 'http://www.emailon-powered-website.tld/api',
        'public_key': 'PUBLIC_KEY',
        'private_key': 'PRIVATE_KEY',
        'charset': 'utf-8'
    })

    # now inject the configuration and we are ready to make api calls
    Base.set_config(config)
