# Check that all Makefiles in the containers directory are linked to the ContainerMakefile in the root

# This list of exclusions is here to allow specific Makefiles to not be linked to the ContainerMakefile
# These makefiles are expected to be doing unique things, such as building multi-arch images
makefile_link_exclusions=('containers/alpine-multiarch-no-amd64' 'containers/alpine-multiarch-amd64-windows-linux')

for makefile in $(find containers -name Makefile); do
    echo -n "Verifying Makefile link: $makefile";
    if [[ $(readlink $makefile) != "../../ContainerMakefile" ]]; then
        exclude=false
        for i in "${makefile_link_exclusions[@]}"; do
            if [[ ${makefile} == *$i* ]]; then
                echo "	[SKIPPED]";
                exclude=true
            fi;
        done
        if [[ $exclude == true ]]; then
            continue
        fi;
        echo "Path is not linked to ../../ContainerMakefile -> ${makefile}" && exit 1;
    fi;
    echo "	[OK]";
done