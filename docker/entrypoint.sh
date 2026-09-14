#!/bin/bash
set -e

# Load ROS 2 Humble environment
source /opt/ros/humble/setup.bash

# Load workspace environment jika sudah di-build
if [ -f /ws/install/setup.bash ]; then
    source /ws/install/setup.bash
fi

exec "$@"
