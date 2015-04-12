{  
   'variables':{  
      'base_dir%':'<(base_dir)',
      'target_arch%':'x64',
      'build_option%':'release',

   },
   'targets':[  
      {  
         'target_name':'libV8_Net_Proxy',
         'type':'shared_library',
         'toolsets': [ 'target' ],
         'msvs_guid':'5ECEC9E5-8F23-47B6-93E0-C3B328B3BE65',
         'include_dirs':[  
            'Source/V8.NET-Proxy/V8/',
            'io.js/src',
            'io.js/deps/cares',
            'io.js/deps/debugger-agent',
            'io.js/deps/http_parser',
            'io.js/deps/mdb_v8',
            'io.js/deps/npm',
            'io.js/deps/openssl',
            'io.js/deps/uv',
            'io.js/deps/v8',
            'io.js/deps/zlib',
         ],
         'sources':[  
            'Source/V8.NET-Proxy/Exports.cpp',
            'Source/V8.NET-Proxy/FunctionTemplateProxy.cpp',
            'Source/V8.NET-Proxy/HandleProxy.cpp',
            'Source/V8.NET-Proxy/ObjectTemplateProxy.cpp',
            'Source/V8.NET-Proxy/Utilities.cpp',
            'Source/V8.NET-Proxy/V8EngineProxy.cpp',
            'Source/V8.NET-Proxy/ValueProxy.cpp',
            'Source/V8.NET-Proxy/ProxyTypes.h',
         ],
         'conditions':[  
            ['OS=="linux"',
               { 
                  'defines': ['_LINUX'],
                  'cflags':[  
                     ' -pthread  -fpermissive  -m64 -fno-strict-aliasing -fPIC -m64 -O3 -ffunction-sections -fdata-sections -fno-omit-frame-pointer -fdata-sections -ffunction-sections -O3 -fno-rtti   -fexceptions -std=gnu++0x  ',
                  ],
                  'ldflags':[  
                     '-pthread  -fpermissive  -m64 -fno-strict-aliasing -fPIC -m64 -O3 -ffunction-sections -fdata-sections -fno-omit-frame-pointer -fdata-sections -ffunction-sections -O3 -fno-rtti   -fexceptions -std=gnu++0x ',
                  ],
                  'copies':[  
                     {  
                        'destination':'<(PRODUCT_DIR)/../../',
                        'files':[  
                           #'Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/lib.target/libv8.so',
                        ],
                     }
                  ],
                  'link_settings':{  
                     'libraries':[  
                       # '<(base_dir)/io.js/out/Release/libcares.a',
                       # '<(base_dir)/io.js/out/Release/libchrome_zlib.a',
                       # '<(base_dir)/io.js/out/Release/libdebugger-agent.a',
                       # '<(base_dir)/io.js/out/Release/libhttp_parser.a',
                       # '<(base_dir)/io.js/out/Release/libnode.a',
                       # '<(base_dir)/io.js/out/Release/libopenssl.a',
                       # '<(base_dir)/io.js/out/Release/libuv.a',
                        '<(base_dir)/io.js/out/Release/libv8.a',
                        '<(base_dir)/io.js/out/Release/libv8_base.a',
                        '<(base_dir)/io.js/out/Release/libv8_libbase.a',
                        '<(base_dir)/io.js/out/Release/libv8_libplatform.a',
                        '<(base_dir)/io.js/out/Release/libv8_nosnapshot.a',
                        '<(base_dir)/io.js/out/Release/libv8_snapshot.a',
                     ]
                  },
               }
            ],
            ['OS=="mac"',
            {
                   'defines': ['_OSX',],
                   'xcode_settings': {
                         'ARCHS': ['i386'],
                         'GCC_CW_ASM_SYNTAX' : ['NO'],
                         'GCC_ENABLE_PASCAL_STRINGS' : ['NO'],
                         'OTHER_CPLUSPLUSFLAGS' : ['-std=gnu++11  -fpermissive '],
                         'OTHER_LDFLAGS': ['-std=gnu++11 -fpermissive '],
                         'OTHER_CFLAGS': [ '-std=gnu++11 -fpermissive ']
                   },
                  'copies':[  
                     {  
                        'destination':'<(PRODUCT_DIR)/../../',
                        'files':[  
                           'Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libv8.dylib',
                        ],
                     }
                  ],
                  'link_settings':{  
                     'libraries':[  
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libgmock.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libgmock_main.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libgtest.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libgtest_main.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libv8_base.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libv8_libbase.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libv8_libplatform.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libv8_nosnapshot.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libv8_snapshot.a',
                     ]
                  },
               }
            ] ,
            ['OS=="win"',
            {
               'defines': [
               '_WIN',
               '_MSC_PLATFORM_TOOLSET=120',
               ],
                'msvs_settings':{
                  'VCCLCompilerTool':{
                      'RuntimeLibrary': '0',
                        'Optimization':  '0' ,
                  },
                  'VCLinkerTool':{
                    'AdditionalDependencies': [
                        '<(base_dir)\\io.js\\build\\Release\\lib\\v8.lib',
                        '<(base_dir)\\io.js\\build\\Release\\lib\\v8_base.lib',
                        '<(base_dir)\\io.js\\build\\Release\\lib\\v8_libbase.lib',
                        '<(base_dir)\\io.js\\build\\Release\\lib\\v8_libplatform.lib',
                        '<(base_dir)\\io.js\\build\\Release\\lib\\v8_nosnapshot.lib',
                        '<(base_dir)\\io.js\\build\\Release\\lib\\v8_snapshot.lib',
                    ]
                  },
                  'VCMIDLTool':{

                  },
                  'VCResourceCompilerTool':{

                  },
                  'VCLibrarianTool':{

                  },
                  'VCManifestTool':{

                  },
                }
               }
            ],           
         ]
      } 
   ]
}
