# `java`
Adds Java packages to an Alpine image, no need to actually install the Java runtime in the image itself. There is an important difference
between current analyzers and `syft`, where `syft` is going to have better accuracy for nested Java packages. There has to be support for these 5 types of Java packages:

* jar
* war
* ear
* jpi
* hpi

Note that this workflow omits `jpi` since it is considered equal to `hpi`.

Note: nomad has been added to include a vulnerability CVE-2021-21681.
