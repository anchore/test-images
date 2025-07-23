# FALSE POSITIVE test case: RHEL vulnerability data on AlmaLinux systems
# CVE-2022-32091 (mariadb) - AlmaLinux fixed earlier than RHEL

FROM almalinux:8

# Install MariaDB with specific version that creates false positive scenario:
# - AlmaLinux fix: 3:10.3.39-1.module_el8.8.0+3609+204d4ab0 (earlier)
# - RHEL fix: 3:10.3.39-1.module+el8.8.0+19673+72b0d35f (later)
# - Available version: 3:10.3.39-1.module_el8.8.0+3609+204d4ab0 (equals AlmaLinux fix)
# - Module: mariadb:10.3

RUN dnf module enable mariadb:10.3 -y && \
    dnf install -y mariadb-3:10.3.39-1.module_el8.8.0+3609+204d4ab0 && \
    dnf clean all

# Expected results when scanning this container for CVE-2022-32091:
# - RHEL-based scanner: Reports as VULNERABLE (version < RHEL fix)
# - AlmaLinux-aware scanner: Reports as FIXED (version = AlmaLinux fix)
#
# This demonstrates why vulnerability scanners need distribution-specific
# vulnerability data rather than assuming RHEL data applies to AlmaLinux.

# Set the default command to show MariaDB installation info when container runs
CMD ["/bin/bash", "-c", "rpm -q mariadb && \
    echo \"=== MARIADB MODULARITYLABEL CHECK ===\" && \
    rpm -qa --qf \"%{\\nNAME}-%{VERSION}-%{RELEASE} %{MODULARITYLABEL}\\n\" | grep mariadb && \
    echo \"=== MARIADB MODULE STATUS ===\" && \
    dnf module list mariadb"]
