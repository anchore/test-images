# `vulnerabilities-package-name-normalization`
Ensures that vulnerability matching works as expected with package name normalization across ecosystems.

This will initially be used in the `grype-db-builder` acceptace tests to ensure matching works as expected across schemas.

Grype database schemas prior to v4 should produce something like the following because names aren't normalized within grype
or in the database, resulting in several missed vulnerability matches.
```
NAME                           INSTALLED  FIXED-IN  TYPE    VULNERABILITY        SEVERITY
Products.PluggableAuthService  2.5        2.6.0     python  GHSA-p75f-g7gx-2r7p  Low
Products.PluggableAuthService  2.5        2.6.1     python  GHSA-p44j-xrqg-4xrr  Low
Products.PluggableAuthService  2.5        2.6.2     python  GHSA-35rg-466w-77h3  Medium
PyYAML                         5.1        5.4       python  GHSA-8q59-q68h-6hv4  Critical
aiohttp-session                2.3.0      2.4.0     python  GHSA-fpwp-69xv-c67f  Medium
aiohttp-session                2.3.0      2.7.0     python  GHSA-mr4x-c4v9-x729  Medium
oslo.middleware                3.20.0     3.23.1    python  GHSA-xcp8-hh74-f6mc  Medium
oslo.middleware                3.20.0               python  CVE-2017-2592        Medium
sopel-plugins.channelmgnt      1.0.0      2.0.1     python  GHSA-23c7-6444-399m  High
```

Grype database schemas starting with v4 should produce extra matches, something like:
```
NAME                           INSTALLED  FIXED-IN  TYPE    VULNERABILITY        SEVERITY
Products.PluggableAuthService  2.5        2.6.1     python  GHSA-p44j-xrqg-4xrr  Low
Products.PluggableAuthService  2.5        2.6.0     python  GHSA-p75f-g7gx-2r7p  Low
Products.PluggableAuthService  2.5        2.6.2     python  GHSA-35rg-466w-77h3  Medium
PyYAML                         5.1        5.2       python  GHSA-3pqx-4fqf-j49f  High
PyYAML                         5.1        5.3.1     python  GHSA-6757-jp84-gxfx  High
PyYAML                         5.1        5.4       python  GHSA-8q59-q68h-6hv4  Critical
aiohttp-session                2.3.0      2.7.0     python  GHSA-mr4x-c4v9-x729  Medium
aiohttp-session                2.3.0      2.4.0     python  GHSA-fpwp-69xv-c67f  Medium
oslo.middleware                3.20.0     3.23.1    python  GHSA-xcp8-hh74-f6mc  Medium
oslo.middleware                3.20.0               python  CVE-2017-2592        Medium
sopel-plugins.channelmgnt      1.0.0      2.0.1     python  GHSA-23c7-6444-399m  High
sopel-plugins.channelmgnt      1.0.0      1.0.3     python  GHSA-j257-jfvv-h3x5  High
url-regex                      1.0.0                python  GHSA-hg3w-7hj9-m3f7  Medium
```
