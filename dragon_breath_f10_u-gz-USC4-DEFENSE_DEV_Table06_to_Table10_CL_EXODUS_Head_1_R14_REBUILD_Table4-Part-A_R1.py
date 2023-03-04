#!/usr/bin/python

# DragonBreath F.10-U-GROUNDZERO-USC4-DEFENSE-CL-EXODUS-JSON-and-URLs

# Date: 08/11/2022
# Updated Date: 09/22/2022
# Updated Time: Approx. 21:21

# USC4 Defense Version R1 (JSON's -> MariaDB/MySQL) -- Zero Call Back Scraping / Data Recovery
# This can be modified to by uncommenting sections of the code to Recovery all Dropped Data from courtlistener.com Dumps... 
# courtlistener.com, Free Law Project claims crawling the website is welcomed. However limits 933 queries per day. 
# This would take a minimum of 5 years to Recover Dropped Data to Complete the Free Law Database of American Constitutionally Bound Judicial Opinions
# Remedy: Proxy or Multi-American Patriot, American Christian Saint Efforts (Like The Free Law Project's Multi-Effort RECAP FireFox Extension to Secure PACER Documents)
# I have Local Government obstructing my Efforts under Illegal Surveillance and Domestic Terrorism
# Twitter #2 - https://twitter.com/BRKastning - I have been defending OUR Constitutional Republic / American Christian Nation per P.Law 97-280 since The Beginning!
# Facebook 1/3 - https://facebook.com/brandon.kastning
# Facebook 2/3 - https://facebook.com/KastningBrandon
# Facebook 3/3 - https://facebook.com/BRKastning
# https://sharpenyoursword.org/21st-century-global-exodus-lat-expod
# https://thewarriorsdojo.com/21st-century-american-exodus-lat-expod
# https://wethepeopleonline.com/mr-brandon-kastnings-public-private-evidentiary-journal-evidence
# https://wethepeopleonline.com/cites-top-page-pre-launch
# https://wethepeopleonline.com/21st-century-american-exodus-lat-expod-top-page-pre-launch
# https://wethepeopleonline.us - OpenSource Development - 21st Century American Constitutional Unity Platform (Non Central Server Dependent)
# https://wethepeopleonline.net - OpenSource Development - Master Server Directory - 21st Century American Constitutional Unity Platform (Anyone Will Be Able to Setup Master Servers)
# https://wethepeopleonline.org - OpenSource Development - CSS Theme Development - 21st Century American Constitutional Unity Platform (Non Central Server Dependent)
# https://uscaselaw.org/21st-century-american-exodus-lat-expod
# If the Websites are DDOS Downtime... You can go to archive.org and see how much I was able to accomplish while being attacked by Corrupt and Criminal Snohomish County Local Governments 
# and their Loyal Co-Conspirators undermining My Rights, The Constitutions (Federal and WA State), and All 80,000+ American Constitutionally Bound Governments across OUR Republic!

# All courtlistener.com JSON Datasets (Before Mike Lissener switched to CSV dumps and removing URL's from Opinions on top of the other data removed that is sold) have been 
# Safeguarded at the Following Internet Archive [Archive.org] URL's :

# Courtlistener.com JSON Opinions Files - 03/2022 - Bulk Data Safeguarded
# Archive.org Safeguard of March, 2022 American Constitutionally Guaranteed and Protected Judicial Court Opinion JSON's (20-30gb) of Free Law Project [My Last Download before the switch to CSV with dropped URL columns]: 
# https://archive.org/details/12.02.2022_freelawproject_cl_bulk_data_03.2022_opinion_jsons_american_law_safeguard

# Courtlistener.com JSON Court Docket Files - 03/2022 - Bulk Data Safeguarded
# Archive.org Safeguard of March, 2022 American Constitutionally Guaranteed and Protected Judicial Court Docket JSON's (6gb) of Free Law Project [My Last Download before the switch to CSV with dropped URL columns]: 
# https://archive.org/details/12.23.2022_freelawproject_cl_bulk_data_03.2022_docket_jsons_american_law_safeguard

# Courtlistener.com JSON Court Audio Files - 03/2022 - Bulk Data Safeguarded
# Archive.org Safeguard of March, 2022 American Constitutionally Guaranteed and Protected Judicial Court Audio JSON's (Kilobytes - Megabytes) of Free Law Project [My Last Download before the switch to CSV with dropped URL columns]: 
# https://archive.org/details/12.23.2022_freelawproject_cl_bulk_data_03.2022_audio_jsons_us_american_law_parti


# Date: 03/03/2023
# Updaed Date: 03/03/2023
# Updated Time: Approx. 14:43

# Codename: "Arrowhead"

# (proiectum coperire fortificationem!) [Lat.]
# Projectile Cover Fortification [En.]

# American Constitutional Supreme and Mandatory Primary Source Case Law Bulk Data Parser
# America; To The Republic, For WHICH IT STANDS! - USCODE4 - Pledge of Allegiance; The Manner if In Which, The Flag
# Codename Target: courtlistener.com (OpenSource American Constitutional Supreme and Mandatory Law Source by Mike Lissener - Executive Director, Free Law Project)

# Debian 11 Bullseye
# Coded by: KnowledgeShark, streetdancer, "LightHouseProphet" ;) , TruthSword | Mr. Brandon Kastning

# python3.11 -V output:
# Python 3.11.1

##### Jesus Christ of Nazareth
##### Genesis-Revelation (KJV/KJV1611)
##### #LetHISPeopleGo
##### "And oppress not the widow, nor the fatherless, the stranger, nor the poor; and ...” - Zechariah 7:10 (KJV)
##### “And I will give power unto my two witnesses, and they shall prophesy a thousand two hundred and threescore days, clothed in sackcloth.” - Revelation 11:3 (KJV)
##### Online Source: https://www.kingjamesbibleonline.org/Zechariah-7-10/
##### Online Source: https://www.kingjamesbibleonline.org/Revelation-11-3/

##### Vox Populi, Vox Dei (Lat.)
##### "The Voice of The People is the Voice of God!"

# Specials Shouts to: __jinsun, nedbat, Repiphany, EdFletcher, BrenBarn, songd, Falc, SnoopJ, grym, auctus, rindolf, dba, deltab, supakeen, ,han-solo, 
# phy1729, Tashtari, Staph, mefistofeles, FunkyBob, hop, ali1234, ChrisWarrick, eyepeetee, JAA, bjs, A_Dragon, and _8lurry who have helped me get this far!
# irc.libera.chat #python
# KnowledgeShark

#### Veritas, Libertas, Justitia (Lat.)
#### Truth, Liberty And Justice

##### Coder: Brandon Kastning (Veritas Gladius), Lat.
##### Age:   38
##### Country: American (USA, Constitutional Republic)
##### Home Free & Independent State: Washington
##### Disabled American Constitutional Law Student

# U.S. Constitutional Supreme and Mandatory American Primary Source Law - Bulk Data Parser & Data Recovery for courtlistener.com American Judges Decisions

# Python 3 (Debian 11/Bullseye_x64)
# Python 3.11.1
# MariaDB 10.5.15

# Python 3.11.1 Libraries Installed:

# root@IceDragon:/usr/bin# /usr/local/bin/python3.11 -m pip install --upgrade pip
# root@FireDragon:~/Python-3.11.1# python3.11 -m pip install --upgrade pip
# python3.11 -m pip install pandas
# python3.11 -m pip install openpyxl
# python3.11 -m pip install odfpy
# python3.11 -m pip install bs4
# python3.11 -m pip install mysql-connector-python
# python3.11 -m pip install sqlalchemy
# python3.11 -m pip install pymysql
# python3.11 -m pip install mariadb
# python3.11 -m pip install csvkit
# python3.11 -m pip install requests
# python3.11 -m pip install beautifulsoup4
# python3.11 -m pip install mysql-connector-python-rf
# python3.11 -m pip install lxml
# python3.11 -m pip install html5
# python3.11 -m pip install html5lib
# apt install python3-mysqldb
# apt install python3-lxml
# apt install libmariadb3 libmariadb-dev

# python3.11 -m pip install Jinja2
# Source URL: https://jinja.palletsprojects.com/en/3.1.x/
# Source URL: https://pypi.org/project/Jinja2/

# root@FireDragon:~# apt install python3-pypdf2
# # python3.11 -m pip install pypdf2

# root@FireDragon:/home/brandon/Downloads# python3.11 -m pip install PyMuPDF

# python3.11 -m pip install --upgrade pip

# apt-get install python-tk
# apt-get install python3-tk
# python3.11 -m pip install tk-tools

#root@FireDragon:~/Python-3.11.1# python3.11 -m pip install "kivy[base]" kivy_examples

# Python3 "textextract" 
# Source URL:

# Debian Installation (Pre-Requisites):

# apt install libxml2-dev libxslt1-dev antiword unrtf poppler-utils tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig



# Manual Download .deb "Debian sid" - Debian Main amd64 pstotext_1.9-6+b2_amd64.deb

# root@defensedragon:~# wget http://ftp.de.debian.org/debian/pool/main/p/pstotext/pstotext_1.9-7_amd64.deb

## RESOLVE / REMEDY - 

# root@defensedragon:~# gdebi pstotext_1.9-7_amd64.deb 
# Reading package lists... Done
# Building dependency tree... Done
# Reading state information... Done
# Reading state information... Done
# This package is uninstallable
# Dependency is not satisfiable: libc6 (>= 2.34)

# root@defensedragon:~# apt-get install libc6=2.34
# Reading package lists... Done
# Building dependency tree... Done
# Reading state information... Done
# E: Version '2.34' for 'libc6' was not found


# root@FireDragon:/home/brandon/Downloads# gdebi pstotext_1.9-6+b2_amd64.deb


# python3.11 -m pip install textract


# apt-get install python-tk (No GUI For Dragon Breath F.10, _this_ U.S. Constitutional American Supreme and Mandatory Primary Source Bulk Data Parser; Reference Only!)

# Add Repository to Debian & Upgrade libmariadb3 libmariadb-dev to latest:

# root@DefenseDragon:~ # apt install curl

#root@FireDragon:/home/brandon/Downloads/mariadb-connector-c-3.3.1-debian-buster-amd64# wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
#--2022-07-20 03:28:26--  https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
#Resolving downloads.mariadb.com (downloads.mariadb.com)... 104.17.191.14, 104.18.135.24, 2606:4700::6812:8718, ...
#Connecting to downloads.mariadb.com (downloads.mariadb.com)|104.17.191.14|:443... connected.
#HTTP request sent, awaiting response... 200 OK
#Length: 33361 (33K) [application/octet-stream]
#Saving to: ‘mariadb_repo_setup’

#mariadb_repo_setup                100%[============================================================>]  32.58K  --.-KB/s    in 0s

#2022-07-20 03:28:28 (84.8 MB/s) - ‘mariadb_repo_setup’ saved [33361/33361]

#root@FireDragon:/home/brandon/Downloads/mariadb-connector-c-3.3.1-debian-buster-amd64# chmod +x mariadb_repo_setup
#root@FireDragon:/home/brandon/Downloads/mariadb-connector-c-3.3.1-debian-buster-amd64# ./mariadb_repo_setup
# [info] Checking for script prerequisites.
# [info] MariaDB Server version 10.8 is valid
# [info] Repository file successfully written to /etc/apt/sources.list.d/mariadb.list
# [info] Adding trusted package signing keys...
# [info] Running apt-get update...
# [info] Done adding trusted package signing keys
#root@FireDragon:/home/brandon/Downloads/mariadb-connector-c-3.3.1-debian-buster-amd64# apt upgrade libmariadb3 libmariadb-dev
#Reading package lists... Done
#Building dependency tree... Done
#Reading state information... Done
#Calculating upgrade... Done
#The following packages have been kept back:
#  mariadb-client mariadb-server
# The following packages will be upgraded:
#  galera-4 libmariadb-dev libmariadb3 mariadb-common mysql-common
# 5 upgraded, 0 newly installed, 0 to remove and 2 not upgraded.
# Need to get 12.0 MB of archives.
# After this operation, 55.6 MB of additional disk space will be used.
# Do you want to continue? [Y/n]

# PostgreSQL Connector - psycopg (V3)

# root@FireDragon:~# python3.11 -m pip install psycopg

# root@FireDragon:~# apt-get install python3-psycopg2

# root@FireDragon:~# apt-get install python3-dev
# wget http://http.us.debian.org/debian/pool/main/p/postgresql-13/libpq5_13.8-0+deb11u1_amd64.deb (Buster 10 -- Requires Bullseye)
# root@FireDragon:~# apt-get install libpq5
# root@FireDragon:~# apt-get install libpq-dev

# Global Variables - PostgreSQL (psycopg3)

#dragon_breath_f10_psycopg3_hostname = "localhost"
#dragon_breath_f10_psycopg3_database_name = ""
#dragon_breath_f10_psycopg3_username = ""
#dragon_breath_f10_psycopg3_password = ""

# Source URL: https://stackoverflow.com/questions/70620960/how-to-create-a-database-using-psycopg3?noredirect=1&lq=1

# psycopg3 - Create Database Example:

# Python3:

#conn = psycopg.connect(dbname='postgres', autocommit=True)
#cur = conn.cursor()
#cur.execute('drop database if exists NewDatabaseName')
#cur.execute('create database NewDatabaseName')

#root@FireDragon psql postgres -tl | grep NewDatabaseName

# Source URL: https://www.postgresqltutorial.com/postgresql-python/
# Practical Examples using psycopg3, Python3 and PostgreSQL

# Source URL: https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/
# PostgreSQL Python psycopg2 CRUD (pymysql style)

# root@FireDragon:~# apt-get install python3-psycopg2

# Learning Sources:
# URL: https://www.tutorialspoint.com/python3/python_while_loop.htm
# URL: https://www.freecodecamp.org/news/python-print-variable-how-to-print-a-string-and-variable/
# URL: https://stackoverflow.com/questions/22955684/how-to-import-py-file-from-another-directory
# URL: https://csatlas.com/python-import-file-module/
# URL: https://www.digitalocean.com/community/tutorials/how-to-define-functions-in-python-3
# URL: https://www.digitalocean.com/community/tutorials/how-to-use-variables-in-python-3#global-and-local-variables
# URL: https://csatlas.com/python-import-file-module/
# URL: https://pynative.com/python-check-if-key-exists-in-json-and-iterate-the-json-array/
# URL: https://stackoverflow.com/questions/70514708/how-to-check-if-key-value-already-exist-in-json
# URL: https://www.digitalocean.com/community/tutorials/how-to-define-functions-in-python-3
# URL: https://www.geeksforgeeks.org/check-multiple-conditions-in-if-statement-python/
# URL: https://stackoverflow.com/questions/3400525/global-variable-from-a-different-file-python
# URL: https://circleci.com/blog/object-validation-and-conversion-with-marshamallow/
# URL: https://pynative.com/python-json-validation/
# URL: https://www.pythontutorial.net/python-basics/python-try-except-else/
# URL: https://www.toolsqa.com/python/python-while-loop/
# URL: https://www.w3schools.com/python/python_operators.asp
# URL: https://www.delftstack.com/howto/python/python-get-hostname/
# URL: https://pynative.com/python-get-execution-time-of-program/
# URL: https://www.programiz.com/python-programming/time
# URL: https://docs.python.org/3/tutorial/errors.html
# URL: https://zetcode.com/python/directory/
# URL: https://www.codegrepper.com/code-examples/python/urllib_errors
# URL: https://stackoverflow.com/questions/5191503/how-to-select-the-last-record-of-a-table-in-sql
# URL: https://appdividend.com/2021/08/13/how-to-delete-file-if-exists-in-python/
# URL: https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object
# URL: https://note.nkmk.me/en/python-list-len/
# URL: https://stackoverflow.com/questions/27726639/writing-variables-to-new-line-of-txt-file-in-python
# URL: https://stackoverflow.com/questions/3193060/how-do-i-catch-a-specific-http-error-in-python
# URL: https://stackabuse.com/python-nested-functions/
# URL: https://www.codeproject.com/Questions/1233791/How-to-get-h-tag-with-class-in-web-scraping-Python

# Learning Sources (Python & Internet Archive | WayBack Portal):

# URL: https://www.holisticseo.digital/python-seo/internet-archive/

# Free HTML BOOK: https://greenteapress.com/thinkpython2/html/index.html



# courtlistener.com Bulk Data (New Format - CSV's w/ Dropped Columns since .json's in 04/2022):

# Source URL: https://com-courtlistener-storage.s3-us-west-2.amazonaws.com/list.html?prefix=bulk-data/ (Monthly Updates)

#
#⠀⠀⠀⠀⠀⠀⢠⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠛⠛⠒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⡤⠶⠚⠁⠀⠀⠀⠀⠀⠀⠉⠙⠉⠓⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⢠⣿⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⢈⣿⣧⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⣴⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⣼⡿⢱⣿⣿⡟⣿⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⢰⣿⢃⣿⣿⣿⣱⡿⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀
#⠀⠀⢸⣿⡾⣽⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀
#⠀⠀⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀
#⠀⢀⡿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡧⠀⠀⠀⠀⢀⡶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀
#⠀⡼⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡼⠋⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀
#⢠⠃⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⡀⠀⠀⣀⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀
#⡸⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠓⠖⠊⣁⠀⢀⣠⡄⠀⠀⠀⢀⣠⣤⣤⣤⣤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀
#⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⡾⠁⠀⣀⣤⣤⣤⣾⣿⣿⣟⢿⣷⡄⠀⢀⣾⣿⣿⢛⣭⣤⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
#⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠈⣟⣛⠿⣿⣿⣿⣿⣿⣦⢻⣷⡀⣾⣿⣿⢣⢋⣾⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⢸⡃⠀⠀⠀⠀⠀
#⢹⠀⠸⡀⠀⠀⠀⠀⠀⣠⣿⣠⣤⣾⣿⣿⣿⣮⡻⣿⣿⣿⣿⣿⣿⣷⢻⣿⢏⣷⣿⣿⣿⣿⡿⣫⣵⣿⣿⣿⣶⣤⣤⣤⣄⡀⠀⠀⠀⠘⣿⠀⠀⢸⠇⠀⠀⠀⠀⠀
#⠀⢣⡀⠈⠒⠤⠤⠖⠊⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⣿⣿⣿⣿⣿⣿⣿⣼⣿⢻⣿⣿⢏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠹⡧⠀⣾⠀⠀⠀⠀⠀⠀
#⠀⠀⠑⠦⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⢇⣮⢏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⣿⣸⠇⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⣛⣯⣽⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢤⣠⣿⡟⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣯⣷⣶⣶⣶⣿⣿⣿⣿⣿⠀⠙⢿⡇⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣽⣿⣟⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠙⠦⣀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢸⢻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣤⡄⠈⠿⠛⠛⢿⣿⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠈⠳⣶⣦⣀⠀
#⠀⠀⠀⠀⣾⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⢹⢛⣷⠀⠀⠀⠀⠀⠁⠈⠻⣿⣏⣿⡏⣿⣿⣿⠭⠤⢄⠀⣾⠟⠑⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠈⢻⣮⠁
#⠀⠀⠀⠀⢻⣾⣿⣿⣿⣿⡿⢛⣥⣶⣿⡄⠈⠀⠀⠀⠊⠉⠉⠀⠠⠄⠀⠀⣹⠙⠃⠉⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⢿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢠⡀⠀⠀⣿⡇
#⠀⠀⠀⠀⠀⣿⣿⣿⣿⢟⣴⣿⣿⣿⣿⣿⣦⠀⠀⠄⣀⣀⡀⠀⠀⠀⠈⢳⠈⢦⠐⠀⠀⠀⠀⣠⡜⠀⠀⠻⣿⣿⣿⣿⣷⡙⣿⣿⣿⣿⡇⠀⠀⠀⢸⡷⠀⠀⣿⠇
#⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠈⢿⣿⣷⣄⡀⠀⢀⣀⠘⣄⣀⣀⣴⣿⡿⠁⠀⠀⠀⠹⣿⣿⣿⣿⣿⡸⣿⣿⣿⠃⠀⠀⠀⢸⠇⠀⠀⣿⠀
#⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⠃⠀⠀⠀⢣⣀⣉⠙⣿⣿⡏⠛⠋⠉⠩⢽⣿⣟⠋⢁⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿⣧⣿⣿⣿⠀⠀⠀⠀⠈⠀⠀⣸⠏⠀
#⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⢣⣾⠀⠀⠀⠀⠀⠈⠉⠀⢠⡏⠀⠀⠀⠀⠀⠀⠹⡍⠉⡉⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀
#⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⢣⣿⣿⣆⠀⠀⠀⠀⠀⠈⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠸⣄⠀⠀⢀⣾⣷⣻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⡏⣿⣿⣿⣿⣷⣄⠀⠀⡌⠀⠀⠈⠄⣀⠀⠀⠀⠀⠀⣠⡾⠀⠀⠸⡄⣠⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣤⣇⠀⠀⠀⣢⠭⠤⣀⣀⣀⡠⠽⠧⡀⠉⢠⣿⣯⡹⣷⣻⣿⢸⣿⣿⣿⡿⠁⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⡟⢿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⢳⠶⣶⣤⣤⣴⣶⠶⡶⠃⠀⢸⣿⣯⢻⣽⣿⣿⣼⣿⣿⠏⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢻⡿⣷⢹⣿⣿⣿⣿⢸⣿⣿⣧⡀⠀⠀⠀⠀⠙⢿⣿⡿⠟⠁⠀⠀⣀⣼⣝⢿⣧⣿⣿⣿⢿⡿⠃⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⣧⡠⠚⠁⠙⣇⣻⣿⣿⣿⣼⣿⣿⣿⣿⣦⣀⣀⡀⢀⣀⣠⣦⣀⣠⠔⡊⢹⣿⣿⣧⣻⣿⢿⣿⠼⠁⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⣿⠓⡄⠀⠀⠙⢿⣿⣿⣷⣋⣿⣿⣿⣿⣿⣿⡍⠫⣹⠿⠿⠿⠛⠙⠜⠀⣼⣿⣿⣿⣿⣿⠻⠀⠀⠀⡐⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⢻⢸⠁⠀⠀⠀⠀⠹⢿⣿⣿⡜⣿⣏⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣟⣿⣿⣿⠋⠀⠀⠀⡸⢡⠀⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⢻⣼⠀⠀⡀⠀⠀⠀⠀⠈⠉⠻⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⣤⣤⣴⣾⣿⣿⣼⣾⣿⡟⠀⠀⠀⢸⡃⠁⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣯⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠊⠀⠀⠀⠀⢰⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠸⣆⠀⠀⠀⠀⢀⣀⣸⣿⣿⣿⣿⣿⡼⡟⣿⣿⣽⣿⡇⣿⣿⣿⣿⠛⠃⠀⠀⡎⠀⠀⠀⠀⠀⢰⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⡀⠹⣧⠀⠀⣀⣀⣉⣙⣻⣿⣿⣿⣿⣷⣽⣿⡿⣿⣿⣷⢹⣿⣧⡇⢠⠴⠲⡄⡇⢀⠔⢆⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⡄⢹⡇⠀⠀⠀⠀⠈⣹⣿⣿⡿⠛⠛⠻⢿⣿⣮⣿⣿⣷⣝⢿⢧⣯⠀⢠⡇⣹⢾⠀⢸⠴⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣹⣿⣤⠖⠛⠻⢶⡿⠋⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣯⣿⡞⠀⠙⣆⣸⠛⠉⠀⠳⠾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠛⣡⡞⠁⠀⠀⠐⠉⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠈⡿⣿⣿⣆⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠀⢸⡟⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠇⠀⢀⡀⠀⠀⠀⠀⡇⠸⡇⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⠒⢪⣧⢀⣠⢄⠀⣇⠀⡠⡶⢦⠀⢸⡞⠈⠹⡄⠀⠀⢠⡇⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢀⣾⣾⡏⢃⢸⣇⠸⣶⠁⡇⣼⣄⣸⣧⡀⣼⣷⣦⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣼⠉⠙⠻⡌⢸⣿⡤⠞⢇⡇⡏⠉⠉⠙⣷⠏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢮⡇⠀⠀⠈⠓⠃⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

#        __                                           __
#       (**)                                         (**)
#       IIII                                         IIII
#       ####                                         ####
#       HHHH      Whenever the people are well       HHHH
#       HHHH    informed, they can be trusted with   HHHH
#       ####   their own government; that whenever   ####
#    ___IIII___        things get so far          ___IIII___
# .-`_._"**"_._`-.      wrong as to           .-`_._"**"_._`-.
#|/``  .`\/`.  ``\|    attract their         |/``  .`\/`.  ``\|
#`     }    {     '  notice, they may    `     }    {     '
#      ) () (  be relied on to set them to rights.  ) () (
#      ( :: )                                       ( :: )
#      | :: |    - Thomas Jefferson                 | :: |
#      | )( |                                       | )( |
#      | || |    - to Richard Price                 | || |
#      | || |                                       | || |
#      | || |    - January 8, 1789                  | || |
#      | || |                                       | || |
#      | || |                                       | || |
#      ( () )    - WE THE PEOPLE, USA               ( () )
#       \  /                                         \  /
#        \/      - Constitutional Republic            \/


# ASCII ART Source URL (LION): https://emojicombos.com/lion-ascii-art
# ASCII ART Source URL (SWORDS WITH QUOTE): 
# Authoriative American Constitutional Republic's Thomas Jefferson Historic Quote:
# Source URL: https://www.loc.gov/collections/thomas-jefferson-papers/articles-and-essays/selected-quotations-from-the-thomas-jefferson-papers/

global dragon_breath_f10_hostname
global dragon_breath_f10_cpu_count
global dragon_breath_f10_start_time
global dragon_breath_f10_end_time
global dragon_breath_f10_elapsed_time

import time 

dragon_breath_f10_start_time = time.time()

import os
dragon_breath_f10_hostname = os.uname()

import multiprocessing

dragon_breath_f10_cpu_count = multiprocessing.cpu_count()

global courtlistener_jurisdiction_dataset

global dragon_breath_f10
dragon_breath_f10 = "Dragon Breath [F.10]"
global dragon_breath_f10_codename 
dragon_breath_f10_codename = "Arrowhead"
global dragon_breath_f10_codename_slogan 
dragon_breath_f10_codename_slogan = "proiectum coperire fortificationem!"
global dragon_breath_f10_update_version
#dragon_breath_f10_update_version = "-Update-GroundZero-CL_Exodus_Head_1_R14"
dragon_breath_f10_update_version = "-Update-GroundZero-CL_Exodus_USC4-DEFENSE_R1"
global dragon_breath_f10_logfile_main 
dragon_breath_f10_logfile_main = f"{dragon_breath_f10}{dragon_breath_f10_update_version}.log"

import logging

logging.basicConfig(
    filename=f"{dragon_breath_f10_logfile_main}",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

print(f"Starting {dragon_breath_f10}{dragon_breath_f10_update_version} on Computer Workstation: {dragon_breath_f10_hostname}...")
logging.debug(f"Starting {dragon_breath_f10}{dragon_breath_f10_update_version} on Computer Workstation: {dragon_breath_f10_hostname}...")

print(f"[{dragon_breath_f10}{dragon_breath_f10_update_version}] on Computer Workstation: {dragon_breath_f10_hostname} - Initializing Logging to File...")
logging.debug(f"[{dragon_breath_f10}{dragon_breath_f10_update_version}] on Computer Workstation: {dragon_breath_f10_hostname} - Initializing Logging to File...")

print(f"[{dragon_breath_f10}{dragon_breath_f10_update_version}] - on Computer Workstation: {dragon_breath_f10_hostname} - [Log Filename:]")
logging.debug(f"[{dragon_breath_f10}{dragon_breath_f10_update_version}] - on Computer Workstation: {dragon_breath_f10_hostname} - [Log Filename:]")

print(f"{dragon_breath_f10_logfile_main}")
logging.debug(f"{dragon_breath_f10_logfile_main}")

print(f"Logging to {dragon_breath_f10_logfile_main} established on Computer Workstation: {dragon_breath_f10_hostname} !")

print(f"{dragon_breath_f10}{dragon_breath_f10_update_version} now Calculating Current Workstation's CPU Type, [Intel Support Only For Accurate Logging] Intel I-7 or Intel-5...")
logging.debug(f"{dragon_breath_f10}{dragon_breath_f10_update_version} now Calculating Current Workstation's CPU Type, [Intel Support Only For Accurate Logging] Intel I-7 or Intel-5...")

print(f"[{dragon_breath_f10}{dragon_breath_f10_update_version}] - on Computer Workstation has CPU Count of: {dragon_breath_f10_cpu_count}")
logging.debug(f"[{dragon_breath_f10}{dragon_breath_f10_update_version}] - on Computer Workstation has CPU Count of: {dragon_breath_f10_cpu_count}")

print(f"Feel free to #tail -f {dragon_breath_f10_logfile_main} in a separate terminal to watch in realtime here on Computer Workstation: {dragon_breath_f10_hostname}...")

# Global Variables 
global dataset
global dir_path
global current_json_dataset_file_count
global current_json_dataset_file_path
global my_match
global json_count

# Global Variables - SQLAlchemy

dragon_breath_f10_sqlalchemy_username = "root"
dragon_breath_f10_sqlalchemy_password = "PASSWORD"
dragon_breath_f10_sqlalchemy_hostname = "127.0.0.1"
dragon_breath_f10_sqlalchemy_port_number = "3306"
#dragon_breath_f10_sqlalchemy_database_name = "FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead"
dragon_breath_f10_sqlalchemy_database_name = "DEFENSEDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead"
dragon_breath_f10_sqlalchemy_charset = "utf8mb4"

# Global Variables - mysql.connector

dragon_breath_f10_mysql_connector_hostname = "localhost"
#dragon_breath_f10_mysql_connector_database_name = "FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead"
dragon_breath_f10_mysql_connector_database_name = "DEFENSEDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead"
dragon_breath_f10_mysql_connector_username = "root"
dragon_breath_f10_mysql_connector_password = "PASSWORD"

# Global Variables - PyMySQL

dragon_breath_f10_pymysql_hostname = "localhost"
#dragon_breath_f10_pymysql_database_name = "FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead"
dragon_breath_f10_pymysql_database_name = "DEFENSEDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead"
dragon_breath_f10_pymysql_username = "root"
dragon_breath_f10_pymysql_password = "PASSWORD"

# Global Variables - Main Loop
global iteration_count

dataset = "foler_name"
print("Dragon Breath [F.10] - Welcome to Dragon Breath [F.10], Dragon Master!")
dataset = input("Dragon Breath [F.10] - Please type courtlistener.com dataset folder name to Bulk Parse to MariaDB from dataset/data_folder, Dragon Master! :")
dir_path = f"datasets/{dataset}/"
courtlistener_jurisdiction_dataset = dir_path

print(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Calculating JSON File Count in Current Jurisidictional Dataset]...)")
print(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Calculating The Amount of JSON Files...")
print(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Selecting JSON Directory]...")

import os
dir_path = rf'datasets/{dataset}/'
print(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [JSON Directory: datasets/{dataset}/]...")
logging.debug(f"[courtlistener.com American Constitutional Republic's Supreme and Mandatory U.S. Case Law Jurisdictional Dataset Selected: {courtlistener_jurisdiction_dataset} ]")

def Startup_Flush():
    global courtlistener_jurisdiction_dataset
    global dir_path
    print(f"Dragon Breath [F.10] - [Startup Flat File Flush] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Deleting wd.json.files.count.txt")
    logging.debug(f"Dragon Breath [F.10] - [Startup Flat File Flush] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Deleting wd.json.files.count.txt")
            
    import os
    
    # Current CL Dataset JSON File Count
    if os.path.exists(f"{dir_path}/wd.json.files.count.txt"):
        os.remove(f"{dir_path}/wd.json.files.count.txt")
        print("wd.json.files.count.txt has been deleted successfully")
    else:
        print("wd.json.files.count.txt does not exist!")

    print(f"Dragon Breath [F.10] - [Startup Flat File Flush] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Deleting wd.json.files.txt")
    logging.debug(f"Dragon Breath [F.10] - [Startup Flat File Flush] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Deleting wd.json.files.txt")

    # Current CL Dataset JSON File List
    if os.path.exists(f"{dir_path}/wd.json.files.txt"):
        os.remove(f"{dir_path}/wd.json.files.txt")
        print("wd.json.files.txt has been deleted successfully")
    else:
        print("wd.json.files.txt does not exist!")

    print(f"Dragon Breath [F.10] - [Startup Flat File Flush] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Deleting dataset_json_files_variant_e.txt")
    logging.debug(f"Dragon Breath [F.10] - [Startup Flat File Flush] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Deleting dataset_json_files_variant_e.txt")

    # Current CL Data JSON Files by Schema Variants: Variant: [A]
    if os.path.exists(f"{dir_path}/dataset_json_files_variant_a.txt"):
        os.remove(f"{dir_path}/dataset_json_files_variant_a.txt")
        print(f"{dir_path}/dataset_json_files_variant_a.txt has been deleted successfully")
    else:
        print(f"{dir_path}/dataset_json_files_variant_a.txt does not exist!")

    # Current CL Data JSON Files by Schema Variants: Variant: [B]
    if os.path.exists(f"{dir_path}/dataset_json_files_variant_b.txt"):
        os.remove(f"{dir_path}/dataset_json_files_variant_b.txt")
        print(f"{dir_path}/dataset_json_files_variant_b.txt has been deleted successfully")
    else:
        print(f"{dir_path}/dataset_json_files_variant_b.txt does not exist!")

    # Current CL Data JSON Files by Schema Variants: Variant: [C]
    if os.path.exists(f"{dir_path}/dataset_json_files_variant_c.txt"):
        os.remove(f"{dir_path}/dataset_json_files_variant_c.txt")
        print(f"{dir_path}/dataset_json_files_variant_c.txt has been deleted successfully")
    else:
        print(f"{dir_path}/dataset_json_files_variant_c.txt does not exist!")

    # Current CL Data JSON Files by Schema Variants: Variant: [D]
    if os.path.exists(f"{dir_path}/dataset_json_files_variant_d.txt"):
        os.remove(f"{dir_path}/dataset_json_files_variant_d.txt")
        print(f"{dir_path}/dataset_json_files_variant_d.txt has been deleted successfully")
    else:
        print(f"{dir_path}/dataset_json_files_variant_d.txt does not exist!")

    # Current CL Data JSON Files by Schema Variants: Variant: [E]
    if os.path.exists(f"{dir_path}/dataset_json_files_variant_e.txt"):
        os.remove(f"{dir_path}/dataset_json_files_variant_e.txt")
        print(f"{dir_path}/dataset_json_files_variant_e.txt has been deleted successfully")
    else:
        print(f"{dir_path}/dataset_json_files_variant_e.txt does not exist!")

    # Current CL Data JSON Files by Schema Variants: Variant: [F]
    if os.path.exists(f"{dir_path}/dataset_json_files_variant_f.txt"):
        os.remove(f"{dir_path}/dataset_json_files_variant_f.txt")
        print(f"{dir_path}/dataset_json_files_variant_f.txt has been deleted successfully")
    else:
        print(f"{dir_path}/dataset_json_files_variant_f.txt does not exist!")

    # Current CL Data JSON Files by Schema Variants: Variant: [G]
    if os.path.exists(f"{dir_path}/dataset_json_files_variant_g.txt"):
        os.remove(f"{dir_path}/dataset_json_files_variant_g.txt")
        print(f"{dir_path}/dataset_json_files_variant_g.txt has been deleted successfully")
    else:
        print(f"{dir_path}/dataset_json_files_variant_g.txt does not exist!")

    # Current CL Data JSON Files Extracted Absolute URLs: [Person]
    if os.path.exists(f"{dir_path}/extracted_person_absolute_urls.txt"):
        os.remove(f"{dir_path}/extracted_person_absolute_urls.txt")
        print(f"{dir_path}/extracted_person_absolute_urls.txt has been deleted successfully")
    else:
        print(f"{dir_path}/extracted_person_absolute_urls.txt does not exist!")

    # Current CL Data JSON Files Extracted Absolute URLs: [Person_SCOTUS]
    if os.path.exists(f"{dir_path}/extracted_person__scotus_absolute_urls.txt"):
        os.remove(f"{dir_path}/extracted_person_scotus_absolute_urls.txt")
        print(f"{dir_path}/extracted_person_scotus_absolute_urls.txt has been deleted successfully")
    else:
        print(f"{dir_path}/extracted_person_scotus_absolute_urls.txt does not exist!")

    # Current CL Data JSON Files Extracted Absolute URLs: [Summary]
    if os.path.exists(f"{dir_path}/extracted_summary_absolute_urls.txt"):
        os.remove(f"{dir_path}/extracted_summary_absolute_urls.txt")
        print(f"{dir_path}/extracted_summary_absolute_urls.txt has been deleted successfully")
    else:
        print(f"{dir_path}/extracted_summary_absolute_urls.txt does not exist!")

    # Current CL Data JSON Files Extracted Absolute URLs: [Summary_SCOTUS]
    if os.path.exists(f"{dir_path}/extracted_summary_scotus_absolute_urls.txt"):
        os.remove(f"{dir_path}/extracted_summary_scotus_absolute_urls.txt")
        print(f"{dir_path}/extracted_summary_scotus_absolute_urls.txt has been deleted successfully")
    else:
        print(f"{dir_path}/extracted_summary_scotus_absolute_urls.txt does not exist!")

    # Current CL Data JSON Files Extracted Absolute URLs: [Cites]
    if os.path.exists(f"{dir_path}/extracted_cites_absolute_urls.txt"):
        os.remove(f"{dir_path}/extracted_cites_absolute_urls.txt")
        print(f"{dir_path}/extracted_cites_absolute_urls.txt has been deleted successfully")
    else:
        print(f"{dir_path}/extracted_cites_absolute_urls.txt does not exist!")

    # Current CL Data JSON Files Extracted Absolute URLs: [Authorities]
    if os.path.exists(f"{dir_path}/extracted_authorities_absolute_urls.txt"):
        os.remove(f"{dir_path}/extracted_authorities_absolute_urls.txt")
        print(f"{dir_path}/extracted_authorities_absolute_urls.txt has been deleted successfully")
    else:
        print(f"{dir_path}/extracted_authorities_absolute_urls.txt does not exist!")


    print(f"Dragon Breath [F.10] - [Startup Flat File Flush] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Start Flat File Flush Completed Succesfully!")
    logging.debug(f"Dragon Breath [F.10] - [Startup Flat File Flush] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Start Flat File Flush Completed Succesfully!")    

Startup_Flush()

print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Now Setting JSON Current Datasets File Count Python Variable: count to 0]...")

count = 0
# Iterate Directory
for path in os.listdir(dir_path):
    # Check if Current Path is a File
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print(f'Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] File Count:', count)
    #print(f'Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] File Count:', count)
    #logging.debug(f'Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] File Count:', count)

print(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Assigning count Python Variable to Python Variable current_json_dataset_file_count...")
current_json_dataset_file_count = count
print(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Assigned count Python Variable to Python Variable current_json_dataset_file_count!")
backup_current_json_dataset_file_count = current_json_dataset_file_count
print(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Assigned current_json_data_set_file_count to backup_current_json_dataset_file_count!")

current_json_dataset_file_path = dir_path
backup_current_json_dataset_file_path = current_json_dataset_file_path
print(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Assigned current_json_dataset_file_path to backup_current_json_dataset_file_path")
print(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - There are currently x amount of JSON Files in this Datasets working directory:")
print(count)
logging.debug(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - There are currently x amount of JSON Files in this Datasets working directory:")
logging.debug(count)

# Write Current Working Directories JSON file(s) (count) -> .txt
import fnmatch
import os

print(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Writing Current Dataset JSON File Count to [wd.json.files.count.txt]")
file = open(f"{dir_path}wd.json.files.count.txt", "w")

# Source to working file.write with specified str(variable) or int(variable)
# irc.libera.chat #python - Repiphany - Thanks :)

file.write(str(current_json_dataset_file_count))
file.close
print(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Current Dataset JSON File Count to [wd.json.files.count.txt] Successful!")
logging.debug(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Current Dataset JSON File Count to [wd.json.files.count.txt] Successful!")

# irc.libera.chat #python - Thanks to songd for file.write line by line variable write to .txt!
# 03/14/2022 @ Approx. 20:40:12

print(f"Dragon Breath [F.10] - [Table 01/10] -[CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now importing Python Libraries fnmatch and os...")
import fnmatch
import os
print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Python Libraries fnmatch and os have been successfully loaded!")
print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now calculating all JSON files in this working directory...")
my_match = []

# American Constitutional Supreme and Mandatory Primary Source Law Jurisdiction JSON Directory:
for file in os.listdir(f"{dir_path}/"):
#for file in os.listdir(f"/home/brandon/python_dragon_breath_f10/codename_arrowhead/datasets/{dataset}/"):
#for file in os.listdir("/home/brandon/python_dragon_breath_f10/codename_speedracer/datasets/dataset1/"):
#    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - [datasets/dataset1/] ... Calculating...")

#    if fnmatch.fnmatch(file, '*.json'):
    if fnmatch.fnmatch(file, '*.json'):
#        print(file)
        my_match.append(file)
print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Calculating all JSON files in current dataset directory successful!")
logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Calculating all JSON files in current dataset directory successful!")
#print(my_match)
print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now writing calculated JSON files in this working directory to wd.json.files.txt...")
file = open(f"{dir_path}wd.json.files.txt", "w")
# Thanks songd! :
file.write('\n'.join(my_match))
file.close
print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished writing wd.json.files.txt with all JSON files in this working directory!")
logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished writing wd.json.files.txt with all JSON files in this working directory!")

print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Storing JSON File Count to Python Variable: 'json_count'...")
logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Storing JSON File Count to Python Variable: 'json_count'...")

# Storing JSON File Count from Python List 'my_match' into Python Variable 'json_count'
json_count = len(my_match)

print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Storing JSON File Count to Python Variable: 'json_count' Successful!")
logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Storing JSON File Count to Python Variable: 'json_count' Successful!")

def my_match_total():
    # Take my_match & Check if it's a List
    print(type(my_match) is list)

# Table 1-A/08: 

# Check if a KEYS x 4 exist in a .json (21):
# KEY Check -> html_lawbox
# KEY Check -> html_columbia
# KEY Check -> html_anon_2020
# KEY Check -> xml_harvard

# Current Bulk Data URL: https://com-courtlistener-storage.s3-us-west-2.amazonaws.com/list.html?prefix=bulk-data/
# Current Bulk Data Update: More Dropped Columns (i.e. - absolute_urls, etc.) as of 08/02/2022 New CL Bulk Data Amazon Datastore

# All American Constitutional Supreme and Mandatory Public Court Judge Decisions (Bulk Archive from courtlistener.com web.archive.org on date: 07/15/2021):
# URL: https://web.archive.org/web/20210715231137/https://www.courtlistener.com/api/bulk-data/opinions/all.tar (38GB) - Doesn't Actually download past 2GB (08/11/2022)
# ^ Contains absolute_url's, etc w/ Zero Case Names, Precedential Status, Date Filed, etc.

# 5 Randomly Picked .JSON Files Based on Incremental File Size for Bulk Parser Development [Washington State Supreme Court]:

# JSON #1 Fulltext American Court Decision URL: https://www.courtlistener.com/opinion/1189556/mcmillan-v-great-northern-r-co/
# JSON #1 JSON American Court Decision Download URL: https://www.courtlistener.com/api/rest/v3/opinions/1189556/?format=json

# JSON #2 Fulltext American Court Decision URL: https://www.courtlistener.com/opinion/2581757/amalgamated-transit-v-state/
# JSON #2 JSON American Court Decision Download URL: https://www.courtlistener.com/api/rest/v3/opinions/2581757/?format=json

# JSON #3 Fulltext American Court Decision URL: https://www.courtlistener.com/opinion/2632900/san-juan-county-v-no-new-gas-tax/
# JSON #3 JSON American Court Decision Download URL: https://www.courtlistener.com/api/rest/v3/opinions/2632900/?format=json

# JSON #4 Fulltext American Court Decision URL: https://www.courtlistener.com/opinion/4902955/state-v-schierman/
# JSON #4 JSON American Court Decision Download URL: https://www.courtlistener.com/api/rest/v3/opinions/4706734/?format=json

# JSON #5 Fulltext American Court Decision URL: https://www.courtlistener.com/opinion/4923927/state-v-abraham/
# JSON #5 JSON American Court Decision Download URL: https://www.courtlistener.com/api/rest/v3/opinions/4731065/?format=json

# Global Variables Defined for Main Loop:

global src

# Global Variables Defined for Tables 01-08: 

# Table #01/08 Global Variables: 

global current_json_key_dataset_variant
global current_json_key_dataset
global current_json_dataset_final

global CurrentDecision

global pvar_value_resource_uri
global pvar_value_id 
global pvar_value_absolute_url 
global pvar_value_cluster 
global pvar_value_date_created 
global pvar_value_date_modified 
global pvar_value_per_curiam 
global pvar_value_type 
global pvar_value_sha1 
global pvar_value_page_count 
global pvar_value_download_url 
global pvar_value_local_path 
global pvar_value_plain_text 
global pvar_value_html 
global pvar_value_html_lawbox 
global pvar_value_html_columbia 
global pvar_value_html_anon_2020 
global pvar_value_xml_harvard 
global pvar_value_html_with_citations 
global pvar_value_extracted_by_ocr 
global pvar_value_opinions_cited 

# Table #02/08 Global Variables:

global urlpart2
global url_part_1
global url_join
global pvar_courtlistener_absolute_url_trimmed_1_leading
global sql_full_url_insert

# Table #03/08 Global Variables:

global filename 
global file_broken_up_1 
global file_broken_up_2

# Table #04/08 Global Variables:
global html

# JSON Keys Required: html (1 Key)

def KeyCheckA(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Checking if Current JSON File is Variant A...")
    if(all(key in CurrentDecision for key in ['html'])):
        print("The Current JSON File is Variant A: html (1 Key)")
        global current_json_key_dataset_variant
        global current_json_key_dataset
        current_json_key_dataset_variant = "A"
        current_json_key_dataset = "A"
        print("Function KeyCheck-A Completed!")
    else:
        print("This Current JSON File is NOT Variant A!")   

# JSON Keys Required: html, html_lawbox (2 Keys)

def KeyCheckB(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Checking if Current JSON File is Variant B...")
    if(all(key in CurrentDecision for key in ['html', 'html_lawbox'])):
        print("The Current JSON File is Variant B: html and html_lawbox (2 Keys)")
        global current_json_key_dataset_variant
        global current_json_key_dataset
        current_json_key_dataset_variant = "B"
        current_json_key_dataset = "B"
        print("Function KeyCheck-B Completed!")
    else:
        print("This Current JSON File is NOT Variant B!")   

# JSON Keys Required: html, html_lawbox, html_columbia (3 Keys)

def KeyCheckC(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Checking if Current JSON File is Variant C...")
    if(all(key in CurrentDecision for key in ['html', 'html_lawbox', 'html_columbia'])):
        print("The Current JSON File is Variant C: html, html_lawbox and html_columbia (3 Keys)")
        global current_json_key_dataset_variant
        global current_json_key_dataset
        current_json_key_dataset_variant = "C"
        current_json_key_dataset = "C"
        print("Function KeyCheck-C Completed!")
    else:
        print("This Current JSON File is NOT Variant C!")   

# JSON Keys Required: html, html_anon_2020, xml_harvard (3 Keys)

def KeyCheckD(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Checking if Current JSON File is Variant D...")
    if(all(key in CurrentDecision for key in ['html', 'html_anon_2020', 'xml_harvard'])):
        print("The Current JSON File is Variant D: html, html_anon_2020 and xml_harvard (3 Keys)")
        global current_json_key_dataset_variant
        global current_json_key_dataset
        current_json_key_dataset_variant = "D"
        current_json_key_dataset = "D"
        print("Function KeyCheck-D Completed!")
    else:
        print("This Current JSON File is NOT Variant D!")   

# JSON Keys Required: html, html_lawbox, html_columbia, xml_harvard (4 Keys)

def KeyCheckE(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Checking if Current JSON File is Variant E...")
    if(all(key in CurrentDecision for key in ['html', 'html_lawbox', 'html_columbia', 'xml_harvard'])):
        print("The Current JSON File is Variant E: html, html_lawbox, html_columbia and xml_harvard (4 Keys)")
        global current_json_key_dataset_variant
        global current_json_key_dataset
        current_json_key_dataset_variant = "E"
        current_json_key_dataset = "E"
        print("Function KeyCheck-E Completed!")
    else:
        print("This Current JSON File is NOT Variant E!")   

# JSON Keys Required: html, html_lawbox, html_columbia, html_anon_2020 (4 Keys)

def KeyCheckF(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Checking if Current JSON File is Variant F...")
    if(all(key in CurrentDecision for key in ['html', 'html_lawbox', 'html_columbia', 'html_anon_2020'])):
        print("The Current JSON File is Variant F: html, html_lawbox, html_columbia and html_anon_2020 (4 Keys)")
        global current_json_key_dataset_variant
        global current_json_key_dataset
        current_json_key_dataset_variant = "F"
        current_json_key_dataset = "F"
        print("Function KeyCheck-F Completed!")
    else:
        print("This Current JSON File is NOT Variant F!")   

# JSON Keys Required: html, html_lawbox, html_columbia, html_anon_2020, xml_harvard (5 Keys)

def KeyCheckG(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Checking if Current JSON File is Variant G...")
    if(all(key in CurrentDecision for key in ['html', 'html_lawbox', 'html_columbia', 'html_anon_2020', 'xml_harvard'])):
        print("The Current JSON File is Variant G: html, html_lawbox, html_columbia, html_anon_2020 and xml_harvard (5 Keys)")
        global current_json_key_dataset_variant
        global current_json_key_dataset
        current_json_key_dataset_variant = "G"
        current_json_key_dataset = "G"
        print("Function KeyCheck-G Completed!")
    else:
        print("This Current JSON File is NOT Variant F!")   

# Functions to Determine What the Final JSON Dataset SQLAlchemy Schema is by Process of Elimination... (Execution Order Determines 100% Accuracy)

def KeyDeterminationA(CurrentDecision, current_json_filename):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Current JSON Dataset Schema Determination Calculation Started...")
    global current_json_key_dataset
    global current_json_dataset_final
    if(current_json_key_dataset == "A"):
        print("Current JSON Dataset Schema Determined to be: [A]")
        current_json_dataset_final = "A"
        # Log dataset, filename
        with open(f'{dir_path}/dataset_json_files_variant_a.txt', 'at') as f:
            f.write(current_json_filename + "\n")
            f.close()
    else:
        print("Current JSON Dataset Schema Determined not to be: [A]")

def KeyDeterminationB(CurrentDecision, current_json_filename):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Current JSON Dataset Schema Determination Calculation Started...")
    global current_json_key_dataset
    global current_json_dataset_final
    if(current_json_key_dataset == "B"):
        print("Current JSON Dataset Schema Determined to be: [B]")
        current_json_dataset_final = "B"
        # Log dataset, filename
        with open(f'{dir_path}/dataset_json_files_variant_b.txt', 'at') as f:
            f.write(current_json_filename + "\n")
            f.close()
    else:
        print("Current JSON Dataset Schema Determined not to be: [B]")

def KeyDeterminationC(CurrentDecision, current_json_filename):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Current JSON Dataset Schema Determination Calculation Started...")
    global current_json_key_dataset
    global current_json_dataset_final
    if(current_json_key_dataset == "C"):
        print("Current JSON Dataset Schema Determined to be: [C]")
        current_json_dataset_final = "C"
        # Log dataset, filename
        with open(f'{dir_path}/dataset_json_files_variant_c.txt', 'at') as f:
            f.write(current_json_filename + "\n")
            f.close()
    else:
        print("Current JSON Dataset Schema Determined not to be: [C]")

def KeyDeterminationD(CurrentDecision, current_json_filename):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Current JSON Dataset Schema Determination Calculation Started...")
    global current_json_key_dataset
    global current_json_dataset_final
    if(current_json_key_dataset == "D"):
        print("Current JSON Dataset Schema Determined to be: [D]")
        current_json_dataset_final = "D"
        # Log dataset, filename
        with open(f'{dir_path}/dataset_json_files_variant_d.txt', 'at') as f:
            f.write(current_json_filename + "\n")
            f.close()
    else:
        print("Current JSON Dataset Schema Determined not to be: [D]")

def KeyDeterminationE(CurrentDecision, current_json_filename):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Current JSON Dataset Schema Determination Calculation Started...")
    global current_json_key_dataset
    global current_json_dataset_final
    if(current_json_key_dataset == "E"):
        print("Current JSON Dataset Schema Determined to be: [E]")
        current_json_dataset_final = "E"
        # Log dataset, filename
        with open(f'{dir_path}/dataset_json_files_variant_e.txt', 'at') as f:
            f.write(current_json_filename + "\n")
            f.close()
    else:
        print("Current JSON Dataset Schema Determined not to be: [E]")

def KeyDeterminationF(CurrentDecision, current_json_filename):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Current JSON Dataset Schema Determination Calculation Started...")
    global current_json_key_dataset
    global current_json_dataset_final
    if(current_json_key_dataset == "F"):
        print("Current JSON Dataset Schema Determined to be: [F]")
        current_json_dataset_final = "F"
        # Log dataset, filename
        with open(f'{dir_path}/dataset_json_files_variant_f.txt', 'at') as f:
            f.write(current_json_filename + "\n")
            f.close()
    else:
        print("Current JSON Dataset Schema Determined not to be: [F]")

def KeyDeterminationG(CurrentDecision, current_json_filename):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Current JSON Dataset Schema Determination Calculation Started...")
    global current_json_key_dataset
    global current_json_dataset_final
    if(current_json_key_dataset == "G"):
        print("Current JSON Dataset Schema Determined to be: [G]")
        current_json_dataset_final = "G"
        # Log dataset, filename
        with open(f'{dir_path}/dataset_json_files_variant_g.txt', 'at') as f:
            f.write(current_json_filename + "\n")
            f.close()
    else:
        print("Current JSON Dataset Schema Determined not to be: [G]")

def Table01_A(CurrentDecision):
        global courtlistener_jurisdiction_dataset
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
        global pvar_value_absolute_url
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant: [A] - Importing all Required Python3 Module Libraries...")
        import json
        import sqlalchemy
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.dialects.mysql import LONGTEXT
        import datetime
        from sqlalchemy import Column, Integer, DateTime
        from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
        from sqlalchemy import Index
        from sqlalchemy import ForeignKeyConstraint
        from sqlalchemy import insert
        from sqlalchemy.sql import select
        from sqlalchemy.sql import func
        from sqlalchemy import cast
        from sqlalchemy import and_, or_, not_
        from sqlalchemy import update, delete
        from sqlalchemy import text
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")
        logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Starting Basic JSON Loader to MariaDB using SQLAlchemy & MariaDB-Connector...")
        # Define the MariaDB engine using MariaDB Connector/Python
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost...")
        #engine = sqlalchemy.create_engine("mysql+pymysql://brandon:__VqE3QVAZmDEx__jkabjKKvR7uGcN__@127.0.0.1:3306/FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead?charset=utf8mb4")
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{dragon_breath_f10_sqlalchemy_username}:{dragon_breath_f10_sqlalchemy_password}@{dragon_breath_f10_sqlalchemy_hostname}:{dragon_breath_f10_sqlalchemy_port_number}/{dragon_breath_f10_sqlalchemy_database_name}?charset={dragon_breath_f10_sqlalchemy_charset}")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost Successful!")
        logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost Successful!")
        # Start an instance of MariaDB-Connector
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initializing...")
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=engine)
        Session = Session()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initialized Successfully!")
        logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initialized Successfully!")
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping Remote MariaDB Table Schematics (21 Columns)...")
        Base = declarative_base()

        class JudicialDecision21Columns(Base):

            __tablename__ = 'Current_JSON_CL_Dataset_Exodus_Table01_File'
            id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
            courtlistener_resource_uri = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_id = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_absolute_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_cluster = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_created = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_modified = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_per_curiam = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_type = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_sha1 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_page_count = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_download_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_local_path = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_plain_text = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_lawbox = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_columbia = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_anon_2020 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_xml_harvard = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_with_citations = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_extracted_by_ocr = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_opinions_cited = sqlalchemy.Column(sqlalchemy.Text)
        # exodus_courtlistener_opinion_entry_timestamp = sqlalchemy.Column(sqlalchemy.DateTime)
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Defined Remote MariaDB & Table Schematics! (21 Columns)")
        logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Defined Remote MariaDB & Table Schematics! (21 Columns)")
        print(f"Current JSON File - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant [A] Map & Payload Verified!")
        logging.debug(f"Current JSON File - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant [A] Map & Payload Verified!")
        
        # Show Only Keys (No Value Names)
        # Assign JSON Key Name to a Python Variable (17) + 4 NULLED  w/ "(NULL)"
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table 01 SCHEMA: [A]...")
        pvar_key_resource_uri = ("resource_uri")
        pvar_key_id = ("id")
        pvar_key_absolute_url = ("absolute_url")
        pvar_key_cluster = ("cluster")
        pvar_key_date_created = ("date_created")
        pvar_key_date_modified = ("date_modified")
        pvar_key_per_curiam = ("per_curiam")
        pvar_key_type = ("type")
        pvar_key_sha1 = ("sha1")
        pvar_key_page_count = ("page_count")
        pvar_key_download_url = ("download_url")
        pvar_key_local_path = ("local_path")
        pvar_key_plain_text = ("plain_text")
        pvar_key_html = ("html")
        pvar_key_html_with_citations = ("html_with_citations")
        pvar_key_extracted_by_ocr = ("extracted_by_ocr")
        pvar_key_opinions_cited = ("opinions_cited")
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table 01 SCHEMA: [A] Successful!")
        logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table 01 SCHEMA: [A] Successful!")

        # Show Only Values (No Key Names)
        # Assign JSON Key Value to a Python Variable (17) + 4 NULLED w/ "(NULL)"
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table 01 SCHEMA: [A]...")
        logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table 01 SCHEMA: [A]...")
        pvar_value_resource_uri = str(CurrentDecision['resource_uri'])
        pvar_value_id = str(CurrentDecision['id'])
        pvar_value_absolute_url = str(CurrentDecision['absolute_url'])
        pvar_value_cluster = str(CurrentDecision['cluster'])
        pvar_value_date_created = str(CurrentDecision['date_created'])
        pvar_value_date_modified = str(CurrentDecision['date_modified'])
        pvar_value_per_curiam = str(CurrentDecision['per_curiam'])
        pvar_value_type = str(CurrentDecision['type'])
        pvar_value_sha1 = str(CurrentDecision['sha1'])
        pvar_value_page_count = str(CurrentDecision['page_count'])
        pvar_value_download_url = str(CurrentDecision['download_url'])
        pvar_value_local_path = str(CurrentDecision['local_path'])
        pvar_value_plain_text = str(CurrentDecision['plain_text'])
        pvar_value_html = str(CurrentDecision['html'])
        pvar_value_html_with_citations = str(CurrentDecision['html_with_citations'])
        pvar_value_html_lawbox = "(NULL)"
        pvar_value_html_columbia = "(NULL)"
        pvar_value_html_anon_2020 = "(NULL)"
        pvar_value_xml_harvard = "(NULL)"
        pvar_value_extracted_by_ocr = str(CurrentDecision['extracted_by_ocr'])
        pvar_value_opinions_cited = str(CurrentDecision['opinions_cited'])
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table 01  SCHEMA: [A] Successful!")
        logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table 01  SCHEMA: [A] Successful!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting The JSON File(s) -> MariaDB 10.5.15 Payload [A]...")
        KeyPair_17_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html=pvar_value_html, courtlistener_html_lawbox=pvar_value_html_lawbox, courtlistener_html_columbia=pvar_value_html_columbia, courtlistener_html_anon_2020=pvar_value_html_anon_2020, courtlistener_xml_harvard=pvar_value_xml_harvard, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        #KeyPair_17_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        Session.add(KeyPair_17_Hit_Combo)
        Session.commit()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Inserted All 17 Key/Value Pairs + 4 Nulled Values to MariaDB SQLAlchemy Mapped Columns into MariaDB 10.5.15 SCHEMA: [A]")
        logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Inserted All 17 Key/Value Pairs + 4 Nulled Values to MariaDB SQLAlchemy Mapped Columns into MariaDB 10.5.15 SCHEMA: [A]")

def Table01_B(CurrentDecision):
        global courtlistener_jurisdiction_dataset
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
        global pvar_value_absolute_url
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant: [B] - Importing all Required Python3 Module Libraries...")
        import json
        import sqlalchemy
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.dialects.mysql import LONGTEXT
        import datetime
        from sqlalchemy import Column, Integer, DateTime
        from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
        from sqlalchemy import Index
        from sqlalchemy import ForeignKeyConstraint
        from sqlalchemy import insert
        from sqlalchemy.sql import select
        from sqlalchemy.sql import func
        from sqlalchemy import cast
        from sqlalchemy import and_, or_, not_
        from sqlalchemy import update, delete
        from sqlalchemy import text
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")
        logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Starting Basic JSON Loader to MariaDB using SQLAlchemy & MariaDB-Connector...")
        # Define the MariaDB engine using MariaDB Connector/Python
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost...")
        #engine = sqlalchemy.create_engine("mysql+pymysql://brandon:__VqE3QVAZmDEx__jkabjKKvR7uGcN__@127.0.0.1:3306/FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead?charset=utf8mb4")
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{dragon_breath_f10_sqlalchemy_username}:{dragon_breath_f10_sqlalchemy_password}@{dragon_breath_f10_sqlalchemy_hostname}:{dragon_breath_f10_sqlalchemy_port_number}/{dragon_breath_f10_sqlalchemy_database_name}?charset={dragon_breath_f10_sqlalchemy_charset}")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost Successful!")
        logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost Successful!")
        # Start an instance of MariaDB-Connector
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initializing...")
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=engine)
        Session = Session()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initialized Successfully!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping Remote MariaDB Table Schematics (21 Columns)...")
        Base = declarative_base()

        class JudicialDecision21Columns(Base):

            __tablename__ = 'Current_JSON_CL_Dataset_Exodus_Table01_File'
            id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
            courtlistener_resource_uri = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_id = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_absolute_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_cluster = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_created = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_modified = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_per_curiam = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_type = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_sha1 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_page_count = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_download_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_local_path = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_plain_text = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_lawbox = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_columbia = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_anon_2020 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_xml_harvard = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_with_citations = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_extracted_by_ocr = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_opinions_cited = sqlalchemy.Column(sqlalchemy.Text)
        # exodus_courtlistener_opinion_entry_timestamp = sqlalchemy.Column(sqlalchemy.DateTime)
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Defined Remote MariaDB & Table Schematics! (21 Columns)")
        print(f"Current JSON File - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant [A] Map & Payload Verified!")

        # Show Only Keys (No Value Names)
        # Assign JSON Key Name to a Python Variable (18) + 3 NULLED  w/ "(NULL)"
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table 01 SCHEMA: [A]...")
        pvar_key_resource_uri = ("resource_uri")
        pvar_key_id = ("id")
        pvar_key_absolute_url = ("absolute_url")
        pvar_key_cluster = ("cluster")
        pvar_key_date_created = ("date_created")
        pvar_key_date_modified = ("date_modified")
        pvar_key_per_curiam = ("per_curiam")
        pvar_key_type = ("type")
        pvar_key_sha1 = ("sha1")
        pvar_key_page_count = ("page_count")
        pvar_key_download_url = ("download_url")
        pvar_key_local_path = ("local_path")
        pvar_key_plain_text = ("plain_text")
        pvar_key_html = ("html")
        pvar_key_html_lawbox = ("html_lawbox")
        pvar_key_html_with_citations = ("html_with_citations")
        pvar_key_extracted_by_ocr = ("extracted_by_ocr")
        pvar_key_opinions_cited = ("opinions_cited")
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table 01 SCHEMA: [B] Successful!")

        # Show Only Values (No Key Names)
        # Assign JSON Key Value to a Python Variable (18) + 3 NULLED w/ "(NULL)"
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table 01 SCHEMA: [B]...")
        pvar_value_resource_uri = str(CurrentDecision['resource_uri'])
        pvar_value_id = str(CurrentDecision['id'])
        pvar_value_absolute_url = str(CurrentDecision['absolute_url'])
        pvar_value_cluster = str(CurrentDecision['cluster'])
        pvar_value_date_created = str(CurrentDecision['date_created'])
        pvar_value_date_modified = str(CurrentDecision['date_modified'])
        pvar_value_per_curiam = str(CurrentDecision['per_curiam'])
        pvar_value_type = str(CurrentDecision['type'])
        pvar_value_sha1 = str(CurrentDecision['sha1'])
        pvar_value_page_count = str(CurrentDecision['page_count'])
        pvar_value_download_url = str(CurrentDecision['download_url'])
        pvar_value_local_path = str(CurrentDecision['local_path'])
        pvar_value_plain_text = str(CurrentDecision['plain_text'])
        pvar_value_html = str(CurrentDecision['html'])
        pvar_value_html_with_citations = str(CurrentDecision['html_with_citations'])
        pvar_value_html_lawbox = str(CurrentDecision['html_lawbox'])
        pvar_value_html_columbia = "(NULL)"
        pvar_value_html_anon_2020 = "(NULL)"
        pvar_value_xml_harvard = "(NULL)"
        pvar_value_extracted_by_ocr = str(CurrentDecision['extracted_by_ocr'])
        pvar_value_opinions_cited = str(CurrentDecision['opinions_cited'])
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table 01  SCHEMA: [B] Successful!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting The JSON File(s) -> MariaDB 10.5.15 Payload [B]...")
        KeyPair_18_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html=pvar_value_html, courtlistener_html_lawbox=pvar_value_html_lawbox, courtlistener_html_columbia=pvar_value_html_columbia, courtlistener_html_anon_2020=pvar_value_html_anon_2020, courtlistener_xml_harvard=pvar_value_xml_harvard, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        #KeyPair_18_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        Session.add(KeyPair_18_Hit_Combo)
        Session.commit()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Inserted All 18 Key/Value Pairs + 3 Nulled Values to MariaDB SQLAlchemy Mapped Columns into MariaDB 10.5.15 SCHEMA: [B]")

def Table01_C(CurrentDecision):
        global courtlistener_jurisdiction_dataset
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
        global pvar_value_absolute_url
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant: [C] - Importing all Required Python3 Module Libraries...")
        import json
        import sqlalchemy
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.dialects.mysql import LONGTEXT
        import datetime
        from sqlalchemy import Column, Integer, DateTime
        from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
        from sqlalchemy import Index
        from sqlalchemy import ForeignKeyConstraint
        from sqlalchemy import insert
        from sqlalchemy.sql import select
        from sqlalchemy.sql import func
        from sqlalchemy import cast
        from sqlalchemy import and_, or_, not_
        from sqlalchemy import update, delete
        from sqlalchemy import text
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Starting Basic JSON Loader to MariaDB using SQLAlchemy & MariaDB-Connector...")
        # Define the MariaDB engine using MariaDB Connector/Python
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost...")
        #engine = sqlalchemy.create_engine("mysql+pymysql://brandon:__VqE3QVAZmDEx__jkabjKKvR7uGcN__@127.0.0.1:3306/FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead?charset=utf8mb4")
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{dragon_breath_f10_sqlalchemy_username}:{dragon_breath_f10_sqlalchemy_password}@{dragon_breath_f10_sqlalchemy_hostname}:{dragon_breath_f10_sqlalchemy_port_number}/{dragon_breath_f10_sqlalchemy_database_name}?charset={dragon_breath_f10_sqlalchemy_charset}")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost Successful!")

        # Start an instance of MariaDB-Connector
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initializing...")
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=engine)
        Session = Session()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initialized Successfully!")

        print(f"Dragon Breath [F.10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Table 01/10] - Mapping Remote MariaDB Table Schematics (21 Columns)...")
        Base = declarative_base()

        class JudicialDecision21Columns(Base):

            __tablename__ = 'Current_JSON_CL_Dataset_Exodus_Table01_File'
            id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
            courtlistener_resource_uri = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_id = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_absolute_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_cluster = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_created = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_modified = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_per_curiam = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_type = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_sha1 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_page_count = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_download_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_local_path = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_plain_text = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_lawbox = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_columbia = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_anon_2020 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_xml_harvard = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_with_citations = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_extracted_by_ocr = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_opinions_cited = sqlalchemy.Column(sqlalchemy.Text)
        # exodus_courtlistener_opinion_entry_timestamp = sqlalchemy.Column(sqlalchemy.DateTime)
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Defined Remote MariaDB & Table Schematics! (21 Columns)")
        print(f"Current JSON File - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant [C] Map & Payload Verified!")

        # Show Only Keys (No Value Names)
        # Assign JSON Key Name to a Python Variable (19) + 2 NULLED w/ "(NULL)"
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [C]...")
        pvar_key_resource_uri = ("resource_uri")
        pvar_key_id = ("id")
        pvar_key_absolute_url = ("absolute_url")
        pvar_key_cluster = ("cluster")
        pvar_key_date_created = ("date_created")
        pvar_key_date_modified = ("date_modified")
        pvar_key_per_curiam = ("per_curiam")
        pvar_key_type = ("type")
        pvar_key_sha1 = ("sha1")
        pvar_key_page_count = ("page_count")
        pvar_key_download_url = ("download_url")
        pvar_key_local_path = ("local_path")
        pvar_key_plain_text = ("plain_text")
        pvar_key_html = ("html")
        pvar_key_html_lawbox = ("html_lawbox")
        pvar_key_html_columbia = ("html_columbia")
        pvar_key_html_with_citations = ("html_with_citations")
        pvar_key_extracted_by_ocr = ("extracted_by_ocr")
        pvar_key_opinions_cited = ("opinions_cited")
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [C] Successful!")

        # Show Only Values (No Key Names)
        # Assign JSON Key Value to a Python Variable (19) + 2 NULLED w/ "(NULL)"
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [C]...")
        pvar_value_resource_uri = str(CurrentDecision['resource_uri'])
        pvar_value_id = str(CurrentDecision['id'])
        pvar_value_absolute_url = str(CurrentDecision['absolute_url'])
        pvar_value_cluster = str(CurrentDecision['cluster'])
        pvar_value_date_created = str(CurrentDecision['date_created'])
        pvar_value_date_modified = str(CurrentDecision['date_modified'])
        pvar_value_per_curiam = str(CurrentDecision['per_curiam'])
        pvar_value_type = str(CurrentDecision['type'])
        pvar_value_sha1 = str(CurrentDecision['sha1'])
        pvar_value_page_count = str(CurrentDecision['page_count'])
        pvar_value_download_url = str(CurrentDecision['download_url'])
        pvar_value_local_path = str(CurrentDecision['local_path'])
        pvar_value_plain_text = str(CurrentDecision['plain_text'])
        pvar_value_html = str(CurrentDecision['html'])
        pvar_value_html_lawbox = str(CurrentDecision['html_lawbox'])
        pvar_value_html_columbia = str(CurrentDecision['html_columbia'])
        pvar_value_html_anon_2020 = "(NULL)"
        pvar_value_xml_harvard = "(NULL)"
        pvar_value_html_with_citations = str(CurrentDecision['html_with_citations'])
        pvar_value_extracted_by_ocr = str(CurrentDecision['extracted_by_ocr'])
        pvar_value_opinions_cited = str(CurrentDecision['opinions_cited'])
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table  SCHEMA: [C] Successful!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting The JSON File(s) -> MariaDB 10.5.15 Payload 1...")
        KeyPair_19_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html=pvar_value_html, courtlistener_html_lawbox=pvar_value_html_lawbox, courtlistener_html_columbia=pvar_value_html_columbia, courtlistener_html_anon_2020=pvar_value_html_anon_2020, courtlistener_xml_harvard=pvar_value_xml_harvard, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        #KeyPair_19_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        Session.add(KeyPair_19_Hit_Combo)
        Session.commit()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Inserted All 19 Key/Value Pairs + 2 NULLED to MariaDB SQLAlchemy Mapped Columns into MariaDB 10.5.15")

def Table01_D(CurrentDecision):
        global courtlistener_jurisdiction_dataset
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
        global pvar_value_absolute_url
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant: [D] - Importing all Required Python3 Module Libraries...")
        import json
        import sqlalchemy
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.dialects.mysql import LONGTEXT
        import datetime
        from sqlalchemy import Column, Integer, DateTime
        from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
        from sqlalchemy import Index
        from sqlalchemy import ForeignKeyConstraint
        from sqlalchemy import insert
        from sqlalchemy.sql import select
        from sqlalchemy.sql import func
        from sqlalchemy import cast
        from sqlalchemy import and_, or_, not_
        from sqlalchemy import update, delete
        from sqlalchemy import text
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Starting Basic JSON Loader to MariaDB using SQLAlchemy & MariaDB-Connector...")
        # Define the MariaDB engine using MariaDB Connector/Python
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost...")
        #engine = sqlalchemy.create_engine("mysql+pymysql://brandon:__VqE3QVAZmDEx__jkabjKKvR7uGcN__@127.0.0.1:3306/FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead?charset=utf8mb4")
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{dragon_breath_f10_sqlalchemy_username}:{dragon_breath_f10_sqlalchemy_password}@{dragon_breath_f10_sqlalchemy_hostname}:{dragon_breath_f10_sqlalchemy_port_number}/{dragon_breath_f10_sqlalchemy_database_name}?charset={dragon_breath_f10_sqlalchemy_charset}")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost Successful!")

        # Start an instance of MariaDB-Connector
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initializing...")
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=engine)
        Session = Session()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initialized Successfully!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping Remote MariaDB Table Schematics (21 Columns)...")
        Base = declarative_base()

        class JudicialDecision21Columns(Base):

            __tablename__ = 'Current_JSON_CL_Dataset_Exodus_Table01_File'
            id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
            courtlistener_resource_uri = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_id = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_absolute_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_cluster = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_created = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_modified = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_per_curiam = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_type = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_sha1 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_page_count = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_download_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_local_path = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_plain_text = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_lawbox = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_columbia = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_anon_2020 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_xml_harvard = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_with_citations = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_extracted_by_ocr = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_opinions_cited = sqlalchemy.Column(sqlalchemy.Text)
        # exodus_courtlistener_opinion_entry_timestamp = sqlalchemy.Column(sqlalchemy.DateTime)
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Defined Remote MariaDB & Table Schematics! (21 Columns)")
        print(f"Current JSON File - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant [D] Map & Payload Verified!")
        # Show Only Keys (No Value Names)
        # Assign JSON Key Name to a Python Variable (19) + 2 NULLED w/ "(NULL)"
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [D]...")
        pvar_key_resource_uri = ("resource_uri")
        pvar_key_id = ("id")
        pvar_key_absolute_url = ("absolute_url")
        pvar_key_cluster = ("cluster")
        pvar_key_date_created = ("date_created")
        pvar_key_date_modified = ("date_modified")
        pvar_key_per_curiam = ("per_curiam")
        pvar_key_type = ("type")
        pvar_key_sha1 = ("sha1")
        pvar_key_page_count = ("page_count")
        pvar_key_download_url = ("download_url")
        pvar_key_local_path = ("local_path")
        pvar_key_plain_text = ("plain_text")
        pvar_key_html = ("html")
        pvar_key_html_anon_2020 = ("html_anon_2020")
        pvar_key_xml_harvard = ("xml_harvard")
        pvar_key_html_with_citations = ("html_with_citations")
        pvar_key_extracted_by_ocr = ("extracted_by_ocr")
        pvar_key_opinions_cited = ("opinions_cited")
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [D] Successful!")

        # Show Only Values (No Key Names)
        # Assign JSON Key Value to a Python Variable (19) + 2 NULLED w/ "(NULL)"
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [D]...")
        pvar_value_resource_uri = str(CurrentDecision['resource_uri'])
        pvar_value_id = str(CurrentDecision['id'])
        pvar_value_absolute_url = str(CurrentDecision['absolute_url'])
        pvar_value_cluster = str(CurrentDecision['cluster'])
        pvar_value_date_created = str(CurrentDecision['date_created'])
        pvar_value_date_modified = str(CurrentDecision['date_modified'])
        pvar_value_per_curiam = str(CurrentDecision['per_curiam'])
        pvar_value_type = str(CurrentDecision['type'])
        pvar_value_sha1 = str(CurrentDecision['sha1'])
        pvar_value_page_count = str(CurrentDecision['page_count'])
        pvar_value_download_url = str(CurrentDecision['download_url'])
        pvar_value_local_path = str(CurrentDecision['local_path'])
        pvar_value_plain_text = str(CurrentDecision['plain_text'])
        pvar_value_html = str(CurrentDecision['html'])
        pvar_value_html_lawbox = "(NULL)"
        pvar_value_html_columbia = "(NULL)"
        pvar_value_html_anon_2020 = str(CurrentDecision['html_anon_2020'])
        pvar_value_xml_harvard = str(CurrentDecision['xml_harvard'])
        pvar_value_html_with_citations = str(CurrentDecision['html_with_citations'])
        pvar_value_extracted_by_ocr = str(CurrentDecision['extracted_by_ocr'])
        pvar_value_opinions_cited = str(CurrentDecision['opinions_cited'])
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table  SCHEMA: [D] Successful!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting The JSON File(s) -> MariaDB 10.5.15 Payload 1...")
        KeyPair_19_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html=pvar_value_html, courtlistener_html_lawbox=pvar_value_html_lawbox, courtlistener_html_columbia=pvar_value_html_columbia, courtlistener_html_anon_2020=pvar_value_html_anon_2020, courtlistener_xml_harvard=pvar_value_xml_harvard, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        #KeyPair_19_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        Session.add(KeyPair_19_Hit_Combo)
        Session.commit()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Inserted All 19 Key/Value Pairs + 2 NULLED to MariaDB SQLAlchemy Mapped Columns into MariaDB 10.5.15")

def Table01_E(CurrentDecision):
        global courtlistener_jurisdiction_dataset
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
        global pvar_value_absolute_url
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant: [E] - Importing all Required Python3 Module Libraries...")
        import json
        import sqlalchemy
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.dialects.mysql import LONGTEXT
        import datetime
        from sqlalchemy import Column, Integer, DateTime
        from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
        from sqlalchemy import Index
        from sqlalchemy import ForeignKeyConstraint
        from sqlalchemy import insert
        from sqlalchemy.sql import select
        from sqlalchemy.sql import func
        from sqlalchemy import cast
        from sqlalchemy import and_, or_, not_
        from sqlalchemy import update, delete
        from sqlalchemy import text
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Starting Basic JSON Loader to MariaDB using SQLAlchemy & MariaDB-Connector...")
        # Define the MariaDB engine using MariaDB Connector/Python
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost...")
        #engine = sqlalchemy.create_engine("mysql+pymysql://brandon:__VqE3QVAZmDEx__jkabjKKvR7uGcN__@127.0.0.1:3306/FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead?charset=utf8mb4")
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{dragon_breath_f10_sqlalchemy_username}:{dragon_breath_f10_sqlalchemy_password}@{dragon_breath_f10_sqlalchemy_hostname}:{dragon_breath_f10_sqlalchemy_port_number}/{dragon_breath_f10_sqlalchemy_database_name}?charset={dragon_breath_f10_sqlalchemy_charset}")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost Successful!")

        # Start an instance of MariaDB-Connector
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initializing...")
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=engine)
        Session = Session()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initialized Successfully!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping Remote MariaDB Table Schematics (21 Columns)...")
        Base = declarative_base()

        class JudicialDecision21Columns(Base):

            __tablename__ = 'Current_JSON_CL_Dataset_Exodus_Table01_File'
            id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
            courtlistener_resource_uri = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_id = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_absolute_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_cluster = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_created = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_modified = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_per_curiam = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_type = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_sha1 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_page_count = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_download_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_local_path = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_plain_text = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_lawbox = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_columbia = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_anon_2020 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_xml_harvard = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_with_citations = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_extracted_by_ocr = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_opinions_cited = sqlalchemy.Column(sqlalchemy.Text)
        # exodus_courtlistener_opinion_entry_timestamp = sqlalchemy.Column(sqlalchemy.DateTime)
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Defined Remote MariaDB & Table Schematics! (21 Columns)")
        print(f"Current JSON File - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant [E] Map & Payload Verified!")

        # Show Only Keys (No Value Names)
        # Assign JSON Key Name to a Python Variable (20) + 1 NULLED w/ "(NULL)"
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [E]...")
        pvar_key_resource_uri = ("resource_uri")
        pvar_key_id = ("id")
        pvar_key_absolute_url = ("absolute_url")
        pvar_key_cluster = ("cluster")
        pvar_key_date_created = ("date_created")
        pvar_key_date_modified = ("date_modified")
        pvar_key_per_curiam = ("per_curiam")
        pvar_key_type = ("type")
        pvar_key_sha1 = ("sha1")
        pvar_key_page_count = ("page_count")
        pvar_key_download_url = ("download_url")
        pvar_key_local_path = ("local_path")
        pvar_key_plain_text = ("plain_text")
        pvar_key_html = ("html")
        pvar_key_html_lawbox = ("html_lawbox")
        pvar_key_html_columbia = ("html_columbia")
        pvar_key_xml_harvard = ("xml_harvard")
        pvar_key_html_with_citations = ("html_with_citations")
        pvar_key_extracted_by_ocr = ("extracted_by_ocr")
        pvar_key_opinions_cited = ("opinions_cited")
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [E] Successful!")

        # Show Only Values (No Key Names)
        # Assign JSON Key Value to a Python Variable (20) + 1 NULLED w/ "(NULL)"
        print("Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset] - Now Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [E]...")
        pvar_value_resource_uri = str(CurrentDecision['resource_uri'])
        pvar_value_id = str(CurrentDecision['id'])
        pvar_value_absolute_url = str(CurrentDecision['absolute_url'])
        pvar_value_cluster = str(CurrentDecision['cluster'])
        pvar_value_date_created = str(CurrentDecision['date_created'])
        pvar_value_date_modified = str(CurrentDecision['date_modified'])
        pvar_value_per_curiam = str(CurrentDecision['per_curiam'])
        pvar_value_type = str(CurrentDecision['type'])
        pvar_value_sha1 = str(CurrentDecision['sha1'])
        pvar_value_page_count = str(CurrentDecision['page_count'])
        pvar_value_download_url = str(CurrentDecision['download_url'])
        pvar_value_local_path = str(CurrentDecision['local_path'])
        pvar_value_plain_text = str(CurrentDecision['plain_text'])
        pvar_value_html = str(CurrentDecision['html'])
        pvar_value_html_lawbox = str(CurrentDecision['html_lawbox'])
        pvar_value_html_columbia = str(CurrentDecision['html_columbia'])
        pvar_value_html_anon_2020 = "(NULL)"
        pvar_value_xml_harvard = str(CurrentDecision['xml_harvard'])
        pvar_value_html_with_citations = str(CurrentDecision['html_with_citations'])
        pvar_value_extracted_by_ocr = str(CurrentDecision['extracted_by_ocr'])
        pvar_value_opinions_cited = str(CurrentDecision['opinions_cited'])
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [E] Successful!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting The JSON File(s) -> MariaDB 10.5.15 Payload 1...")
        KeyPair_20_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html=pvar_value_html, courtlistener_html_lawbox=pvar_value_html_lawbox, courtlistener_html_columbia=pvar_value_html_columbia, courtlistener_html_anon_2020=pvar_value_html_anon_2020, courtlistener_xml_harvard=pvar_value_xml_harvard, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        #KeyPair_20_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        Session.add(KeyPair_20_Hit_Combo)
        Session.commit()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Inserted All 20 Key/Value Pairs + 1 NULLED to MariaDB SQLAlchemy Mapped Columns into MariaDB 10.5.15")

def Table01_F(CurrentDecision):
        global courtlistener_jurisdiction_dataset
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
        global pvar_value_absolute_url
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant: [F] - Importing all Required Python3 Module Libraries...")
        import json
        import sqlalchemy
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.dialects.mysql import LONGTEXT
        import datetime
        from sqlalchemy import Column, Integer, DateTime
        from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
        from sqlalchemy import Index
        from sqlalchemy import ForeignKeyConstraint
        from sqlalchemy import insert
        from sqlalchemy.sql import select
        from sqlalchemy.sql import func
        from sqlalchemy import cast
        from sqlalchemy import and_, or_, not_
        from sqlalchemy import update, delete
        from sqlalchemy import text
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Starting Basic JSON Loader to MariaDB using SQLAlchemy & MariaDB-Connector...")
        # Define the MariaDB engine using MariaDB Connector/Python
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost...")
        #engine = sqlalchemy.create_engine("mysql+pymysql://brandon:__VqE3QVAZmDEx__jkabjKKvR7uGcN__@127.0.0.1:3306/FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead?charset=utf8mb4")
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{dragon_breath_f10_sqlalchemy_username}:{dragon_breath_f10_sqlalchemy_password}@{dragon_breath_f10_sqlalchemy_hostname}:{dragon_breath_f10_sqlalchemy_port_number}/{dragon_breath_f10_sqlalchemy_database_name}?charset={dragon_breath_f10_sqlalchemy_charset}")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost Successful!")

        # Start an instance of MariaDB-Connector
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initializing...")
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=engine)
        Session = Session()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initialized Successfully!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping Remote MariaDB Table Schematics (21 Columns)...")
        Base = declarative_base()

        class JudicialDecision21Columns(Base):

            __tablename__ = 'Current_JSON_CL_Dataset_Exodus_Table01_File'
            id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
            courtlistener_resource_uri = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_id = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_absolute_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_cluster = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_created = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_modified = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_per_curiam = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_type = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_sha1 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_page_count = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_download_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_local_path = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_plain_text = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_lawbox = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_columbia = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_anon_2020 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_xml_harvard = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_with_citations = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_extracted_by_ocr = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_opinions_cited = sqlalchemy.Column(sqlalchemy.Text)
        # exodus_courtlistener_opinion_entry_timestamp = sqlalchemy.Column(sqlalchemy.DateTime)
        print("Dragon Breath [F.10] - [Table 01/10] - Successfully Defined Remote MariaDB & Table Schematics! (21 Columns)")
        print("Current JSON File - Variant [E] Map & Payload Verified!")

        # Show Only Keys (No Value Names)
        # Assign JSON Key Name to a Python Variable (20) + 1 NULLED w/ "(NULL)"
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [F]...")
        pvar_key_resource_uri = ("resource_uri")
        pvar_key_id = ("id")
        pvar_key_absolute_url = ("absolute_url")
        pvar_key_cluster = ("cluster")
        pvar_key_date_created = ("date_created")
        pvar_key_date_modified = ("date_modified")
        pvar_key_per_curiam = ("per_curiam")
        pvar_key_type = ("type")
        pvar_key_sha1 = ("sha1")
        pvar_key_page_count = ("page_count")
        pvar_key_download_url = ("download_url")
        pvar_key_local_path = ("local_path")
        pvar_key_plain_text = ("plain_text")
        pvar_key_html = ("html")
        pvar_key_html_lawbox = ("html_lawbox")
        pvar_key_html_columbia = ("html_columbia")
        pvar_key_html_anon_2020 = ("html_anon_2020")
        pvar_key_html_with_citations = ("html_with_citations")
        pvar_key_extracted_by_ocr = ("extracted_by_ocr")
        pvar_key_opinions_cited = ("opinions_cited")
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [F] Successful!")

        # Show Only Values (No Key Names)
        # Assign JSON Key Value to a Python Variable (20) + 1 NULLED w/ "(NULL)"
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [F]...")
        pvar_value_resource_uri = str(CurrentDecision['resource_uri'])
        pvar_value_id = str(CurrentDecision['id'])
        pvar_value_absolute_url = str(CurrentDecision['absolute_url'])
        pvar_value_cluster = str(CurrentDecision['cluster'])
        pvar_value_date_created = str(CurrentDecision['date_created'])
        pvar_value_date_modified = str(CurrentDecision['date_modified'])
        pvar_value_per_curiam = str(CurrentDecision['per_curiam'])
        pvar_value_type = str(CurrentDecision['type'])
        pvar_value_sha1 = str(CurrentDecision['sha1'])
        pvar_value_page_count = str(CurrentDecision['page_count'])
        pvar_value_download_url = str(CurrentDecision['download_url'])
        pvar_value_local_path = str(CurrentDecision['local_path'])
        pvar_value_plain_text = str(CurrentDecision['plain_text'])
        pvar_value_html = str(CurrentDecision['html'])
        pvar_value_html_lawbox = str(CurrentDecision['html_lawbox'])
        pvar_value_html_columbia = str(CurrentDecision['html_columbia'])
        pvar_value_html_anon_2020 = str(CurrentDecision['html_anon_2020'])
        pvar_value_xml_harvard = "(NULL)"
        pvar_value_html_with_citations = str(CurrentDecision['html_with_citations'])
        pvar_value_extracted_by_ocr = str(CurrentDecision['extracted_by_ocr'])
        pvar_value_opinions_cited = str(CurrentDecision['opinions_cited'])
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [F] Successful!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting The JSON File(s) -> MariaDB 10.5.15 Payload 1...")
        KeyPair_20_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html=pvar_value_html, courtlistener_html_lawbox=pvar_value_html_lawbox, courtlistener_html_columbia=pvar_value_html_columbia, courtlistener_html_anon_2020=pvar_value_html_anon_2020, courtlistener_xml_harvard=pvar_value_xml_harvard, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        #KeyPair_20_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        Session.add(KeyPair_20_Hit_Combo)
        Session.commit()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Inserted All 20 Key/Value Pairs + 1 NULLED to MariaDB SQLAlchemy Mapped Columns into MariaDB 10.5.15")

def Table01_G(CurrentDecision):
        global courtlistener_jurisdiction_dataset
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
        global pvar_value_absolute_url
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Variant: [G] - Importing all Required Python3 Module Libraries...")
        import json
        import sqlalchemy
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.dialects.mysql import LONGTEXT
        import datetime
        from sqlalchemy import Column, Integer, DateTime
        from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
        from sqlalchemy import Index
        from sqlalchemy import ForeignKeyConstraint
        from sqlalchemy import insert
        from sqlalchemy.sql import select
        from sqlalchemy.sql import func
        from sqlalchemy import cast
        from sqlalchemy import and_, or_, not_
        from sqlalchemy import update, delete
        from sqlalchemy import text
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Starting Basic JSON Loader to MariaDB using SQLAlchemy & MariaDB-Connector...")
        # Define the MariaDB engine using MariaDB Connector/Python
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost...")
        #engine = sqlalchemy.create_engine("mysql+pymysql://brandon:__VqE3QVAZmDEx__jkabjKKvR7uGcN__@127.0.0.1:3306/FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead?charset=utf8mb4")
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{dragon_breath_f10_sqlalchemy_username}:{dragon_breath_f10_sqlalchemy_password}@{dragon_breath_f10_sqlalchemy_hostname}:{dragon_breath_f10_sqlalchemy_port_number}/{dragon_breath_f10_sqlalchemy_database_name}?charset={dragon_breath_f10_sqlalchemy_charset}")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Setting up Connection to MariaDB: localhost Successful!")

        # Start an instance of MariaDB-Connector
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initializing...")
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=engine)
        Session = Session()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Connecting to MariaDB: localhost Session Initialized Successfully!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping Remote MariaDB Table Schematics (21 Columns)...")
        Base = declarative_base()

        class JudicialDecision21Columns(Base):

            __tablename__ = 'Current_JSON_CL_Dataset_Exodus_Table01_File'
            id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
            courtlistener_resource_uri = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_id = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_absolute_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_cluster = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_created = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_date_modified = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_per_curiam = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_type = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_sha1 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_page_count = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_download_url = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_local_path = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_plain_text = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_lawbox = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_columbia = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_anon_2020 = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_xml_harvard = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_html_with_citations = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_extracted_by_ocr = sqlalchemy.Column(sqlalchemy.Text)
            courtlistener_opinions_cited = sqlalchemy.Column(sqlalchemy.Text)
        # exodus_courtlistener_opinion_entry_timestamp = sqlalchemy.Column(sqlalchemy.DateTime)
        print("Dragon Breath [F.10] - [Table 01/10] - Successfully Defined Remote MariaDB & Table Schematics! (21 Columns)")
        print("Current JSON File - Variant [E] Map & Payload Verified!")

        # Show Only Keys (No Value Names)
        # Assign JSON Key Name to a Python Variable (21)
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [G]...")
        pvar_key_resource_uri = ("resource_uri")
        pvar_key_id = ("id")
        pvar_key_absolute_url = ("absolute_url")
        pvar_key_cluster = ("cluster")
        pvar_key_date_created = ("date_created")
        pvar_key_date_modified = ("date_modified")
        pvar_key_per_curiam = ("per_curiam")
        pvar_key_type = ("type")
        pvar_key_sha1 = ("sha1")
        pvar_key_page_count = ("page_count")
        pvar_key_download_url = ("download_url")
        pvar_key_local_path = ("local_path")
        pvar_key_plain_text = ("plain_text")
        pvar_key_html = ("html")
        pvar_key_html_lawbox = ("html_lawbox")
        pvar_key_html_columbia = ("html_columbia")
        pvar_key_html_anon_2020 = ("html_anon_2020")
        pvar_key_xml_harvard = ("xml_harvard")
        pvar_key_html_with_citations = ("html_with_citations")
        pvar_key_extracted_by_ocr = ("extracted_by_ocr")
        pvar_key_opinions_cited = ("opinions_cited")
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Key Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [G] Successful!")

        # Show Only Values (No Key Names)
        # Assign JSON Key Value to a Python Variable (21) 
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [G]...")
        pvar_value_resource_uri = str(CurrentDecision['resource_uri'])
        pvar_value_id = str(CurrentDecision['id'])
        pvar_value_absolute_url = str(CurrentDecision['absolute_url'])
        pvar_value_cluster = str(CurrentDecision['cluster'])
        pvar_value_date_created = str(CurrentDecision['date_created'])
        pvar_value_date_modified = str(CurrentDecision['date_modified'])
        pvar_value_per_curiam = str(CurrentDecision['per_curiam'])
        pvar_value_type = str(CurrentDecision['type'])
        pvar_value_sha1 = str(CurrentDecision['sha1'])
        pvar_value_page_count = str(CurrentDecision['page_count'])
        pvar_value_download_url = str(CurrentDecision['download_url'])
        pvar_value_local_path = str(CurrentDecision['local_path'])
        pvar_value_plain_text = str(CurrentDecision['plain_text'])
        pvar_value_html = str(CurrentDecision['html'])
        pvar_value_html_lawbox = str(CurrentDecision['html_lawbox'])
        pvar_value_html_columbia = str(CurrentDecision['html_columbia'])
        pvar_value_html_anon_2020 = str(CurrentDecision['html_anon_2020'])
        pvar_value_xml_harvard = str(CurrentDecision['xml_harvard'])
        pvar_value_html_with_citations = str(CurrentDecision['html_with_citations'])
        pvar_value_extracted_by_ocr = str(CurrentDecision['extracted_by_ocr'])
        pvar_value_opinions_cited = str(CurrentDecision['opinions_cited'])
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Mapping JSON Value Pairs to Maria DB 10.5.15 DB/Table SCHEMA: [G] Successful!")

        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting The JSON File(s) -> MariaDB 10.5.15 Payload 1...")
        KeyPair_21_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html=pvar_value_html, courtlistener_html_lawbox=pvar_value_html_lawbox, courtlistener_html_columbia=pvar_value_html_columbia, courtlistener_html_anon_2020=pvar_value_html_anon_2020, courtlistener_xml_harvard=pvar_value_xml_harvard, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        #KeyPair_21_Hit_Combo = JudicialDecision21Columns(courtlistener_resource_uri=pvar_value_resource_uri, courtlistener_id=pvar_value_id, courtlistener_absolute_url=pvar_value_absolute_url, courtlistener_cluster=pvar_value_cluster, courtlistener_date_created=pvar_value_date_created, courtlistener_date_modified=pvar_value_date_modified, courtlistener_per_curiam=pvar_value_per_curiam, courtlistener_type=pvar_value_type, courtlistener_sha1=pvar_value_sha1, courtlistener_page_count=pvar_value_page_count, courtlistener_download_url=pvar_value_download_url, courtlistener_local_path=pvar_value_local_path, courtlistener_plain_text=pvar_value_plain_text, courtlistener_html_with_citations=pvar_value_html_with_citations, courtlistener_extracted_by_ocr=pvar_value_extracted_by_ocr, courtlistener_opinions_cited=pvar_value_opinions_cited)
        Session.add(KeyPair_21_Hit_Combo)
        Session.commit()
        print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully Inserted All 21 Key/Value Pairs to MariaDB SQLAlchemy Mapped Columns into MariaDB 10.5.15")

def Table02(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    # Code [02/10]: [Read from Table: Current_JSON_CL_Dataset_Exodus_Table01_File]
    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
    global pvar_value_absolute_url
    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: sql_full_url_insert...")
    global sql_full_url_insert
    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_courtlistener_absolute_url_trimmed_1_leading...")
    global pvar_courtlistener_absolute_url_trimmed_1_leading
    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Table01_File] -> [Table02_RemoteURLGen] Executing...")

    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing all Requried Python3 Module Libraries...")
    import json
    import sqlalchemy
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.dialects.mysql import LONGTEXT
    import datetime
    from sqlalchemy import Column, Integer, DateTime
    from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
    from sqlalchemy import Index
    from sqlalchemy import ForeignKeyConstraint
    from sqlalchemy import insert
    from sqlalchemy.sql import select
    from sqlalchemy.sql import func
    from sqlalchemy import cast
    from sqlalchemy import and_, or_, not_
    from sqlalchemy import update, delete
    from sqlalchemy import text
    import pymysql
    import pymysql.cursors
    from bs4 import BeautifulSoup

    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")

    # Extract Data


    import mysql.connector
    try:
        connection = mysql.connector.connect(host=f'{dragon_breath_f10_mysql_connector_hostname}',
                                             database=f'{dragon_breath_f10_mysql_connector_database_name}',
                                             user=f'{dragon_breath_f10_mysql_connector_username}',
                                             password=f'{dragon_breath_f10_mysql_connector_password}')


#    import mysql.connector
#    try:
#        connection = mysql.connector.connect(host='localhost',
#                                             database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                             user='brandon',
#                                             password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__')

        print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Database Connection Successful! Now Quering Courtlistener Absolute URL for current JSON")
#        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table01_File"
#        SELECT * FROM Table ORDER BY ID DESC LIMIT 1
        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table01_File order by id desc limit 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("courtlistener_absolute_url = ", row[3], )
            with open("extracted_absolute_urls.txt", "w", encoding="utf-8") as f:
                print(row[3], file=f)

    except mysql.connector.Error as e:
        print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - MySQL connection is closed")

    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Creating new courtlistener.com URL...")

    # Source: irc.libera.chat #python - jinsun__
    # Date: 03/12/2022 @ Approx. 21:03
    # Dpaste: https://dpaste.com/D83JVVE2K

    from urllib.parse import urljoin
    with open("extracted_absolute_urls.txt", "r", encoding="utf-8") as f:
        urlpart2 = f.read()
    url_part_1 = "https://www.courtlistener.com"

    url_join = (urljoin(url_part_1,
                  urlpart2))
    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - New courtlistener.com URL is:")
    print(url_join)

    pvar_courtlistener_absolute_url_trimmed_1_leading = pvar_value_absolute_url[1:]
    print(pvar_courtlistener_absolute_url_trimmed_1_leading)

    # Copy Columns & INSERT url_join to new Table + Column
    # Copy Columns from Table: Current_JSON_CL_Dataset_Exodus_Table1_File

    # New Table: Current_JSON_CL_Dataset_Exodus_Table2_RemoteURLGen
    # New Column: courtlistener_full_absolute_url
    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL into Table02_RemoteURLGen...")
    sql_full_url_insert = url_join


    import pymysql.cursors
    # Connect to the database
    connection = pymysql.connect(host=f'{dragon_breath_f10_pymysql_hostname}',
                                 user=f'{dragon_breath_f10_pymysql_username}',
                                 password=f'{dragon_breath_f10_pymysql_password}',
                                 database=f'{dragon_breath_f10_pymysql_database_name}',
                                 cursorclass=pymysql.cursors.DictCursor)

#    import pymysql.cursors
#    # Connect to the database
#    connection = pymysql.connect(host='localhost',
#                                 user='brandon',
#                                 password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__',
#                                 database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
                sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table02_RemoteURLGen` (`courtlistener_full_absolute_url`, `courtlistener_absolute_url`, `courtlistener_absolute_url_leading_trim`)  VALUES (%s, %s, %s)"
                cursor.execute(sql, (sql_full_url_insert, pvar_value_absolute_url, pvar_courtlistener_absolute_url_trimmed_1_leading))
        connection.commit()
    finally:
        connection.close()
    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

    # JSON Filename & Full Filename -> Python Vars -> MariaDB
    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished!")
 
def Table03(CurrentDecision, current_json_filename):
    # Source: irc.libera.chat #python - ChrisWarrick
    # Date: 08/15/2022 @ Approx. 03:20
    # Taught me how to use double arguments, remove & avoid global variables, improve code (not messy/lengthy or unecessary when I know how to correctly program!)
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 03/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: file_broken_up_1...")
    global file_broken_up_1
    print(f"Dragon Breath [F.10] - [Table 03/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: dir_path...")
    global dir_path
    print(f"Dragon Breath [F.10] - [Table 03/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: current_json_dataset_final...")
    global current_json_dataset_final
    print(f"Dragon Breath [F.10] - [Table 03/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Reading filename Contents of Specified Jurisidiction Dataset Current JSON File...")
    import pathlib
    from pathlib import Path
    print(f"Dragon Breath [F.10] - [Table 03/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning filename variable to Specified Jurisidiction Dataset (Largest File)...")    
    filename = Path(f'{dir_path}{current_json_filename}')
    #filename = Path(f'{current_json_filename}')
    print(f"Dragon Breath [F.10] - [Table 03/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Reading filename contents of Specified Jurisidiction Dataset (Largest File) Successful!")
    file_broken_up_1 = filename.stem
    file_broken_up_2 = filename.suffix
     # Source: irc.libera.chat #python - EdFletcher
    # Date: 03/13/2022 @ Approx. 01:00
    # paste: https://ideone.com/2KJM0e
    print(file_broken_up_1)
    print(file_broken_up_2)
    print(f"Dragon Breath [F.10] - [Table 03/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - filename variable for Specified Jurisidiction Dataset (Current Decision) set to:")
    print(filename)
    print(f"Dragon Breath [F.10] - [Table 03/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - file schema variant variable for Specified Jurisidiction Dataset (Current Decision) set to:")
    print(current_json_dataset_final)

    # Now INSERTING Python Vars - Current Filename Details -> MariaDB
    # Table: Current_JSON_CL_Dataset_Exodus_Table3_File2
    # Column #1: pvar = file_broken_up_1 -> "courtlistener_current_json_file_number"
    # Column #2: pvar = file_broken_up_2 -> "courtlistener_current_json_file_extension"
    # Column #3: pvar = filename -> "courtlistener_current_json_filename"

    # PyMySQL Connection

    print(f"Dragon Breath [F.10] - [Table 03/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - filename variables (3);stem, suffix and joined Payload Injecting to MariaDB Table3_File2...")

    import pymysql
    import pymysql.cursors
    connection = pymysql.connect(host=f'{dragon_breath_f10_pymysql_hostname}',
      user=f"{dragon_breath_f10_pymysql_username}",
      passwd=f"{dragon_breath_f10_pymysql_password}",
      db=f"{dragon_breath_f10_pymysql_database_name}"
    )

#    import pymysql
#    import pymysql.cursors
#    connection = pymysql.connect(host='localhost',
#      user="brandon",
#      passwd="password",
#      db="FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead"

#    )
    print(f"Dragon Breath [F.10] - [Table 03/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - PyMySQL Connected Successfully!")

    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table03_File2` (`courtlistener_current_json_file_number`, `courtlistener_current_json_file_extension`, `courtlistener_current_json_filename`, `courtlistener_current_json_variant`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (file_broken_up_1, file_broken_up_2, filename, current_json_dataset_final))
            connection.commit()

    print(f"Dragon Breath [F.10] - [Table 03/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - filename variables (3);stem, suffix and joined Payload Injection to MariaDB Table03_File2 Successful!")

def Table04(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Reverse URL Column Recovery] - Started...")
    print(f"Dragon Breath [F.10] - [Table 04/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: sql_full_url_insert...")
    global sql_full_url_insert
    print(f"Dragon Breath [F.10] - [Table 04/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_courtlistener_absolute_url_trimmed_1_leading...")
    global pvar_courtlistener_absolute_url_trimmed_1_leading
    print(f"Dragon Breath [F.10] - [Table 04/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: dir_path...")
    global dir_path
    print(f"Dragon Breath [F.10] - [Table 04/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: html...")
    global html
    print(f"Dragon Breath [F.10] - [Table 04/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: Table04_Opinion_newpath_mkdir...")
    global Table04_Opinion_newpath_mkdir
    print(f"Dragon Breath [F.10] - [Table 04/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: Table04_Opinion_current_html...")
    global Table04_Opinion_current_html
    import urllib.request
    from urllib.request import Request, urlopen
    import pathlib
    from pathlib import Path
    import datetime
    import os
    import sys
    
    # Part 1/3: (Without Error Handling):
    # User-Agent: Mozilla/5.0 
    print("Request URL is Python Variable 'sql_full_url_insert':")
    print(sql_full_url_insert)
    req = Request(sql_full_url_insert, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req,timeout=30).read()
    print("Current American Constitutional Opinion in THIS Dataset:")
    print(sql_full_url_insert)
    PATH = pathlib.Path(__file__).parent
    print("Now Printing Python Variable Value for PATH:")
    print(PATH)
    fpath = pvar_courtlistener_absolute_url_trimmed_1_leading
    fname = PATH /  f'{dir_path}' / f'{fpath}' / 'index.html'
    print("fname is:")
    print(fname)
    print("dir_path is:")
    print(dir_path)
    print("mkdir test Path assigned to Python Variable: 'newpath_mkdir':")
    newpath_mkdir = pathlib.Path(f'{dir_path}{fpath}')
    print("Python Variable Contents of 'newpath_mkdir is now:")
    print(newpath_mkdir)
    try:
        if not newpath_mkdir.exists():
            pathlib.Path(f'{newpath_mkdir}').mkdir(parents=True)
    except DebianLinuxError:
        print(f"Debian Linux Error - [Errorno 17]: Already Exists, Creating Directory: {newpath_mkdir} for {current_json_filename} on Dataset: {courtlistener_jurisdiction_dataset}")
        logging.debug(f"Debian Linux - [Errorno 17]: Already Exists, Creating Directory: {newpath_mkdir} for {current_json_filename} on Dataset: {courtlistener_jurisdiction_dataset}")
        pathlib.Path(f'{newpath_mkdir}').mkdir(exist_ok=True, parents=True)
    #pathlib.Path(f'{newpath_mkdir}').mkdir(parents=True)
    print("Successfully Created Directory:")
    print(fpath)
    print("Successfully Created Directory - Full Path:")
    print(newpath_mkdir)
    print("Now writing index.html in newly created Directory (Includes Casename Folder)...")
    with open(fname, 'w') as f:
       f.write(str(html))


    print(f"Dragon Breath [F.10] - [Table 04/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning New Python Variable 'Table04_Opinion_current_html' to match Variable 'html'...")
    Table04_Opinion_current_html = html
    
    # MariaDB Table04, Column: courtlistener_opinion_current_html
    print(f"Dragon Breath [F.10] - [Table 04/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning New Python Variable 'Table04_Opinion_newpath_mkdir' to match Variable 'newpath_mkdir'...")
    Table04_Opinion_newpath_mkdir = newpath_mkdir

def Table04_BS4_LXML_Recovery(CurrentDecision):
        global courtlistener_jurisdiction_dataset
        print(f"Current American Constitutional Supreme and Mandatory Jurisdiction: {courtlistener_jurisdiction_dataset} ...")
        global Table04_Opinion_current_html
                # Import Additional Python3 Require Module Libraries
        from bs4 import BeautifulSoup
        from lxml import etree
        import requests

        # Assign a Python Variable to Beautiful Soup 4's HTML Parser
        htmlParse = BeautifulSoup(html, 'html.parser')

        # Select HTML Element for Data Parsing Column #1 [courtlistener_case_name]
        # SAME
        htmlParse.find_all("h2")[0].get_text()

        # SAME
        pvar_bs4_tag_courtlistener_case_name = htmlParse.find_all("h2")[0].get_text()
        print(htmlParse.find_all("h2")[0].get_text())

        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now using Requests to Query Selected Court Opinion from Remote Server using BS4 Successful!")

        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now using Requests to Query Selected Court Opinion from Remote Server using LXML XPATH...")

        #URL = "https://www.courtlistener.com/opinion/2581757/amalgamated-transit-v-state/"
        URL = sql_full_url_insert

        # First Instance of XPATH Request / Parse Requirements & Variables (Thanks to chevignon93 on reddit.com!)

        # Select HTML Element for Data Parsing Column #2 (Cont.) [courtlistener_jurisdiction]
        HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                    'Accept-Language': 'en-US, en;q=0.5'})

        webpage = requests.get(URL, headers=HEADERS)
        xsoup = BeautifulSoup(webpage.content, "html5lib")
        dom = etree.HTML(str(xsoup))

        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now using Requests to Query Selected Court Opinion from Remote Server using LXML XPATH Successful!")

        #### JURISDICTION #ALL: START [63 Columns] -> Python Variables -> PyMYSQL MariaDB Insert Payload!

        # Assign Table4 Column 1 / 63 - MariaDB Column Name: courtlistener_case_name
        # SEE above code to see BS4 tag scrape for complete courtlistener_case_name

        # Assign Tabl4 Column 1 / 63 - MariaDB Column Name: courtlistener_case_name
        #print("Dragon Breath [F.10] - [Table 4/6] - Table4_RemoteServer - [CL Jurisdiction Dataset] - Now Assigning Table4 Column Python Variable 1 out of 12...")
        #pvar_dom_xpath_courtlistener_case_name = dom.xpath('/html/body/div[1]/div[1]/article/h2')[0].text.strip()
        #print(dom.xpath('/html/body/div[1]/div[1]/article/h2')[0].text.strip())

        # Assign Table4 Column 2 / 63 - MariaDB Column Name: courtlistener_jurisdiction
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 2 out of 63...")
        try:  
            pvar_dom_xpath_courtlistener_jurisdiction = dom.xpath('/html/body/div[1]/div[1]/article/h3')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_jurisdiction) !=0:
                print(pvar_dom_xpath_courtlistener_jurisdiction)
            else:
                pvar_dom_xpath_courtlistener_jurisdiction = "(NULL)"
                print(pvar_dom_xpath_courtlistener_jurisdiction)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 2 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 2 out of 63...")
            pvar_dom_xpath_courtlistener_jurisdiction = "(NULL)"
        print(pvar_dom_xpath_courtlistener_jurisdiction)

        #print(dom.xpath('/html/body/div[1]/div[1]/article/h3')[0].text.strip())
        # VERIFIED - 08/17/2022

        # Assign Table4 Column 2 / 63 - MariaDB Column Name: courtlistener_jurisdiction
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 2 out of 63...")
    #    pvar_dom_xpath_courtlistener_jurisdiction = dom.xpath('/html/body/div[1]/div[1]/article/h3')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_jurisdiction) !=0:
    #        print(pvar_dom_xpath_courtlistener_jurisdiction)
    #    else:
    #        pvar_dom_xpath_courtlistener_jurisdiction = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_jurisdiction)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/h3')[0].text.strip())
        # VERIFIED - 08/17/2022

        # Assign Table4 Column 2 / 63 - MariaDB Column Name: courtlistener_jurisdiction
        #print("Dragon Breath [F.10] - [Table 4/6] - Table4_RemoteServer - [CL Jurisdiction Dataset] - Now Assigning Table4 Column Python Variable 2 out of 63...")
        #pvar_dom_xpath_courtlistener_jurisdiction = dom.xpath('/html/body/div[1]/div[1]/article/h3')[0].text.strip()
        #print(dom.xpath('/html/body/div[1]/div[1]/article/h3')[0].text.strip())

        # Assign Table4 Column 3 / 63 - MariaDB Column Name: courtlistener_filed
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 3 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_filed = dom.xpath('/html/body/div[1]/div[1]/article/p[1]/span[2]')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_filed) !=0:
                print(pvar_dom_xpath_courtlistener_filed)
            else:
                pvar_dom_xpath_courtlistener_filed = "(NULL)"
                print(pvar_dom_xpath_courtlistener_filed)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 3 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 3 out of 63...")
            pvar_dom_xpath_courtlistener_filed = "(NULL)"
        print(pvar_dom_xpath_courtlistener_filed)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[1]/span[2]')[0].text.strip())
        # VERIFIED - 08/17/2022

    #    # Assign Table4 Column 3 / 63 - MariaDB Column Name: courtlistener_filed
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 3 out of 63...")
    #    pvar_dom_xpath_courtlistener_filed = dom.xpath('/html/body/div[1]/div[1]/article/p[1]/span[2]')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_filed) !=0:
    #        print(pvar_dom_xpath_courtlistener_filed)
    #    else:
    #        pvar_dom_xpath_courtlistener_filed = "(NULL)"
    #   print(pvar_dom_xpath_courtlistener_filed)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[1]/span[2]')[0].text.strip())
        # VERIFIED - 08/17/2022

        # Assign Table4 Column 3 / 63 - MariaDB Column Name: courtlistener_filed
        #print("Dragon Breath [F.10] - [Table 4/6] - Table4_RemoteServer - [CL Jurisdiction Dataset] - Now Assigning Table4 Column Python Variable 3 out of 63...")
        #pvar_dom_xpath_courtlistener_filed = dom.xpath('/html/body/div[1]/div[1]/article/p[1]/span[2]')[0].text.strip()
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[1]/span[2]')[0].text.strip())

        # Assign Table4 Column 4 / 63 - MariaDB Column Name: courtlistener_precedential_status
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 4 out of 63...")
        try:    
            pvar_dom_xpath_courtlistener_precedential_status = dom.xpath('/html/body/div[1]/div[1]/article/p[2]/span[2]')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_precedential_status) !=0:
                print(pvar_dom_xpath_courtlistener_precedential_status)
            else:
                pvar_dom_xpath_courtlistener_precedential_status = "(NULL)"
                print(pvar_dom_xpath_courtlistener_precedential_status)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 4 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 4 out of 63...")
            pvar_dom_xpath_courtlistener_precedential_status = "(NULL)"
        print(pvar_dom_xpath_courtlistener_precedential_status)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[2]/span[2]')[0].text.strip())
        # VERIFIED - 08/17/2022

    #    # Assign Table4 Column 4 / 63 - MariaDB Column Name: courtlistener_precedential_status
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 4 out of 63...")
    #    pvar_dom_xpath_courtlistener_precedential_status = dom.xpath('/html/body/div[1]/div[1]/article/p[2]/span[2]')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_precedential_status) !=0:
    #        print(pvar_dom_xpath_courtlistener_precedential_status)
    #    else:
    #        pvar_dom_xpath_courtlistener_precedential_status = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_precedential_status)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[2]/span[2]')[0].text.strip())
        # VERIFIED - 08/17/2022

        # Assign Table4 Column 4 / 63 - MariaDB Column Name: courtlistener_precedential_status
        #print("Dragon Breath [F.10] - [Table 4/6] - Table4_RemoteServer - [CL Jurisdiction Dataset] - Now Assigning Table4 Column Python Variable 4 out of 63...")
        #pvar_dom_xpath_courtlistener_precedential_status = dom.xpath('/html/body/div[1]/div[1]/article/p[2]/span[2]')[0].text.strip()
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[2]/span[2]')[0].text.strip())

        # Assign Table4 Column 5 / 63 - MariaDB Column Name: courtlistener_docket_number
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 5 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_docket_number = dom.xpath('/html/body/div[1]/div[1]/article/p[4]/span[2]')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_docket_number) !=0:
                print(pvar_dom_xpath_courtlistener_docket_number)
            else:
                pvar_dom_xpath_courtlistener_docket_number = "(NULL)"
                print(pvar_dom_xpath_courtlistener_docket_number)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 5 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 5 out of 63...")
            pvar_dom_xpath_courtlistener_docket_number = "(NULL)"
        print(pvar_dom_xpath_courtlistener_docket_number)

        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[4]/span[2]')[0].text.strip())
        # VERIFIED - 08/17/2022

    #    # Assign Table4 Column 5 / 63 - MariaDB Column Name: courtlistener_docket_number
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 5 out of 63...")
    #    pvar_dom_xpath_courtlistener_docket_number = dom.xpath('/html/body/div[1]/div[1]/article/p[4]/span[2]')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_docket_number) !=0:
    #        print(pvar_dom_xpath_courtlistener_docket_number)
    #    else:
    #        pvar_dom_xpath_courtlistener_docket_number = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_docket_number)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[4]/span[2]')[0].text.strip())
        # VERIFIED - 08/17/2022

        # Assign Table4 Column 5 / 63 - MariaDB Column Name: courtlistener_docket_number
        #print("Dragon Breath [F.10] - [Table 4/6] - Table4_RemoteServer - [CL Jurisdiction Dataset] - Now Assigning Table4 Column Python Variable 5 out of 63...")
        #pvar_dom_xpath_courtlistener_docket_number = dom.xpath('/html/body/div[1]/div[1]/article/p[4]/span[2]')[0].text.strip()
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[4]/span[2]')[0].text.strip())

        # Assign Table4 Column 6 / 63 - MariaDB Column Name: courtlistener_pdf_opinion_url_storage
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 6 out of 63...")
        try: 
            pvar_dom_xpath_courtlistener_pdf_opinion_url_storage = dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[1]/a/@href')
            if len(pvar_dom_xpath_courtlistener_pdf_opinion_url_storage) !=0:
                print(pvar_dom_xpath_courtlistener_pdf_opinion_url_storage)
            else:
                pvar_dom_xpath_courtlistener_pdf_opinion_url_storage = "(NULL)"
                print(pvar_dom_xpath_courtlistener_pdf_opinion_url_storage)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 6 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 6 out of 63...")
            pvar_dom_xpath_courtlistener_pdf_opinion_url_storage = "(NULL)"
        print(pvar_dom_xpath_courtlistener_pdf_opinion_url_storage)    
        #print(dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[1]/a/@href'))

    #    # Assign Table4 Column 6 / 63 - MariaDB Column Name: courtlistener_pdf_opinion_url_storage
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 6 out of 63...")
    #    pvar_dom_xpath_courtlistener_pdf_opinion_url_storage = dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[1]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_pdf_opinion_url_storage) !=0:
    #        print(pvar_dom_xpath_courtlistener_pdf_opinion_url_storage)
    #    else:
    #        pvar_dom_xpath_courtlistener_pdf_opinion_url_storage = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_pdf_opinion_url_storage)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[1]/a/@href'))


        # Assign Table4 Column 6 / 63 - MariaDB Column Name: courtlistener_pdf_opinion_url_storage
        #print("Dragon Breath [F.10] - [Table 4/6] - Table4_RemoteServer - [CL Jurisdiction Dataset] - Now Assigning Table4 Column Python Variable 6 out of 63...")
        #pvar_dom_xpath_courtlistener_pdf_opinion_url_storage = dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[1]/a/@href')
        #print(dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[1]/a/@href'))

        # Assign Table4 Column 7 / 63 - MariaDB Column Name: courtlistener_pdf_opinion_url_gov
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 7 out of 63...")
        try:    
            pvar_dom_xpath_courtlistener_pdf_opinion_url_gov = dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[3]/a/@href')
            # dba - !=0: checks for non-empty - Repiphany's explanation
            if len(pvar_dom_xpath_courtlistener_pdf_opinion_url_gov) !=0:
                print(pvar_dom_xpath_courtlistener_pdf_opinion_url_gov)
            else:
                 pvar_dom_xpath_courtlistener_pdf_opinion_url_gov = "(NULL)"
                 print(pvar_dom_xpath_courtlistener_pdf_opinion_url_gov)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 7 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 7 out of 63...")
            pvar_dom_xpath_courtlistener_pdf_opinion_url_gov = "(NULL)"
        print(pvar_dom_xpath_courtlistener_pdf_opinion_url_gov)    
        #print(dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[3]/a/@href'))


    #    # Assign Table4 Column 7 / 63 - MariaDB Column Name: courtlistener_pdf_opinion_url_gov
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 7 out of 63...")
    #    pvar_dom_xpath_courtlistener_pdf_opinion_url_gov = dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[3]/a/@href')
    #    # dba - !=0: checks for non-empty - Repiphany's explanation
    #    if len(pvar_dom_xpath_courtlistener_pdf_opinion_url_gov) !=0:
    #        print(pvar_dom_xpath_courtlistener_pdf_opinion_url_gov)
    #    else:
    #        pvar_dom_xpath_courtlistener_pdf_opinion_url_gov = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_pdf_opinion_url_gov)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[3]/a/@href'))

        # Assign Table4 Column 7 / 63 - MariaDB Column Name: courtlistener_pdf_opinion_url_gov
        #print("Dragon Breath [F.10] - [Table 4/6] - Table4_RemoteServer - [CL Jurisdiction Dataset] - Now Assigning Table4 Column Python Variable 7 out of 63...")
        #pvar_dom_xpath_courtlistener_pdf_opinion_url_gov = dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[3]/a/@href')
        #print(dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[3]/a/@href'))


        # Assign Table4 Column 8 / 63 - MariaDB Column Name: courtlistener_supreme_court_citations
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 8 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_supreme_court_citations = dom.xpath('/html/body/div[1]/div[1]/article/p[3]/span[2]')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_supreme_court_citations) !=0:
                print(pvar_dom_xpath_courtlistener_supreme_court_citations)
            else:
                pvar_dom_xpath_courtlistener_supreme_court_citations = "(NULL)"
                print(pvar_dom_xpath_courtlistener_supreme_court_citations)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 8 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 8 out of 63...")
            pvar_dom_xpath_courtlistener_supreme_court_citations = "(NULL)"
        print(pvar_dom_xpath_courtlistener_supreme_court_citations)
                
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[3]/span[2]'))
        # VERIFIED - 08/17/2022


    #    # Assign Table4 Column 8 / 63 - MariaDB Column Name: courtlistener_supreme_court_citations
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 8 out of 63...")
    #    pvar_dom_xpath_courtlistener_supreme_court_citations = dom.xpath('/html/body/div[1]/div[1]/article/p[3]/span[2]')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_supreme_court_citations) !=0:
    #        print(pvar_dom_xpath_courtlistener_supreme_court_citations)
    #    else:
    #        pvar_dom_xpath_courtlistener_supreme_court_citations = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_supreme_court_citations)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[3]/span[2]'))
        # VERIFIED - 08/17/2022

        # Assign Table4 Column 8 / 63 - MariaDB Column Name: courtlistener_supreme_court_citations
        #print("Dragon Breath [F.10] - [Table 4/6] - Table4_RemoteServer - [CL Jurisdiction Dataset] - Now Assigning Table4 Column Python Variable 8 out of 63...")
        #pvar_dom_xpath_courtlistener_supreme_court_citations = dom.xpath('/html/body/div[1]/div[1]/article/p[3]/span[2]')[0].text.strip()
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[3]/span[2]'))


        # (SCOTUS: SHOWING JUDGE/AUTHOR NAMES [PERSON TEXT]) XPATH: dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a')[0].text.strip()
        # Assign Table4 Column 9 / 63 - MariaDB Column Name: courtlistener_supreme_court_database_id
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 9 out of 63...")
        try:
            #pvar_dom_xpath_courtlistener_supreme_court_database_id = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a')[0].text.strip()
            pvar_dom_xpath_courtlistener_supreme_court_database_id = dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_supreme_court_database_id) !=0:
                print(pvar_dom_xpath_courtlistener_supreme_court_database_id)
            else:
                pvar_dom_xpath_courtlistener_supreme_court_database_id = "(NULL)"
                print(pvar_dom_xpath_courtlistener_supreme_court_database_id)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Not Dataset: SCOTUS) Table04 Column Python Variable 9 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Not Dataset: SCOTUS) Table04 Column Python Variable 9 out of 63...")
            pvar_dom_xpath_courtlistener_supreme_court_database_id = "(NULL)"
        print(pvar_dom_xpath_courtlistener_supreme_court_database_id)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a'))
        # VERIFIED - 08/17/2022

    #     Assign Table4 Column 9 / 63 - MariaDB Column Name: courtlistener_supreme_court_database_id
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 9 out of 63...")
    #    pvar_dom_xpath_courtlistener_supreme_court_database_id = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_supreme_court_database_id) !=0:
    #        print(pvar_dom_xpath_courtlistener_supreme_court_database_id)
    #    else:
    #        pvar_dom_xpath_courtlistener_supreme_court_database_id = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_supreme_court_database_id)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a'))
        # VERIFIED - 08/17/2022

        # Assign Table4 Column 9 / 63 - MariaDB Column Name: courtlistener_supreme_court_database_id
        #print("Dragon Breath [F.10] - [Table 4/6] - Table4_RemoteServer - [CL Jurisdiction Dataset] - Now Assigning Table4 Column Python Variable 9 out of 63...")
        #pvar_dom_xpath_courtlistener_supreme_court_database_id = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a')[0].text.strip()
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a'))

        
        # (SCOTUS: SHOWING JUDGE/AUTHOR NAME URL [PERSON URL]) XPATH: dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href')
        # Assign Table4 Column 10 / 63 - MariaDB Column Name: courtlistener_supreme_court_database_id_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE  (Not Dataset: SCOTUS) Table04 Column Python Variable 10 out of 63...")
        try:
           #pvar_dom_xpath_courtlistener_supreme_court_database_id_url = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href')
           pvar_dom_xpath_courtlistener_supreme_court_database_id_url = dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a/@href')
           if len(pvar_dom_xpath_courtlistener_supreme_court_database_id_url) !=0:
               print(pvar_dom_xpath_courtlistener_supreme_court_database_id_url)
           else:
               pvar_dom_xpath_courtlistener_supreme_court_database_id_url = "(NULL)"
               print(pvar_dom_xpath_courtlistener_supreme_court_database_id_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Not Dataset: SCOTUS) Table04 Column Python Variable 10 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Not Dataset: SCOTUS) Table04 Column Python Variable 10 out of 63...")
            pvar_dom_xpath_courtlistener_supreme_court_database_id_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_supreme_court_database_id_url)    

        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href'))
        # VERIFIED - 08/17/2022

    #    # Assign Table4 Column 10 / 63 - MariaDB Column Name: courtlistener_supreme_court_database_id_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 10 out of 63...")
    #    pvar_dom_xpath_courtlistener_supreme_court_database_id_url = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_supreme_court_database_id_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_supreme_court_database_id_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_supreme_court_database_id_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_supreme_court_database_id_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href'))
        # VERIFIED - 08/17/2022

        # Assign Table4 Column 10 / 63 - MariaDB Column Name: courtlistener_supreme_court_database_id_url
        #print("Dragon Breath [F.10] - [Table 4/6] - Table4_RemoteServer - [CL Jurisdiction Dataset] - Now Assigning Table4 Column Python Variable 10 out of 63...")
        #pvar_dom_xpath_courtlistener_supreme_court_database_id_url = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href')
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href'))


        # (SCOTUS: SHOWING SCDB ID # [SCDB ID# TEXT]) XPATH: dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a')[0].text.strip()
        # Assign Table4 Column 11 / 63 - MariaDB Column Name: courtlistener_supreme_court_author_name
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 11 out of 63...")
        try:
            #pvar_dom_xpath_courtlistener_supreme_court_author_name = dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a')[0].text.strip()
            pvar_dom_xpath_courtlistener_supreme_court_author_name = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_supreme_court_author_name) !=0:
                print(pvar_dom_xpath_courtlistener_supreme_court_author_name)
            else:
                pvar_dom_xpath_courtlistener_supreme_court_author_name = "(NULL)"
                print(pvar_dom_xpath_courtlistener_supreme_court_author_name)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Not Dataset: SCOTUS) Table04 Column Python Variable 11 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Not Dataset: SCOTUS) Table04 Column Python Variable 11 out of 63...")
            pvar_dom_xpath_courtlistener_supreme_court_author_name = "(NULL)"
        print(pvar_dom_xpath_courtlistener_supreme_court_author_name)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a'))
        # VERIFIED - 08/17/2022

    #    # Assign Table4 Column 11 / 63 - MariaDB Column Name: courtlistener_supreme_court_author_name
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 11 out of 63...")
    #    pvar_dom_xpath_courtlistener_supreme_court_author_name = dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_supreme_court_author_name) !=0:
    #        print(pvar_dom_xpath_courtlistener_supreme_court_author_name)
    #    else:
    #        pvar_dom_xpath_courtlistener_supreme_court_author_name = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_supreme_court_author_name)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a'))
        # VERIFIED - 08/17/2022

        # Assign Table4 Column 11 / 63 - MariaDB Column Name: courtlistener_supreme_court_author_name
        #print("Dragon Breath [F.10] - [Table 4/6] - Table4_RemoteServer - [CL Jurisdiction Dataset] - Now Assigning Table4 Column Python Variable 11 out of 63...")
        #pvar_dom_xpath_courtlistener_supreme_court_author_name = dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a')[0].text.strip()
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a'))


        # (SCOTUS: SHOWING SCDB ID # URL [SCDB ID# URL]) XPATH: dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a/@href')
        # Assign Table4 Column 12 / 63 - MariaDB Column Name: courtlistener_supreme_court_author_name_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 12 out of 63...")
        try:
            #pvar_dom_xpath_courtlistener_supreme_court_author_name_url = dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a/@href')
            pvar_dom_xpath_courtlistener_supreme_court_author_name_url = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href')
            if len(pvar_dom_xpath_courtlistener_supreme_court_author_name_url) !=0:
                print(pvar_dom_xpath_courtlistener_supreme_court_author_name_url)
            else:
                pvar_dom_xpath_courtlistener_supreme_court_author_name_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_supreme_court_author_name_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Not Dataset: SCOTUS) Table04 Column Python Variable 12 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Not Dataset: SCOTUS) Table04 Column Python Variable 12 out of 63...")
            pvar_dom_xpath_courtlistener_supreme_court_author_name_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_supreme_court_author_name_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a/@href'))
        # VERIFIED - 08/17/2022

        # Assign Table4 Column 12 / 63 - MariaDB Column Name: courtlistener_supreme_court_author_name_url
        #print("Dragon Breath [F.10] - [Table 4/6] - Table4_RemoteServer - [CL Jurisdiction Dataset] - Now Assigning Table4 Column Python Variable 12 out of 63...")
        #pvar_dom_xpath_courtlistener_supreme_court_author_name_url = dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a/@href')
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a/@href'))

        # Assign Table4 Column 13 / 63 - MariaDB Column Name: courtlistener_citations
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 13 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_citations = dom.xpath('/html/body/div[1]/div[1]/article/p[3]/span[2]')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_citations) !=0:
                print(pvar_dom_xpath_courtlistener_citations)
            else:
                pvar_dom_xpath_courtlistener_citations = "(NULL)"
                print(pvar_dom_xpath_courtlistener_citations)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 13 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 13 out of 63...")
            pvar_dom_xpath_courtlistener_citations = "(NULL)"
        print(pvar_dom_xpath_courtlistener_citations)    
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[3]/span[2]'))
        # VERIFIED - 08/17/2022

    #    # Assign Table4 Column 13 / 63 - MariaDB Column Name: courtlistener_citations
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 13 out of 63...")
    #    pvar_dom_xpath_courtlistener_citations = dom.xpath('/html/body/div[1]/div[1]/article/p[3]/span[2]')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_citations) !=0:
    #        print(pvar_dom_xpath_courtlistener_citations)
    #    else:
    #        pvar_dom_xpath_courtlistener_citations = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_citations)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[3]/span[2]'))
        # VERIFIED - 08/17/2022


        # courtlistener_old_author_flag XPATH: dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]')[0].text.strip() (Make assign IF above null)...
        # Assign Table4 Column 14 / 63 - MariaDB Column Name: courtlistener_author_name
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 14 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_author_name = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_author_name) !=0:
                print(pvar_dom_xpath_courtlistener_author_name)
            else:
                pvar_dom_xpath_courtlistener_author_name = "(NULL)"
                print(pvar_dom_xpath_courtlistener_author_name)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 14 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 14 out of 63...")
            pvar_dom_xpath_courtlistener_author_name = "(NULL)"
        print(pvar_dom_xpath_courtlistener_author_name)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a'))

    #    # Assign Table4 Column 14 / 63 - MariaDB Column Name: courtlistener_author_name
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 14 out of 63...")
    #    pvar_dom_xpath_courtlistener_author_name = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_author_name) !=0:
    #        print(pvar_dom_xpath_courtlistener_author_name)
    #    else:
    #        pvar_dom_xpath_courtlistener_author_name = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_author_name)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a'))

        # courtlistener_old_author_flag XPATH: dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]')[0].text.strip() (Make assign IF above null)...
        # Assign Table4 Column 15 / 63 - MariaDB Column Name: courtlistener_author_name_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 15 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_author_name_url = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href')
            if len(pvar_dom_xpath_courtlistener_author_name_url) !=0:
                print(pvar_dom_xpath_courtlistener_author_name_url)
            else:
                pvar_dom_xpath_courtlistener_author_name_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_author_name_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 15 out of 63...")
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 15 out of 63...")
            pvar_dom_xpath_courtlistener_author_name_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_author_name_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href'))

    #    # Assign Table4 Column 15 / 63 - MariaDB Column Name: courtlistener_author_name_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 15 out of 63...")
    #    pvar_dom_xpath_courtlistener_author_name_url = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_author_name_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_author_name_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_author_name_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_author_name_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href'))

        # Assign Table4 Column 16 / 63 - MariaDB Column Name: courtlistener_summary_count
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 16 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_summary_count = dom.xpath('/html/body/div[1]/div[1]/div/div[2]/h3/span')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_summary_count) !=0:
                print(pvar_dom_xpath_courtlistener_summary_count)
            else:
                pvar_dom_xpath_courtlistener_summary_count = "(NULL)"
                print(pvar_dom_xpath_courtlistener_summary_count)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 16 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 16 out of 63...")
            pvar_dom_xpath_courtlistener_summary_count = "(NULL)"
        print(pvar_dom_xpath_courtlistener_summary_count)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[2]/h3/span'))

    #    # Assign Table4 Column 16 / 63 - MariaDB Column Name: courtlistener_summary_count
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 16 out of 63...")
    #    pvar_dom_xpath_courtlistener_summary_count = dom.xpath('/html/body/div[1]/div[1]/div/div[2]/h3/span')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_summary_count) !=0:
    #        print(pvar_dom_xpath_courtlistener_summary_count)
    #    else:
    #        pvar_dom_xpath_courtlistener_summary_count = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_summary_count)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[2]/h3/span'))

        # Assign Table4 Column 17 / 63 - MariaDB Column Name: courtlistener_summary_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 17 out of 63...")
        try:   
            pvar_dom_xpath_courtlistener_summary_url = dom.xpath('/html/body/div[1]/div[1]/div/div[2]/h4/a/@href')
            if len(pvar_dom_xpath_courtlistener_summary_url) !=0:
                print(pvar_dom_xpath_courtlistener_summary_url)
            else:
                pvar_dom_xpath_courtlistener_summary_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_summary_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 17 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 17 out of 63...")
            pvar_dom_xpath_courtlistener_summary_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_summary_url)    
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[2]/h4/a/@href'))

        # Assign Table4 Column 17 / 63 - MariaDB Column Name: courtlistener_summary_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 17 out of 63...")
    #    pvar_dom_xpath_courtlistener_summary_url = dom.xpath('/html/body/div[1]/div[1]/div/div[2]/h4/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_summary_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_summary_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_summary_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_summary_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[2]/h4/a/@href'))

        # Assign Table4 Column 18 / 63 - MariaDB Column Name: courtlistener_cited_by_count
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 18 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_cited_by_count = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/h3/span')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_cited_by_count) !=0:
                print(pvar_dom_xpath_courtlistener_cited_by_count)
            else:
                pvar_dom_xpath_courtlistener_cited_by_count = "(NULL)"
                print(pvar_dom_xpath_courtlistener_cited_by_count)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 18 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 18 out of 63...")
            pvar_dom_xpath_courtlistener_cited_by_count = "(NULL)"
        print(pvar_dom_xpath_courtlistener_cited_by_count)


        # Assign Table4 Column 18 / 63 - MariaDB Column Name: courtlistener_cited_by_count
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 18 out of 63...")
    #    pvar_dom_xpath_courtlistener_cited_by_count = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/h3/span')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_cited_by_count) !=0:
    #        print(pvar_dom_xpath_courtlistener_cited_by_count)
    #    else:
    #        pvar_dom_xpath_courtlistener_cited_by_count = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_cited_by_count)

        # Assign Table4 Column 19 / 63 - MariaDB Column Name: courtlistener_cited_by_1
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 19 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_cited_by_1 = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[1]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_cited_by_1) !=0:
                print(pvar_dom_xpath_courtlistener_cited_by_1)
            else:
                pvar_dom_xpath_courtlistener_cited_by_1 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_cited_by_1)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 19 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 19 out of 63...")
            pvar_dom_xpath_courtlistener_cited_by_1 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_cited_by_1)

        # Assign Table4 Column 19 / 63 - MariaDB Column Name: courtlistener_cited_by_1
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 19 out of 63...")
    #    pvar_dom_xpath_courtlistener_cited_by_1 = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[1]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_cited_by_1) !=0:
    #        print(pvar_dom_xpath_courtlistener_cited_by_1)
    #    else:
    #        pvar_dom_xpath_courtlistener_cited_by_1 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_cited_by_1)

        # Assign Table4 Column 20 / 63 - MariaDB Column Name: courtlistener_cited_by_1_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 20 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_cited_by_1_url = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[1]/a/@href')
            if len(pvar_dom_xpath_courtlistener_cited_by_1_url) !=0:
                print(pvar_dom_xpath_courtlistener_cited_by_1_url)
            else:
                pvar_dom_xpath_courtlistener_cited_by_1_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_cited_by_1_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 20 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 20 out of 63...")
            pvar_dom_xpath_courtlistener_cited_by_1_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_cited_by_1_url)

        # Assign Table4 Column 20 / 63 - MariaDB Column Name: courtlistener_cited_by_1_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 20 out of 63...")
    #    pvar_dom_xpath_courtlistener_cited_by_1_url = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[1]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_cited_by_1_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_cited_by_1_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_cited_by_1_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_cited_by_1_url)

        # Assign Table4 Column 21 / 63 - MariaDB Column Name: courtlistener_cited_by_2
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 21 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_cited_by_2 = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[2]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_cited_by_2) !=0:
                print(pvar_dom_xpath_courtlistener_cited_by_2)
            else:
                pvar_dom_xpath_courtlistener_cited_by_2 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_cited_by_2)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 21 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 21 out of 63...")
            pvar_dom_xpath_courtlistener_cited_by_2 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_cited_by_2)

        # Assign Table4 Column 21 / 63 - MariaDB Column Name: courtlistener_cited_by_2
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 21 out of 63...")
    #    pvar_dom_xpath_courtlistener_cited_by_2 = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[2]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_cited_by_2) !=0:
    #       print(pvar_dom_xpath_courtlistener_cited_by_2)
    #    else:
    #        pvar_dom_xpath_courtlistener_cited_by_2 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_cited_by_2)

        # Assign Table4 Column 22 / 63 - MariaDB Column Name: courtlistener_cited_by_2_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 22 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_cited_by_2_url = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[2]/a/@href')
            if len(pvar_dom_xpath_courtlistener_cited_by_2_url) !=0:
                print(pvar_dom_xpath_courtlistener_cited_by_2_url)
            else:
                pvar_dom_xpath_courtlistener_cited_by_2_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_cited_by_2_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 22 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 22 out of 63...")
            pvar_dom_xpath_courtlistener_cited_by_2_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_cited_by_2_url)

        # Assign Table4 Column 22 / 63 - MariaDB Column Name: courtlistener_cited_by_2_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 22 out of 63...")
    #    pvar_dom_xpath_courtlistener_cited_by_2_url = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[2]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_cited_by_2_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_cited_by_2_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_cited_by_2_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_cited_by_2_url)

        # Assign Table4 Column 23 / 63 - MariaDB Column Name: courtlistener_cited_by_3
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 23 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_cited_by_3 = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[3]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_cited_by_3) !=0:
                print(pvar_dom_xpath_courtlistener_cited_by_3)
            else:
                pvar_dom_xpath_courtlistener_cited_by_3 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_cited_by_3)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 23 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 23 out of 63...")
            pvar_dom_xpath_courtlistener_cited_by_3 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_cited_by_3)

        # Assign Table4 Column 23 / 63 - MariaDB Column Name: courtlistener_cited_by_3
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 23 out of 63...")
    #    pvar_dom_xpath_courtlistener_cited_by_3 = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[3]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_cited_by_3) !=0:
    #        print(pvar_dom_xpath_courtlistener_cited_by_3)
    #    else:
    #        pvar_dom_xpath_courtlistener_cited_by_3 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_cited_by_3)

        # Assign Table4 Column 24 / 63 - MariaDB Column Name: courtlistener_cited_by_3_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 24 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_cited_by_3_url = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[3]/a/@href')
            if len(pvar_dom_xpath_courtlistener_cited_by_3_url) !=0:
                print(pvar_dom_xpath_courtlistener_cited_by_3_url)
            else:
                pvar_dom_xpath_courtlistener_cited_by_3_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_cited_by_3_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 24 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 24 out of 63...")
            pvar_dom_xpath_courtlistener_cited_by_3_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_cited_by_3_url)

        # Assign Table4 Column 24 / 63 - MariaDB Column Name: courtlistener_cited_by_3_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 24 out of 63...")
    #    pvar_dom_xpath_courtlistener_cited_by_3_url = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[3]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_cited_by_3_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_cited_by_3_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_cited_by_3_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_cited_by_3_url)

        # Assign Table4 Column 25 / 63 - MariaDB Column Name: courtlistener_cited_by_4
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 25 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_cited_by_4 = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[4]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_cited_by_4) !=0:
                print(pvar_dom_xpath_courtlistener_cited_by_4)
            else:
                pvar_dom_xpath_courtlistener_cited_by_4 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_cited_by_4)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 25 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 25 out of 63...")
            pvar_dom_xpath_courtlistener_cited_by_4 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_cited_by_4)

        # Assign Table4 Column 25 / 63 - MariaDB Column Name: courtlistener_cited_by_4
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 25 out of 63...")
    #    pvar_dom_xpath_courtlistener_cited_by_4 = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[4]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_cited_by_4) !=0:
    #        print(pvar_dom_xpath_courtlistener_cited_by_4)
    #    else:
    #        pvar_dom_xpath_courtlistener_cited_by_4 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_cited_by_4)

        # Assign Table4 Column 26 / 63 - MariaDB Column Name: courtlistener_cited_by_4_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 26 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_cited_by_4_url = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[4]/a/@href')
            if len(pvar_dom_xpath_courtlistener_cited_by_4_url) !=0:
                print(pvar_dom_xpath_courtlistener_cited_by_4_url)
            else:
                pvar_dom_xpath_courtlistener_cited_by_4_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_cited_by_4_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 26 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 26 out of 63...")
            pvar_dom_xpath_courtlistener_cited_by_4_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_cited_by_4_url)

        # Assign Table4 Column 26 / 63 - MariaDB Column Name: courtlistener_cited_by_4_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 26 out of 63...")
    #    pvar_dom_xpath_courtlistener_cited_by_4_url = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[4]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_cited_by_4_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_cited_by_4_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_cited_by_4_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_cited_by_4_url)

        # Assign Table4 Column 27 / 63 - MariaDB Column Name: courtlistener_cited_by_5
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 27 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_cited_by_5 = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[5]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_cited_by_5) !=0:
                print(pvar_dom_xpath_courtlistener_cited_by_5)
            else:
                pvar_dom_xpath_courtlistener_cited_by_5 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_cited_by_5)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 27 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 27 out of 63...")
            pvar_dom_xpath_courtlistener_cited_by_5 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_cited_by_5)
  
        # Assign Table4 Column 27 / 63 - MariaDB Column Name: courtlistener_cited_by_5
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 27 out of 63...")
    #    pvar_dom_xpath_courtlistener_cited_by_5 = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[5]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_cited_by_5) !=0:
    #        print(pvar_dom_xpath_courtlistener_cited_by_5)
    #    else:
    #        pvar_dom_xpath_courtlistener_cited_by_5 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_cited_by_5)

        # Assign Table4 Column 28 / 63 - MariaDB Column Name: courtlistener_cited_by_5_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 28 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_cited_by_5_url = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[5]/a/@href')
            if len(pvar_dom_xpath_courtlistener_cited_by_5_url) !=0:
                print(pvar_dom_xpath_courtlistener_cited_by_5_url)
            else:
                pvar_dom_xpath_courtlistener_cited_by_5_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_cited_by_5_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 28 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 28 out of 63...")
            pvar_dom_xpath_courtlistener_cited_by_5_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_cited_by_5_url)
  
        # Assign Table4 Column 28 / 63 - MariaDB Column Name: courtlistener_cited_by_5_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 28 out of 63...")
    #    pvar_dom_xpath_courtlistener_cited_by_5_url = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[5]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_cited_by_5_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_cited_by_5_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_cited_by_5_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_cited_by_5_url)

        # Assign Table4 Column 29 / 63 - MariaDB Column Name: courtlistener_cited_by_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 29 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_cited_by_url = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/p[2]/a/@href')
            if len(pvar_dom_xpath_courtlistener_cited_by_url) !=0:
                print(pvar_dom_xpath_courtlistener_cited_by_url)
            else:
                pvar_dom_xpath_courtlistener_cited_by_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_cited_by_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 29 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 29 out of 63...")
            pvar_dom_xpath_courtlistener_cited_by_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_cited_by_url)

        # Assign Table4 Column 29 / 63 - MariaDB Column Name: courtlistener_cited_by_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 29 out of 63...")
    #    pvar_dom_xpath_courtlistener_cited_by_url = dom.xpath('/html/body/div[1]/div[1]/div/div[3]/p[2]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_cited_by_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_cited_by_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_cited_by_url = "(NULL)"
    #   print(pvar_dom_xpath_courtlistener_cited_by_url)

        # Assign Table4 Column 30 / 63 - MariaDB Column Name: courtlistener_authorities_count
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 30 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_count = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/h3/span')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_authorities_count) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_count)
            else:
                pvar_dom_xpath_courtlistener_authorities_count = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_count)
        except BaseException: 
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 30 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 30 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_count = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_count)

        # Assign Table4 Column 30 / 63 - MariaDB Column Name: courtlistener_authorities_count
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 30 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_count = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/h3/span')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_authorities_count) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_count)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_count = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_count)

        # Assign Table4 Column 31 / 63 - MariaDB Column Name: courtlistener_authorities_1
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 31 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_1 = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[1]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_authorities_1) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_1)
            else:
                pvar_dom_xpath_courtlistener_authorities_1 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_1)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 31 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 31 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_1 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_1)

        # Assign Table4 Column 31 / 63 - MariaDB Column Name: courtlistener_authorities_1
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 31 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_1 = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[1]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_authorities_1) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_1)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_1 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_1)

        # Assign Table4 Column 32 / 63 - MariaDB Column Name: courtlistener_authorities_1_instances
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 32 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_1_instances = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[1]/span')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_authorities_1_instances) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_1_instances)
            else:
                pvar_dom_xpath_courtlistener_authorities_1_instances = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_1_instances)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 32 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 32 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_1_instances = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_1_instances)

        # Assign Table4 Column 32 / 63 - MariaDB Column Name: courtlistener_authorities_1_instances
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 32 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_1_instances = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[1]/span')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_authorities_1_instances) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_1_instances)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_1_instances = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_1_instances)

        # Assign Table4 Column 33 / 63 - MariaDB Column Name: courtlistener_authorities_1_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 33 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_1_url = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[1]/a/@href')
            if len(pvar_dom_xpath_courtlistener_authorities_1_url) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_1_url)
            else:
                pvar_dom_xpath_courtlistener_authorities_1_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_1_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 33 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 33 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_1_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_1_url)

        # Assign Table4 Column 33 / 63 - MariaDB Column Name: courtlistener_authorities_1_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 33 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_1_url = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[1]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_authorities_1_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_1_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_1_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_1_url)

        # Assign Table4 Column 34 / 63 - MariaDB Column Name: courtlistener_authorities_2
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 34 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_2 = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[2]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_authorities_2) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_2)
            else:
                pvar_dom_xpath_courtlistener_authorities_2 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_2)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 34 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 34 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_2 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_2)

        # Assign Table4 Column 34 / 63 - MariaDB Column Name: courtlistener_authorities_2
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 34 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_2 = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[2]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_authorities_2) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_2)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_2 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_2)

        # Assign Table4 Column 35 / 63 - MariaDB Column Name: courtlistener_authorities_2_instances
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 35 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_2_instances = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[2]/span')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_authorities_2_instances) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_2_instances)
            else:
                pvar_dom_xpath_courtlistener_authorities_2_instances = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_2_instances)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 35 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 35 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_2_instances = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_2_instances)
        
        # Assign Table4 Column 35 / 63 - MariaDB Column Name: courtlistener_authorities_2_instances
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 35 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_2_instances = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[2]/span')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_authorities_2_instances) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_2_instances)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_2_instances = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_2_instances)

        # Assign Table4 Column 36 / 63 - MariaDB Column Name: courtlistener_authorities_2_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 36 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_2_url = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[2]/a/@href')
            if len(pvar_dom_xpath_courtlistener_authorities_2_url) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_2_url)
            else:
                 pvar_dom_xpath_courtlistener_authorities_2_url = "(NULL)"
                 print(pvar_dom_xpath_courtlistener_authorities_2_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 36 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 36 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_2_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_2_url)
        
        # Assign Table4 Column 36 / 63 - MariaDB Column Name: courtlistener_authorities_2_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 36 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_2_url = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[2]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_authorities_2_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_2_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_2_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_2_url)

        # Assign Table4 Column 37 / 63 - MariaDB Column Name: courtlistener_authorities_3
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 37 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_3 = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[3]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_authorities_3) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_3)
            else:
                pvar_dom_xpath_courtlistener_authorities_3 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_3)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 37 out of 63...")
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 37 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_3 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_3)

        # Assign Table4 Column 37 / 63 - MariaDB Column Name: courtlistener_authorities_3
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 37 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_3 = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[3]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_authorities_3) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_3)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_3 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_3)

        # Assign Table4 Column 38 / 63 - MariaDB Column Name: courtlistener_authorities_3_instances
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 38 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_3_instances = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[3]/span')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_authorities_3_instances) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_3_instances)
            else:
                pvar_dom_xpath_courtlistener_authorities_3_instances = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_3_instances)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 38 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 38 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_3_instances = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_3_instances)

        # Assign Table4 Column 38 / 63 - MariaDB Column Name: courtlistener_authorities_3_instances
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 38 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_3_instances = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[3]/span')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_authorities_3_instances) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_3_instances)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_3_instances = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_3_instances)

        # Assign Table4 Column 39 / 63 - MariaDB Column Name: courtlistener_authorities_3_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 39 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_3_url = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[3]/a/@href')
            if len(pvar_dom_xpath_courtlistener_authorities_3_url) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_3_url)
            else:
                pvar_dom_xpath_courtlistener_authorities_3_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_3_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 39 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 39 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_3_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_3_url)

        # Assign Table4 Column 39 / 63 - MariaDB Column Name: courtlistener_authorities_3_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 39 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_3_url = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[3]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_authorities_3_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_3_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_3_url = "(NULL)"
    #   print(pvar_dom_xpath_courtlistener_authorities_3_url)

        # Assign Table4 Column 40 / 63 - MariaDB Column Name: courtlistener_authorities_4
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 40 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_4 = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[4]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_authorities_4) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_4)
            else:
                pvar_dom_xpath_courtlistener_authorities_4 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_4)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 40 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 40 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_4 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_4)

        # Assign Table4 Column 40 / 63 - MariaDB Column Name: courtlistener_authorities_4
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 40 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_4 = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[4]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_authorities_4) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_4)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_4 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_4)

        # Assign Table4 Column 41 / 63 - MariaDB Column Name: courtlistener_authorities_4_instances
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 41 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_4_instances = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[4]/span')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_authorities_4_instances) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_4_instances)
            else:
                pvar_dom_xpath_courtlistener_authorities_4_instances = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_4_instances)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 41 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 41 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_4_instances = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_4_instances)

        # Assign Table4 Column 41 / 63 - MariaDB Column Name: courtlistener_authorities_4_instances
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 41 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_4_instances = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[4]/span')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_authorities_4_instances) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_4_instances)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_4_instances = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_4_instances)

        # Assign Table4 Column 42 / 63 - MariaDB Column Name: courtlistener_authorities_4_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 42 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_4_url = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[4]/a/@href')
            if len(pvar_dom_xpath_courtlistener_authorities_4_url) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_4_url)
            else:
                 pvar_dom_xpath_courtlistener_authorities_4_url = "(NULL)"
                 print(pvar_dom_xpath_courtlistener_authorities_4_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 42 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 42 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_4_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_4_url)

        # Assign Table4 Column 42 / 63 - MariaDB Column Name: courtlistener_authorities_4_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 42 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_4_url = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[4]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_authorities_4_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_4_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_4_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_4_url)

        # Assign Table4 Column 43 / 63 - MariaDB Column Name: courtlistener_authorities_5
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 43 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_5 = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[5]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_authorities_5) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_5)
            else:
                pvar_dom_xpath_courtlistener_authorities_5 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_5)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 43 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 43 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_5 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_5)

        # Assign Table4 Column 43 / 63 - MariaDB Column Name: courtlistener_authorities_5
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 43 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_5 = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[5]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_authorities_5) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_5)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_5 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_5)

        # Assign Table4 Column 44 / 63 - MariaDB Column Name: courtlistener_authorities_5_instances
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 44 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_5_instances = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[5]/span')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_authorities_5_instances) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_5_instances)
            else:
                pvar_dom_xpath_courtlistener_authorities_5_instances = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_5_instances)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 44 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 44 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_5_instances = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_5_instances)

        # Assign Table4 Column 44 / 63 - MariaDB Column Name: courtlistener_authorities_5_instances
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 44 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_5_instances = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[5]/span')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_authorities_5_instances) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_5_instances)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_5_instances = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_5_instances)

        # Assign Table4 Column 45 / 63 - MariaDB Column Name: courtlistener_authorities_5_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 45 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_5_url = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[5]/a/@href')
            if len(pvar_dom_xpath_courtlistener_authorities_5_url) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_5_url)
            else:
                pvar_dom_xpath_courtlistener_authorities_5_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_5_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 45 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 45 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_5_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_5_url)
        
        # Assign Table4 Column 45 / 63 - MariaDB Column Name: courtlistener_authorities_5_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 45 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_5_url = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[5]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_authorities_5_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_5_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_5_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_5_url)

        # Assign Table4 Column 46 / 63 - MariaDB Column Name: courtlistener_authorities_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 46 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_authorities_url = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/h4/a/@href')
            if len(pvar_dom_xpath_courtlistener_authorities_url) !=0:
                print(pvar_dom_xpath_courtlistener_authorities_url)
            else:
                pvar_dom_xpath_courtlistener_authorities_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_authorities_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 46 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUES (Index Out of Range) Table04 Column Python Variable 46 out of 63...")
            pvar_dom_xpath_courtlistener_authorities_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_authorities_url)

        # Assign Table4 Column 46 / 63 - MariaDB Column Name: courtlistener_authorities_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 46 out of 63...")
    #    pvar_dom_xpath_courtlistener_authorities_url = dom.xpath('/html/body/div[1]/div[1]/div/div[4]/h4/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_authorities_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_authorities_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_authorities_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_authorities_url)

        # Assign Table4 Column 47 / 63 - MariaDB Column Name: courtlistener_similiar_decision_1
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 47 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_similiar_decision_1 = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[1]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_similiar_decision_1) !=0:
                print(pvar_dom_xpath_courtlistener_similiar_decision_1)
            else:
                pvar_dom_xpath_courtlistener_similiar_decision_1 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_similiar_decision_1)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 47 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 47 out of 63...")
            pvar_dom_xpath_courtlistener_similiar_decision_1 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_similiar_decision_1)

        # Assign Table4 Column 47 / 63 - MariaDB Column Name: courtlistener_similiar_decision_1
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 47 out of 63...")
    #    pvar_dom_xpath_courtlistener_similiar_decision_1 = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[1]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_similiar_decision_1) !=0:
    #        print(pvar_dom_xpath_courtlistener_similiar_decision_1)
    #    else:
    #        pvar_dom_xpath_courtlistener_similiar_decision_1 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_similiar_decision_1)

        # Assign Table4 Column 48 / 63 - MariaDB Column Name: courtlistener_similiar_decision_1_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 48 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_similiar_decision_1_url = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[1]/a/@href')
            if len(pvar_dom_xpath_courtlistener_similiar_decision_1_url) !=0:
                print(pvar_dom_xpath_courtlistener_similiar_decision_1_url)
            else:
                pvar_dom_xpath_courtlistener_similiar_decision_1_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_similiar_decision_1_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 48 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 48 out of 63...")
            pvar_dom_xpath_courtlistener_similiar_decision_1_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_similiar_decision_1_url)

        # Assign Table4 Column 48 / 63 - MariaDB Column Name: courtlistener_similiar_decision_1_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 48 out of 63...")
    #    pvar_dom_xpath_courtlistener_similiar_decision_1_url = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[1]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_similiar_decision_1_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_similiar_decision_1_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_similiar_decision_1_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_similiar_decision_1_url)

        # Assign Table4 Column 49 / 63 - MariaDB Column Name: courtlistener_similiar_decision_2
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 49 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_similiar_decision_2 = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[2]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_similiar_decision_2) !=0:
                print(pvar_dom_xpath_courtlistener_similiar_decision_2)
            else:
                pvar_dom_xpath_courtlistener_similiar_decision_2 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_similiar_decision_2)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 49 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 49 out of 63...")
            pvar_dom_xpath_courtlistener_similiar_decision_2 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_similiar_decision_2)

        # Assign Table4 Column 49 / 63 - MariaDB Column Name: courtlistener_similiar_decision_2
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 49 out of 63...")
    #    pvar_dom_xpath_courtlistener_similiar_decision_2 = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[2]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_similiar_decision_2) !=0:
    #        print(pvar_dom_xpath_courtlistener_similiar_decision_2)
    #    else:
    #        pvar_dom_xpath_courtlistener_similiar_decision_2 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_similiar_decision_2)

        # Assign Table4 Column 50 / 63 - MariaDB Column Name: courtlistener_similiar_decision_2_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 50 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_similiar_decision_2_url = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[2]/a/@href')
            if len(pvar_dom_xpath_courtlistener_similiar_decision_2_url) !=0:
                print(pvar_dom_xpath_courtlistener_similiar_decision_2_url)
            else:
                pvar_dom_xpath_courtlistener_similiar_decision_2_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_similiar_decision_2_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 50 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 50 out of 63...")
            pvar_dom_xpath_courtlistener_similiar_decision_2_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_similiar_decision_2_url)

        # Assign Table4 Column 50 / 63 - MariaDB Column Name: courtlistener_similiar_decision_2_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 50 out of 63...")
    #    pvar_dom_xpath_courtlistener_similiar_decision_2_url = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[2]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_similiar_decision_2_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_similiar_decision_2_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_similiar_decision_2_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_similiar_decision_2_url)

        # Assign Table4 Column 51 / 63 - MariaDB Column Name: courtlistener_similiar_decision_3
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 51 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_similiar_decision_3 = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[3]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_similiar_decision_3) !=0:
                print(pvar_dom_xpath_courtlistener_similiar_decision_3)
            else:
                pvar_dom_xpath_courtlistener_similiar_decision_3 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_similiar_decision_3)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 51 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 51 out of 63...")
            pvar_dom_xpath_courtlistener_similiar_decision_3 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_similiar_decision_3)

        # Assign Table4 Column 51 / 63 - MariaDB Column Name: courtlistener_similiar_decision_3
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 51 out of 63...")
    #    pvar_dom_xpath_courtlistener_similiar_decision_3 = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[3]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_similiar_decision_3) !=0:
    #        print(pvar_dom_xpath_courtlistener_similiar_decision_3)
    #    else:
    #        pvar_dom_xpath_courtlistener_similiar_decision_3 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_similiar_decision_3)

        # Assign Table4 Column 52 / 63 - MariaDB Column Name: courtlistener_similiar_decision_3_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 52 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_similiar_decision_3_url = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[3]/a/@href')
            if len(pvar_dom_xpath_courtlistener_similiar_decision_3_url) !=0:
                print(pvar_dom_xpath_courtlistener_similiar_decision_3_url)
            else:
                pvar_dom_xpath_courtlistener_similiar_decision_3_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_similiar_decision_3_url)
        except BaseException: 
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 52 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 52 out of 63...")
            pvar_dom_xpath_courtlistener_similiar_decision_3_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_similiar_decision_3_url)

        # Assign Table4 Column 52 / 63 - MariaDB Column Name: courtlistener_similiar_decision_3_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 52 out of 63...")
    #    pvar_dom_xpath_courtlistener_similiar_decision_3_url = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[3]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_similiar_decision_3_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_similiar_decision_3_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_similiar_decision_3_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_similiar_decision_3_url)

        # Assign Table4 Column 53 / 63 - MariaDB Column Name: courtlistener_similiar_decision_4
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 53 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_similiar_decision_4 = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[4]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_similiar_decision_4) !=0:
                print(pvar_dom_xpath_courtlistener_similiar_decision_4)
            else:
                pvar_dom_xpath_courtlistener_similiar_decision_4 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_similiar_decision_4)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 53 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 53 out of 63...")
            pvar_dom_xpath_courtlistener_similiar_decision_4 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_similiar_decision_4)

        # Assign Table4 Column 53 / 63 - MariaDB Column Name: courtlistener_similiar_decision_4
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 53 out of 63...")
    #    pvar_dom_xpath_courtlistener_similiar_decision_4 = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[4]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_similiar_decision_4) !=0:
    #        print(pvar_dom_xpath_courtlistener_similiar_decision_4)
    #    else:
    #        pvar_dom_xpath_courtlistener_similiar_decision_4 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_similiar_decision_4)

        # Assign Table4 Column 54 / 63 - MariaDB Column Name: courtlistener_similiar_decision_4_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 54 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_similiar_decision_4_url = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[4]/a/@href')
            if len(pvar_dom_xpath_courtlistener_similiar_decision_4_url) !=0:
                print(pvar_dom_xpath_courtlistener_similiar_decision_4_url)
            else:
                pvar_dom_xpath_courtlistener_similiar_decision_4_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_similiar_decision_4_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 54 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 54 out of 63...")
            pvar_dom_xpath_courtlistener_similiar_decision_4_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_similiar_decision_4_url)

        # Assign Table4 Column 54 / 63 - MariaDB Column Name: courtlistener_similiar_decision_4_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 54 out of 63...")
    #    pvar_dom_xpath_courtlistener_similiar_decision_4_url = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[4]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_similiar_decision_4_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_similiar_decision_4_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_similiar_decision_4_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_similiar_decision_4_url)

        # Assign Table4 Column 55 / 63 - MariaDB Column Name: courtlistener_similiar_decision_5
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 55 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_similiar_decision_5 = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[5]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_similiar_decision_5) !=0:
                print(pvar_dom_xpath_courtlistener_similiar_decision_5)
            else:
                pvar_dom_xpath_courtlistener_similiar_decision_5 = "(NULL)"
                print(pvar_dom_xpath_courtlistener_similiar_decision_5)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 55 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 55 out of 63...")
            pvar_dom_xpath_courtlistener_similiar_decision_5 = "(NULL)"
        print(pvar_dom_xpath_courtlistener_similiar_decision_5)

        # Assign Table4 Column 55 / 63 - MariaDB Column Name: courtlistener_similiar_decision_5
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 55 out of 63...")
    #    pvar_dom_xpath_courtlistener_similiar_decision_5 = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[5]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_similiar_decision_5) !=0:
    #        print(pvar_dom_xpath_courtlistener_similiar_decision_5)
    #    else:
    #        pvar_dom_xpath_courtlistener_similiar_decision_5 = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_similiar_decision_5)

        # Assign Table4 Column 56 / 63 - MariaDB Column Name: courtlistener_similiar_decision_5_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 56 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_similiar_decision_5_url = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[5]/a/@href')
            if len(pvar_dom_xpath_courtlistener_similiar_decision_5_url) !=0:
                print(pvar_dom_xpath_courtlistener_similiar_decision_5_url)
            else:
                pvar_dom_xpath_courtlistener_similiar_decision_5_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_similiar_decision_5_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 56 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 56 out of 63...")
            pvar_dom_xpath_courtlistener_similiar_decision_5_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_similiar_decision_5_url)

        # Assign Table4 Column 56 / 63 - MariaDB Column Name: courtlistener_similiar_decision_5_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 56 out of 63...")
    #    pvar_dom_xpath_courtlistener_similiar_decision_5_url = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[5]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_similiar_decision_5_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_similiar_decision_5_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_similiar_decision_5_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_similiar_decision_5_url)

        # Assign Table4 Column 57 / 63 - MariaDB Column Name: courtlistener_similiar_decisions_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 57 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_similiar_decisions_url = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/p[2]/a/@href')
            if len(pvar_dom_xpath_courtlistener_similiar_decisions_url) !=0:
                print(pvar_dom_xpath_courtlistener_similiar_decisions_url)
            else:
                pvar_dom_xpath_courtlistener_similiar_decisions_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_similiar_decisions_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 57 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 57 out of 63...")
            pvar_dom_xpath_courtlistener_similiar_decisions_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_similiar_decisions_url)

        # Assign Table4 Column 57 / 63 - MariaDB Column Name: courtlistener_similiar_decisions_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 57 out of 63...")
    #    pvar_dom_xpath_courtlistener_similiar_decisions_url = dom.xpath('/html/body/div[1]/div[1]/div/div[5]/p[2]/a/@href')
    #    if len(pvar_dom_xpath_courtlistener_similiar_decisions_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_similiar_decisions_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_similiar_decisions_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_similiar_decisions_url)

     #   # Assign Table4 Column 58 / 63 - MariaDB Column Name: courtlistener_supreme_court_author_flag
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 58 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_supreme_court_author_flag = dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_supreme_court_author_flag) !=0:
                print(pvar_dom_xpath_courtlistener_supreme_court_author_flag)
            else:
                pvar_dom_xpath_courtlistener_supreme_court_author_flag = "False"
                print(pvar_dom_xpath_courtlistener_supreme_court_author_flag)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (False) VALUE (Not Dataset: SCOTUS) Table04 Column Python Variable 58 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (False) VALUE (Not Dataset: SCOTUS) Table04 Column Python Variable 58 out of 63...")
            pvar_dom_xpath_courtlistener_supreme_court_author_flag = "False"    
        print(pvar_dom_xpath_courtlistener_supreme_court_author_flag)

    #    # Assign Table4 Column 58 / 63 - MariaDB Column Name: courtlistener_supreme_court_author_flag
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 58 out of 63...")
    #    pvar_dom_xpath_courtlistener_supreme_court_author_flag = dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_supreme_court_author_flag) !=0:
    #        print(pvar_dom_xpath_courtlistener_supreme_court_author_flag)
    #    else:
    #        pvar_dom_xpath_courtlistener_supreme_court_author_flag = "False"
    #    print(pvar_dom_xpath_courtlistener_supreme_court_author_flag)

        # Assign Table4 Column 59 / 63 - MariaDB Column Name: courtlistener_old_author_flag
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 59 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_old_author_flag = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_old_author_flag) !=0:
                print(pvar_dom_xpath_courtlistener_old_author_flag)
            else:
                pvar_dom_xpath_courtlistener_old_author_flag = "False"
                print(pvar_dom_xpath_courtlistener_old_author_flag)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (False) VALUE (Index Out of Range) Table04 Column Python Variable 59 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (False) VALUE (Index Out of Range) Table04 Column Python Variable 59 out of 63...")
            pvar_dom_xpath_courtlistener_old_author_flag = "False"
        print(pvar_dom_xpath_courtlistener_old_author_flag)

        # Assign Table4 Column 59 / 63 - MariaDB Column Name: courtlistener_old_author_flag
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 59 out of 63...")
    #    pvar_dom_xpath_courtlistener_old_author_flag = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_old_author_flag) !=0:
    #        print(pvar_dom_xpath_courtlistener_old_author_flag)
    #    else:
    #        pvar_dom_xpath_courtlistener_old_author_flag = "False"
    #    print(pvar_dom_xpath_courtlistener_old_author_flag)

        # Assign Table4 Column 60 / 63 - MariaDB Column Name: courtlistener_new_author_flag
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 60 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_new_author_flag = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_new_author_flag) !=0:
                print(pvar_dom_xpath_courtlistener_new_author_flag)
            else:
                pvar_dom_xpath_courtlistener_new_author_flag = "False"
                print(pvar_dom_xpath_courtlistener_new_author_flag)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (False) VALUE (Index Out of Range) Table04 Column Python Variable 60 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (False) VALUE (Index Out of Range) Table04 Column Python Variable 60 out of 63...")
            pvar_dom_xpath_courtlistener_new_author_flag = "False"
        print(pvar_dom_xpath_courtlistener_new_author_flag)

        # Assign Table4 Column 60 / 63 - MariaDB Column Name: courtlistener_new_author_flag
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 60 out of 63...")
    #    pvar_dom_xpath_courtlistener_new_author_flag = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_new_author_flag) !=0:
    #        print(pvar_dom_xpath_courtlistener_new_author_flag)
    #    else:
    #        pvar_dom_xpath_courtlistener_new_author_flag = "False"
    #    print(pvar_dom_xpath_courtlistener_new_author_flag)

        # Assign Table4 Column 61 / 63 - MariaDB Column Name: courtlistener_panel
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 61 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_panel = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/a[1]')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_panel) !=0:
                print(pvar_dom_xpath_courtlistener_panel)
            else:
                pvar_dom_xpath_courtlistener_panel = "(NULL)"
                print(pvar_dom_xpath_courtlistener_panel)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 61 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 61 out of 63...")
            pvar_dom_xpath_courtlistener_panel = "(NULL)"
        print(pvar_dom_xpath_courtlistener_panel)    

        # Assign Table4 Column 61 / 63 - MariaDB Column Name: courtlistener_panel
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 61 out of 63...")
    #    pvar_dom_xpath_courtlistener_panel = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/a[1]')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_panel) !=0:
    #        print(pvar_dom_xpath_courtlistener_panel)
    #    else:
    #        pvar_dom_xpath_courtlistener_panel = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_panel)

        # Assign Table4 Column 62 / 63 - MariaDB Column Name: courtlistener_panel_url
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 62 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_panel_url = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/a[1]/@href')
            if len(pvar_dom_xpath_courtlistener_panel_url) !=0:
                print(pvar_dom_xpath_courtlistener_panel_url)
            else:
                pvar_dom_xpath_courtlistener_panel_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_panel_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 62 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table04 Column Python Variable 62 out of 63...")
            pvar_dom_xpath_courtlistener_panel_url = "(NULL)"    
        print(pvar_dom_xpath_courtlistener_panel_url)

        # Assign Table4 Column 62 / 63 - MariaDB Column Name: courtlistener_panel_url
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 62 out of 63...")
    #    pvar_dom_xpath_courtlistener_panel_url = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/a[1]/@href')
    #    if len(pvar_dom_xpath_courtlistener_panel_url) !=0:
    #        print(pvar_dom_xpath_courtlistener_panel_url)
    #    else:
    #        pvar_dom_xpath_courtlistener_panel_url = "(NULL)"
    #    print(pvar_dom_xpath_courtlistener_panel_url)

        # Assign Table4 Column 63 / 63 - MariaDB Column Name: courtlistener_panel_flag
        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 63 out of 63...")
        try:
            pvar_dom_xpath_courtlistener_panel_flag = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/a[1]')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_panel_flag) !=0:
                print(pvar_dom_xpath_courtlistener_panel_flag)
            else:
                pvar_dom_xpath_courtlistener_panel_flag = "False"
                print(pvar_dom_xpath_courtlistener_panel_flag)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (False) VALUE (Index Out of Range) Table04 Column Python Variable 63 out of 63...")
            logging.debug(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (False) VALUE (Index Out of Range) Table04 Column Python Variable 63 out of 63...")
            pvar_dom_xpath_courtlistener_panel_flag = "False"
        print(pvar_dom_xpath_courtlistener_panel_flag)    

        # Assign Table4 Column 63 / 63 - MariaDB Column Name: courtlistener_panel_flag
    #    print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable 63 out of 63...")
    #    pvar_dom_xpath_courtlistener_panel_flag = dom.xpath('/html/body/div[1]/div[1]/article/p[5]/a[1]')[0].text.strip()
    #    if len(pvar_dom_xpath_courtlistener_panel_flag) !=0:
    #        print(pvar_dom_xpath_courtlistener_panel_flag)
    #    else:
    #        pvar_dom_xpath_courtlistener_panel_flag = "False"
    #    print(pvar_dom_xpath_courtlistener_panel_flag)

        # Chain Print

        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Chain Printing Python Variables for Payload INJECTION to MariaDB]...")

        # [1] - XPATH tag: h2 | [courtlistener_case_name] (Only BS4 Pulls Full courtlistener_case_name)
        print(pvar_bs4_tag_courtlistener_case_name)

        # [2] - XPATH tag: h3 | [courtlistener_jurisdiction]
        print(pvar_dom_xpath_courtlistener_jurisdiction)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/h3')[0].text.strip())

        # [3] - XPATH tag: XPATH () | [courtlistener_filed]
        print(pvar_dom_xpath_courtlistener_filed)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[1]/span[2]')[0].text.strip())
        
        # [4] - XPATH tag: XPATH () | [courtlistener_precedential_status]
        print(pvar_dom_xpath_courtlistener_precedential_status)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[2]/span[2]')[0].text.strip())
        
        # [5] - XPATH tag: XPATH () | [courtlistener_docket_number]
        print(pvar_dom_xpath_courtlistener_docket_number)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[1]/a/@href'))
        
        # [6] - XPATH tag: XPATH () | [courtlistener_pdf_opinion_url_storage]
        print(pvar_dom_xpath_courtlistener_pdf_opinion_url_storage)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/div[2]/ul/li[3]/a/@href'))
        
        # [7] - XPATH tag: XPATH () | [courtlistener_pdf_opinion_url_gov]
        print(pvar_dom_xpath_courtlistener_pdf_opinion_url_gov)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[2]/span[2]')[0].text.strip())
        
        # [8] - XPATH tag: XPATH () | [courtlistener_citations]
        print(pvar_dom_xpath_courtlistener_supreme_court_citations)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[3]/span[2]'))

        # [9] - XPATH tag: XPATH () | [courtlistener_supreme_court_database_id]
        print(pvar_dom_xpath_courtlistener_supreme_court_database_id)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a'))

        # [10] - XPATH tag: XPATH () | [courtlistener_supreme_court_database_id_url]
        print(pvar_dom_xpath_courtlistener_supreme_court_database_id_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href'))

        # [11] - XPATH tag: XPATH () | [courtlistener_supreme_court_author_name]
        print(pvar_dom_xpath_courtlistener_supreme_court_author_name)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a'))

        # [12] - XPATH tag: XPATH () | [courtlistener_supreme_court_author_name_url]
        print(pvar_dom_xpath_courtlistener_supreme_court_author_name_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a/@href'))

        # [13] - XPATH tag: XPATH () | [courtlistener_citations]
        print(pvar_dom_xpath_courtlistener_citations)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[3]/span[2]')[0].text.strip())

        # [14] - XPATH tag: XPATH () | [courtlistener_author_name]
        print(pvar_dom_xpath_courtlistener_author_name)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a')[0].text.strip())

        # [15] - XPATH tag: XPATH () | [courtlistener_author_name_url]
        print(pvar_dom_xpath_courtlistener_author_name_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a/@href'))

        # [16] - XPATH tag: XPATH () | [courtlistener_summary_count]
        print(pvar_dom_xpath_courtlistener_summary_count)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[2]/h3/span')[0].text.strip())

        # [17] - XPATH tag: XPATH () | [courtlistener_summary_url]
        print(pvar_dom_xpath_courtlistener_summary_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[2]/h4/a/@href'))

        # [18] - XPATH tag: XPATH () | [courtlistener_cited_by_count]
        print(pvar_dom_xpath_courtlistener_cited_by_count)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[3]/h3/span')[0].text.strip())

        # [19] - XPATH tag: XPATH () | [courtlistener_cited_by_1]
        print(pvar_dom_xpath_courtlistener_cited_by_1)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[1]/a')[0].text.strip())

        # [20] - XPATH tag: XPATH () | [courtlistener_cited_by_1_url]
        print(pvar_dom_xpath_courtlistener_cited_by_1_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[1]/a/@href'))

        # [21] - XPATH tag: XPATH () | [courtlistener_cited_by_2]
        print(pvar_dom_xpath_courtlistener_cited_by_2)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[2]/a')[0].text.strip())

        # [22] - XPATH tag: XPATH () | [courtlistener_cited_by_2_url]
        print(pvar_dom_xpath_courtlistener_cited_by_2_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[2]/a/@href'))

        # [23] - XPATH tag: XPATH () | [courtlistener_cited_by_3]
        print(pvar_dom_xpath_courtlistener_cited_by_3)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[3]/a')[0].text.strip())

        # [24] - XPATH tag: XPATH () | [courtlistener_cited_by_3_url]
        print(pvar_dom_xpath_courtlistener_cited_by_3_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[3]/a/@href'))

        # [25] - XPATH tag: XPATH () | [courtlistener_cited_by_4]
        print(pvar_dom_xpath_courtlistener_cited_by_4)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[4]/a')[0].text.strip())

        # [26] - XPATH tag: XPATH () | [courtlistener_cited_by_4_url]
        print(pvar_dom_xpath_courtlistener_cited_by_4_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[4]/a/@href'))

        # [27] - XPATH tag: XPATH () | [courtlistener_cited_by_5]
        print(pvar_dom_xpath_courtlistener_cited_by_5)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[5]/a')[0].text.strip())

        # [28] - XPATH tag: XPATH () | [courtlistener_cited_by_5_url]
        print(pvar_dom_xpath_courtlistener_cited_by_5_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[5]/a/@href'))

        # [29] - XPATH tag: XPATH () | [courtlistener_cited_by_url]
        print(pvar_dom_xpath_courtlistener_cited_by_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[3]/p[2]/a/@href'))

        # [30] - XPATH tag: XPATH () | [courtlistener_authorities_count]
        print(pvar_dom_xpath_courtlistener_authorities_count)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/h3/span')[0].text.strip())

        # [31] - XPATH tag: XPATH () | [courtlistener_authorities_1]
        print(pvar_dom_xpath_courtlistener_authorities_1)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[1]/a')[0].text.strip())

        # [32] - XPATH tag: XPATH () | [courtlistener_authorities_1_instances]
        print(pvar_dom_xpath_courtlistener_authorities_1_instances)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[1]/span')[0].text.strip())

        # [33] - XPATH tag: XPATH () | [courtlistener_authorities_1_url]
        print(pvar_dom_xpath_courtlistener_authorities_1_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[1]/a/@href'))

        # [34] - XPATH tag: XPATH () | [courtlistener_authorities_2]
        print(pvar_dom_xpath_courtlistener_authorities_2)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[2]/a')[0].text.strip())

        # [35] - XPATH tag: XPATH () | [courtlistener_authorities_2_instances]
        print(pvar_dom_xpath_courtlistener_authorities_2_instances)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[2]/span')[0].text.strip())

        # [36] - XPATH tag: XPATH () | [courtlistener_authorities_2_url]
        print(pvar_dom_xpath_courtlistener_authorities_2_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[2]/a/@href'))

        # [37] - XPATH tag: XPATH () | [courtlistener_authorities_3]
        print(pvar_dom_xpath_courtlistener_authorities_3)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[3]/a')[0].text.strip())

        # [38] - XPATH tag: XPATH () | [courtlistener_authorities_3_instances]
        print(pvar_dom_xpath_courtlistener_authorities_3_instances)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[3]/span')[0].text.strip())

        # [39] - XPATH tag: XPATH () | [courtlistener_authorities_3_url]
        print(pvar_dom_xpath_courtlistener_authorities_3_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[3]/a/@href'))

        # [40] - XPATH tag: XPATH () | [courtlistener_authorities_4]
        print(pvar_dom_xpath_courtlistener_authorities_4)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[4]/a')[0].text.strip())

        # [41] - XPATH tag: XPATH () | [courtlistener_authorities_4_instances]
        print(pvar_dom_xpath_courtlistener_authorities_4_instances)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[4]/span')[0].text.strip())

        # [42] - XPATH tag: XPATH () | [courtlistener_authorities_4_url]
        print(pvar_dom_xpath_courtlistener_authorities_4_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[4]/a/@href'))

        # [43] - XPATH tag: XPATH () | [courtlistener_authorities_5]
        print(pvar_dom_xpath_courtlistener_authorities_5)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[5]/a')[0].text.strip())

        # [44] - XPATH tag: XPATH () | [courtlistener_authorities_5_instances]
        print(pvar_dom_xpath_courtlistener_authorities_5_instances)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[5]/span')[0].text.strip())

        # [45] - XPATH tag: XPATH () | [courtlistener_authorities_5_url]
        print(pvar_dom_xpath_courtlistener_authorities_5_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/ul/li[5]/a/@href'))

        # [46] - XPATH tag: XPATH () | [courtlistener_authorities_url]
        print(pvar_dom_xpath_courtlistener_authorities_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[4]/h4/a/@href'))

        # [47] - XPATH tag: XPATH () | [courtlistener_similiar_decision_1]
        print(pvar_dom_xpath_courtlistener_similiar_decision_1)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[1]/a')[0].text.strip())

        # [48] - XPATH tag: XPATH () | [courtlistener_similiar_decision_1_url]
        print(pvar_dom_xpath_courtlistener_similiar_decision_1_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[1]/a/@href'))

        # [49] - XPATH tag: XPATH () | [courtlistener_similiar_decision_2]
        print(pvar_dom_xpath_courtlistener_similiar_decision_2)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[2]/a')[0].text.strip())

        # [50] - XPATH tag: XPATH () | [courtlistener_similiar_decision_2_url]
        print(pvar_dom_xpath_courtlistener_similiar_decision_2_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[2]/a/@href'))

        # [51] - XPATH tag: XPATH () | [courtlistener_similiar_decision_3]
        print(pvar_dom_xpath_courtlistener_similiar_decision_3)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[3]/a')[0].text.strip())

        # [52] - XPATH tag: XPATH () | [courtlistener_similiar_decision_3_url]
        print(pvar_dom_xpath_courtlistener_similiar_decision_3_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[3]/a/@href'))

        # [53] - XPATH tag: XPATH () | [courtlistener_similiar_decision_4]
        print(pvar_dom_xpath_courtlistener_similiar_decision_4)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[4]/a')[0].text.strip())

        # [54] - XPATH tag: XPATH () | [courtlistener_similiar_decision_4_url]
        print(pvar_dom_xpath_courtlistener_similiar_decision_4_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[4]/a/@href'))

        # [55] - XPATH tag: XPATH () | [courtlistener_similiar_decision_5]
        print(pvar_dom_xpath_courtlistener_similiar_decision_5)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[5]/a')[0].text.strip())

        # [56] - XPATH tag: XPATH () | [courtlistener_similiar_decision_5_url]
        print(pvar_dom_xpath_courtlistener_similiar_decision_5_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[5]/ul/li[5]/a/@href'))

        # [57] - XPATH tag: XPATH () | [courtlistener_similiar_decision_url]
        print(pvar_dom_xpath_courtlistener_similiar_decisions_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[5]/p[2]/a/@href'))

        # [58] - XPATH tag: XPATH () | [courtlistener_supreme_court_author_flag]
        print(pvar_dom_xpath_courtlistener_supreme_court_author_flag)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[6]/span[2]/a')[0].text.strip())

        # [59] - XPATH tag: XPATH () | [courtlistener_old_author_flag]
        print(pvar_dom_xpath_courtlistener_old_author_flag)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]')[0].text.strip())

        # [60] - XPATH tag: XPATH () | [courtlistener_new_author_flag]
        print(pvar_dom_xpath_courtlistener_new_author_flag)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/span[2]/a')[0].text.strip())

        # [61] - XPATH tag: XPATH () | [courtlistener_panel]
        print(pvar_dom_xpath_courtlistener_panel)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/a[1]')[0].text.strip())

        # [62] - XPATH tag: XPATH () | [courtlistener_panel_url]
        print(pvar_dom_xpath_courtlistener_panel_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/a[1]/@href'))

        # [63] - XPATH tag: XPATH () | [courtlistener_panel_flag]
        print(pvar_dom_xpath_courtlistener_panel_flag)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/p[5]/a[1]')[0].text.strip())

        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Chain Printing Python Variables for Payload INJECTION to MariaDB Successful!]")

        # Chain Re-Assign

        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Chain Re-Assigning Python Variables for Payload INJECTION to MariaDB]...")
        #bs4_xpath_courtlistener_case_name = pvar_dom_xpath_courtlistener_case_name
        # Added to remedy XPATH overwriting good BS4 Values with Incomplete Data [courtlistener_case_name] "Dred Scott" (XPATH) vs. "Dred Scott v. Sandford, 60 U.S. 393" (BS4)

        # [1] - XPATH tag: h2 | [courtlistener_case_name] (Only BS4 Pulls Full courtlistener_case_name)
        bs4_courtlistener_case_name = pvar_bs4_tag_courtlistener_case_name
        # [2] - XPATH tag: h3 | [courtlistener_jurisdiction]
        lxml_xpath_courtlistener_jurisdiction = pvar_dom_xpath_courtlistener_jurisdiction
        # [3] - XPATH tag: XPATH () | [courtlistener_filed]
        lxml_xpath_courtlistener_filed = pvar_dom_xpath_courtlistener_filed
        # [4] - XPATH tag: XPATH () | [courtlistener_precedential_status]
        lxml_xpath_courtlistener_precedential_status = pvar_dom_xpath_courtlistener_precedential_status
        # [5] - XPATH tag: XPATH () | [courtlistener_docket_number]
        lxml_xpath_courtlistener_docket_number = pvar_dom_xpath_courtlistener_docket_number
        # [6] - XPATH tag: XPATH () | [courtlistener_pdf_opinion_url_storage]
        lxml_xpath_courtlistener_pdf_opinion_url_storage = pvar_dom_xpath_courtlistener_pdf_opinion_url_storage
        # [7] - XPATH tag: XPATH () | [courtlistener_pdf_opinion_url_gov]
        lxml_xpath_courtlistener_pdf_opinion_url_gov = pvar_dom_xpath_courtlistener_pdf_opinion_url_gov
        # [8] - XPATH tag: XPATH () | [courtlistener_citations]
        lxml_xpath_courtlistener_supreme_court_citations = pvar_dom_xpath_courtlistener_supreme_court_citations
        # [9] - XPATH tag: XPATH () | [courtlistener_supreme_court_db_id]
        lxml_xpath_courtlistener_supreme_court_database_id = pvar_dom_xpath_courtlistener_supreme_court_database_id
        # [10] - XPATH tag: XPATH () | [courtlistener_supreme_court_db_id_url]
        lxml_xpath_courtlistener_supreme_court_database_id_url = pvar_dom_xpath_courtlistener_supreme_court_database_id_url
        # [11] - XPATH tag: XPATH () | [courtlistener_supreme_court_author_name]
        lxml_xpath_courtlistener_supreme_court_author_name = pvar_dom_xpath_courtlistener_supreme_court_author_name
        # [12] - XPATH tag: XPATH () | [courtlistener_supreme_court_author_name_url]
        lxml_xpath_courtlistener_supreme_court_author_name_url = pvar_dom_xpath_courtlistener_supreme_court_author_name_url
        # [13] - XPATH tag: XPATH () | [courtlistener_citations]
        lxml_xpath_courtlistener_citations = pvar_dom_xpath_courtlistener_citations
        # [14] - XPATH tag: XPATH () | [courtlistener_author_name]
        lxml_xpath_courtlistener_author_name = pvar_dom_xpath_courtlistener_author_name
        # [15] - XPATH tag: XPATH () | [courtlistener_author_name_url]
        lxml_xpath_courtlistener_author_name_url = pvar_dom_xpath_courtlistener_author_name_url
        # [16] - XPATH tag: XPATH () | [courtlistener_summary_count]
        lxml_xpath_courtlistener_summary_count = pvar_dom_xpath_courtlistener_summary_count
        # [17] - XPATH tag: XPATH () | [courtlistener_summary_url]
        lxml_xpath_courtlistener_summary_url = pvar_dom_xpath_courtlistener_summary_url
        # [18] - XPATH tag: XPATH () | [courtlistener_cited_by_count]
        lxml_xpath_courtlistener_cited_by_count = pvar_dom_xpath_courtlistener_cited_by_count
        # [19] - XPATH tag: XPATH () | [courtlistener_cited_by_1]
        lxml_xpath_courtlistener_cited_by_1 = pvar_dom_xpath_courtlistener_cited_by_1
        # [20] - XPATH tag: XPATH () | [courtlistener_cited_by_1_url]
        lxml_xpath_courtlistener_cited_by_1_url = pvar_dom_xpath_courtlistener_cited_by_1_url
        # [21] - XPATH tag: XPATH () | [courtlistener_cited_by_2]
        lxml_xpath_courtlistener_cited_by_2 = pvar_dom_xpath_courtlistener_cited_by_2
        # [22] - XPATH tag: XPATH () | [courtlistener_cited_by_2_url]
        lxml_xpath_courtlistener_cited_by_2_url = pvar_dom_xpath_courtlistener_cited_by_2_url 
        # [23] - XPATH tag: XPATH () | [courtlistener_cited_by_3]
        lxml_xpath_courtlistener_cited_by_3 = pvar_dom_xpath_courtlistener_cited_by_3
        # [24] - XPATH tag: XPATH () | [courtlistener_cited_by_3_url]
        lxml_xpath_courtlistener_cited_by_3_url = pvar_dom_xpath_courtlistener_cited_by_3_url
        # [25] - XPATH tag: XPATH () | [courtlistener_cited_by_4]
        lxml_xpath_courtlistener_cited_by_4 = pvar_dom_xpath_courtlistener_cited_by_4
        # [26] - XPATH tag: XPATH () | [courtlistener_cited_by_4_url]
        lxml_xpath_courtlistener_cited_by_4_url = pvar_dom_xpath_courtlistener_cited_by_4_url
        # [27] - XPATH tag: XPATH () | [courtlistener_cited_by_5]
        lxml_xpath_courtlistener_cited_by_5 = pvar_dom_xpath_courtlistener_cited_by_5
        # [28] - XPATH tag: XPATH () | [courtlistener_cited_by_5_url]
        lxml_xpath_courtlistener_cited_by_5_url = pvar_dom_xpath_courtlistener_cited_by_5_url
        # [29] - XPATH tag: XPATH () | [courtlistener_cited_by_url]
        lxml_xpath_courtlistener_cited_by_url = pvar_dom_xpath_courtlistener_cited_by_url
        # [30] - XPATH tag: XPATH () | [courtlistener_authorities_count]
        lxml_xpath_courtlistener_authorities_count = pvar_dom_xpath_courtlistener_authorities_count
        # [31] - XPATH tag: XPATH () | [courtlistener_authorities_1]
        lxml_xpath_courtlistener_authorities_1 = pvar_dom_xpath_courtlistener_authorities_1
        # [32] - XPATH tag: XPATH () | [courtlistener_authorities_1_instances]
        lxml_xpath_courtlistener_authorities_1_instances = pvar_dom_xpath_courtlistener_authorities_1_instances
        # [33] - XPATH tag: XPATH () | [courtlistener_authorities_1_url]
        lxml_xpath_courtlistener_authorities_1_url = pvar_dom_xpath_courtlistener_authorities_1_url
        # [34] - XPATH tag: XPATH () | [courtlistener_authorities_2]
        lxml_xpath_courtlistener_authorities_2 = pvar_dom_xpath_courtlistener_authorities_2
        # [35] - XPATH tag: XPATH () | [courtlistener_authorities_2_instances]
        lxml_xpath_courtlistener_authorities_2_instances = pvar_dom_xpath_courtlistener_authorities_2_instances
        # [36] - XPATH tag: XPATH () | [courtlistener_authorities_2_url]
        lxml_xpath_courtlistener_authorities_2_url = pvar_dom_xpath_courtlistener_authorities_2_url
        # [37] - XPATH tag: XPATH () | [courtlistener_authorities_3]
        lxml_xpath_courtlistener_authorities_3 = pvar_dom_xpath_courtlistener_authorities_3
        # [38] - XPATH tag: XPATH () | [courtlistener_authorities_3_instances]
        lxml_xpath_courtlistener_authorities_3_instances = pvar_dom_xpath_courtlistener_authorities_3_instances
        # [39] - XPATH tag: XPATH () | [courtlistener_authorities_3_url]
        lxml_xpath_courtlistener_authorities_3_url = pvar_dom_xpath_courtlistener_authorities_3_url
        # [40] - XPATH tag: XPATH () | [courtlistener_authorities_4]
        lxml_xpath_courtlistener_authorities_4 = pvar_dom_xpath_courtlistener_authorities_4
        # [41] - XPATH tag: XPATH () | [courtlistener_authorities_4_instances]
        lxml_xpath_courtlistener_authorities_4_instances = pvar_dom_xpath_courtlistener_authorities_4_instances
        # [42] - XPATH tag: XPATH () | [courtlistener_authorities_4_url] 
        lxml_xpath_courtlistener_authorities_4_url = pvar_dom_xpath_courtlistener_authorities_4_url
        # [43] - XPATH tag: XPATH () | [courtlistener_authorities_5]
        lxml_xpath_courtlistener_authorities_5 = pvar_dom_xpath_courtlistener_authorities_5
        # [44] - XPATH tag: XPATH () | [courtlistener_authorities_5_instances]
        lxml_xpath_courtlistener_authorities_5_instances = pvar_dom_xpath_courtlistener_authorities_5_instances
        # [45] - XPATH tag: XPATH () | [courtlistener_authorities_5_url] 
        lxml_xpath_courtlistener_authorities_5_url = pvar_dom_xpath_courtlistener_authorities_5_url
        # [46] - XPATH tag: XPATH () | [courtlistener_authorities_url]
        lxml_xpath_courtlistener_authorities_url = pvar_dom_xpath_courtlistener_authorities_url
        # [47] - XPATH tag: XPATH () | [courtlistener_similiar_decision_1]
        lxml_xpath_courtlistener_similiar_decision_1 = pvar_dom_xpath_courtlistener_similiar_decision_1
        # [48] - XPATH tag: XPATH () | [courtlistener_similiar_decision_1_url]
        lxml_xpath_courtlistener_similiar_decision_1_url = pvar_dom_xpath_courtlistener_similiar_decision_1_url
        # [49] - XPATH tag: XPATH () | [courtlistener_similiar_decision_2]
        lxml_xpath_courtlistener_similiar_decision_2 = pvar_dom_xpath_courtlistener_similiar_decision_2
        # [50] - XPATH tag: XPATH () | [courtlistener_similiar_decision_2_url]
        lxml_xpath_courtlistener_similiar_decision_2_url = pvar_dom_xpath_courtlistener_similiar_decision_2_url
        # [51] - XPATH tag: XPATH () | [courtlistener_similiar_decision_3]
        lxml_xpath_courtlistener_similiar_decision_3 = pvar_dom_xpath_courtlistener_similiar_decision_3
        # [52] - XPATH tag: XPATH () | [courtlistener_similiar_decision_3_url]
        lxml_xpath_courtlistener_similiar_decision_3_url = pvar_dom_xpath_courtlistener_similiar_decision_3_url
        # [53] - XPATH tag: XPATH () | [courtlistener_similiar_decision_4]
        lxml_xpath_courtlistener_similiar_decision_4 = pvar_dom_xpath_courtlistener_similiar_decision_4
        # [54] - XPATH tag: XPATH () | [courtlistener_similiar_decision_4_url]
        lxml_xpath_courtlistener_similiar_decision_4_url = pvar_dom_xpath_courtlistener_similiar_decision_4_url
        # [55] - XPATH tag: XPATH () | [courtlistener_similiar_decision_5]
        lxml_xpath_courtlistener_similiar_decision_5 = pvar_dom_xpath_courtlistener_similiar_decision_5
        # [56] - XPATH tag: XPATH () | [courtlistener_similiar_decision_5_url]
        lxml_xpath_courtlistener_similiar_decision_5_url = pvar_dom_xpath_courtlistener_similiar_decision_5_url
        # [57] - XPATH tag: XPATH () | [courtlistener_similiar_decision_url]
        lxml_xpath_courtlistener_similiar_decision_url = pvar_dom_xpath_courtlistener_similiar_decisions_url
        # [58] - XPATH tag: XPATH () | [courtlistener_supreme_court_author_flag]
        lxml_xpath_courtlistener_supreme_court_author_flag = pvar_dom_xpath_courtlistener_supreme_court_author_flag
        # [59] - XPATH tag: XPATH () | [courtlistener_old_author_flag]
        lxml_xpath_courtlistener_old_author_flag = pvar_dom_xpath_courtlistener_old_author_flag
        # [60] - XPATH tag: XPATH () | [courtlistener_new_author_flag]
        lxml_xpath_courtlistener_new_author_flag = pvar_dom_xpath_courtlistener_new_author_flag
        # [61] - XPATH tag: XPATH () | [courtlistener_panel]
        lxml_xpath_courtlistener_panel = pvar_dom_xpath_courtlistener_panel
        # [62] - XPATH tag: XPATH () | [courtlistener_panel_url]
        lxml_xpath_courtlistener_panel_url = pvar_dom_xpath_courtlistener_panel_url
        # [63] - XPATH tag: XPATH () | [courtlistener_panel_flag]
        lxml_xpath_courtlistener_panel_flag = pvar_dom_xpath_courtlistener_panel_flag

        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Chain Re-Assigning Python Variables for Payload INJECTION to MariaDB Successful!]")

        # Table 4 MariaDB Payload (RemoteServer Data Recovery)

        #global courtlistener_jurisdiction_dataset
        
        print(f"{courtlistener_jurisdiction_dataset} Decision Payload...")

        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting XPATH Python Variable Payload to MariaDB...")

        import pymysql
        import pymysql.cursors
        connection = pymysql.connect(host=f'{dragon_breath_f10_pymysql_hostname}',
          user=f"{dragon_breath_f10_pymysql_username}",
          passwd=f"{dragon_breath_f10_pymysql_password}",
          db=f"{dragon_breath_f10_pymysql_database_name}"
        )

#        import pymysql
#        import pymysql.cursors
#        connection = pymysql.connect(host='localhost',
#          user="brandon",
#          passwd="",
#          db="FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead"
#        )
        print("Dragon Breath [F.10] - [Table 04/10] - PyMySQL Connected Successfully!")

        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer` (`courtlistener_case_name`,`courtlistener_jurisdiction`, `courtlistener_filed`, `courtlistener_precedential_status`, `courtlistener_docket_number`, `courtlistener_pdf_opinion_url_storage`, `courtlistener_pdf_opinion_url_gov`, `courtlistener_supreme_court_citations`, `courtlistener_supreme_court_author_name`, `courtlistener_supreme_court_author_name_url`, `courtlistener_supreme_court_database_id`, `courtlistener_supreme_court_database_id_url`, `courtlistener_citations`, `courtlistener_author_name`, `courtlistener_author_name_url`, `courtlistener_summary_count`, `courtlistener_summary_url`, `courtlistener_cited_by_count`, `courtlistener_cited_by_1`, `courtlistener_cited_by_1_url`, `courtlistener_cited_by_2`, `courtlistener_cited_by_2_url`, `courtlistener_cited_by_3`, `courtlistener_cited_by_3_url`, `courtlistener_cited_by_4`, `courtlistener_cited_by_4_url`, `courtlistener_cited_by_5`, `courtlistener_cited_by_5_url`, `courtlistener_cited_by_url`, `courtlistener_authorities_count`, `courtlistener_authorities_1`, `courtlistener_authorities_1_instances`, `courtlistener_authorities_1_url`, `courtlistener_authorities_2`, `courtlistener_authorities_2_instances`, `courtlistener_authorities_2_url`, `courtlistener_authorities_3`, `courtlistener_authorities_3_instances`, `courtlistener_authorities_3_url`, `courtlistener_authorities_4`, `courtlistener_authorities_4_instances`, `courtlistener_authorities_4_url`, `courtlistener_authorities_5`, `courtlistener_authorities_5_instances`, `courtlistener_authorities_5_url`, `courtlistener_authorities_url`, `courtlistener_similiar_decision_1`, `courtlistener_similiar_decision_1_url`, `courtlistener_similiar_decision_2`, `courtlistener_similiar_decision_2_url`, `courtlistener_similiar_decision_3`, `courtlistener_similiar_decision_3_url`, `courtlistener_similiar_decision_4`, `courtlistener_similiar_decision_4_url`, `courtlistener_similiar_decision_5`, `courtlistener_similiar_decision_5_url`, `courtlistener_similiar_decisions_url`, `courtlistener_supreme_court_author_flag`, `courtlistener_old_author_flag`, `courtlistener_new_author_flag`, `courtlistener_panel`, `courtlistener_panel_url`, `courtlistener_panel_flag`, `courtlistener_opinion_current_html`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (bs4_courtlistener_case_name, lxml_xpath_courtlistener_jurisdiction, lxml_xpath_courtlistener_filed, lxml_xpath_courtlistener_precedential_status, lxml_xpath_courtlistener_docket_number, lxml_xpath_courtlistener_pdf_opinion_url_storage, lxml_xpath_courtlistener_pdf_opinion_url_gov, lxml_xpath_courtlistener_supreme_court_citations, lxml_xpath_courtlistener_supreme_court_database_id, lxml_xpath_courtlistener_supreme_court_database_id_url, lxml_xpath_courtlistener_supreme_court_author_name, lxml_xpath_courtlistener_supreme_court_author_name_url, lxml_xpath_courtlistener_citations, lxml_xpath_courtlistener_author_name, lxml_xpath_courtlistener_author_name_url, lxml_xpath_courtlistener_summary_count, lxml_xpath_courtlistener_summary_url, lxml_xpath_courtlistener_cited_by_count, lxml_xpath_courtlistener_cited_by_1, lxml_xpath_courtlistener_cited_by_1_url, lxml_xpath_courtlistener_cited_by_2, lxml_xpath_courtlistener_cited_by_2_url, lxml_xpath_courtlistener_cited_by_3, lxml_xpath_courtlistener_cited_by_3_url, lxml_xpath_courtlistener_cited_by_4, lxml_xpath_courtlistener_cited_by_4_url, lxml_xpath_courtlistener_cited_by_5, lxml_xpath_courtlistener_cited_by_5_url, lxml_xpath_courtlistener_cited_by_url, lxml_xpath_courtlistener_authorities_count, lxml_xpath_courtlistener_authorities_1, lxml_xpath_courtlistener_authorities_1_instances, lxml_xpath_courtlistener_authorities_1_url, lxml_xpath_courtlistener_authorities_2, lxml_xpath_courtlistener_authorities_2_instances, lxml_xpath_courtlistener_authorities_2_url, lxml_xpath_courtlistener_authorities_3, lxml_xpath_courtlistener_authorities_3_instances, lxml_xpath_courtlistener_authorities_3_url, lxml_xpath_courtlistener_authorities_4, lxml_xpath_courtlistener_authorities_4_instances, lxml_xpath_courtlistener_authorities_4_url, lxml_xpath_courtlistener_authorities_5, lxml_xpath_courtlistener_authorities_5_instances, lxml_xpath_courtlistener_authorities_5_url, lxml_xpath_courtlistener_authorities_url, lxml_xpath_courtlistener_similiar_decision_1, lxml_xpath_courtlistener_similiar_decision_1_url, lxml_xpath_courtlistener_similiar_decision_2, lxml_xpath_courtlistener_similiar_decision_2_url, lxml_xpath_courtlistener_similiar_decision_3, lxml_xpath_courtlistener_similiar_decision_3_url, lxml_xpath_courtlistener_similiar_decision_4, lxml_xpath_courtlistener_similiar_decision_4_url, lxml_xpath_courtlistener_similiar_decision_5, lxml_xpath_courtlistener_similiar_decision_5_url, lxml_xpath_courtlistener_similiar_decision_url, lxml_xpath_courtlistener_supreme_court_author_flag, lxml_xpath_courtlistener_old_author_flag, lxml_xpath_courtlistener_new_author_flag, lxml_xpath_courtlistener_panel, lxml_xpath_courtlistener_panel_url, lxml_xpath_courtlistener_panel_flag, Table04_Opinion_current_html))
                connection.commit()

        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Injecting XPATH Python Variable Payload to MariaDB Successful!")

        print(f"Dragon Breath [F.10] - [Table 04/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished!")

def Table05_People_SCOTUS(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    # DATASET: SCOTUS)
    # Code [02/10]: [Read from Table: Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer]
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
#    global pvar_value_absolute_url
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: sql_full_url_insert...")
#    global sql_full_url_insert
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_courtlistener_absolute_url_trimmed_1_leading...")
#    global pvar_courtlistener_absolute_url_trimmed_1_leading
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Table01_File] -> [Table02_RemoteURLGen] Executing...")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing all Requried Python3 Module Libraries...")

    import pymysql
    import pymysql.cursors

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")

    # Extract Data

    import mysql.connector
    try:
        connection = mysql.connector.connect(host=f'{dragon_breath_f10_mysql_connector_hostname}',
                                             database=f'{dragon_breath_f10_mysql_connector_database_name}',
                                             user=f'{dragon_breath_f10_mysql_connector_username}',
                                             password=f'{dragon_breath_f10_mysql_connector_password}')

#    import mysql.connector
#    try:
#        connection = mysql.connector.connect(host='localhost',
#                                             database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                             user='brandon',
#                                             password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__')

        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Database Connection Successful! Now Quering Courtlistener 'Person' URL for current JSON")
#        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer"
#        SELECT * FROM Table ORDER BY ID DESC LIMIT 1
        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer order by id desc limit 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("courtlistener_person_scotus_absolute_url = ", row[10], )
            with open(f"{courtlistener_jurisdiction_dataset}extracted_person_scotus_absolute_urls.txt", "w", encoding="utf-8") as f:
#            with open("extracted_person_scotus_absolute_urls.txt", "w", encoding="utf-8") as f:
                print(row[10], file=f)

    except mysql.connector.Error as e:
        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - MySQL connection is closed")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Creating new /person/ courtlistener.com URL...")

    # Source: irc.libera.chat #python - jinsun__
    # Date: 03/12/2022 @ Approx. 21:03
    # Dpaste: https://dpaste.com/D83JVVE2K
    global sql_full_url_insert_person_scotus
    global person_scotus_urlpart2
    global pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading
    from urllib.parse import urljoin
    with open(f"{courtlistener_jurisdiction_dataset}extracted_person_scotus_absolute_urls.txt", "r", encoding="utf-8") as f:
#    with open("extracted_person_scotus_absolute_urls.txt", "r", encoding="utf-8") as f:
        person_scotus_urlpart2 = f.read().strip()
    #person_urlpart2_trail_trimmed = person_urlpart2[:1]
    #person_urlpart2 = person_urlpart2_trail_trimmed
    person_scotus_url_part_1 = "https://www.courtlistener.com"

    person_scotus_url_join = (urljoin(person_scotus_url_part_1,
                  person_scotus_urlpart2))
    #print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - /person courtlistener.com absolute URL is:")
    #print(person_urlpart2)
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - New /person/ courtlistener.com URL is:")
    print(person_scotus_url_join)
    #exit()
    pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading = person_scotus_urlpart2
    #pvar_courtlistener_person_absolute_url_trimmed_1_leading = person_urlpart2[1:]
    print(pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading)

    #pvar_courtlistener_absolute_url_trimmed_1_leading = pvar_value_absolute_url[1:]
    #print(pvar_courtlistener_absolute_url_trimmed_1_leading) 

    # Copy Columns & INSERT url_join to new Table + Column
    # Copy Columns from Table: Current_JSON_CL_Dataset_Exodus_Table1_File

    # New Table: Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2
    # New Column: courtlistener_full_absolute_url
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL into Table05_RemoteURLGen2...")
    sql_full_url_insert_person_scotus = person_scotus_url_join

#    import pymysql.cursors
    # Connect to the database
#    connection = pymysql.connect(host='localhost',
#                                 user='brandon',
#                                 password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__',
#                                 database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                 cursorclass=pymysql.cursors.DictCursor)
#    try:
#        with connection.cursor() as cursor:
#                sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2` (`courtlistener_full_supreme_court_person_absolute_url`, `courtlistener_supreme_court_person_absolute_url`, `courtlistener_supreme_court_person_absolute_url_leading_trim`)  VALUES (%s, %s, %s)"
#                cursor.execute(sql, (sql_full_url_insert_person_scotus, person_scotus_urlpart2, pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading))
#        connection.commit()
#    finally:
#        connection.close()
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

    # JSON Filename & Full Filename -> Python Vars -> MariaDB
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished!")


def Table05_People(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    # DATASET: NON-SCOTUS)
    # Code [02/10]: [Read from Table: Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer]
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
#    global pvar_value_absolute_url
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: sql_full_url_insert...")
#    global sql_full_url_insert
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_courtlistener_absolute_url_trimmed_1_leading...")
#    global pvar_courtlistener_absolute_url_trimmed_1_leading
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Table01_File] -> [Table02_RemoteURLGen] Executing...")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing all Requried Python3 Module Libraries...")

    import pymysql
    import pymysql.cursors

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")

    # Extract Data

    import mysql.connector
    try:
        connection = mysql.connector.connect(host=f'{dragon_breath_f10_mysql_connector_hostname}',
                                             database=f'{dragon_breath_f10_mysql_connector_database_name}',
                                             user=f'{dragon_breath_f10_mysql_connector_username}',
                                             password=f'{dragon_breath_f10_mysql_connector_password}')

#    import mysql.connector
#    try:
#        connection = mysql.connector.connect(host='localhost',
#                                             database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                             user='brandon',
#                                             password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__')

        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Database Connection Successful! Now Quering Courtlistener 'Person' URL for current JSON")
#        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer"
#        SELECT * FROM Table ORDER BY ID DESC LIMIT 1
        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer order by id desc limit 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("courtlistener_person_absolute_url = ", row[15], )
            with open(f"{courtlistener_jurisdiction_dataset}extracted_person_absolute_urls.txt", "w", encoding="utf-8") as f:    
#            with open("extracted_person_absolute_urls.txt", "w", encoding="utf-8") as f:
                print(row[15], file=f)

    except mysql.connector.Error as e:
        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - MySQL connection is closed")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Creating new courtlistener.com URL...")

    # Source: irc.libera.chat #python - jinsun__
    # Date: 03/12/2022 @ Approx. 21:03
    # Dpaste: https://dpaste.com/D83JVVE2K
    global sql_full_url_insert_person
    global person_urlpart2
    global pvar_courtlistener_person_absolute_url_trimmed_1_leading
    from urllib.parse import urljoin
    with open(f"{courtlistener_jurisdiction_dataset}extracted_person_absolute_urls.txt", "r", encoding="utf-8") as f:
#    with open("extracted_person_absolute_urls.txt", "r", encoding="utf-8") as f:
#        person_urlpart2 = f.read()
        person_urlpart2 = f.read().strip()
    #person_urlpart2_trail_trimmed = person_urlpart2[:1]
    #person_urlpart2 = person_urlpart2_trail_trimmed    
    person_url_part_1 = "https://www.courtlistener.com"

    person_url_join = (urljoin(person_url_part_1,
                  person_urlpart2))
    #print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - /person courtlistener.com absolute URL is:")
    #print(person_urlpart2)
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - New /person courtlistener.com URL is:")
    print(person_url_join)
    #exit()
    pvar_courtlistener_person_absolute_url_trimmed_1_leading = person_urlpart2
    #pvar_courtlistener_person_absolute_url_trimmed_1_leading = person_urlpart2[1:]
    print(pvar_courtlistener_person_absolute_url_trimmed_1_leading)

    #pvar_courtlistener_absolute_url_trimmed_1_leading = pvar_value_absolute_url[1:]
    #print(pvar_courtlistener_absolute_url_trimmed_1_leading) 

    # Copy Columns & INSERT url_join to new Table + Column
    # Copy Columns from Table: Current_JSON_CL_Dataset_Exodus_Table1_File

    # New Table: Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2
    # New Column: courtlistener_full_absolute_url
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting /person courtlistener.com URL into Table05_RemoteURLGen2...")
    sql_full_url_insert_person = person_url_join

#    import pymysql.cursors
    # Connect to the database
#    connection = pymysql.connect(host='localhost',
#                                 user='brandon',
#                                 password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__',
#                                 database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                 cursorclass=pymysql.cursors.DictCursor)
#    try:
#        with connection.cursor() as cursor:
#                sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2` (`courtlistener_full_person_absolute_url`, `courtlistener_person_absolute_url`, `courtlistener_person_absolute_url_leading_trim`)  VALUES (%s, %s, %s)"
#                cursor.execute(sql, (sql_full_url_insert_person, person_urlpart2, pvar_courtlistener_person_absolute_url_trimmed_1_leading))
#        connection.commit()
#    finally:
#        connection.close()
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

    # JSON Filename & Full Filename -> Python Vars -> MariaDB
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished!")

def Table05_Summaries_SCOTUS(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    # DATASET: SCOTUS [Summaries])
    # Code [02/10]: [Read from Table: Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer]
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
#    global pvar_value_absolute_url
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: sql_full_url_insert...")
#    global sql_full_url_insert
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_courtlistener_absolute_url_trimmed_1_leading...")
#    global pvar_courtlistener_absolute_url_trimmed_1_leading
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Table01_File] -> [Table02_RemoteURLGen] Executing...")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing all Requried Python3 Module Libraries...")

    import pymysql
    import pymysql.cursors

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")

    # Extract Data

    import mysql.connector
    try:
        connection = mysql.connector.connect(host=f'{dragon_breath_f10_mysql_connector_hostname}',
                                             database=f'{dragon_breath_f10_mysql_connector_database_name}',
                                             user=f'{dragon_breath_f10_mysql_connector_username}',
                                             password=f'{dragon_breath_f10_mysql_connector_password}')

#    import mysql.connector
#    try:
#        connection = mysql.connector.connect(host='localhost',
#                                             database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                             user='brandon',
#                                             password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__')

        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Database Connection Successful! Now Quering Courtlistener 'Summary' URL for current JSON")
#        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer"
#        SELECT * FROM Table ORDER BY ID DESC LIMIT 1
        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer order by id desc limit 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("courtlistener_summary_scotus_absolute_url = ", row[17], )
            with open(f"{courtlistener_jurisdiction_dataset}extracted_summary_scotus_absolute_urls.txt", "w", encoding="utf-8") as f:
#            with open("extracted_summary_scotus_absolute_urls.txt", "w", encoding="utf-8") as f:
                print(row[17], file=f)

    except mysql.connector.Error as e:
        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summaries] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - MySQL connection is closed")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Creating new /summaries/ courtlistener.com URL...")

    # Source: irc.libera.chat #python - jinsun__
    # Date: 03/12/2022 @ Approx. 21:03
    # Dpaste: https://dpaste.com/D83JVVE2K
    global sql_full_url_insert_summary_scotus
    global summary_scotus_urlpart2
    global pvar_courtlistener_summary_scotus_absolute_url_trimmed_1_leading
    from urllib.parse import urljoin
    with open(f"{courtlistener_jurisdiction_dataset}extracted_summary_scotus_absolute_urls.txt", "r", encoding="utf-8") as f:
#    with open("extracted_summary_scotus_absolute_urls.txt", "r", encoding="utf-8") as f:
        summary_scotus_urlpart2 = f.read().strip()
    summary_scotus_url_part_1 = "https://www.courtlistener.com"

    summary_scotus_url_join = (urljoin(summary_scotus_url_part_1,
                  summary_scotus_urlpart2))
    #print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - /opinion/xxxxxx/x-v-x/summaries/? courtlistener.com absolute URL is:")
    #print(person_urlpart2)
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - New /summaries/ courtlistener.com URL is:")
    print(summary_scotus_url_join)
    #exit()
    pvar_courtlistener_summary_scotus_absolute_url_trimmed_1_leading = summary_scotus_urlpart2[1:]
    print(pvar_courtlistener_summary_scotus_absolute_url_trimmed_1_leading)

    #pvar_courtlistener_absolute_url_trimmed_1_leading = pvar_value_absolute_url[1:]
    #print(pvar_courtlistener_absolute_url_trimmed_1_leading) 

    # Copy Columns & INSERT url_join to new Table + Column
    # Copy Columns from Table: Current_JSON_CL_Dataset_Exodus_Table1_File

    # New Table: Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2
    # New Column: courtlistener_full_absolute_url
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL into Table05_RemoteURLGen2...")
    sql_full_url_insert_summary_scotus = summary_scotus_url_join

#    import pymysql.cursors
    # Connect to the database
#    connection = pymysql.connect(host='localhost',
#                                 user='brandon',
#                                 password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__',
#                                 database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                 cursorclass=pymysql.cursors.DictCursor)
#    try:
#        with connection.cursor() as cursor:
#                sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2` (`courtlistener_full_summaries_absolute_url`, `courtlistener_summaries_absolute_url`, `courtlistener_summaries_absolute_url_leading_trim`)  VALUES (%s, %s, %s)"
#                cursor.execute(sql, (sql_full_url_insert_summary_scotus, summary_scotus_urlpart2, pvar_courtlistener_summary_scotus_absolute_url_trimmed_1_leading))
#        connection.commit()
#    finally:
#        connection.close()
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

    # JSON Filename & Full Filename -> Python Vars -> MariaDB
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished!")

def Table05_Summaries(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    # DATASET: NON-SCOTUS: [Summaries])
    # Code [02/10]: [Read from Table: Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer]
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
#    global pvar_value_absolute_url
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: sql_full_url_insert...")
#    global sql_full_url_insert
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_courtlistener_absolute_url_trimmed_1_leading...")
#    global pvar_courtlistener_absolute_url_trimmed_1_leading
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Table01_File] -> [Table02_RemoteURLGen] Executing...")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing all Requried Python3 Module Libraries...")

    import pymysql
    import pymysql.cursors

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")

    # Extract Data

    import mysql.connector
    try:
        connection = mysql.connector.connect(host=f'{dragon_breath_f10_mysql_connector_hostname}',
                                             database=f'{dragon_breath_f10_mysql_connector_database_name}',
                                             user=f'{dragon_breath_f10_mysql_connector_username}',
                                             password=f'{dragon_breath_f10_mysql_connector_password}')

#    import mysql.connector
#    try:
#        connection = mysql.connector.connect(host='localhost',
#                                             database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                             user='brandon',
#                                             password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__')

        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Database Connection Successful! Now Quering Courtlistener 'Summary' URL for current JSON")
#        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer"
#        SELECT * FROM Table ORDER BY ID DESC LIMIT 1
        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer order by id desc limit 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("courtlistener_summary_absolute_url = ", row[17], )
#            with open("extracted_summary_absolute_urls.txt", "w", encoding="utf-8") as f:
            with open(f"{courtlistener_jurisdiction_dataset}extracted_summary_absolute_urls.txt", "w", encoding="utf-8") as f:
                print(row[17], file=f)

    except mysql.connector.Error as e:
        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summaries] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - MySQL connection is closed")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Creating new /summaries/ courtlistener.com URL...")

    # Source: irc.libera.chat #python - jinsun__
    # Date: 03/12/2022 @ Approx. 21:03
    # Dpaste: https://dpaste.com/D83JVVE2K
    global sql_full_url_insert_summary
    global summary_urlpart2
    global pvar_courtlistener_summary_absolute_url_trimmed_1_leading
    from urllib.parse import urljoin
    with open(f"{courtlistener_jurisdiction_dataset}extracted_summary_absolute_urls.txt", "r", encoding="utf-8") as f:
#    with open("extracted_summary_absolute_urls.txt", "r", encoding="utf-8") as f:
        summary_urlpart2 = f.read().strip()
    summary_url_part_1 = "https://www.courtlistener.com"

    summary_url_join = (urljoin(summary_url_part_1,
                  summary_urlpart2))
    #print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - /opinion/xxxxxx/x-v-x/summaries/? courtlistener.com absolute URL is:")
    #print(person_urlpart2)
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - New /summaries/ courtlistener.com URL is:")
    print(summary_url_join)
    #exit()
    pvar_courtlistener_summary_absolute_url_trimmed_1_leading = summary_urlpart2[1:]
    print(pvar_courtlistener_summary_absolute_url_trimmed_1_leading)

    #pvar_courtlistener_absolute_url_trimmed_1_leading = pvar_value_absolute_url[1:]
    #print(pvar_courtlistener_absolute_url_trimmed_1_leading) 

    # Copy Columns & INSERT url_join to new Table + Column
    # Copy Columns from Table: Current_JSON_CL_Dataset_Exodus_Table1_File

    # New Table: Current_JSON_Courtlistener_Dataset_Exodus_Table05_RemoteURLGen2
    # New Column: courtlistener_full_absolute_url
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL into Table05_RemoteURLGen2...")
    sql_full_url_insert_summary = summary_url_join

#    import pymysql.cursors
    # Connect to the database
#    connection = pymysql.connect(host='localhost',
#                                 user='brandon',
#                                 password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__',
#                                 database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                 cursorclass=pymysql.cursors.DictCursor)
#    try:
#        with connection.cursor() as cursor:
#                sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2` (`courtlistener_full_summaries_absolute_url`, `courtlistener_summaries_absolute_url`, `courtlistener_summaries_absolute_url_leading_trim`)  VALUES (%s, %s, %s)"
#                cursor.execute(sql, (sql_full_url_insert_summary, summary_urlpart2, pvar_courtlistener_summary_absolute_url_trimmed_1_leading))
#        connection.commit()
#    finally:
#        connection.close()
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

    # JSON Filename & Full Filename -> Python Vars -> MariaDB
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished!")

def Table05_Cites(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    # DATASET: SCOTUS/NON-SCOTUS [Cites])
    # Code [02/10]: [Read from Table: Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer]
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
#    global pvar_value_absolute_url
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: sql_full_url_insert...")
#    global sql_full_url_insert
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_courtlistener_absolute_url_trimmed_1_leading...")
#    global pvar_courtlistener_absolute_url_trimmed_1_leading
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Table01_File] -> [Table02_RemoteURLGen] Executing...")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing all Requried Python3 Module Libraries...")

    import pymysql
    import pymysql.cursors

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")

    # Extract Data

    import mysql.connector
    try:
        connection = mysql.connector.connect(host=f'{dragon_breath_f10_mysql_connector_hostname}',
                                             database=f'{dragon_breath_f10_mysql_connector_database_name}',
                                             user=f'{dragon_breath_f10_mysql_connector_username}',
                                             password=f'{dragon_breath_f10_mysql_connector_password}')

#    import mysql.connector
#    try:
#        connection = mysql.connector.connect(host='localhost',
#                                             database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                             user='brandon',
#                                             password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__')

        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Database Connection Successful! Now Quering Courtlistener 'Summary' URL for current JSON")
#        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer"
#        SELECT * FROM Table ORDER BY ID DESC LIMIT 1
        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer order by id desc limit 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("courtlistener_cites_absolute_url = ", row[17], )
            #with open("extracted_cites_absolute_urls.txt", "w", encoding="utf-8") as f:
            with open(f"{courtlistener_jurisdiction_dataset}extracted_cites_absolute_urls.txt", "w", encoding="utf-8") as f:
                print(row[17], file=f)

    except mysql.connector.Error as e:
        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - MySQL connection is closed")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Creating new /summaries/ courtlistener.com URL...")

    # Source: irc.libera.chat #python - jinsun__
    # Date: 03/12/2022 @ Approx. 21:03
    # Dpaste: https://dpaste.com/D83JVVE2K
    global sql_full_url_insert_cites
    global cites_urlpart2
    global pvar_courtlistener_cites_absolute_url_trimmed_1_leading
    from urllib.parse import urljoin
#    with open("extracted_cites_absolute_urls.txt", "r", encoding="utf-8") as f:
    with open(f"{courtlistener_jurisdiction_dataset}extracted_cites_absolute_urls.txt", "r", encoding="utf-8") as f:
        cites_urlpart2 = f.read().strip()
    cites_url_part_1 = "https://www.courtlistener.com"

    cites_url_join = (urljoin(cites_url_part_1,
                  cites_urlpart2))
    #print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - /opinion/xxxxxx/x-v-x/summaries/? courtlistener.com absolute URL is:")
    #print(person_urlpart2)
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - New /summaries/ courtlistener.com URL is:")
    print(cites_url_join)
    #exit()
    pvar_courtlistener_cites_absolute_url_trimmed_1_leading = cites_urlpart2[1:]
    print(pvar_courtlistener_cites_absolute_url_trimmed_1_leading)

    #pvar_courtlistener_absolute_url_trimmed_1_leading = pvar_value_absolute_url[1:]
    #print(pvar_courtlistener_absolute_url_trimmed_1_leading) 

    # Copy Columns & INSERT url_join to new Table + Column
    # Copy Columns from Table: Current_JSON_CL_Dataset_Exodus_Table1_File

    # New Table: Current_JSON_Courtlistener_Dataset_Exodus_Table05_RemoteURLGen2
    # New Column: courtlistener_full_absolute_url
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL into Table05_RemoteURLGen2...")
    sql_full_url_insert_cites = cites_url_join

#    import pymysql.cursors
    # Connect to the database
#    connection = pymysql.connect(host='localhost',
#                                 user='brandon',
#                                 password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__',
#                                 database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                 cursorclass=pymysql.cursors.DictCursor)
#    try:
#        with connection.cursor() as cursor:
#                sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2` (`courtlistener_full_cites_absolute_url`, `courtlistener_cites_absolute_url`, `courtlistener_cites_absolute_url_leading_trim`)  VALUES (%s, %s, %s)"
#                cursor.execute(sql, (sql_full_url_insert_cites, cites_urlpart2, pvar_courtlistener_cites_absolute_url_trimmed_1_leading))
#        connection.commit()
#    finally:
#        connection.close()
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

    # JSON Filename & Full Filename -> Python Vars -> MariaDB
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished!")

def Table05_Authorities(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    # DATASET: SCOTUS/NON-SCOTUS [Authorities])
    # Code [02/10]: [Read from Table: Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer]
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_value_absolute_url...")
#    global pvar_value_absolute_url
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: sql_full_url_insert...")
#    global sql_full_url_insert
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: pvar_courtlistener_absolute_url_trimmed_1_leading...")
#    global pvar_courtlistener_absolute_url_trimmed_1_leading
#    print(f"Dragon Breath [F.10] - [Table 02/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Table01_File] -> [Table02_RemoteURLGen] Executing...")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing all Requried Python3 Module Libraries...")

    import pymysql
    import pymysql.cursors

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing Python3 Module Libraries Required for This Python Program Successful!")

    # Extract Data

    import mysql.connector
    try:
        connection = mysql.connector.connect(host=f'{dragon_breath_f10_mysql_connector_hostname}',
                                             database=f'{dragon_breath_f10_mysql_connector_database_name}',
                                             user=f'{dragon_breath_f10_mysql_connector_username}',
                                             password=f'{dragon_breath_f10_mysql_connector_password}')

#    import mysql.connector
#    try:
#        connection = mysql.connector.connect(host='localhost',
#                                             database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                             user='brandon',
#                                             password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__')

        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Database Connection Successful! Now Quering Courtlistener 'Summary' URL for current JSON")
#        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer"
#        SELECT * FROM Table ORDER BY ID DESC LIMIT 1
        sql_select_Query = "select * from Current_JSON_CL_Dataset_Exodus_Table04_RemoteServer order by id desc limit 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("courtlistener_authorities_absolute_url = ", row[17], )
#            with open("extracted_authorities_absolute_urls.txt", "w", encoding="utf-8") as f:
            with open(f"{courtlistener_jurisdiction_dataset}extracted_authorities_absolute_urls.txt", "w", encoding="utf-8") as f:
                print(row[17], file=f)

    except mysql.connector.Error as e:
        print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - MySQL connection is closed")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Creating new /authorities/ courtlistener.com URL...")

    # Source: irc.libera.chat #python - jinsun__
    # Date: 03/12/2022 @ Approx. 21:03
    # Dpaste: https://dpaste.com/D83JVVE2K
    global sql_full_url_insert_authorities
    global authorities_urlpart2
    global pvar_courtlistener_authorities_absolute_url_trimmed_1_leading
    from urllib.parse import urljoin
#    with open("extracted_authorities_absolute_urls.txt", "r", encoding="utf-8") as f:
    with open(f"{courtlistener_jurisdiction_dataset}extracted_authorities_absolute_urls.txt", "r", encoding="utf-8") as f:
        authorities_urlpart2 = f.read().strip()
    authorities_url_part_1 = "https://www.courtlistener.com"

    authorities_url_join = (urljoin(authorities_url_part_1,
                  authorities_urlpart2))
    #print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - /opinion/xxxxxx/x-v-x/summaries/? courtlistener.com absolute URL is:")
    #print(person_urlpart2)
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - New /authorities/ courtlistener.com URL is:")
    print(authorities_url_join)
    #exit()
    pvar_courtlistener_authorities_absolute_url_trimmed_1_leading = authorities_urlpart2[1:]
    print(pvar_courtlistener_authorities_absolute_url_trimmed_1_leading)

    #pvar_courtlistener_absolute_url_trimmed_1_leading = pvar_value_absolute_url[1:]
    #print(pvar_courtlistener_absolute_url_trimmed_1_leading) 

    # Copy Columns & INSERT url_join to new Table + Column
    # Copy Columns from Table: Current_JSON_CL_Dataset_Exodus_Table1_File

    # New Table: Current_JSON_Courtlistener_Dataset_Exodus_Table05_RemoteURLGen2
    # New Column: courtlistener_full_absolute_url
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL into Table05_RemoteURLGen2...")
    sql_full_url_insert_authorities = authorities_url_join

#    import pymysql.cursors
    # Connect to the database
#    connection = pymysql.connect(host='localhost',
#                                 user='brandon',
#                                 password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__',
#                                 database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                 cursorclass=pymysql.cursors.DictCursor)
#    try:
#        with connection.cursor() as cursor:
#                sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2` (`courtlistener_full_authorities_absolute_url`, `courtlistener_authorities_absolute_url`, `courtlistener_authorities_absolute_url_leading_trim`)  VALUES (%s, %s, %s)"
#                cursor.execute(sql, (sql_full_url_insert_authorities, authorities_urlpart2, pvar_courtlistener_authorities_absolute_url_trimmed_1_leading))
#        connection.commit()
#    finally:
#        connection.close()
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

    # JSON Filename & Full Filename -> Python Vars -> MariaDB
#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL into MariaDB Database!")

#    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished!")


def Table05_Payload_SCOTUS(CurrentDecision):
    print("Payload w/ Carries from Person_SCOTUS, Summary_SCOTUS, Cites and Authorities...")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variables from Table05_People_SCOTUS into Table05_RemoteURLGen2...")
    global sql_full_url_insert_person_scotus
    global person_scotus_urlpart2
    global pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading
    
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variables from Table05_Summary_SCOTUS into Table05_RemoteURLGen2...")
    global sql_full_url_insert_summary_scotus
    global summary_scotus_urlpart2
    global pvar_courtlistener_summary_scotus_absolute_url_trimmed_1_leading    
    
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variables from Table05_Cites into Table05_RemoteURLGen2...")
    global sql_full_url_insert_cites
    global cites_urlpart2
    global pvar_courtlistener_cites_absolute_url_trimmed_1_leading

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variables from Table05_Authorities into Table05_RemoteURLGen2...")
    global sql_full_url_insert_authorities
    global authorities_urlpart2
    global pvar_courtlistener_authorities_absolute_url_trimmed_1_leading

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL's into Table05_RemoteURLGen2...")
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL's into Table05_RemoteURLGen2...")
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL's into Table05_RemoteURLGen2...")
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL's into Table05_RemoteURLGen2...")
    
    #sql_full_url_insert_authorities = authorities_url_join

    import pymysql.cursors
    # Connect to the database
    connection = pymysql.connect(host=f'{dragon_breath_f10_pymysql_hostname}',
                                 user=f'{dragon_breath_f10_pymysql_username}',
                                 password=f'{dragon_breath_f10_pymysql_password}',
                                 database=f'{dragon_breath_f10_pymysql_database_name}',
                                 cursorclass=pymysql.cursors.DictCursor)

#    import pymysql.cursors
#    # Connect to the database
#    connection = pymysql.connect(host='localhost',
#                                 user='brandon',
#                                 password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__',
#                                 database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
                sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table05_SCOTUS_RemoteURLGen2` (`courtlistener_full_person_scotus_absolute_url`, `courtlistener_person_scotus_absolute_url`, `courtlistener_person_scotus_absolute_url_leading_trim`, `courtlistener_full_summary_scotus_absolute_url`, `courtlistener_summary_scotus_absolute_url`, `courtlistener_summary_scotus_absolute_url_leading_trim`, `courtlistener_full_cites_absolute_url`, `courtlistener_cites_absolute_url`, `courtlistener_cites_absolute_url_leading_trim`, `courtlistener_full_authorities_absolute_url`, `courtlistener_authorities_absolute_url`, `courtlistener_authorities_absolute_url_leading_trim`)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (sql_full_url_insert_person_scotus, person_scotus_urlpart2, pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading, sql_full_url_insert_summary_scotus, summary_scotus_urlpart2, pvar_courtlistener_summary_scotus_absolute_url_trimmed_1_leading, sql_full_url_insert_cites, cites_urlpart2, pvar_courtlistener_cites_absolute_url_trimmed_1_leading, sql_full_url_insert_authorities, authorities_urlpart2, pvar_courtlistener_authorities_absolute_url_trimmed_1_leading))
                #sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2` (`courtlistener_full_authorities_absolute_url`, `courtlistener_authorities_absolute_url`, `courtlistener_authorities_absolute_url_leading_trim`)  VALUES (%s, %s, %s)"
                #cursor.execute(sql, (sql_full_url_insert_authorities, authorities_urlpart2, pvar_courtlistener_authorities_absolute_url_trimmed_1_leading))
        connection.commit()
    finally:
        connection.close()
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01-04 Payload] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL's into MariaDB Database!")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01-04 Payload] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished!")

def Table05_Payload(CurrentDecision):

    print("Payload w/ Global Carries from Table05_People, Table05_Summary, Table05_Cites and Table05_Authorities...")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variables from Table05_People into Table05_RemoteURLGen2...")
    global sql_full_url_insert_person
    global person_urlpart2
    global pvar_courtlistener_person_absolute_url_trimmed_1_leading
    
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variables from Table05_Summary into Table05_RemoteURLGen2...")
    global sql_full_url_insert_summary
    global summary_urlpart2
    global pvar_courtlistener_summary_absolute_url_trimmed_1_leading    
    
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variables from Table05_Cites into Table05_RemoteURLGen2...")
    global sql_full_url_insert_cites
    global cites_urlpart2
    global pvar_courtlistener_cites_absolute_url_trimmed_1_leading

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variables from Table05_Authorities into Table05_RemoteURLGen2...")
    global sql_full_url_insert_authorities
    global authorities_urlpart2
    global pvar_courtlistener_authorities_absolute_url_trimmed_1_leading

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL's into Table05_RemoteURLGen2...")
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 02: Summary] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL's into Table05_RemoteURLGen2...")
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 03: Cites] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL's into Table05_RemoteURLGen2...")
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 04: Authorities] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting URL's into Table05_RemoteURLGen2...")
    
    #sql_full_url_insert_authorities = authorities_url_join

    import pymysql.cursors
    # Connect to the database
    connection = pymysql.connect(host=f'{dragon_breath_f10_pymysql_hostname}',
                                 user=f'{dragon_breath_f10_pymysql_username}',
                                 password=f'{dragon_breath_f10_pymysql_password}',
                                 database=f'{dragon_breath_f10_pymysql_database_name}',
                                 cursorclass=pymysql.cursors.DictCursor)

#    import pymysql.cursors
#    # Connect to the database
#    connection = pymysql.connect(host='localhost',
#                                 user='brandon',
#                                 password='__VqE3QVAZmDEx__jkabjKKvR7uGcN__',
#                                 database='FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead',
#                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
                sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2` (`courtlistener_full_person_absolute_url`, `courtlistener_person_absolute_url`, `courtlistener_person_absolute_url_leading_trim`, `courtlistener_full_summaries_absolute_url`, `courtlistener_summaries_absolute_url`, `courtlistener_summaries_absolute_url_leading_trim`, `courtlistener_full_cites_absolute_url`, `courtlistener_cites_absolute_url`, `courtlistener_cites_absolute_url_leading_trim`, `courtlistener_full_authorities_absolute_url`, `courtlistener_authorities_absolute_url`, `courtlistener_authorities_absolute_url_leading_trim`)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (sql_full_url_insert_person, person_urlpart2, pvar_courtlistener_person_absolute_url_trimmed_1_leading, sql_full_url_insert_summary, summary_urlpart2, pvar_courtlistener_summary_absolute_url_trimmed_1_leading, sql_full_url_insert_cites, cites_urlpart2, pvar_courtlistener_cites_absolute_url_trimmed_1_leading, sql_full_url_insert_authorities, authorities_urlpart2, pvar_courtlistener_authorities_absolute_url_trimmed_1_leading))
                #sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2` (`courtlistener_full_authorities_absolute_url`, `courtlistener_authorities_absolute_url`, `courtlistener_authorities_absolute_url_leading_trim`)  VALUES (%s, %s, %s)"
                #cursor.execute(sql, (sql_full_url_insert_authorities, authorities_urlpart2, pvar_courtlistener_authorities_absolute_url_trimmed_1_leading))
        connection.commit()
    finally:
        connection.close()
    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01-04 Payload] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Successfully INSERTED Courtlistener_FULL_URL's into MariaDB Database!")

    print(f"Dragon Breath [F.10] - [Table 05/10] - [Part 01-04 Payload] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished!")

def Table06_People_SCOTUS(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    # DATASET: SCOTUS [People])
    # REQUESTS SAVE index.html [People]
    # Table06_People_SCOTUS: [Read from Table: Current_JSON_CL_Dataset_Exodus_Table05_SCOTUS_RemoteURLGen2]

    print("Table06_People_SCOTUS w/ Global Variable Carries from Table05_Payload_SCOTUS...")

    print(f"Dragon Breath [F.10] - [Table 06/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variables from Table05_People_SCOTUS into Table05_RemoteURLGen2...")
    global sql_full_url_insert_person_scotus
    global person_scotus_urlpart2
    global pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading
    
    print(f"Dragon Breath [F.10] - [Table 06/10] - Table05_SCOTUS_RemoteURLGen2 - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Reverse URL Column Recovery] - Started...")

    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variable: dir_path...")
    global dir_path
    
    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variable: Table04_Opinion_newpath_mkdir...")
    global Table04_Opinion_newpath_mkdir
    
    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: Table06_People_SCOTUS_url...")
    global Table06_People_SCOTUS_url

    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: Table06_People_SCOTUS_absolute_url...")
    global Table06_People_SCOTUS_absolute_url

    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: Table06_People_SCOTUS_CurrentDecision_path...")
    global Table06_People_SCOTUS_CurrentDecision_path
    
    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: Table06_People_SCOTUS_url_NULL...")
    global Table06_People_SCOTUS_url_NULL

    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Re-Assigning Variable: (Imported Table05_People_SCOTUS): pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading to 'Table06_People_SCOTUS_absolute_url'...")
    Table06_People_SCOTUS_absolute_url = pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading

    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Global Variable: Table06_People_SCOTUS_url to match Variable 'sql_full_url_insert_person_scotus' for urllib Request URL uniqueness...")
    Table06_People_SCOTUS_url = sql_full_url_insert_person_scotus

    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Global Variable: Table06_People_SCOTUS_CurrentDecision_path to match Variable 'Table04_Opinion_newpath_mkdir' for urllib Request URL uniqueness...")
    Table06_People_SCOTUS_CurrentDecision_path = Table04_Opinion_newpath_mkdir

    # Need to Global Assign newpath_mkdir from Table05_People_SCOTUS and use this variable for _NEW_ Table04_BS4_LXML_Recovery pathlib fname path before / 'index.html'
    
    # Error Handling for Specific Error Code for urllib.Request (StackOverFlow Source):
    # URL: https://stackoverflow.com/questions/3193060/how-do-i-catch-a-specific-http-error-in-python

    # Part 1/2: (Without Error Handling):
    # User-Agent: Mozilla/5.0 
    
    def Table06_People_SCOTUS_CheckNullValue(CurrentDecision):
        global Table06_People_SCOTUS_url
        global Table06_People_SCOTUS_url_NULL
        print("Checking to see if this Current Constitutional Supreme and Mandatory Judge Decision has a NULL Value for Table06_People_SCOTUS...")
        if(Table06_People_SCOTUS_url == "https://www.courtlistener.com/(NULL)"):
            print("This Decision has a NULL Value for Table06_People_SCOTUS...")
            print("Now Setting The Variable 'Table06_People_SCOTUS_url_NULL' to 'True'...")
            Table06_People_SCOTUS_url_NULL = "True"
            print("Setting The Variable 'Table06_People_SCOTUS_url_NULL' to 'True' Successful...")
            print(Table06_People_SCOTUS_url_NULL)
            Table06_People_SCOTUS_NULL(CurrentDecision)
        else:
            print("This Decision does NOT have a NULL Value for Table06_People_SCOTUS...")
            Table06_People_SCOTUS_url_NULL = "False"
            Table06_People_SCOTUS_Not_NULL(CurrentDecision)
            #return

    def Table06_People_SCOTUS_Not_NULL(CurrentDecision):
        global courtlistener_jurisdiction_dataset
        print(f"Dragon Breath [F.10] - [Table 06/10] - [Nested Function: Table06_People_SCOTUS_Not_NULL] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Global Variable: Table06_People_SCOTUS_CurrentDecision_path to match Variable 'Table04_Opinion_newpath_mkdir' for urllib Request URL uniqueness...")
    
        print("Now Importing Parent Function Global Variables...")
        global sql_full_url_insert_person_scotus
        global person_scotus_urlpart2
        global pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading
        global dir_path
        global Table04_Opinion_newpath_mkdir
        global Table06_People_SCOTUS_url
        global Table06_People_SCOTUS_absolute_url
        global Table06_People_SCOTUS_CurrentDecision_path
        global Table06_People_SCOTUS_url_NULL
        global Table06_People_SCOTUS_newpath_mkdir
        global Table06_People_SCOTUS_current_html

        print(f"Dragon Breath [F.10] - [Table 06/10] - [Part 01: People] - [Nested Function: Table06_People_SCOTUS_Not_NULL] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing all Requried Python3 Module Libraries...")
        import urllib.request
        from urllib.request import Request, urlopen
        import pathlib
        from pathlib import Path
        import datetime
        import os
        import sys
    
        print("Now Performing Full Function...")

        print("Request URL is Python Variable 'Table06_People_SCOTUS_url':")
        print(Table06_People_SCOTUS_url)

        print("Now Printing Python Variable 'Table06_People_SCOTUS_url_NULL':")
        print(Table06_People_SCOTUS_url_NULL)
        
        #print("NESTED FUNCTION - CONDITIONAL FUNCTION .... Did _NOT_ Work! Exiting...")
        #exit()

        req = Request(Table06_People_SCOTUS_url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req,timeout=30).read()
    
        print("Current American Constitutional Opinion in THIS Dataset:")
        print(Table06_People_SCOTUS_url)

        # New Path: (using CurrentDecision's Table04 /opinion/number/petition-v-respondent/ for Path Value...)
        PATH = pathlib.Path(__file__).parent
        print("Now Printing Python Variable Value for PATH:")
        print(PATH)
        print("Now Printing Python Variable Value for Table06_People_SCOTUS_CurrentDecision_path...")
        print(Table06_People_SCOTUS_CurrentDecision_path)
        print("Now Printing Python Variable Value for Table06_People_SCOTUS_absolute_url...")
        print(Table06_People_SCOTUS_absolute_url)
        fpath = f"{Table06_People_SCOTUS_CurrentDecision_path}{Table06_People_SCOTUS_absolute_url}" 
        print("Now Printing Python Variable Value for fpath...")
        print(fpath)
        fname = PATH /  f'{fpath}' / 'index.html'
        print("Now Printing Python Variable Value for fname...")
        print(fname)
        print("mkdir test Path assigned to Python Variable: 'Table06_People_SCOTUS_newpath_mkdir':")
        Table06_People_SCOTUS_newpath_mkdir = pathlib.Path(f'{fpath}')
        print("Python Variable Contents of 'Table06_People_SCOTUS_newpath_mkdir' is now:")
        print(Table06_People_SCOTUS_newpath_mkdir)

        try:
            if not Table06_People_SCOTUS_newpath_mkdir.exists():
                pathlib.Path(f'{Table06_People_SCOTUS_newpath_mkdir}').mkdir(parents=True)
        except DebianLinuxError:
            print(f"Debian Linux Error - [Errorno 17]: Already Exists, Creating Directory: {Table06_People_SCOTUS_newpath_mkdir} for {current_json_filename} on Dataset: {courtlistener_jurisdiction_dataset}")
            logging.debug(f"Debian Linux - [Errorno 17]: Already Exists, Creating Directory: {Table06_People_SCOTUS_newpath_mkdir} for {current_json_filename} on Dataset: {courtlistener_jurisdiction_dataset}")
            pathlib.Path(f'{Table06_People_SCOTUS_newpath_mkdir}').mkdir(exist_ok=True, parents=True)
        print("Successfully Created Directory:")
        #print(fpath)
        print(Table06_People_SCOTUS_absolute_url)
        print("Successfully Created Directory - Full Path:")
        print(Table06_People_SCOTUS_newpath_mkdir)
        print("Now writing index.html in newly created Directory (Includes Opinion/Case_Number/Petititon-v-Respondent/People Folder)...")
        with open(fname, 'w') as f:
           f.write(str(html))
        print("Now Saving Full HTML as-is on courtlistener.com into a Python Variable to be carried into a Payload Nested Function...")
        Table06_People_SCOTUS_current_html = html
        exit()

    def Table06_People_SCOTUS_NULL(CurrentDecision):
        print("Now Importing Parent Function Global Variables...")
        global courtlistener_jurisdiction_dataset
        global sql_full_url_insert_person_scotus
        global person_scotus_urlpart2
        global pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading
        global dir_path
        global Table04_Opinion_newpath_mkdir
        global Table06_People_SCOTUS_url
        global Table06_People_SCOTUS_absolute_url
        global Table06_People_SCOTUS_CurrentDecision_path
    
        print("Now Returning to Finish The Parent Function and Continue The Flow of Code for Dragon Breath F.10...")
        return

    def Table06_People_SCOTUS_BS4_LXML_Recovery(CurrentDecision):
        # DATASET: SCOTUS [People])
        # DATA RECOVERY [People]

        # Make sure to Save Portrait .jpeg's 
        # Domain: portraits.free.law
        # Portrait_Absolute_URL: /v2/512/field-stephen-1816-11-04.jpeg
        # Example URL: https://portraits.free.law/v2/512/field-stephen-1816-11-04.jpeg

        # Carry Over The 1st urllib.request instead of opening a new request and hitting the server twice! 
        print("Now Importing Parent Function Global Variables...")
        global sql_full_url_insert_person_scotus
        global person_scotus_urlpart2
        global pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading
        global dir_path
        global Table04_Opinion_newpath_mkdir
        global Table06_People_SCOTUS_url
        global Table06_People_SCOTUS_absolute_url
        global Table06_People_SCOTUS_CurrentDecision_path
        global Table06_People_SCOTUS_url_NULL
        global Table06_People_SCOTUS_newpath_mkdir
        global Table06_People_SCOTUS_current_html
        global courtlistener_jurisdiction_dataset
        print(f"Current American Constitutional Supreme and Mandatory Jurisdiction: {courtlistener_jurisdiction_dataset} ...")
                # Import Additional Python3 Require Module Libraries
        from bs4 import BeautifulSoup
        from lxml import etree
        import requests

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table06_People_SCOTUS Column Python Variable 1 out of ...")

        # Assign a Python Variable to Beautiful Soup 4's HTML Parser
        #htmlParse = BeautifulSoup(html, 'html.parser')
        htmlParse = BeautifulSoup(Table06_People_SCOTUS_current_html, 'html.parser')

        # Select HTML Element for Data Parsing Column #1 [courtlistener_people_header_text]
        htmlParse.find_all("h2")[0].get_text()

        # Assign Table06_People_SCOTUS Column 1 /  - MariaDB Column Name: courtlistener_person_header_text
        #pvar_bs4_tag_courtlistener_case_name = htmlParse.find_all("h2")[0].get_text()
        pvar_bs4_courtlistener_person_header_text = htmlParse.find_all("h2")[0].get_text()
        print(htmlParse.find_all("h2")[0].get_text())

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Quering Selected Court Opinion from Remote Servers Prior Functions Saved Webpage Python Variable using BS4 Successful!")

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Quering Selected Court Opinion from Remote Servers Prior Functions Saved Webpage Python Variable using LXML XPATH...")

        #URL = "https://www.courtlistener.com/opinion/2581757/amalgamated-transit-v-state/"
        #URL = sql_full_url_insert
        URL = sql_full_url_insert_person_scotus

        # First Instance of XPATH Request / Parse Requirements & Variables (Thanks to chevignon93 on reddit.com!)

        # Select HTML Element for Data Parsing Column #2 (Cont.) [courtlistener_jurisdiction]
        HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                    'Accept-Language': 'en-US, en;q=0.5'})

        #webpage = requests.get(URL, headers=HEADERS)
        webpage = Table06_People_SCOTUS_current_html
        xsoup = BeautifulSoup(webpage.content, "html5lib")
        dom = etree.HTML(str(xsoup))

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Quering Selected Court Opinion from Remote Server using LXML XPATH Successful!")


        # Assign Table06_People_SCOTUS Column 2 / 63 - MariaDB Column Name: courtlistener_person_fjc_id

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table06_People_SCOTUS Column Python Variable 2 out of ...")
        try:  
            pvar_dom_xpath_courtlistener_person_fjc_id = dom.xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/span')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_person_fjc_id) !=0:
                print(pvar_dom_xpath_courtlistener_person_fjc_id)
            else:
                pvar_dom_xpath_courtlistener_person_fjc_id = "(NULL)"
                print(pvar_dom_xpath_courtlistener_person_fjc_id)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table06_People_SCOTUS Column Python Variable 2 out of ...")
            logging.debug(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table06_People_SCOTUS Column Python Variable 2 out of ...")
            pvar_dom_xpath_courtlistener_person_fjc_id = "(NULL)"
        print(pvar_dom_xpath_courtlistener_person_fjc_id)

        # Assign Table06_People_SCOTUS Column 3 / 63 - MariaDB Column Name: courtlistener_person_fjc_id_url

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table06_People_SCOTUS Column Python Variable 3 out of ...")
        try:  
            pvar_dom_xpath_courtlistener_person_fjc_id_url = dom.xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/span/@href')
            if len(pvar_dom_xpath_courtlistener_person_fjc_id_url) !=0:
                print(pvar_dom_xpath_courtlistener_person_fjc_id_url)
            else:
                pvar_dom_xpath_courtlistener_person_fjc_id_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_person_fjc_id_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table06_People_SCOTUS Column Python Variable 3 out of ...")
            logging.debug(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table06_People_SCOTUS Column Python Variable 3 out of ...")
            pvar_dom_xpath_courtlistener_person_fjc_id_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_person_fjc_id_url)

                # Chain Print

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Chain Printing Python Variables for Payload INJECTION to MariaDB]...")

        # [1] - XPATH tag: h2 | [courtlistener_person_header_text] (Only BS4 Pulls Full courtlistener_case_name on Table04)
        print(pvar_bs4_tag_courtlistener_person_header_text)

        # [2] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/span | [courtlistener_person_fjc_id]
        print(pvar_dom_xpath_courtlistener_person_fjc_id)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/h3')[0].text.strip())

        # [3] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/span/@href | [courtlistener_person_fjc_id_url]
        print(pvar_dom_xpath_courtlistener_person_fjc_id_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/span/@href')

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Chain Printing Python Variables for Payload INJECTION to MariaDB Successful!]")

        # Chain Re-Assign

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Chain Re-Assigning Python Variables for Payload INJECTION to MariaDB]...")
        #bs4_xpath_courtlistener_person_header_text = pvar_dom_xpath_courtlistener_person_header_text
        # Added to remedy XPATH overwriting good BS4 Values with Incomplete Data [courtlistener_case_name] "Dred Scott" (XPATH) vs. "Dred Scott v. Sandford, 60 U.S. 393" (BS4)

        # [1] - XPATH tag: h2 | [courtlistener_person_header_text] (Only BS4 Pulls Full courtlistener_case_name on Table04)
        bs4_courtlistener_person_header_text = pvar_bs4_tag_courtlistener_person_header_text
        # [2] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/span | [courtlistener_person_header_text]
        lxml_xpath_courtlistener_person_fjc_id = pvar_dom_xpath_courtlistener_person_fjc_id
        # [3] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/span/@href | [courtlistener_person_fjc_id_url]
        lxml_xpath_courtlistener_person_fjc_id_url = pvar_dom_xpath_courtlistener_person_fjc_id_url


# [4] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/p/span[2] | [courtlistener_person_born_text]

# [5] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/p/span[2]/@href | [courtlistener_person_born_text_url]

# [6] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[3]/p[1]/span[2] | [courtlistener_person_race]

# [7] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[3]/p[2]/span[2] | [courtlistener_person_gender]

# [8] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[4]/p | [courtlistener_person_aba_ratings]

# [9] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[1] | [courtlistener_person_political_aff_1]

# [10] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[1]/@href | [courtlistener_person_political_aff_1_url]

# [11] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[2] | [courtlistener_person_political_aff_2]

# [12] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[2]/@href | [courtlistener_person_political_aff_2_url]

# [13] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[3] | [courtlistener_person_political_aff_3]

# [14] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[3]/@href | [courtlistener_person_political_aff_3_url]

# [15] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[4] | [courtlistener_person_political_aff_4]

# [16] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[4]/@href | [courtlistener_person_political_aff_4_url]

# [17] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[5] | [courtlistener_person_political_aff_5]

# [18] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[5]/@href | [courtlistener_person_political_aff_5_url]

# [19] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[1] | [courtlistener_person_edu_1]

# [20] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[1]/@href | [courtlistener_person_edu_1_url]

# [21] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[2] | [courtlistener_person_edu_2]

# [22] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[2]/@href | [courtlistener_person_edu_2_url]

# [23] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[3] | [courtlistener_person_edu_3]

# [24] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[3]/@href | [courtlistener_person_edu_3_url]

# [25] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[4] | [courtlistener_person_edu_4]

# [26] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[4]/@href | [courtlistener_person_edu_4_url]

# [27] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[5] | [courtlistener_person_edu_5]

# [28] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[5]/@href | [courtlistener_person_edu_5_url]

# [29] - BS4 tag:

        # Assign Table06_People_SCOTUS Column 29 /  - MariaDB Column Name: courtlistener_person_judicial_header_text
        #pvar_bs4_tag_courtlistener_person_judicial_header_text = htmlParse.find_all("h4")[0].get_text()
        pvar_bs4_courtlistener_person_judicial_header_text = htmlParse.find_all("h4")[0].get_text()
        print(htmlParse.find_all("h4")[0].get_text())


# [30] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/p/span[2]/a | [courtlistener_person_judicial_appointed_by]

# [31] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/p/span[2]/a/@href | [courtlistener_person_judicial_appointed_by_url]

# [32] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[3]/p/span[2] | [courtlistener_person_judicial_selected_by]

# [33] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[3]/p/span[2]/@href | [courtlistener_person_judicial_selected_by_url]

# [34] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[4]/p/span[2] | [courtlistener_person_judicial_committee_action_date]

# [35] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[5]/p[1]/span[2] | [courtlistener_person_nomination_hearing_date]

# [36] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[5]/p[2]/span[2] | [courtlistener_person_confirmation_date]

# [37] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[5]/p[3]/span[2] | [courtlistener_person_vote_info]

# [38] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[6]/p/span[2] | [courtlistener_person_judicial_termination_reason]

# [39] - BS4 tag:

        # Assign Table06_People_SCOTUS Column 38 /  - MariaDB Column Name: courtlistener_person_judicial_header_text_2
        #pvar_bs4_tag_courtlistener_person_judicial_header_text_2 = htmlParse.find_all("h4")[1].get_text()
        pvar_bs4_courtlistener_person_judicial_header_text_2 = htmlParse.find_all("h4")[1].get_text()
        print(htmlParse.find_all("h4")[1].get_text())



# [40] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[2]/p/span[2]/a | [courtlistener_person_judicial_ii_appointed_by]

# [41] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[2]/p/span[2]/a/@href | [courtlistener_person_judicial_ii_appointed_by_url]

# [42] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[3]/p/span[2] | [courtlistener_person_judicial_ii_selected_by]

# [43] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[3]/p/span[2]/@href | [courtlistener_person_judicial_ii_selected_by_url]

# [44] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[4]/p/span[2] | [courtlistener_person_judicial_ii_committee_action_date]

# [45] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[5]/p[1]/span[2] | [courtlistener_person_judicial_ii_nomination_hearing_date]

# [46] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[5]/p[2]/span[2] | [courtlistener_person_judicial_ii_confirmation_date]

# [47] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[5]/p[3]/span[2] | [courtlistener_person_judicial_ii_vote_info]

# [48] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[6]/p/span[2] | [courtlistener_person_judicial_ii_termination_reason]

# [49] - BS4 tag:

        # Assign Table06_People_SCOTUS Column 48 /  - MariaDB Column Name: courtlistener_person_judicial_header_text_3
        #pvar_bs4_tag_courtlistener_person_judicial_header_text_3 = htmlParse.find_all("h4")[2].get_text()
        pvar_bs4_courtlistener_person_judicial_header_text_3 = htmlParse.find_all("h4")[2].get_text()
        print(htmlParse.find_all("h4")[2].get_text())

# [50] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/p/span[2]/a | [courtlistener_person_judicial_iii_apointed_by]

# [51] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/p/span[2]/a/@href | [courtlistener_person_judicial_iii_apointed_by_url]

# [52] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[3]/p/span[2] | [courtlistener_person_judicial_iii_selected_by]

# [53] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[3]/p/span[2]/@href | [courtlistener_person_judicial_iii_selected_by_url]

# [54] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[4]/p/span[2] | [courtlistener_person_judicial_iii_committee_action_date]

# [55] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[5]/p[1]/span[2] | [courtlistener_person_judicial_iii_confirmation_date]

# [56] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[5]/p[2]/span[2] | [courtlistener_person_judicial_iii_vote_info]

# [57] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[6]/p/span[2] | [courtlistener_person_judicial_iii_terminated_reason]

# [58] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[4]/div/h4 | [courtlistener_person_non_judicial_position_1]

# [59] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[5]/div/h4 | [courtlistener_person_non_judicial_position_2]

# [60] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[6]/div/h4 | [courtlistener_person_non_judicial_position_3]

# [61] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[7]/div/h4 | [courtlistener_person_non_judicial_position_4]

# [62] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[8]/div/h4 | [courtlistener_person_non_judicial_position_5]

# [63] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[1]/h4/a | [courtlistener_person_financial_disclosure_year_1]

# [64] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[1]/h4/a/@href | [courtlistener_person_financial_disclosure_year_1_url]

# [65] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[2]/h4/a | [courtlistener_person_financial_disclosure_year_2]

# [66] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[2]/h4/a/@href | [courtlistener_person_financial_disclosure_year_2_url]

# [67] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[3]/h4/a | [courtlistener_person_financial_disclosure_year_3]

# [68] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[3]/h4/a/@href | [courtlistener_person_financial_disclosure_year_3_url]

# [69] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[4]/h4/a | [courtlistener_person_financial_disclosure_year_4]

# [70] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[4]/h4/a/@href | [courtlistener_person_financial_disclosure_year_4_url]

# [71] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[5]/h4/a | [courtlistener_person_financial_disclosure_year_5]

# [72] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[5]/h4/a/@href | [courtlistener_person_financial_disclosure_year_5_url]

# [73] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[6]/h4/a | [courtlistener_person_financial_disclosure_year_6]

# [74] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[6]/h4/a/@href | [courtlistener_person_financial_disclosure_year_6_url]

# [75] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[7]/h4/a | [courtlistener_person_financial_disclosure_year_7]

# [76] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[7]/h4/a/@href | [courtlistener_person_financial_disclosure_year_7_url]

# [77] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[8]/h4/a | [courtlistener_person_financial_disclosure_year_8]

# [78] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[8]/h4/a/@href | [courtlistener_person_financial_disclosure_year_8_url]

# [79] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[9]/h4/a | [courtlistener_person_financial_disclosure_year_9]

# [80] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[9]/h4/a/@href | [courtlistener_person_financial_disclosure_year_9_url]

# [81] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[10]/h4/a | [courtlistener_person_financial_disclosure_year_10]

# [82] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[10]/h4/a/@href | [courtlistener_person_financial_disclosure_year_10_url]

# [83] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[11]/h4/a | [courtlistener_person_financial_disclosure_year_11]

# [84] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[11]/h4/a/@href | [courtlistener_person_financial_disclosure_year_11_url]

# [85] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[12]/h4/a | [courtlistener_person_financial_disclosure_year_12]

# [86] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[12]/h4/a/@href | [courtlistener_person_financial_disclosure_year_12_url]

# [87] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[13]/h4/a | [courtlistener_person_financial_disclosure_year_13]

# [88] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[13]/h4/a/@href | [courtlistener_person_financial_disclosure_year_13_url]

# [89] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[14]/h4/a | [courtlistener_person_financial_disclosure_year_14]

# [90] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[14]/h4/a/@href | [courtlistener_person_financial_disclosure_year_14_url]

# [91] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[15]/h4/a | [courtlistener_person_financial_disclosure_year_15]

# [92] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[15]/h4/a/@href | [courtlistener_person_financial_disclosure_year_15_url]

# [93] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[16]/h4/a | [courtlistener_person_financial_disclosure_year_16]

# [94] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[16]/h4/a/@href | [courtlistener_person_financial_disclosure_year_16_url]

# [95] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[17]/h4/a | [courtlistener_person_financial_disclosure_year_17]

# [96] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[17]/h4/a/@href | [courtlistener_person_financial_disclosure_year_17_url]

# [97] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[18]/h4/a | [courtlistener_person_financial_disclosure_year_18]

# [98] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[18]/h4/a/@href | [courtlistener_person_financial_disclosure_year_18_url]

# [99] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[19]/h4/a | [courtlistener_person_financial_disclosure_year_19]

# [100] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[19]/h4/a/@href | [courtlistener_person_financial_disclosure_year_19_url]

# [101] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[20]/h4/a | [courtlistener_person_financial_disclosure_year_20]

# [102] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[20]/h4/a/@href | [courtlistener_person_financial_disclosure_year_20_url]

# [103] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[21]/h4/a | [courtlistener_person_financial_disclosure_year_21]

# [104] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[21]/h4/a/@href | [courtlistener_person_financial_disclosure_year_21_url]

# [105] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[22]/h4/a | [courtlistener_person_financial_disclosure_year_22]

# [106] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[22]/h4/a/@href | [courtlistener_person_financial_disclosure_year_22_url]

# [107] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[23]/h4/a | [courtlistener_person_financial_disclosure_year_23]

# [108] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[23]/h4/a/@href | [courtlistener_person_financial_disclosure_year_23_url]

# [109] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[24]/h4/a | [courtlistener_person_financial_disclosure_year_24]

# [110] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[24]/h4/a/@href | [courtlistener_person_financial_disclosure_year_24_url]

# [111] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[25]/h4/a | [courtlistener_person_financial_disclosure_year_25]

# [112] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[25]/h4/a/@href | [courtlistener_person_financial_disclosure_year_25_url]

# [113] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[26]/h4/a | [courtlistener_person_financial_disclosure_year_26]

# [114] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[26]/h4/a/@href | [courtlistener_person_financial_disclosure_year_26_url]

# [115] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[27]/h4/a | [courtlistener_person_financial_disclosure_year_27]

# [116] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[27]/h4/a/@href | [courtlistener_person_financial_disclosure_year_27_url]

# [117] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[28]/h4/a | [courtlistener_person_financial_disclosure_year_28]

# [118] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[28]/h4/a/@href | [courtlistener_person_financial_disclosure_year_28_url]

# [119] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[29]/h4/a | [courtlistener_person_financial_disclosure_year_29]

# [120] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[29]/h4/a/@href | [courtlistener_person_financial_disclosure_year_29_url]

# [121] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[30]/h4/a | [courtlistener_person_financial_disclosure_year_30]

# [122] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[30]/h4/a/@href | [courtlistener_person_financial_disclosure_year_30_url]

# [123] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[31]/h4/a | [courtlistener_person_financial_disclosure_year_31]

# [124] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[31]/h4/a/@href | [courtlistener_person_financial_disclosure_year_31_url]

# [125] - XPATH tag: /html/body/div[1]/div[1]/div/h3 | [courtlistener_person_financial_disclosures_total]

# [126] - BS4 tag:

        # Assign Table06_People_SCOTUS Column 126 /  - MariaDB Column Name: courtlistener_person_judicial_authored_opinion_count
        #pvar_bs4_courtlistener_person_judicial_authored_opinion_count = htmlParse.find_all("h4")[2].get_text()
        pvar_bs4_courtlistener_person_judicial_authored_opinion_count = htmlParse.find(name="h3", class_="authored-opinions").get_text()
        print(htmlParse.find(name="h3", class_="authored-opinions").get_text())

# [127] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/h4/a | [courtlistener_person_judicial_authored_opinion_1_name]

# [128] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/h4/a/@href | [courtlistener_person_judicial_authored_opinion_1_name_url]

# [129] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/div[1]/time | [courtlistener_person_judicial_authored_opinion_1_filed]

# [130] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/div[2]/span[2] | [courtlistener_person_judicial_authored_opinion_1_status]

# [131] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/div[3]/span[2] | [courtlistener_person_judicial_authored_opinion_1_docket_num]

# [132] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[2]/div/article/h4/a | [courtlistener_person_judicial_authored_opinion_2]

# [133] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[2]/div/article/h4/a/@href | [courtlistener_person_judicial_authored_opinion_2_url]

# [134] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[2]/div/article/div[1]/time | [courtlistener_person_judicial_authored_opinion_2_filed]

# [135] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[2]/div/article/div[2]/span[2] | [courtlistener_person_judicial_authored_opinion_2_status]

# [136] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[2]/div/article/div[3]/span[2] | [courtlistener_person_judicial_authored_opinion_2_docket_num]

# [137] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[3]/div/article/h4/a | [courtlistener_person_judicial_authored_opinion_3]

# [138] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[3]/div/article/h4/a/@href | [courtlistener_person_judicial_authored_opinion_3_url]

# [139] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[3]/div/article/div[1]/time | [courtlistener_person_judicial_authored_opinion_3_filed]

# [140] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[3]/div/article/div[2]/span[2] | [courtlistener_person_judicial_authored_opinion_3_status]

# [141] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[3]/div/article/div[3]/span[2] | [courtlistener_person_judicial_authored_opinion_3_docket_num]

# [142] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[4]/div/article/h4/a | [courtlistener_person_judicial_authored_opinion_4]

# [143] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[4]/div/article/h4/a/@href | [courtlistener_person_judicial_authored_opinion_4_url]

# [144] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[4]/div/article/div[1]/time | [courtlistener_person_judicial_authored_opinion_4_filed]

# [145] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[4]/div/article/div[2]/span[2] | [courtlistener_person_judicial_authored_opinion_4_status]

# [146] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[4]/div/article/div[3]/span[2] | [courtlistener_person_judicial_authored_opinion_4_docket_num]

# [147] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[5]/div/article/h4/a | [courtlistener_person_judicial_authored_opinion_5]

# [148] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[5]/div/article/h4/a/@href | [courtlistener_person_judicial_authored_opinion_5_url]

# [149] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[5]/div/article/div[1]/time | [courtlistener_person_judicial_authored_opinion_5_filed]

# [150] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[5]/div/article/div[2]/span[2] | [courtlistener_person_judicial_authored_opinion_5_status]

# [151] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[5]/div/article/div[3]/span[2] | [courtlistener_person_judicial_authored_opinion_5_docket_num]

# [152] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/p[2]/a/@href | [courtlistener_person_judicial_authored_opinions_all_url]

# [153] - BS4 tag:

        # Assign Table06_People_SCOTUS Column / - MariaDB Column Name: pvar_bs4_courtlistener_person_judicial_assigned_cases_count
        #pvar_bs4_courtlistener_person_judicial_assigned_cases_count = htmlParse.find(name="h3", class_="assigned-cases").get_text()
        pvar_bs4_courtlistener_person_judicial_assigned_cases_count = htmlParse.find(name="h3", class_="assigned-cases").get_text()
        print(htmlParse.find(name="h3", class_="assigned-cases").get_text())

# [154] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[1]/div/article/h4/a | [courtlistener_person_judicial_assigned_case_1]

# [155] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[1]/div/article/h4/a/@href | [courtlistener_person_judicial_assigned_case_1_url]

# [156] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[1]/div/article/div[1]/time | [courtlistener_person_judicial_assigned_case_1_filed]

# [157] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[1]/div/article/div[2]/span[2] | [courtlistener_person_judicial_assigned_case_1_docket_num]

# [158] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[2]/div/article/h4/a | [courtlistener_person_judicial_assigned_case_2]

# [159] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[2]/div/article/h4/a/@href | [courtlistener_person_judicial_assigned_case_2_url]

# [160] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[2]/div/article/div[1]/time | [courtlistener_person_judicial_assigned_case_2_filed]

# [161] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[2]/div/article/div[2]/span[2] | [courtlistener_person_judicial_assigned_case_2_docket_num]

# [162] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[3]/div/article/h4/a | [courtlistener_person_judicial_assigned_case_3]

# [163] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[3]/div/article/h4/a/@href | [courtlistener_person_judicial_assigned_case_3_url]

# [164] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[3]/div/article/div[1]/time | [courtlistener_person_judicial_assigned_case_3_filed]

# [165] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[3]/div/article/div[2]/span[2] | [courtlistener_person_judicial_assigned_case_3_docket_num]

# [166] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[4]/div/article/h4/a | [courtlistener_person_judicial_assigned_case_4]

# [167] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[4]/div/article/h4/a/@href | [courtlistener_person_judicial_assigned_case_4_url]

# [168] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[4]/div/article/div[1]/time | [courtlistener_person_judicial_assigned_case_4_filed]

# [169] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[4]/div/article/div[2]/span[2] | [courtlistener_person_judicial_assigned_case_4_docket_num]

# [170] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[5]/div/article/h4/a | [courtlistener_person_judicial_assigned_case_5]

# [171] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[5]/div/article/h4/a/@href | [courtlistener_person_judicial_assigned_case_5_url]

# [172] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[5]/div/article/div[1]/time | [courtlistener_person_judicial_assigned_case_5_filed]

# [173] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/p/a/@href | [courtlistener_person_judicial_assigned_referred_cases_recap_url]

# [174] - BS4 tag:

        # Assign Table06_People_SCOTUS Column / - MariaDB Column Name: pvar_bs4_courtlistener_person_judicial_most_recent_oral_arguments_heard
        #pvar_bs4_courtlistener_person_judicial_most_recent_oral_arguments_heard = find(name="h3", class_="oral-arguments-heard").get_text()
        pvar_bs4_courtlistener_person_judicial_most_recent_oral_arguments_heard = htmlParse.find(name="h3", class_="oral-arguments-heard").get_text()
        print(htmlParse.find(name="h3", class_="oral-arguments-heard").get_text())

# [175] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[1]/div/article/h4/a | [courtlistener_person_judicial_oral_argument_1]

# [176] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[1]/div/article/h4/a/@href | [courtlistener_person_judicial_oral_argument_1_url]

# [177] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[1]/div/article/div[1]/time | [courtlistener_person_judicial_oral_argument_1_argued]

# [178] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[1]/div/article/div[2]/span[2] | [courtlistener_person_judicial_oral_argument_1_docket_num]

# [179] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[2]/div/article/h4/a | [courtlistener_person_judicial_oral_argument_2]

# [180] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[2]/div/article/h4/a/@href | [courtlistener_person_judicial_oral_argument_2_url]

# [181] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[2]/div/article/div[1]/time | [courtlistener_person_judicial_oral_argument_2_argued]

# [182] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[2]/div/article/div[2]/span[2] | [courtlistener_person_judicial_oral_argument_2_docket_num]

# [183] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[3]/div/article/h4/a | [courtlistener_person_judicial_oral_argument_3]

# [184] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[3]/div/article/h4/a/@href | [courtlistener_person_judicial_oral_argument_3_url]

# [185] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[3]/div/article/div[1]/time | [courtlistener_person_judicial_oral_argument_3_argued]

# [186] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[3]/div/article/div[2]/span[2] | [courtlistener_person_judicial_oral_argument_3_docket_num]

# [187] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[4]/div/article/h4/a | [courtlistener_person_judicial_oral_argument_4]

# [188] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[4]/div/article/h4/a/@href | [courtlistener_person_judicial_oral_argument_4_url]

# [189] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[4]/div/article/div[1]/time | [courtlistener_person_judicial_oral_argument_4_argued]

# [190] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[4]/div/article/div[2]/span[2] | [courtlistener_person_judicial_oral_argument_4_docket_num]

# [191] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[5]/div/article/h4/a | [courtlistener_person_judicial_oral_argument_5]

# [192] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[5]/div/article/h4/a/@href | [courtlistener_person_judicial_oral_argument_5_url]

# [193] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[5]/div/article/div[1]/time | [courtlistener_person_judicial_oral_argument_5_argued]

# [194] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[5]/div/article/div[2]/span[2] | [courtlistener_person_judicial_oral_argument_5_docket_num]

# [195] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/p[2]/a/@href | [courtlistener_person_judicial_oral_arguments_all_url]

# [196] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[1]/h2/img | [courtlistener_person_judicial_portrait]

# [197] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[1]/h2/img/@href | [courtlistener_person_judicial_portrait_url]


        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Chain Re-Assigning Python Variables for Payload INJECTION to MariaDB Successful!]")

        # Table06_People_SCOTUS MariaDB Payload (RemoteServer Data Recovery)

        #global courtlistener_jurisdiction_dataset
        
        print(f"{courtlistener_jurisdiction_dataset} Decision Payload...")

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting XPATH Python Variable Payload to MariaDB...")

        import pymysql
        import pymysql.cursors
        connection = pymysql.connect(host=f'{dragon_breath_f10_pymysql_hostname}',
          user=f"{dragon_breath_f10_pymysql_username}",
          passwd=f"{dragon_breath_f10_pymysql_password}",
          db=f"{dragon_breath_f10_pymysql_database_name}"
        )

#        import pymysql
#        import pymysql.cursors
#        connection = pymysql.connect(host='localhost',
#          user="brandon",
#          passwd="__VqE3QVAZmDEx__jkabjKKvR7uGcN__",
#          db="FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead"
#        )
        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - PyMySQL Connected Successfully!")

        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table06_People_SCOTUS` (`courtlistener_person_header_text`,`courtlistener_person_fjc_id`, `courtlistener_person_fjc_id_url`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (bs4_courtlistener_person_header_text, lxml_xpath_courtlistener_person_fjc_id, lxml_xpath_courtlistener_person_fjc_id_url))
                connection.commit()

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Injecting XPATH Python Variable Payload to MariaDB Successful!")

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People_SCOTUS - [Nested Function: Table06_People_SCOTUS_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished!")


    Table06_People_SCOTUS_CheckNullValue(CurrentDecision)

# urllib.HTTPError Example Nested Try/Except Block from StackOverflow 
# Source URL: https://stackoverflow.com/questions/3193060/how-do-i-catch-a-specific-http-error-in-python

#import urllib
#try:
#    urllib.urlopen("some url")
#except urllib.HTTPError as err:
#    try:
#        if err.code == 404:
#            # Handle the error
#        else:
#            raise
#    except:
#        ...

    #print("Nested Function w/ Conditioning Worked!... Exiting...")
    #exit()

def Table06_People(CurrentDecision):
    global courtlistener_jurisdiction_dataset
    # DATASET: [People])
    # REQUESTS SAVE index.html [People]
    # Table06_People: [Read from Table: Current_JSON_CL_Dataset_Exodus_Table05_RemoteURLGen2]

    print("Table06_People w/ Global Variable Carries from Table05_Payload...")

    print(f"Dragon Breath [F.10] - [Table 06/10] - [Part 01: Person] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variables from Table05_People into Table05_RemoteURLGen2...")
    global sql_full_url_insert_person
    global person_urlpart2
    global pvar_courtlistener_person_absolute_url_trimmed_1_leading
    
    print(f"Dragon Breath [F.10] - [Table 06/10] - Table05_RemoteURLGen2 - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Reverse URL Column Recovery] - Started...")

    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variable: dir_path...")
    global dir_path
    
    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Importing Global Variable: Table04_Opinion_newpath_mkdir...")
    global Table04_Opinion_newpath_mkdir
    
    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: Table06_People_url...")
    global Table06_People_url

    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: Table06_People_absolute_url...")
    global Table06_People_absolute_url

    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: Table06_People_CurrentDecision_path...")
    global Table06_People_CurrentDecision_path
    
    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Declaring Global Variable: Table06_People_url_NULL...")
    global Table06_People_url_NULL

    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Re-Assigning Variable: (Imported Table05_People): pvar_courtlistener_person_scotus_absolute_url_trimmed_1_leading to 'Table06_People_absolute_url'...")
    Table06_People_absolute_url = pvar_courtlistener_person_absolute_url_trimmed_1_leading

    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Global Variable: Table06_People_url to match Variable 'sql_full_url_insert_person' for urllib Request URL uniqueness...")
    Table06_People_url = sql_full_url_insert_person

    print(f"Dragon Breath [F.10] - [Table 06/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Global Variable: Table06_People_CurrentDecision_path to match Variable 'Table04_Opinion_newpath_mkdir' for urllib Request URL uniqueness...")
    Table06_People_CurrentDecision_path = Table04_Opinion_newpath_mkdir

    # Need to Global Assign newpath_mkdir from Table05_People_SCOTUS and use this variable for _NEW_ Table04_BS4_LXML_Recovery pathlib fname path before / 'index.html'
    
    # Error Handling for Specific Error Code for urllib.Request (StackOverFlow Source):
    # URL: https://stackoverflow.com/questions/3193060/how-do-i-catch-a-specific-http-error-in-python

    # Part 1/2: (Without Error Handling):
    # User-Agent: Mozilla/5.0 
    
    def Table06_People_CheckNullValue(CurrentDecision):
        global Table06_People_url
        global Table06_People_url_NULL
        print("Checking to see if this Current Constitutional Supreme and Mandatory Judge Decision has a NULL Value for Table06_People...")
        if(Table06_People_url == "https://www.courtlistener.com/(NULL)"):
            print("This Decision has a NULL Value for Table06_People...")
            print("Now Setting The Variable 'Table06_People_url_NULL' to 'True'...")
            Table06_People_url_NULL = "True"
            print("Setting The Variable 'Table06_People_url_NULL' to 'True' Successful...")
            print(Table06_People_url_NULL)
            Table06_People_NULL(CurrentDecision)
        else:
            print("This Decision does NOT have a NULL Value for Table06_People...")
            Table06_People_url_NULL = "False"
            Table06_People_Not_NULL(CurrentDecision)
            #return

    def Table06_People_Not_NULL(CurrentDecision):
        global courtlistener_jurisdiction_dataset
        print(f"Dragon Breath [F.10] - [Table 06/10] - [Nested Function: Table06_People_Not_NULL] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Global Variable: Table06_People_CurrentDecision_path to match Variable 'Table04_Opinion_newpath_mkdir' for urllib Request URL uniqueness...")
    
        print("Now Importing Parent Function Global Variables...")
        global sql_full_url_insert_person
        global person_urlpart2
        global pvar_courtlistener_person_absolute_url_trimmed_1_leading
        global dir_path
        global Table04_Opinion_newpath_mkdir
        global Table06_People_url
        global Table06_People_absolute_url
        global Table06_People_CurrentDecision_path
        global Table06_People_url_NULL
        global Table06_People_newpath_mkdir
        global Table06_People_current_html

        print(f"Dragon Breath [F.10] - [Table 06/10] - [Part 01: People] - [Nested Function: Table06_People_Not_NULL] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Importing all Requried Python3 Module Libraries...")
        import urllib.request
        from urllib.request import Request, urlopen
        import pathlib
        from pathlib import Path
        import datetime
        import os
        import sys
    
        print("Now Performing Full Function...")

        print("Request URL is Python Variable 'Table06_People_url':")
        print(Table06_People_url)

        print("Now Printing Python Variable 'Table06_People_url_NULL':")
        print(Table06_People_url_NULL)
        
        #print("NESTED FUNCTION - CONDITIONAL FUNCTION .... Did _NOT_ Work! Exiting...")
        #exit()

        req = Request(Table06_People_url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req,timeout=30).read()
    
        print("Current American Constitutional Opinion in THIS Dataset:")
        print(Table06_People_url)

        # New Path: (using CurrentDecision's Table04 /opinion/number/petition-v-respondent/ for Path Value...)
        PATH = pathlib.Path(__file__).parent
        print("Now Printing Python Variable Value for PATH:")
        print(PATH)
        print("Now Printing Python Variable Value for Table06_People_CurrentDecision_path...")
        print(Table06_People_CurrentDecision_path)
        print("Now Printing Python Variable Value for Table06_People_absolute_url...")
        print(Table06_People_absolute_url)
        fpath = f"{Table06_People_CurrentDecision_path}{Table06_People_absolute_url}" 
        print("Now Printing Python Variable Value for fpath...")
        print(fpath)
        fname = PATH /  f'{fpath}' / 'index.html'
        print("Now Printing Python Variable Value for fname...")
        print(fname)
        print("mkdir test Path assigned to Python Variable: 'Table06_People_newpath_mkdir':")
        Table06_People_newpath_mkdir = pathlib.Path(f'{fpath}')
        print("Python Variable Contents of 'Table06_People_newpath_mkdir' is now:")
        print(Table06_People_newpath_mkdir)

        try:
            if not Table06_People_newpath_mkdir.exists():
                pathlib.Path(f'{Table06_People_newpath_mkdir}').mkdir(parents=True)
        except DebianLinuxError:
            print(f"Debian Linux Error - [Errorno 17]: Already Exists, Creating Directory: {Table06_People_newpath_mkdir} for {current_json_filename} on Dataset: {courtlistener_jurisdiction_dataset}")
            logging.debug(f"Debian Linux - [Errorno 17]: Already Exists, Creating Directory: {Table06_People_newpath_mkdir} for {current_json_filename} on Dataset: {courtlistener_jurisdiction_dataset}")
            pathlib.Path(f'{Table06_People_newpath_mkdir}').mkdir(exist_ok=True, parents=True)
        print("Successfully Created Directory:")
        #print(fpath)
        print(Table06_People_absolute_url)
        print("Successfully Created Directory - Full Path:")
        print(Table06_People_newpath_mkdir)
        print("Now writing index.html in newly created Directory (Includes Opinion/Case_Number/Petititon-v-Respondent/People Folder)...")
        with open(fname, 'w') as f:
           f.write(str(html))
        print("Now Saving Full HTML as-is on courtlistener.com into a Python Variable to be carried into a Payload Nested Function...")
        Table06_People_current_html = html
        exit()

    def Table06_People_NULL(CurrentDecision):
        print("Now Importing Parent Function Global Variables...")
        global courtlistener_jurisdiction_dataset
        global sql_full_url_insert_person
        global person_urlpart2
        global pvar_courtlistener_person_absolute_url_trimmed_1_leading
        global dir_path
        global Table04_Opinion_newpath_mkdir
        global Table06_People_url
        global Table06_People_absolute_url
        global Table06_People_CurrentDecision_path
    
        print("Now Returning to Finish The Parent Function and Continue The Flow of Code for Dragon Breath F.10...")
        return

    def Table06_People_BS4_LXML_Recovery(CurrentDecision):
        # DATASET: [People])
        # DATA RECOVERY [People]

        # Make sure to Save Portrait .jpeg's 
        # Domain: portraits.free.law
        # Portrait_Absolute_URL: /v2/512/field-stephen-1816-11-04.jpeg
        # Example URL: https://portraits.free.law/v2/512/field-stephen-1816-11-04.jpeg

        # Carry Over The 1st urllib.request instead of opening a new request and hitting the server twice! 
        print("Now Importing Parent Function Global Variables...")
        global sql_full_url_insert_person
        global person_urlpart2
        global pvar_courtlistener_person_absolute_url_trimmed_1_leading
        global dir_path
        global Table04_Opinion_newpath_mkdir
        global Table06_People_url
        global Table06_People_absolute_url
        global Table06_People_CurrentDecision_path
        global Table06_People_url_NULL
        global Table06_People_newpath_mkdir
        global Table06_People_current_html
        global courtlistener_jurisdiction_dataset
        print(f"Current American Constitutional Supreme and Mandatory Jurisdiction: {courtlistener_jurisdiction_dataset} ...")
                # Import Additional Python3 Require Module Libraries
        from bs4 import BeautifulSoup
        from lxml import etree
        import requests

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table06_People Column Python Variable 1 out of ...")

        # Assign a Python Variable to Beautiful Soup 4's HTML Parser
        #htmlParse = BeautifulSoup(html, 'html.parser')
        htmlParse = BeautifulSoup(Table06_People_SCOTUS_current_html, 'html.parser')

        # Select HTML Element for Data Parsing Column #1 [courtlistener_people_header_text]
        htmlParse.find_all("h2")[0].get_text()

        # Assign Table06_People_SCOTUS Column 1 /  - MariaDB Column Name: courtlistener_person_header_text
        #pvar_bs4_tag_courtlistener_case_name = htmlParse.find_all("h2")[0].get_text()
        pvar_bs4_courtlistener_person_header_text = htmlParse.find_all("h2")[0].get_text()
        print(htmlParse.find_all("h2")[0].get_text())

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Quering Selected Court Opinion from Remote Servers Prior Functions Saved Webpage Python Variable using BS4 Successful!")

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Quering Selected Court Opinion from Remote Servers Prior Functions Saved Webpage Python Variable using LXML XPATH...")

        #URL = "https://www.courtlistener.com/opinion/2581757/amalgamated-transit-v-state/"
        #URL = sql_full_url_insert
        URL = sql_full_url_insert_person_scotus

        # First Instance of XPATH Request / Parse Requirements & Variables (Thanks to chevignon93 on reddit.com!)

        # Select HTML Element for Data Parsing Column #2 (Cont.) [courtlistener_jurisdiction]
        HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                    'Accept-Language': 'en-US, en;q=0.5'})

        #webpage = requests.get(URL, headers=HEADERS)
        webpage = Table06_People_SCOTUS_current_html
        xsoup = BeautifulSoup(webpage.content, "html5lib")
        dom = etree.HTML(str(xsoup))

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Quering Selected Court Opinion from Remote Server using LXML XPATH Successful!")


        # Assign Table06_People_SCOTUS Column 2 / 63 - MariaDB Column Name: courtlistener_person_fjc_id

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table06_People Column Python Variable 2 out of ...")
        try:  
            pvar_dom_xpath_courtlistener_person_fjc_id = dom.xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/span')[0].text.strip()
            if len(pvar_dom_xpath_courtlistener_person_fjc_id) !=0:
                print(pvar_dom_xpath_courtlistener_person_fjc_id)
            else:
                pvar_dom_xpath_courtlistener_person_fjc_id = "(NULL)"
                print(pvar_dom_xpath_courtlistener_person_fjc_id)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table06_People Column Python Variable 2 out of ...")
            logging.debug(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table06_People Column Python Variable 2 out of ...")
            pvar_dom_xpath_courtlistener_person_fjc_id = "(NULL)"
        print(pvar_dom_xpath_courtlistener_person_fjc_id)

        # Assign Table06_People Column 3 / 63 - MariaDB Column Name: courtlistener_person_fjc_id_url

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table06_People Column Python Variable 3 out of ...")
        try:  
            pvar_dom_xpath_courtlistener_person_fjc_id_url = dom.xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/span/@href')
            if len(pvar_dom_xpath_courtlistener_person_fjc_id_url) !=0:
                print(pvar_dom_xpath_courtlistener_person_fjc_id_url)
            else:
                pvar_dom_xpath_courtlistener_person_fjc_id_url = "(NULL)"
                print(pvar_dom_xpath_courtlistener_person_fjc_id_url)
        except BaseException:
            print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table06_People Column Python Variable 3 out of ...")
            logging.debug(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning (NULL) VALUE (Index Out of Range) Table06_People Column Python Variable 3 out of ...")
            pvar_dom_xpath_courtlistener_person_fjc_id_url = "(NULL)"
        print(pvar_dom_xpath_courtlistener_person_fjc_id_url)

                # Chain Print

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Chain Printing Python Variables for Payload INJECTION to MariaDB]...")

        # [1] - XPATH tag: h2 | [courtlistener_person_header_text] (Only BS4 Pulls Full courtlistener_case_name on Table04)
        print(pvar_bs4_tag_courtlistener_person_header_text)

        # [2] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/span | [courtlistener_person_fjc_id]
        print(pvar_dom_xpath_courtlistener_person_fjc_id)
        #print(dom.xpath('/html/body/div[1]/div[1]/article/h3')[0].text.strip())

        # [3] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/span/@href | [courtlistener_person_fjc_id_url]
        print(pvar_dom_xpath_courtlistener_person_fjc_id_url)
        #print(dom.xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/span/@href')

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Chain Printing Python Variables for Payload INJECTION to MariaDB Successful!]")

        # Chain Re-Assign

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Chain Re-Assigning Python Variables for Payload INJECTION to MariaDB]...")
        #bs4_xpath_courtlistener_person_header_text = pvar_dom_xpath_courtlistener_person_header_text
        # Added to remedy XPATH overwriting good BS4 Values with Incomplete Data [courtlistener_case_name] "Dred Scott" (XPATH) vs. "Dred Scott v. Sandford, 60 U.S. 393" (BS4)

        # [1] - XPATH tag: h2 | [courtlistener_person_header_text] (Only BS4 Pulls Full courtlistener_case_name on Table04)
        bs4_courtlistener_person_header_text = pvar_bs4_tag_courtlistener_person_header_text
        # [2] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/span | [courtlistener_person_header_text]
        lxml_xpath_courtlistener_person_fjc_id = pvar_dom_xpath_courtlistener_person_fjc_id
        # [3] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/span/@href | [courtlistener_person_fjc_id_url]
        lxml_xpath_courtlistener_person_fjc_id_url = pvar_dom_xpath_courtlistener_person_fjc_id_url


# [4] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/p/span[2] | [courtlistener_person_born_text]
#                   /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/p/span[2] # 9TH CIR
#                   /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/p/span[2] # WASH STATE


# [5] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/p/span[2]/@href | [courtlistener_person_born_text_url]


# [6] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[3]/p[1]/span[2] | [courtlistener_person_race]

# [7] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[3]/p[2]/span[2] | [courtlistener_person_gender]
#                   /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[3]/p/span[2] # 9TH CIR
#                   /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[3]/p/span[2] # WASH STATE

# [8] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[4]/p | [courtlistener_person_aba_ratings]

# [] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[2]/h4  # WASH STATE | [courtlistener_person_campaign_finance_text]
#                  /html/body/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[2]/h4

# [] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[2]/h4/@href  # WASH STATE | [courtlistener_person_campaign_finance_text_url]
#                  /html/body/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[2]/h4/@href


# [9] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[1] | [courtlistener_person_political_aff_1]

# [10] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[1]/@href | [courtlistener_person_political_aff_1_url]

# [11] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[2] | [courtlistener_person_political_aff_2]

# [12] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[2]/@href | [courtlistener_person_political_aff_2_url]

# [13] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[3] | [courtlistener_person_political_aff_3]

# [14] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[3]/@href | [courtlistener_person_political_aff_3_url]

# [15] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[4] | [courtlistener_person_political_aff_4]

# [16] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[4]/@href | [courtlistener_person_political_aff_4_url]

# [17] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[5] | [courtlistener_person_political_aff_5]

# [18] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[1]/ul/li[5]/@href | [courtlistener_person_political_aff_5_url]

# [19] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[1] | [courtlistener_person_edu_1]
#                    /html/body/div[1]/div[1]/div/div[2]/div/ul/li # WASH STATE

# [20] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[1]/@href | [courtlistener_person_edu_1_url]

# [21] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[2] | [courtlistener_person_edu_2]

# [22] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[2]/@href | [courtlistener_person_edu_2_url]

# [23] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[3] | [courtlistener_person_edu_3]

# [24] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[3]/@href | [courtlistener_person_edu_3_url]

# [25] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[4] | [courtlistener_person_edu_4]

# [26] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[4]/@href | [courtlistener_person_edu_4_url]

# [27] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[5] | [courtlistener_person_edu_5]

# [28] - XPATH tag: /html/body/div[1]/div[1]/div/div[2]/div[3]/ul/li[5]/@href | [courtlistener_person_edu_5_url]

# [29] - BS4 tag:

        # Assign Table06_People_SCOTUS Column 29 /  - MariaDB Column Name: courtlistener_person_judicial_header_text
        #pvar_bs4_tag_courtlistener_person_judicial_header_text = htmlParse.find_all("h4")[0].get_text()
#        pvar_bs4_courtlistener_person_judicial_header_text = htmlParse.find_all("h4")[0].get_text()
#        print(htmlParse.find_all("h4")[0].get_text())


# [30] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/p/span[2]/a | [courtlistener_person_judicial_appointed_by]

# [31] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/p/span[2]/a/@href | [courtlistener_person_judicial_appointed_by_url]

# [32] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[3]/p/span[2] | [courtlistener_person_judicial_selected_by]

# [33] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[3]/p/span[2]/@href | [courtlistener_person_judicial_selected_by_url]

# [34] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[4]/p/span[2] | [courtlistener_person_judicial_committee_action_date]

# [35] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[5]/p[1]/span[2] | [courtlistener_person_nomination_hearing_date]

# [36] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[5]/p[2]/span[2] | [courtlistener_person_confirmation_date]

# [37] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[5]/p[3]/span[2] | [courtlistener_person_vote_info]

# [38] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div[6]/p/span[2] | [courtlistener_person_judicial_termination_reason]

# [39] - BS4 tag:

        # Assign Table06_People Column 38 /  - MariaDB Column Name: courtlistener_person_judicial_header_text_2
        #pvar_bs4_tag_courtlistener_person_judicial_header_text_2 = htmlParse.find_all("h4")[1].get_text()
#        pvar_bs4_courtlistener_person_judicial_header_text_2 = htmlParse.find_all("h4")[1].get_text()
#        print(htmlParse.find_all("h4")[1].get_text())



# [40] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[2]/p/span[2]/a | [courtlistener_person_judicial_ii_appointed_by]

# [41] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[2]/p/span[2]/a/@href | [courtlistener_person_judicial_ii_appointed_by_url]

# [42] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[3]/p/span[2] | [courtlistener_person_judicial_ii_selected_by]

# [43] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[3]/p/span[2]/@href | [courtlistener_person_judicial_ii_selected_by_url]

# [44] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[4]/p/span[2] | [courtlistener_person_judicial_ii_committee_action_date]

# [45] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[5]/p[1]/span[2] | [courtlistener_person_judicial_ii_nomination_hearing_date]

# [46] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[5]/p[2]/span[2] | [courtlistener_person_judicial_ii_confirmation_date]

# [47] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[5]/p[3]/span[2] | [courtlistener_person_judicial_ii_vote_info]

# [48] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div[6]/p/span[2] | [courtlistener_person_judicial_ii_termination_reason]

# [49] - BS4 tag:

        # Assign Table06_People Column 48 /  - MariaDB Column Name: courtlistener_person_judicial_header_text_3
        #pvar_bs4_tag_courtlistener_person_judicial_header_text_3 = htmlParse.find_all("h4")[2].get_text()
#        pvar_bs4_courtlistener_person_judicial_header_text_3 = htmlParse.find_all("h4")[2].get_text()
#        print(htmlParse.find_all("h4")[2].get_text())

# [50] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/p/span[2]/a | [courtlistener_person_judicial_iii_apointed_by]

# [51] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[2]/p/span[2]/a/@href | [courtlistener_person_judicial_iii_apointed_by_url]

# [52] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[3]/p/span[2] | [courtlistener_person_judicial_iii_selected_by]

# [53] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[3]/p/span[2]/@href | [courtlistener_person_judicial_iii_selected_by_url]

# [54] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[4]/p/span[2] | [courtlistener_person_judicial_iii_committee_action_date]

# [55] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[5]/p[1]/span[2] | [courtlistener_person_judicial_iii_confirmation_date]

# [56] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[5]/p[2]/span[2] | [courtlistener_person_judicial_iii_vote_info]

# [57] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div[6]/p/span[2] | [courtlistener_person_judicial_iii_terminated_reason]


# [] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div/h4 | [courtlistener_person_judicial_position_1]
#                  /html/body/div[1]/div[1]/div/div[3]/div/div[1]/div/h4 # WASH STATE

# [] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div/h4/span | [courtlistener_person_judicial_position_2]
#                  /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div/h4/span


# [58] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[4]/div/h4 | [courtlistener_person_non_judicial_position_1]
#                    /html/body/div[1]/div[1]/div/div[3]/div/div[2]/div/h4 # 9 CIR


# [59] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[5]/div/h4 | [courtlistener_person_non_judicial_position_2]
#                    /html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/h4 # 9 CIR

# [60] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[6]/div/h4 | [courtlistener_person_non_judicial_position_3]
#                    /html/body/div[1]/div[1]/div/div[3]/div/div[4]/div/h4 # 9 CIR

# [61] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[7]/div/h4 | [courtlistener_person_non_judicial_position_4]
#                    /html/body/div[1]/div[1]/div/div[3]/div/div[5]/div/h4 # 9 CIR

# [62] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[8]/div/h4 | [courtlistener_person_non_judicial_position_5]
#                    /html/body/div[1]/div[1]/div/div[3]/div/div[6]/div/h4 # 9 CIR


# [58] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[4]/div/h4 | [courtlistener_person_non_judicial_position_6]
#                    /html/body/div[1]/div[1]/div/div[3]/div/div[7]/div/h4 # 9 CIR

# [59] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[5]/div/h4 | [courtlistener_person_non_judicial_position_7]
#                    /html/body/div[1]/div[1]/div/div[3]/div/div[8]/div/h4 # 9 CIR

# [60] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[6]/div/h4 | [courtlistener_person_non_judicial_position_8]
#                    /html/body/div[1]/div[1]/div/div[3]/div/div[9]/div/h4 # 9 CIR

# [61] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[7]/div/h4 | [courtlistener_person_non_judicial_position_9]
#                    /html/body/div[1]/div[1]/div/div[3]/div/div[10]/div/h4 # 9 CIR

# [62] - XPATH tag: /html/body/div[1]/div[1]/div/div[3]/div/div[8]/div/h4 | [courtlistener_person_non_judicial_position_10]
#                    /html/body/div[1]/div[1]/div/div[3]/div/div[11]/div/h4 # 9 CIR
                    

# [63] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[1]/h4/a | [courtlistener_person_financial_disclosure_year_1]
#                    /html/body/div[1]/div[1]/div/div[4]/div[1]/h4/a # 9 CIR

# [64] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[1]/h4/a/@href | [courtlistener_person_financial_disclosure_year_1_url]

# [65] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[2]/h4/a | [courtlistener_person_financial_disclosure_year_2]

# [66] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[2]/h4/a/@href | [courtlistener_person_financial_disclosure_year_2_url]

# [67] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[3]/h4/a | [courtlistener_person_financial_disclosure_year_3]

# [68] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[3]/h4/a/@href | [courtlistener_person_financial_disclosure_year_3_url]

# [69] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[4]/h4/a | [courtlistener_person_financial_disclosure_year_4]

# [70] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[4]/h4/a/@href | [courtlistener_person_financial_disclosure_year_4_url]

# [71] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[5]/h4/a | [courtlistener_person_financial_disclosure_year_5]

# [72] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[5]/h4/a/@href | [courtlistener_person_financial_disclosure_year_5_url]

# [73] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[6]/h4/a | [courtlistener_person_financial_disclosure_year_6]

# [74] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[6]/h4/a/@href | [courtlistener_person_financial_disclosure_year_6_url]

# [75] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[7]/h4/a | [courtlistener_person_financial_disclosure_year_7]

# [76] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[7]/h4/a/@href | [courtlistener_person_financial_disclosure_year_7_url]

# [77] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[8]/h4/a | [courtlistener_person_financial_disclosure_year_8]

# [78] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[8]/h4/a/@href | [courtlistener_person_financial_disclosure_year_8_url]

# [79] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[9]/h4/a | [courtlistener_person_financial_disclosure_year_9]

# [80] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[9]/h4/a/@href | [courtlistener_person_financial_disclosure_year_9_url]

# [81] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[10]/h4/a | [courtlistener_person_financial_disclosure_year_10]

# [82] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[10]/h4/a/@href | [courtlistener_person_financial_disclosure_year_10_url]

# [83] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[11]/h4/a | [courtlistener_person_financial_disclosure_year_11]

# [84] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[11]/h4/a/@href | [courtlistener_person_financial_disclosure_year_11_url]

# [85] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[12]/h4/a | [courtlistener_person_financial_disclosure_year_12]

# [86] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[12]/h4/a/@href | [courtlistener_person_financial_disclosure_year_12_url]

# [87] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[13]/h4/a | [courtlistener_person_financial_disclosure_year_13]

# [88] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[13]/h4/a/@href | [courtlistener_person_financial_disclosure_year_13_url]

# [89] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[14]/h4/a | [courtlistener_person_financial_disclosure_year_14]

# [90] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[14]/h4/a/@href | [courtlistener_person_financial_disclosure_year_14_url]

# [91] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[15]/h4/a | [courtlistener_person_financial_disclosure_year_15]

# [92] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[15]/h4/a/@href | [courtlistener_person_financial_disclosure_year_15_url]

# [93] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[16]/h4/a | [courtlistener_person_financial_disclosure_year_16]

# [94] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[16]/h4/a/@href | [courtlistener_person_financial_disclosure_year_16_url]

# [95] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[17]/h4/a | [courtlistener_person_financial_disclosure_year_17]

# [96] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[17]/h4/a/@href | [courtlistener_person_financial_disclosure_year_17_url]

# [97] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[18]/h4/a | [courtlistener_person_financial_disclosure_year_18]

# [98] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[18]/h4/a/@href | [courtlistener_person_financial_disclosure_year_18_url]

# [99] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[19]/h4/a | [courtlistener_person_financial_disclosure_year_19]

# [100] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[19]/h4/a/@href | [courtlistener_person_financial_disclosure_year_19_url]

# [101] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[20]/h4/a | [courtlistener_person_financial_disclosure_year_20]

# [102] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[20]/h4/a/@href | [courtlistener_person_financial_disclosure_year_20_url]

# [103] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[21]/h4/a | [courtlistener_person_financial_disclosure_year_21]

# [104] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[21]/h4/a/@href | [courtlistener_person_financial_disclosure_year_21_url]

# [105] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[22]/h4/a | [courtlistener_person_financial_disclosure_year_22]

# [106] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[22]/h4/a/@href | [courtlistener_person_financial_disclosure_year_22_url]

# [107] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[23]/h4/a | [courtlistener_person_financial_disclosure_year_23]

# [108] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[23]/h4/a/@href | [courtlistener_person_financial_disclosure_year_23_url]

# [109] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[24]/h4/a | [courtlistener_person_financial_disclosure_year_24]

# [110] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[24]/h4/a/@href | [courtlistener_person_financial_disclosure_year_24_url]

# [111] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[25]/h4/a | [courtlistener_person_financial_disclosure_year_25]

# [112] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[25]/h4/a/@href | [courtlistener_person_financial_disclosure_year_25_url]

# [113] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[26]/h4/a | [courtlistener_person_financial_disclosure_year_26]

# [114] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[26]/h4/a/@href | [courtlistener_person_financial_disclosure_year_26_url]

# [115] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[27]/h4/a | [courtlistener_person_financial_disclosure_year_27]

# [116] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[27]/h4/a/@href | [courtlistener_person_financial_disclosure_year_27_url]

# [117] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[28]/h4/a | [courtlistener_person_financial_disclosure_year_28]

# [118] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[28]/h4/a/@href | [courtlistener_person_financial_disclosure_year_28_url]

# [119] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[29]/h4/a | [courtlistener_person_financial_disclosure_year_29]

# [120] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[29]/h4/a/@href | [courtlistener_person_financial_disclosure_year_29_url]

# [121] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[30]/h4/a | [courtlistener_person_financial_disclosure_year_30]

# [122] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[30]/h4/a/@href | [courtlistener_person_financial_disclosure_year_30_url]

# [123] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[31]/h4/a | [courtlistener_person_financial_disclosure_year_31]

# [124] - XPATH tag: /html/body/div[1]/div[1]/div/div[4]/div[31]/h4/a/@href | [courtlistener_person_financial_disclosure_year_31_url]

# [125] - XPATH tag: /html/body/div[1]/div[1]/div/h3 | [courtlistener_person_financial_disclosures_total]

# [126] - BS4 tag:

        # Assign Table06_People Column 126 /  - MariaDB Column Name: courtlistener_person_judicial_authored_opinion_count
        #pvar_bs4_courtlistener_person_judicial_authored_opinion_count = htmlParse.find_all("h4")[2].get_text()
#        pvar_bs4_courtlistener_person_judicial_authored_opinion_count = htmlParse.find(name="h3", class_="authored-opinions").get_text()
#        print(htmlParse.find(name="h3", class_="authored-opinions").get_text())

# [127] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/h4/a | [courtlistener_person_judicial_authored_opinion_1_name]
#                     /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/h4/a # 9th CIR


# [128] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/h4/a/@href | [courtlistener_person_judicial_authored_opinion_1_name_url]

# [129] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/div[1]/time | [courtlistener_person_judicial_authored_opinion_1_filed]
#                     /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/div[1]/time # 9th CIR

# [130] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/div[2]/span[2] | [courtlistener_person_judicial_authored_opinion_1_status]
#                     /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/div[2]/span[2] # 9th CIR


# [131] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/div[3]/span[2] # 9th CIR | [courtlistener_person_judicial_authored_opinion_1_citations]
        
# [131] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/div[3]/span[2] | [courtlistener_person_judicial_authored_opinion_1_docket_num]
#                     /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/div[4]/span[2] # 9th CIR


# [131] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/div[5]/span/a #9th CIR | [courtlistener_person_judicial_authored_opinion_1_cite_num]              


# [131] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[1]/div/article/div[5]/span/a/@href #9th CIR | [courtlistener_person_judicial_authored_opinion_1_cite_num_url]              


# [132] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[2]/div/article/h4/a | [courtlistener_person_judicial_authored_opinion_2]

# [133] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[2]/div/article/h4/a/@href | [courtlistener_person_judicial_authored_opinion_2_url]

# [134] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[2]/div/article/div[1]/time | [courtlistener_person_judicial_authored_opinion_2_filed]

# [135] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[2]/div/article/div[2]/span[2] | [courtlistener_person_judicial_authored_opinion_2_status]

# [136] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[2]/div/article/div[3]/span[2] | [courtlistener_person_judicial_authored_opinion_2_docket_num]

# [137] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[3]/div/article/h4/a | [courtlistener_person_judicial_authored_opinion_3]

# [138] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[3]/div/article/h4/a/@href | [courtlistener_person_judicial_authored_opinion_3_url]

# [139] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[3]/div/article/div[1]/time | [courtlistener_person_judicial_authored_opinion_3_filed]

# [140] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[3]/div/article/div[2]/span[2] | [courtlistener_person_judicial_authored_opinion_3_status]

# [141] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[3]/div/article/div[3]/span[2] | [courtlistener_person_judicial_authored_opinion_3_docket_num]

# [142] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[4]/div/article/h4/a | [courtlistener_person_judicial_authored_opinion_4]

# [143] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[4]/div/article/h4/a/@href | [courtlistener_person_judicial_authored_opinion_4_url]

# [144] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[4]/div/article/div[1]/time | [courtlistener_person_judicial_authored_opinion_4_filed]

# [145] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[4]/div/article/div[2]/span[2] | [courtlistener_person_judicial_authored_opinion_4_status]

# [146] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[4]/div/article/div[3]/span[2] | [courtlistener_person_judicial_authored_opinion_4_docket_num]

# [147] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[5]/div/article/h4/a | [courtlistener_person_judicial_authored_opinion_5]

# [148] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[5]/div/article/h4/a/@href | [courtlistener_person_judicial_authored_opinion_5_url]

# [149] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[5]/div/article/div[1]/time | [courtlistener_person_judicial_authored_opinion_5_filed]

# [150] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[5]/div/article/div[2]/span[2] | [courtlistener_person_judicial_authored_opinion_5_status]

# [151] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/div[5]/div/article/div[3]/span[2] | [courtlistener_person_judicial_authored_opinion_5_docket_num]

# [152] - XPATH tag: /html/body/div[1]/div[1]/div/div[5]/div/p[2]/a/@href | [courtlistener_person_judicial_authored_opinions_all_url]
#                    /html/body/div[1]/div[1]/div/div[5]/div/p[2]/a/@href # 9TH CIR
 
# [153] - BS4 tag:

        # Assign Table06_People Column / - MariaDB Column Name: pvar_bs4_courtlistener_person_judicial_assigned_cases_count
        #pvar_bs4_courtlistener_person_judicial_assigned_cases_count = htmlParse.find(name="h3", class_="assigned-cases").get_text()
#        pvar_bs4_courtlistener_person_judicial_assigned_cases_count = htmlParse.find(name="h3", class_="assigned-cases").get_text()
#        print(htmlParse.find(name="h3", class_="assigned-cases").get_text())



# [154] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[1]/div/article/h4/a | [courtlistener_person_judicial_assigned_case_1]

# [155] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[1]/div/article/h4/a/@href | [courtlistener_person_judicial_assigned_case_1_url]

# [156] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[1]/div/article/div[1]/time | [courtlistener_person_judicial_assigned_case_1_filed]

# [157] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[1]/div/article/div[2]/span[2] | [courtlistener_person_judicial_assigned_case_1_docket_num]

# [158] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[2]/div/article/h4/a | [courtlistener_person_judicial_assigned_case_2]

# [159] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[2]/div/article/h4/a/@href | [courtlistener_person_judicial_assigned_case_2_url]

# [160] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[2]/div/article/div[1]/time | [courtlistener_person_judicial_assigned_case_2_filed]

# [161] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[2]/div/article/div[2]/span[2] | [courtlistener_person_judicial_assigned_case_2_docket_num]

# [162] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[3]/div/article/h4/a | [courtlistener_person_judicial_assigned_case_3]

# [163] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[3]/div/article/h4/a/@href | [courtlistener_person_judicial_assigned_case_3_url]

# [164] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[3]/div/article/div[1]/time | [courtlistener_person_judicial_assigned_case_3_filed]

# [165] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[3]/div/article/div[2]/span[2] | [courtlistener_person_judicial_assigned_case_3_docket_num]

# [166] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[4]/div/article/h4/a | [courtlistener_person_judicial_assigned_case_4]

# [167] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[4]/div/article/h4/a/@href | [courtlistener_person_judicial_assigned_case_4_url]

# [168] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[4]/div/article/div[1]/time | [courtlistener_person_judicial_assigned_case_4_filed]

# [169] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[4]/div/article/div[2]/span[2] | [courtlistener_person_judicial_assigned_case_4_docket_num]

# [170] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[5]/div/article/h4/a | [courtlistener_person_judicial_assigned_case_5]

# [171] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[5]/div/article/h4/a/@href | [courtlistener_person_judicial_assigned_case_5_url]

# [172] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/div[5]/div/article/div[1]/time | [courtlistener_person_judicial_assigned_case_5_filed]

# [173] - XPATH tag: /html/body/div[1]/div[1]/div/div[6]/div/p/a/@href | [courtlistener_person_judicial_assigned_referred_cases_recap_url]

# [174] - BS4 tag:

        # Assign Table06_People Column / - MariaDB Column Name: pvar_bs4_courtlistener_person_judicial_most_recent_oral_arguments_heard
        #pvar_bs4_courtlistener_person_judicial_most_recent_oral_arguments_heard = find(name="h3", class_="oral-arguments-heard").get_text()
#        pvar_bs4_courtlistener_person_judicial_most_recent_oral_arguments_heard = htmlParse.find(name="h3", class_="oral-arguments-heard").get_text()
#        print(htmlParse.find(name="h3", class_="oral-arguments-heard").get_text())

# [175] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[1]/div/article/h4/a | [courtlistener_person_judicial_oral_argument_1]
#                     /html/body/div[1]/div[1]/div/div[6]/div/div[1]/div/article/h4/a # 9TH CIR

# [176] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[1]/div/article/h4/a/@href | [courtlistener_person_judicial_oral_argument_1_url]

# [177] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[1]/div/article/div[1]/time | [courtlistener_person_judicial_oral_argument_1_argued]
#                     /html/body/div[1]/div[1]/div/div[6]/div/div[1]/div/article/div[1]/time # 9TH CIR

# [178] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[1]/div/article/div[2]/span[2] | [courtlistener_person_judicial_oral_argument_1_docket_num]
#                     /html/body/div[1]/div[1]/div/div[6]/div/div[1]/div/article/div[2]/span[2]/@href # 9TH CIR

# [179] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[2]/div/article/h4/a | [courtlistener_person_judicial_oral_argument_2]
#                     /html/body/div[1]/div[1]/div/div[6]/div/div[2]/div/article/h4/a # 9TH CIR

# [180] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[2]/div/article/h4/a/@href | [courtlistener_person_judicial_oral_argument_2_url]
                    
# [181] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[2]/div/article/div[1]/time | [courtlistener_person_judicial_oral_argument_2_argued]

# [182] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[2]/div/article/div[2]/span[2] | [courtlistener_person_judicial_oral_argument_2_docket_num]

# [183] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[3]/div/article/h4/a | [courtlistener_person_judicial_oral_argument_3]

# [184] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[3]/div/article/h4/a/@href | [courtlistener_person_judicial_oral_argument_3_url]

# [185] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[3]/div/article/div[1]/time | [courtlistener_person_judicial_oral_argument_3_argued]

# [186] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[3]/div/article/div[2]/span[2] | [courtlistener_person_judicial_oral_argument_3_docket_num]

# [187] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[4]/div/article/h4/a | [courtlistener_person_judicial_oral_argument_4]

# [188] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[4]/div/article/h4/a/@href | [courtlistener_person_judicial_oral_argument_4_url]

# [189] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[4]/div/article/div[1]/time | [courtlistener_person_judicial_oral_argument_4_argued]

# [190] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[4]/div/article/div[2]/span[2] | [courtlistener_person_judicial_oral_argument_4_docket_num]

# [191] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[5]/div/article/h4/a | [courtlistener_person_judicial_oral_argument_5]

# [192] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[5]/div/article/h4/a/@href | [courtlistener_person_judicial_oral_argument_5_url]

# [193] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[5]/div/article/div[1]/time | [courtlistener_person_judicial_oral_argument_5_argued]

# [194] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/div[5]/div/article/div[2]/span[2] | [courtlistener_person_judicial_oral_argument_5_docket_num]

# [195] - XPATH tag: /html/body/div[1]/div[1]/div/div[7]/div/p[2]/a/@href | [courtlistener_person_judicial_oral_arguments_all_url]
#                     /html/body/div[1]/div[1]/div/div[6]/div/p[2]/a/@href # 9TH CIR


# [196] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[1]/h2/img | [courtlistener_person_judicial_portrait]

# [197] - XPATH tag: /html/body/div[1]/div[1]/div/div[1]/div[1]/h2/img/@href | [courtlistener_person_judicial_portrait_url]


        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Chain Re-Assigning Python Variables for Payload INJECTION to MariaDB Successful!]")

        # Table06_People_SCOTUS MariaDB Payload (RemoteServer Data Recovery)

        #global courtlistener_jurisdiction_dataset
        
        print(f"{courtlistener_jurisdiction_dataset} Decision Payload...")

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Injecting XPATH Python Variable Payload to MariaDB...")

        import pymysql
        import pymysql.cursors
        connection = pymysql.connect(host=f'{dragon_breath_f10_pymysql_hostname}',
          user=f"{dragon_breath_f10_pymysql_username}",
          passwd=f"{dragon_breath_f10_pymysql_password}",
          db=f"{dragon_breath_f10_pymysql_database_name}"
        )

#        import pymysql
#        import pymysql.cursors
#        connection = pymysql.connect(host='localhost',
#          user="brandon",
#          passwd="__VqE3QVAZmDEx__jkabjKKvR7uGcN__",
#          db="FIREDRAGON_EXODUS_CL_DragonBreath_F10_Arrowhead"
#        )
        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - PyMySQL Connected Successfully!")

        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `Current_JSON_CL_Dataset_Exodus_Table06_People` (`courtlistener_person_header_text`,`courtlistener_person_fjc_id`, `courtlistener_person_fjc_id_url`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (bs4_courtlistener_person_header_text, lxml_xpath_courtlistener_person_fjc_id, lxml_xpath_courtlistener_person_fjc_id_url))
                connection.commit()

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Injecting XPATH Python Variable Payload to MariaDB Successful!")

        print(f"Dragon Breath [F.10] - [Table 06/10] - Table06_People - [Nested Function: Table06_People_BS4_LXML_Recovery] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Finished!")


    Table06_People_CheckNullValue(CurrentDecision)

# urllib.HTTPError Example Nested Try/Except Block from StackOverflow 
# Source URL: https://stackoverflow.com/questions/3193060/how-do-i-catch-a-specific-http-error-in-python

#import urllib
#try:
#    urllib.urlopen("some url")
#except urllib.HTTPError as err:
#    try:
#        if err.code == 404:
#            # Handle the error
#        else:
#            raise
#    except:
#        ...

    #print("Nested Function w/ Conditioning Worked!... Exiting...")
    #exit()

def TableX_Free_US_Proxies():
    print("Free US Proxies...")

def TableX_IP_Pools():
    print("IP Pools...")

    def TableX_IP_Pools_Nested_Pool_1():
        print("Nested Pool 1...")

    def TableX_IP_Pools_Nested_Pool_2():
        print("Nested Pool 2...")

    def TableX_IP_Pools_Nested_Pool_3():
        print("Nested Pool 3...")

    def TableX_IP_Pools_Nested_Pool_4():
        print("Nested Pool 4...")

def TableX_Table04_Processed():
    print("Table04 Processed...")

def TableX_Table04_Rejected():
    print("Table04 Rejected...")

def TableX_Table06_SCOTUS_Processed():
    print("Table06_SCOTUS Processed...")

def TableX_Table06_SCOTUS_Rejected():
    print("Table06_SCOTUS Rejected...")

def TableX_Table06_Processed():
    print("Table06 Processed...")

def TableX_Table06_Rejected():
    print("Table06 Rejected...")

def TableX_Table07_SCOTUS_Processed():
    print("Table07_SCOTUS_Processed...")

def TableX_Table07_SCOTUS_Rejected():
    print("Table07_SCOTUS_Rejected...")

def TableX_Table07_Processed():
    print("Table07_Processed...")

def TableX_Table07_Rejected():
    print("Table07_Rejected...")

def TableX_Table08_Processed():
    print("Table08_Processed...")

def TableX_Table08_Rejected():
    print("Table08_Rejected...")

def TableX_Table09_Processed():
    print("Table09_Processed...")

def TableX_Table09_Rejected():
    print("Table09_Rejected...")

def TableX_Timers():
    print("Timers...")

def TableX_Urllib_Requests():
    print("Urllib_Requests...")



def Table10_CL_Exodus_Head_1(CurrentDecision):
        # DATASET: ALL [American_Constitutional_Supreme_and_Mandatory_Case_Law]
        # DATA RECOVERY [American_Constitutional_Supreme_and_Mandatory_Case_Law]
        global courtlistener_jurisdiction_dataset
        print(f"Current American Constitutional Supreme and Mandatory Jurisdiction: {courtlistener_jurisdiction_dataset} ...")
                # Import Additional Python3 Require Module Libraries

def Table00_Exodus_Head_1_Progress():
    print("dataset1/WASH")
    print("dataset2/SCOTUS")

print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Setting Iteration Counter Variable: iteration_count to '0' ...")
logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Setting Iteration Counter Variable: iteration_count to '0' ...")
iteration_count = 0
# irc.libera.chat #python - Repiphany - Thanks :)
     
print("Now Loading Python Module 'json'")
import json
print("Loading Python Module 'json' Successful!")
# FunkyBob - Main Loop Construction - irc.libera.chat #python - 08/xx/22 @ Approx. N/A
def mainloop(json_filenames):
        for current_json_filename in json_filenames:
            global courtlistener_jurisdiction_dataset
            global dir_path
            global iteration_count
            global json_count

            print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Current Iteration Count: {iteration_count}")
            logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Current Iteration Count: {iteration_count}")
            print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Reading Current JSON Datasets Specific .json file: from '{dir_path}wd.json.files.txt'...")
            logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisidiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Reading Current JSON Datasets Specific .json file: from '{dir_path}wd.json.files.txt'...")
            print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiciton Dataset: {courtlistener_jurisdiction_dataset} ] - Now Loading JSON File...")
            logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiciton Dataset: {courtlistener_jurisdiction_dataset} ] - Now Loading JSON File...")

#            with open(current_json_filename.strip()) as src: 
#            -- Thank you JAA for the remedy target - 08/23/2022 @ Approx. 18:20
#            `with open(f'{dir_path}{current_json_filename.strip()}') as src:` should work, I guess. -- JAA's version - 08/23/2022 @ Approx. 19:56 (I prefer mine better)
            with open(f"{dir_path}{current_json_filename}".strip()) as src:
                CurrentDecision = json.load(src)
            print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Current JSON Iteration Count]: {iteration_count}")
            logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Current JSON Iteration Count]: {iteration_count}")
            print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Current JSON Filename]: {current_json_filename}")
            logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Current JSON Filename]: {current_json_filename}")
            print(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Current JSON Casename Absolute URL]: {CurrentDecision['absolute_url']}")
            logging.debug(f"Dragon Breath [F.10] - [Table 01/10] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Current JSON Casename Absolute URL]: {CurrentDecision['absolute_url']}")
            #print(CurrentDecision["absolute_url"])    
            print("Now Checking Current JSON File to Determine Dataset Key Variant...")
        
            print("Checking Current JSON File for Variant A Schema (1 Key)...")
            KeyCheckA(CurrentDecision)
            print("Loop Finished Running Function: 'KeyCheckA(CurrentDecision)'")
            print("Checking Current JSON File for Variant B Schema (2 Keys)...")
            KeyCheckB(CurrentDecision)
            print("Loop Finished Running Function: 'KeyCheckB(CurrentDecision)'")
            print("Checking Current JSON File for Variant C Schema (3 Keys)...")
            KeyCheckC(CurrentDecision)
            print("Loop Finished Running Function: 'KeyCheckC(CurrentDecision)'")
            print("Checking Current JSON File for Variant D Schema (3 Keys)...")
            KeyCheckD(CurrentDecision)
            print("Loop Finished Running Function: 'KeyCheckD(CurrentDecision)'")
            print("Checking Current JSON File for Variant E Schema (4 Keys)...")
            KeyCheckE(CurrentDecision)
            print("Loop Finished Running Function: 'KeyCheckE(CurrentDecision)'")          
            print("Checking Current JSON File for Variant F Schema (4 Keys)...")
            KeyCheckF(CurrentDecision)
            print("Loop Finished Running Function: 'KeyCheckF(CurrentDecision)'")          
            print("Checking Current JSON File for Variant G Schema (5 Keys)...")
            KeyCheckG(CurrentDecision)
            print("Loop Finished Running Function: 'KeyCheckG(CurrentDecision)'")          

            print("Checking Current JSON File for Variant A Schema Final Determination (1 Key)...")
            KeyDeterminationA(CurrentDecision, current_json_filename)
            print("Loop Finished Running Function: 'KeyCheckDeterminationA()'")
            print("Checking Current JSON File for Variant B Schema Final Determination (2 Keys)...")
            KeyDeterminationB(CurrentDecision, current_json_filename)
            print("Loop Finished Running Function: 'KeyCheckDeterminationB()'")
            print("Checking Current JSON File for Variant C Schema Final Determination (3 Keys)...")
            KeyDeterminationC(CurrentDecision, current_json_filename)
            print("Loop Finished Running Function: 'KeyCheckDeterminationC()'")
            print("Checking Current JSON File for Variant D Schema Final Determination (3 Keys)...")
            KeyDeterminationD(CurrentDecision, current_json_filename)
            print("Loop Finished Running Function: 'KeyCheckDeterminationD()'")
            print("Checking Current JSON File for Variant E Schema Final Determination (4 Keys)...")
            KeyDeterminationE(CurrentDecision, current_json_filename)
            print("Loop Finished Running Function: 'KeyCheckDeterminationE()'")
            print("Checking Current JSON File for Variant F Schema Final Determination (4 Keys)...")
            KeyDeterminationF(CurrentDecision, current_json_filename)
            print("Loop Finished Running Function: 'KeyCheckDeterminationF()'")
            print("Checking Current JSON File for Variant G Schema Final Determination (5 Keys)...")
            KeyDeterminationG(CurrentDecision, current_json_filename)
            print("Loop Finished Running Function: 'KeyCheckDeterminationG()'")
            print("Current JSON File Variant Schema Final Determination is:")
            global current_json_dataset_final
            print(current_json_dataset_final)
            if(current_json_dataset_final == "A"):
                print("Current JSON File - Variant [A] Map & Payload Verified!")
                print("Current JSON File - Variant [A] Now Executing Table 01_A Function...")
                Table01_A(CurrentDecision)
            elif(current_json_dataset_final == "B"):
                print("Current JSON File - Variant [B] Map & Payload Verified!")
                print("Current JSON File - Variant [B] Now Executing Table 01_B Function...")
                Table01_B(CurrentDecision)
            elif(current_json_dataset_final == "C"):
                print("Current JSON File - Variant [C] Map & Payload Verified!")
                print("Current JSON File - Variant [C] Now Executing Table 01_C Function...")
                Table01_C(CurrentDecision)
            elif(current_json_dataset_final == "D"):
                print("Current JSON File - Variant [D] Map & Payload Verified!")
                print("Current JSON File - Variant [D] Now Executing Table 01_D Function...")
                Table01_D(CurrentDecision)
            elif(current_json_dataset_final == "E"):
                print("Current JSON File - Variant [E] Map & Payload Verified!")
                print("Current JSON File - Variant [E] Now Executing Table 01_E Function...")
                Table01_E(CurrentDecision)
            elif(current_json_dataset_final == "F"):
                print("Current JSON File - Variant [F] Map & Payload Verified!")
                print("Current JSON File - Variant [F] Now Executing Table 01_F Function...")
                Table01_F(CurrentDecision)
            #else(current_json_dataset_final == "G"):
            else:
                print("Current JSON File - Variant [G] Map & Payload Verified!")
                print("Current JSON File - Variant [G] Now Executing Table 01_G Function...")
                Table01_G(CurrentDecision)
            Table02(CurrentDecision)
            Table03(CurrentDecision, current_json_filename)
            Table04(CurrentDecision)
            #Table04_BS4_LXML_Recovery(CurrentDecision)
            #Table05_People_SCOTUS(CurrentDecision)
            #Table05_People(CurrentDecision)
            #Table05_Summaries_SCOTUS(CurrentDecision)
            #Table05_Summaries(CurrentDecision)
            #Table05_Cites(CurrentDecision)
            #Table05_Authorities(CurrentDecision)
            #Table05_Payload_SCOTUS(CurrentDecision)
            #Table05_Payload(CurrentDecision)
    
            #Table06_People_SCOTUS(CurrentDecision)
            #Table06_People(CurrentDecision)
            #Table07_Summaries_SCOTUS(CurrentDecision)
            #Table07_Summaries(CurrentDecision)
            #Table08_Cites(CurrentDecision)
            #Table09_Authorities(CurrentDecision)
            #Table10_CL_Exodus_Head_1(CurrentDecision)
            
            #print(f"Dragon Breath [F.10] - [Data Recovery - ALL Tables Populated!] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Current JSON Filename]: {current_json_filename}")
            #logging.debug(f"Dragon Breath [F.10] - [Data Recovery - ALL Tables Populated!] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Current JSON Filename]: {current_json_filename}")

            #print(f"Dragon Breath [F.10] - [Data Recovery - ALL Tables Populated!] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Increasing Python Variable by +1: 'iteration_count'") 
            #logging.debug(f"Dragon Breath [F.10] - [Data Recovery - ALL Tables Populated!] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Increasing Python Variable by +1: 'iteration_count'") 
            
            iteration_count = iteration_count+1
            print(f"Dragon Breath [F.10] - [JSON to MariaDB - Table 01 - 04-Part-A Populated!] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Current JSON Filename: {current_json_filename} ] - [Successful Iteration Runs (Unique JSON Files) : {iteration_count} out of Total JSON Files: {json_count}")
            logging.debug(f"Dragon Breath [F.10] - [JSON to MariaDB - Table 01 - 04-Part-A Populated!] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Current JSON Filename: {current_json_filename} ] - [Successful Iteration Runs (Unique JSON Files) : {iteration_count} out of Total JSON Files: {json_count}")
            #print(f"Dragon Breath [F.10] - [Data Recovery - ALL Tables Populated!] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Current JSON Filename: {current_json_filename} ] - [Successful Iteration Runs (Unique JSON Files) : {iteration_count} out of Total JSON Files: {json_count}")
            #logging.debug(f"Dragon Breath [F.10] - [Data Recovery - ALL Tables Populated!] - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - [Current JSON Filename: {current_json_filename} ] - [Successful Iteration Runs (Unique JSON Files) : {iteration_count} out of Total JSON Files: {json_count}")

mainloop(my_match)
# han-solo - irc.libera.chat #python @ Approx. 02:25 - 08/13/2022 - 
# Using Python List w/ contents of .json file list .txt and argument passes for main loop

# Dataset (SCOTUS)
#input(f"Successfully Ran Dataset: {courtlistener_jurisdiction_dataset} JSON Files Against Loop Functions, 'Startup', 'Table01', 'Table02', 'Table03', 'Table04', 'Table04_BS4_LXML_Recovery', 'Table05_People_SCOTUS', 'Table05_Summaries_SCOTUS', 'Table05_Cites', 'Table05_Authorities', 'Table05_SCOTUS_Payload' and 'Table06_People_SCOTUS'... Press ENTER to Exit {dragon_breath_f10}{dragon_breath_f10_codename}{dragon_breath_f10_update_version}!")
input(f"Successfully Ran Dataset: {courtlistener_jurisdiction_dataset} JSON Files Against Loop Functions, 'Startup', 'Table01', 'Table02', 'Table03', 'Table04'... Press ENTER to Exit {dragon_breath_f10}{dragon_breath_f10_codename}{dragon_breath_f10_update_version}!")

# Dataset (Non-SCOTUS)
#input(f"Successfully Ran Dataset: {courtlistener_jurisdiction_dataset} JSON Files Against Loop Functions, 'Startup', 'Table01', 'Table02', 'Table03', 'Table04', 'Table04_BS4_LXML_Recovery', 'Table05_People', 'Table05_Summaries', 'Table05_Cites', 'Table05_Authorities', and 'Table05_Payload'... Press ENTER to Exit {dragon_breath_f10}{dragon_breath_f10_codename}{dragon_breath_f10_update_version}!")


dragon_breath_f10_end_time = time.time()

dragon_breath_f10_elapsed_time = dragon_breath_f10_end_time - dragon_breath_f10_start_time

print(f'{dragon_breath_f10} {dragon_breath_f10_codename}{dragon_breath_f10_update_version} - Execution Time:', time.strftime("Hours: %H: Minutes: %M: Seconds: %S", time.gmtime(dragon_breath_f10_elapsed_time)))

# Update Overall Progress of EXODUS courtlistener.com Head 1/4
#Table00_Exodus_Head_1_Progress()

# Table 9/10:

#import table_functions.table09
#table_functions.table09.table09()

# Table 10/10:

#import table_functions.table10
#table_functions.table10.table10()

# Dragon Breath F.10 - (Update 5) - Table 11/11 - Statistics/Parsing Progress:

#import table_functions.table11
#table_functions.table11.table11()


#### Requests Error Handling (Need Similiar for urllib Request):

    # Part 1/2: (Proxy Requests from ScrapeHero)
    # Source URL: https://scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/

#    import requests
#    url = "https://httpbin.org/ip"
#    proxies = {
#    "http": 'http://209.50.52.162:9050'
#    "https": 'http://209.50.52.162:9050'
#    }
#    response = requests.get(url,proxies=proxies)
#    print(response.json())

    # Part 1/2: (Error Handling from StackOverflow) (Requests, NOT urllib Request):
    # Source URL: https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
    

#    url = "http://www.google.com/blahblah"

#    try:
#        r = requests.get(url,timeout=3)
#        r.raise_for_status()
#    except requests.exceptions.HTTPError as errh:
#        print("Http Error:",errh)
#    except requests.exceptions.ConnectionError as errc:
#        print("Error Connecting:",errc)
#    except requests.exceptions.Timeout as errt:
#        print("Timeout Error:",errt)
#    except requests.exceptions.RequestException as err:
#        print("OOps: Something Else",err)

    # Part 1/2: (Error Handling - Codes) (HTTP In General)
    # Source URL: https://www.codegrepper.com/code-examples/python/urllib_errors

    # Table mapping response codes to messages; entries have the
# form {code: (shortmessage, longmessage)}.
# responses = {
#    100: ('Continue', 'Request received, please continue'),
#    101: ('Switching Protocols',
#          'Switching to new protocol; obey Upgrade header'),

#    200: ('OK', 'Request fulfilled, document follows'),
#    201: ('Created', 'Document created, URL follows'),
#    202: ('Accepted',
#          'Request accepted, processing continues off-line'),
#    203: ('Non-Authoritative Information', 'Request fulfilled from cache'),
#    204: ('No Content', 'Request fulfilled, nothing follows'),
#    205: ('Reset Content', 'Clear input form for further input.'),
#    206: ('Partial Content', 'Partial content follows.'),

#    300: ('Multiple Choices',
#          'Object has several resources -- see URI list'),
#    301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
#    302: ('Found', 'Object moved temporarily -- see URI list'),
#    303: ('See Other', 'Object moved -- see Method and URL list'),
#    304: ('Not Modified',
#          'Document has not changed since given time'),
#    305: ('Use Proxy',
#          'You must use proxy specified in Location to access this '
#          'resource.'),
#    307: ('Temporary Redirect',
#          'Object moved temporarily -- see URI list'),

#    400: ('Bad Request',
#          'Bad request syntax or unsupported method'),
#    401: ('Unauthorized',
#          'No permission -- see authorization schemes'),
#    402: ('Payment Required',
#          'No payment -- see charging schemes'),
#    403: ('Forbidden',
#          'Request forbidden -- authorization will not help'),
#    404: ('Not Found', 'Nothing matches the given URI'),
#    405: ('Method Not Allowed',
#          'Specified method is invalid for this server.'),
#    406: ('Not Acceptable', 'URI not available in preferred format.'),
#    407: ('Proxy Authentication Required', 'You must authenticate with '
#          'this proxy before proceeding.'),
#    408: ('Request Timeout', 'Request timed out; try again later.'),
#    409: ('Conflict', 'Request conflict.'),
#    410: ('Gone',
#          'URI no longer exists and has been permanently removed.'),
#    411: ('Length Required', 'Client must specify Content-Length.'),
#    412: ('Precondition Failed', 'Precondition in headers is false.'),
#    413: ('Request Entity Too Large', 'Entity is too large.'),
#    414: ('Request-URI Too Long', 'URI is too long.'),
#    415: ('Unsupported Media Type', 'Entity body in unsupported format.'),
#    416: ('Requested Range Not Satisfiable',
#          'Cannot satisfy request range.'),
#    417: ('Expectation Failed',
#          'Expect condition could not be satisfied.'),

#    500: ('Internal Server Error', 'Server got itself in trouble'),
#    501: ('Not Implemented',
#          'Server does not support this operation'),
#    502: ('Bad Gateway', 'Invalid responses from another server/proxy.'),
#    503: ('Service Unavailable',
#          'The server cannot process the request due to a high load'),
#    504: ('Gateway Timeout',
#          'The gateway server did not receive a timely response'),
#    505: ('HTTP Version Not Supported', 'Cannot fulfill request.'),
#    }


# Code For CL_Exodus_Head_2
def Table09(CurrentDecision):
    print("Table7? /cites next pages...")

    # Table 5 import from table10.u1.py

    # Table 5 Mod - Request save /author page

    # Table 5 Mod - Request save courtlistener_cites_url

    # Table 5 Mod - Request save courtlistener_summary_url

    # Table 5 Mod - Request save courtlistener_authorities_url

    # Table 5 Mod - lxml scrape courtlistener_cites_url -> :

    # Assign Table5 Column x / - MariaDB Column Name: courtlistener_cites_page_count
    print(f"Dragon Breath [F.10] - [Table x/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable x out of ...")
    pvar_dom_xpath_courtlistener_cites_page_count = dom.xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div/div[2]/div')[0].text.strip()
    if len(pvar_dom_xpath_courtlistener_cites_page_count) !=0:
        print(pvar_dom_xpath_courtlistener_cites_page_count)
    else:
        pvar_dom_xpath_courtlistener_cites_page_count = "(NULL)"
    print(pvar_dom_xpath_courtlistener_cites_page_count)

    # Assign Table4 Column x / - MariaDB Column Name: courtlistener_cites_page_next
    print(f"Dragon Breath [F.10] - [Table x/10] - Table04_RemoteServer - [CL Jurisdiction Dataset: {courtlistener_jurisdiction_dataset} ] - Now Assigning Table04 Column Python Variable x out of ...")
    pvar_dom_xpath_courtlistener_cites_page_next = dom.xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div/div[3]')[0].text.strip()
    if len(pvar_dom_xpath_courtlistener_cites_page_next) !=0:
        print(pvar_dom_xpath_courtlistener_cites_page_next)
    else:
        pvar_dom_xpath_courtlistener_cites_page_next = "(NULL)"
    print(pvar_dom_xpath_courtlistener_cites_page_next)


def Table04_Timer(CurrentDecision):
    print("Dragon Breath [F.10] - [Table 04-05/10] - Random Timer for Remote Server Respect...")
