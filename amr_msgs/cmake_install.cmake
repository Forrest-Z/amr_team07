# Install script for directory: /home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/home/kishaan/catkin_ws/install")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/amr_msgs/msg" TYPE FILE FILES
    "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/msg/Cone.msg"
    "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/msg/Obstacle.msg"
    "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/msg/PathExecutionFailure.msg"
    "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/msg/Ranges.msg"
    "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/msg/WheelSpeeds.msg"
    "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/msg/Frontiers.msg"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/amr_msgs/action" TYPE FILE FILES
    "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/action/ExecutePath.action"
    "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/action/MoveTo.action"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/amr_msgs/msg" TYPE FILE FILES
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/ExecutePathAction.msg"
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/ExecutePathActionGoal.msg"
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/ExecutePathActionResult.msg"
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/ExecutePathActionFeedback.msg"
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/ExecutePathGoal.msg"
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/ExecutePathResult.msg"
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/ExecutePathFeedback.msg"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/amr_msgs/msg" TYPE FILE FILES
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/MoveToAction.msg"
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/MoveToActionGoal.msg"
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/MoveToActionResult.msg"
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/MoveToActionFeedback.msg"
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/MoveToGoal.msg"
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/MoveToResult.msg"
    "/home/kishaan/catkin_ws/devel/share/amr_msgs/msg/MoveToFeedback.msg"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/amr_msgs/cmake" TYPE FILE FILES "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/catkin_generated/installspace/amr_msgs-msg-paths.cmake")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/kishaan/catkin_ws/devel/include/amr_msgs")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/kishaan/catkin_ws/devel/share/common-lisp/ros/amr_msgs")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/home/kishaan/anaconda2/bin/python" -m compileall "/home/kishaan/catkin_ws/devel/lib/python2.7/dist-packages/amr_msgs")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/kishaan/catkin_ws/devel/lib/python2.7/dist-packages/amr_msgs")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/catkin_generated/installspace/amr_msgs.pc")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/amr_msgs/cmake" TYPE FILE FILES "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/catkin_generated/installspace/amr_msgs-msg-extras.cmake")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/amr_msgs/cmake" TYPE FILE FILES
    "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/catkin_generated/installspace/amr_msgsConfig.cmake"
    "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/catkin_generated/installspace/amr_msgsConfig-version.cmake"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/amr_msgs" TYPE FILE FILES "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_msgs/package.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

