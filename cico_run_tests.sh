#!/bin/bash

set -ex

prep() {
    yum -y update
    yum -y install epel-release
    yum -y install python34 python34-virtualenv which libarchive
    yum -y install gcc git
}

prep
./runtests.sh
