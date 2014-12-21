#!/bin/bash
currentDir=`pwd`

 buildV8 (){

 	 printf '\e[1;34m%-6s\e[m \n' "Create Directories"
	 mkdir -p BuildOutput/{Debug,Release}
	 mkdir -p Source/V8.NET-Proxy/out

	printf '\e[1;34m%-6s\e[m \n' "Init V8 Submodule"
 	git submodule update --init --recursive
	cd $currentDir
	cd Source/V8.NET-Proxy/V8/
	printf '\e[1;34m%-6s\e[m \n' "Building V8 "
	printf '\e[1;34m%-6s\e[m \n' "Version 3.29.40 (based on bleeding_edge revision r23628)"
	printf '\e[1;34m%-6s\e[m \n' "commit 21d700eedcdd6570eff22ece724b63a5eefe78cb"
	printf '\e[1;34m%-6s\e[m \n' "make builddeps -j ${JOBSV8=$1}"
	make builddeps -j ${JOBSV8=$1}
	printf '\e[1;34m%-6s\e[m \n' "make native library=shared -j ${JOBSV8=$1}"
	make native library=shared -j ${JOBSV8=$1}
}

 buildV8Proxy (){
	cd $currentDir
	
     printf '\e[1;34m%-6s\e[m \n' "Create Directories"
	 mkdir -p BuildOutput/{Debug,Release}
	 mkdir -p Source/V8.NET-Proxy/out

	cd Source/V8.NET-Proxy/
	printf '\e[1;34m%-6s\e[m \n' "Build V8DotNet Proxy"
	ls | grep cpp | awk -F. '{ system("g++ -g -std=c++11 -w -fpermissive -fPIC  -lstdc++ -Wl,--gc-sections   -c -IV8/ -I/usr/include/glib-2.0/ -I/usr/lib/x86_64-linux-gnu/glib-2.0/include/ "$1".cpp -o out/"$1".o ") }'
	cd out
	cp ../V8/out/native/lib.target/libicui18n.so .
	cp ../V8/out/native/lib.target/libicuuc.so .
	cp ../V8/out/native/lib.target/libv8.so .
	g++  -g -Wall -std=c++11 -shared -fPIC -I../ -I../V8/ -I/usr/include/glib-2.0/ -I/usr/lib/x86_64-linux-gnu/glib-2.0/include/   -Wl,-soname,libV8_Net_Proxy.so  -o libV8_Net_Proxy.so *.o ../V8/out/native/obj.host/testing/libgtest.a ../V8/out/native/obj.target/testing/libgmock.a ../V8/out/native/obj.target/testing/libgtest.a ../V8/out/native/obj.target/third_party/icu/libicudata.a ../V8/out/native/obj.target/tools/gyp/libv8_base.a ../V8/out/native/obj.target/tools/gyp/libv8_libbase.a ../V8/out/native/obj.target/tools/gyp/libv8_libplatform.a ../V8/out/native/obj.target/tools/gyp/libv8_nosnapshot.a ../V8/out/native/obj.target/tools/gyp/libv8_snapshot.a  -Wl,-rpath,. -L. -L../  -lpthread  -lstdc++ -licui18n -licuuc -lv8 -lglib-2.0 -lrt  -Wl,--verbose
	cp *.so ../../../BuildOutput/Debug
	cp *.so ../../../BuildOutput/Release
}

 buildV8DotNet (){
	cd $currentDir

	 printf '\e[1;34m%-6s\e[m \n' "Create Directories"
	 mkdir -p BuildOutput/{Debug,Release}
	 mkdir -p Source/V8.NET-Proxy/out
	
	/opt/monodevelop/lib/monodevelop/bin/mdtool.exe -v build "--configuration:Release" "Source/V8.Net.MonoDevelop.sln"
	/opt/monodevelop/lib/monodevelop/bin/mdtool.exe -v build "--configuration:Debug" "Source/V8.Net.MonoDevelop.sln"
	cp Source/V8.NET-Console/bin/Debug/* BuildOutput/Debug/
	cp Source/V8.NET-Console/bin/Release/* BuildOutput/Release/
}
 function helptext {
     echo -e $USAGE
    exit 1;
}


USAGE="$(basename "$0") [-h] [-l] [-d jobs] [-v8 jobs] -- program to build V8DotNet\n\n

Use: [$(basename "$0") --default 4] to build all\n\n

where:\n
    -h,  --help:     \t Show this help text\n
    -l,  --lib:      \t libV8_Net_Proxy.so only\n
    -v8, --v8:       \t Build Google V8 only \n
    -w, --w:         \t Build v8 wrapper \n
    -d, --default:   Build V8DotNet with extern Google V8\n\n

    param jobs: specifies the number of parallel build processes. Set it (roughly) to the number of CPU cores your machine has. 
    The GYP/make based V8 build also supports distcc, so you can compile with -j100 or so, provided you have enough machines around." 
    
if [ $# == 0 ] ; then
    echo -e $USAGE
    exit 1;
fi
#######################################

while [[ $# > 0 ]]
do
key="$1"
shift

case $key in
    -l|--lib)
    buildV8Proxy
    shift
    ;;
    -d|--default)
	JOBSV8=$1
    buildV8
    buildV8Proxy
    buildV8DotNet
    shift
    ;;
    -v8|--v8)
	JOBSV8=$1
    buildV8
    shift
    ;;
    -w|--w)
    buildV8DotNet
    shift
    ;;
    -h|--help)
    helptext
    shift
    ;;
    *)
            # unknown option
    ;;
esac
done