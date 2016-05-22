{
  'targets': [
    {
      'target_name': 'libSkiaSharp',
      'type': 'shared_library',
      'include_dirs' : [
        '../include/c',
		'../include/core',
        '../include/config',
        '../include/images',
        '../src/c',
      ],
      'sources': [
        '../../native-builds/src/sk_xamarin.cpp',
        '../../native-builds/src/SkiaKeeper.c',
        '../../native-builds/src/sk_managedstream.cpp',
        '../../native-builds/src/SkManagedStream.cpp',
        '../../native-builds/src/sk_xamarin.cpp',
      ],
      'dependencies': [
        'skia_lib.gyp:skia_lib',
      ],
    },
  ],
}
