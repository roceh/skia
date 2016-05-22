Skia is a complete 2D graphic library for drawing Text, Geometries, and Images.

See full details, and build instructions, at https://skia.org.

Raspberry Pi build for libSkiaSharp is like the linux build:

https://skia.org/user/quick/linux

except you will have to get the dependacies manually if on raspbian and instead of 

```
bin/sync-and-gyp"
```

do

```
GYP_DEFINES='skia_arch_type=arm' python bin/sync-and-gyp
```

and to build the library

```
ninja -C out/Debug libSkiaSharp
```

I also had to build ninja for raspbian:

```
git clone https://github.com/martine/ninja.git -b v1.7.1
cd ninja && ./configure.py --bootstrap
```

and mv the built ninja into depot_tools

For the .net skiasharp assembly use the generic build
