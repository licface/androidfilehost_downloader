androidfilehost_downloader
=================================
androidfilehost downloader

Usage
===========
    usage: afh.py [-h] [-c] [-d] [-p PATH] [-n NAME] [-i] [-D] URL

    positional arguments:
      URL                   androidfilehost url, example: https://androidfilehost.com/?fid=890129502657592740

    optional arguments:
      -h, --help            show this help message and exit
      -c, --clip            Download url from clipboard
      -d, --download        it will download directly, for windows default using IDM if installed and wget (build in) if not exists and for *nix
      -p PATH, --path PATH  directory of downloaded
      -n NAME, --name NAME  Option name it
      -i, --wget            Use wget (build in) download manager instead
      -D, --debug           Debugging Process

Author
===========
[LICFACE](mailto:licface@yahoo.com)

Debug
==========
set system environment DEBUG=1 for debug process
