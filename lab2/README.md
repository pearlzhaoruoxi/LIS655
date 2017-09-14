# Summary
In this lab you will use Bagger to create, validate, and invalidate a bag.

## Recommended Tools
In order to create a bag, you need a bag utility. This lab uses [Bagger](https://github.com/LibraryOfCongress/bagger/releases/tag/v2.7.6), which has a GUI, but if you are more comfortable on the command-line, you can also use [bagit-python](https://github.com/LibraryOfCongress/bagit-python) or [bagit-ruby](https://github.com/tipr/bagit).

## Installing Bagger
1. Download the zipped version of 2.7.1 from the [release page](https://github.com/LibraryOfCongress/bagger/releases)
2. Unzip the zip file and open the `bin` folder.
3. For macOS,  double-click `bagger`. For Windows, double-click `bagger.bat`
    * If you receive a security error in macOS, open you Security settings in System Preferences and `Allow apps downloaded from anywhere`

## Installing bagit-python
_This is not required_
1. From your terminal, type `pip install bagit-python`
2. Once the installation is complete, test with the command `bagit.py --help`

## Installing bagit-ruby
_This is not required_
1. From your terminal, type `gem install bagit`
2. Once the installation is complete, test with the command `bagit`
