#!/usr/bin/env bash
set -uxe

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
PKGSDIR="build"

cd "$SCRIPTPATH/../"



# note: this can be easily done in a 1-liner, however circle CI does NOT allow volume mounts from the host in docker executors (since they are on remote hosts, where the host files are inaccessible)

CTRID=$(docker create -u "$(id -u):$(id -g)" -v /example-java-app -w /example-java-app gradle:jdk gradle build)

function cleanup() {
  docker rm "${CTRID}"
}

trap cleanup EXIT
set +e

docker cp "$(pwd)/example-java-app" "${CTRID}:/"
docker start -a "${CTRID}"
mkdir -p "$PKGSDIR"
docker cp "${CTRID}:/example-java-app/build/libs/example-java-app-gradle-0.1.0.ear" "$PKGSDIR"
