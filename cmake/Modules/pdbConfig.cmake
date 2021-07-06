INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_PDB pdb)

FIND_PATH(
    PDB_INCLUDE_DIRS
    NAMES pdb/api.h
    HINTS $ENV{PDB_DIR}/include
        ${PC_PDB_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    PDB_LIBRARIES
    NAMES gnuradio-pdb
    HINTS $ENV{PDB_DIR}/lib
        ${PC_PDB_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/pdbTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(PDB DEFAULT_MSG PDB_LIBRARIES PDB_INCLUDE_DIRS)
MARK_AS_ADVANCED(PDB_LIBRARIES PDB_INCLUDE_DIRS)
