# `analyzer-ensure-no-failure-on-unparseable-records`

This image is for testing that analysis doesn't fail when encountering unparseable entries.

Currently it contains an rpmdb with some records that the upstream library that syft uses cannot parse, but syft >= 0.56.0 should no longer fail and just log a warning per package that could not be parsed: https://github.com/anchore/syft/pull/1200


