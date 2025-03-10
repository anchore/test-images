# Check that all Makefiles in the containers directory are linked to the ContainerMakefile in the root

# This list of exclusions is here to allow specific Makefiles to not be linked to the ContainerMakefile
# These makefiles are expected to be doing unique things, such as building multi-arch images
makefile_link_exclusions=('containers/alpine-multiarch-no-amd64')

for makefile in $(find containers -name Makefile); do
    echo -n "Verifying Makefile link: $makefile";
    if [[ $(readlink $makefile) != "../../ContainerMakefile" ]]; then
        if [[ ${makefile} == *${makefile_link_exclusions}* ]]; then
            echo "	[SKIPPED]";
            continue;
        fi;
        echo "Path is not linked to ../../ContainerMakefile -> $${makefile}" && exit 1;
    fi;
    echo "	[OK]";
done