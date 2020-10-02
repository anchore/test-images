# `lean`
This container was created initially to ensure parity in Anchore Engine analyzers with `syft` output. The idea is to make the resulting container
image as lean as possible.

This process means that some oddities are present like:

* Ruby packages are installed, but there is no Ruby interpreter present.
