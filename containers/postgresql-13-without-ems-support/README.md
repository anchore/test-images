## postgresql-13-without-ems-support
This image allows testing against a Postgresql 13 server without support for the Extended Master Secrets (EMS) TLS extension which is required to be enabled for all TLS connections prior to 1.3 when on a FIPS 104-3 compliant host.

This essentially recreates the [PostgreSQL 13 official Docker image](https://github.com/docker-library/postgres/blob/ab6925051ca097d415816928a50c483ecc370c00/13/bookworm/Dockerfile) on top of Amazon Linux 2 (which does not support EMS by default)
