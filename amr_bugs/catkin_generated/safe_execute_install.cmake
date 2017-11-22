execute_process(COMMAND "/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_bugs/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/kishaan/catkin_ws/src/ws17-kkisha2s/amr_bugs/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
