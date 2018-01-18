#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/kishaan/catkin_ws/src/team07/amr_localization"

# snsure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/kishaan/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/kishaan/catkin_ws/install/lib/python2.7/dist-packages:/home/kishaan/catkin_ws/src/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/kishaan/catkin_ws/src" \
    "/home/kishaan/anaconda2/bin/python" \
    "/home/kishaan/catkin_ws/src/team07/amr_localization/setup.py" \
    build --build-base "/home/kishaan/catkin_ws/src/team07/amr_localization" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/kishaan/catkin_ws/install" --install-scripts="/home/kishaan/catkin_ws/install/bin"
