# `vulnerabilities-alpine`
An Alpine base image with openjdk 11, python 3.8, ruby 2.7.2, and nodejs 12.21. 
Includes the following packages:

* ftpd 0.2.1 (gem) [CVE-2013-2512](https://nvd.nist.gov/vuln/detail/CVE-2013-2512)
* xmldom 0.5.0 (npm) [CVE-2021-21366](https://nvd.nist.gov/vuln/detail/CVE-2021-21366)
* aiohttp 3.7.3 (python) [CVE-2021-21330](https://nvd.nist.gov/vuln/detail/CVE-2021-21330)
* guava 23.0 (java) [CVE-2020-8908](https://nvd.nist.gov/vuln/detail/CVE-2020-8908)

Used in policy engine tests.
