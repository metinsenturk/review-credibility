# How to setup MS SQL in Mac

This project uses Microsoft SQL Server as database. To set up sql server properly, following can be done.

## Instructions 

First, install [`Homebrew`](https://brew.sh/) from it's homepage. On terminal, you can paste the following.

``` sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

In order to use SQL server, you need to install it's mac drivers. Based on the sql server version, select any of the following [instructions](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15) in Microsoft Docs. I choose Microsoft ODBC Driver 17 for SQL Server. For that, you need to run the following commands in your terminal.

Download the homebrew release of mssql.

``` sh
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
```

if brew is not updated, update the brew itself.

``` sh
brew update
```

Install the following two packages with brew. While install, accept EULA and licence terms.

``` sh
brew install msodbcsql17 mssql-tools
```

Verify that the following command displays your configuration file path.

``` sh
odbcinst -j
```

Above command show output something similar to this.

``` sh
Duke:~ owl$ odbcinst -j
unixODBC 2.3.7
DRIVERS............: /usr/local/etc/odbcinst.ini
SYSTEM DATA SOURCES: /usr/local/etc/odbc.ini
FILE DATA SOURCES..: /usr/local/etc/ODBCDataSources
USER DATA SOURCES..: /Users/owl/.odbc.ini
SQLULEN Size.......: 8
SQLLEN Size........: 8
SQLSETPOSIROW Size.: 8
```

## Conclusion

Above instructions will install the SQL Server Command Line Tools on your Mac. After installation, you can connect to SQL Server database in anywhere and anyway you want.
