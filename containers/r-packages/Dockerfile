# hadolint ignore=DL3006
FROM rocker/r-ver:4.3.2

# Install specific (non-latest) versions of R packages for testing
# Uses remotes::install_version() to get exact versions from CRAN archive
# hadolint ignore=DL3059
RUN R -e "install.packages('remotes', repos='https://cloud.r-project.org')" && \
    R -e "remotes::install_version('commonmark', version='1.8.1', repos='https://cloud.r-project.org')" && \
    R -e "remotes::install_version('plotly', version='4.10.0', repos='https://cloud.r-project.org')" && \
    R -e "remotes::install_version('gdata', version='3.0.0', repos='https://cloud.r-project.org')" && \
    R -e "remotes::install_version('haven', version='2.5.3', repos='https://cloud.r-project.org')" && \
    rm -rf /tmp/downloaded_packages /tmp/*.rds
