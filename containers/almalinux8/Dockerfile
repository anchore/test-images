FROM almalinux:8.7

RUN \
    dnf -y install --nogpgcheck \
    python3 \
    python3-pip \
    php \
    npm \
    nodejs

RUN dnf -y downgrade --nogpgcheck python3-pip

