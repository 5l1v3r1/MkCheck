<p align="center">
 <img align="center" src="https://raw.githubusercontent.com/s1l3nt78/Private/master/Photos/mcheck.PNG" />
<br />
 <img align="center" src="https://img.shields.io/github/issues/s1l3nt78/MCheck" />
 <img align="center" src="https://img.shields.io/github/forks/s1l3nt78/MCheck" />
 <img align="center" src="https://img.shields.io/github/stars/s1l3nt78/MCheck" />
 <br />
 <img align="center" src="https://img.shields.io/badge/Build-Alfa-orange" />
 <img align="center" src="https://img.shields.io/badge/Version-0.2-red" />
 <br />
  <img align="center" src="https://img.shields.io/badge/Author-s1l3nt78-yellowgreen" />
</p>
<br />
<br />

# MCheck
*s1l3nt78*

# Functions

  MCheck is used to check MikroTik Routers for winbox_auth_bypass_creds_disclosure & routeros_jailbreak
  <br>
    -If routersploit module (in development) confirms the Mikrotik device is vulnerable it parses the credentials into the miko.py script.
  <br>
  <br>
  The main function spawns a quick ssh session on the compromised machine to enumerate the Net AP name from IP
  <br>
    -Once the Network AP Name has been found the attacker can use the IP and login credentials to work with
     Mikrotik Routers config from a web-session.
    <br>
    <br>
    
# USAGE

  -The user must create the 'scripts/tiks.txt' list with MikroTik Router IP's.
  <br>
  -Easiest way to do this is using bulk nMap scrapes or Shodan.
    <br>
    Once the attacker has a specific netblock <eg. 111.69.145.1/24>, the best way to create the list is using Microsoft Excel
    As you need to fill in the first block (111.69.145.1), then you can drag the coloum to quickly fill the IP's in the colom.
    Then copy the entire block into the 'scripts/tiks.txt' file.


# TODO

  Incorporation of routersploit to do automatic vuln checks for the MikroTik Router firmware.
  For now manual checks must be done by user.
  
