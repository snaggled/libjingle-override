# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'includes': [
    '../../build/win_precompile.gypi',
  ],
  'target_defaults': {
    'defines': [
      'FEATURE_ENABLE_SSL',
      'HAVE_OPENSSL_SSL_H=1',
      'EXPAT_RELATIVE_PATH',
      'FEATURE_ENABLE_SSL',
      'GTEST_RELATIVE_PATH',
      'HAVE_SRTP',
      'LOGGING_INSIDE_LIBJINGLE',
      'NO_MAIN_THREAD_WRAPPING',
      'NO_SOUND_SYSTEM',
      'SRTP_RELATIVE_PATH',
      'WEBRTC_RELATIVE_PATH',
      'USE_WEBRTC_DEV_BRANCH',
      '_USE_32BIT_TIME_T',
      'DISABLE_YUV',
    ],
    'configurations': {
      'Debug': {
        'defines': [
          # TODO(sergeyu): Fix libjingle to use NDEBUG instead of
          # _DEBUG and remove this define. See below as well.
          '_DEBUG',
        ],
      }
    },
    'include_dirs': [
      './',
#      '../../third_party/openssl/include',
      '../../testing/gtest/include',
      '../../third_party/libyuv/include',
    ],
    'dependencies': [
#      '<(DEPTH)/base/base.gyp:base',
#      '<(DEPTH)/net/net.gyp:net',
      '<(DEPTH)/third_party/expat/expat.gyp:expat',
      '<(DEPTH)/third_party/openssl/openssl.gyp:openssl',
    ],
    'export_dependent_settings': [
      '<(DEPTH)/third_party/expat/expat.gyp:expat',
    ],
    'direct_dependent_settings': {
      'include_dirs': [
        './',
        '../../testing/gtest/include',
      ],
      'defines': [
        'FEATURE_ENABLE_SSL',
        'FEATURE_ENABLE_VOICEMAIL',
        'EXPAT_RELATIVE_PATH',
        'GTEST_RELATIVE_PATH',
        'WEBRTC_RELATIVE_PATH',
        'NO_MAIN_THREAD_WRAPPING',
        'NO_SOUND_SYSTEM',
      ],
      'conditions': [
        ['OS=="win"', {
          'link_settings': {
            'libraries': [
              '-lsecur32.lib',
              '-lcrypt32.lib',
              '-liphlpapi.lib',
            ],
          },
        }],
        ['OS=="win"', {
          'include_dirs': [
            '../third_party/platformsdk_win7/files/Include',
          ],
          'defines': [
              '_CRT_SECURE_NO_WARNINGS',  # Suppres warnings about _vsnprinf
          ],
        }],
        ['OS=="linux"', {
          'defines': [
            'LINUX',
          ],
        }],
        ['OS=="mac"', {
          'defines': [
            'OSX',
          ],
        }],
        ['OS=="android"', {
          'defines': [
            'ANDROID',
          ],
        }],
        ['os_posix == 1', {
          'defines': [
            'POSIX',
          ],
        }],
        ['os_bsd==1', {
          'defines': [
            'BSD',
          ],
        }],
        ['OS=="openbsd"', {
          'defines': [
            'OPENBSD',
          ],
        }],
        ['OS=="freebsd"', {
          'defines': [
            'FREEBSD',
          ],
        }],
      ],
    },
    'all_dependent_settings': {
      'configurations': {
        'Debug': {
          'defines': [
            # TODO(sergeyu): Fix libjingle to use NDEBUG instead of
            # _DEBUG and remove this define. See above as well.
            '_DEBUG',
          ],
        }
      },
    },
    'conditions': [
      ['OS=="win"', {
        'include_dirs': [
          '../third_party/platformsdk_win7/files/Include',
        ],
      }],
      ['OS=="linux"', {
        'defines': [
          'LINUX',
        ],
      }],
      ['OS=="mac"', {
        'defines': [
          'OSX',
        ],
      }],
      ['OS=="ios"', {
        'defines': [
          'IOS',
          # Add this back with xmppframework branch
          'IOS_XMPP_FRAMEWORK=1',
          'CARBON_DEPRECATED',
        ],
      }],
      ['os_posix == 1', {
        'defines': [
          'POSIX',
        ],
      }],
      ['os_bsd==1', {
        'defines': [
          'BSD',
        ],
      }],
      ['OS=="openbsd"', {
        'defines': [
          'OPENBSD',
        ],
      }],
      ['OS=="freebsd"', {
        'defines': [
          'FREEBSD',
        ],
      }],
    ],
  },
  'targets': [
    {
      'target_name': 'libjingle',
      'IPHONEOS_DEPLOYMENT_TARGET': '7.0',
      'type': 'static_library',
      'sources': [
        'talk/base/basictypes.h',
        'talk/base/constructormagic.h',

        # Overrides logging.h/.cc because libjingle logging should be done to
        # the same place as the chromium logging.
        'talk/base/logging.cc',
        'talk/base/logging.h',
        
        'talk/base/asyncfile.cc',
        'talk/base/asyncfile.h',
        'talk/base/asynchttprequest.cc',
        'talk/base/asynchttprequest.h',
        'talk/base/asyncpacketsocket.h',
        'talk/base/asyncsocket.cc',
        'talk/base/asyncsocket.h',
        'talk/base/asynctcpsocket.cc',
        'talk/base/asynctcpsocket.h',
        'talk/base/asyncudpsocket.cc',
        'talk/base/asyncudpsocket.h',
        'talk/base/autodetectproxy.cc',
        'talk/base/autodetectproxy.h',
        'talk/base/base64.cc',
        'talk/base/base64.h',
        'talk/base/basicdefs.h',
        'talk/base/bytebuffer.cc',
        'talk/base/bytebuffer.h',
        'talk/base/byteorder.h',
        'talk/base/checks.cc',
        'talk/base/checks.h',
        'talk/base/common.cc',
        'talk/base/common.h',
        'talk/base/crc32.cc',
        'talk/base/crc32.h',
        'talk/base/criticalsection.h',
        'talk/base/cryptstring.h',
        'talk/base/diskcache.cc',
        'talk/base/diskcache.h',
        'talk/base/event.cc',
        'talk/base/event.h',
        'talk/base/fileutils.cc',
        'talk/base/fileutils.h',
        'talk/base/firewallsocketserver.cc',
        'talk/base/firewallsocketserver.h',
        'talk/base/flags.cc',
        'talk/base/flags.h',
        'talk/base/helpers.cc',
        'talk/base/helpers.h',
        'talk/base/host.cc',
        'talk/base/host.h',
        'talk/base/httpbase.cc',
        'talk/base/httpbase.h',
        'talk/base/httpclient.h',
        'talk/base/httpclient.cc',
        'talk/base/httpcommon-inl.h',
        'talk/base/httpcommon.cc',
        'talk/base/httpcommon.h',
        'talk/base/httprequest.cc',
        'talk/base/httprequest.h',
        'talk/base/ipaddress.cc',
        'talk/base/ipaddress.h',
        'talk/base/linked_ptr.h',
        'talk/base/md5.cc',
        'talk/base/md5.h',
        'talk/base/md5digest.h',
        'talk/base/messagedigest.cc',
        'talk/base/messagedigest.h',
        'talk/base/messagehandler.cc',
        'talk/base/messagehandler.h',
        'talk/base/messagequeue.cc',
        'talk/base/messagequeue.h',
        'talk/base/nethelpers.cc',
        'talk/base/nethelpers.h',
        'talk/base/network.cc',
        'talk/base/network.h',
        'talk/base/nullsocketserver.h',
        'talk/base/pathutils.cc',
        'talk/base/pathutils.h',
        'talk/base/physicalsocketserver.cc',
        'talk/base/physicalsocketserver.h',
        'talk/base/proxydetect.cc',
        'talk/base/proxydetect.h',
        'talk/base/proxyinfo.cc',
        'talk/base/proxyinfo.h',
        'talk/base/ratelimiter.cc',
        'talk/base/ratelimiter.h',
        'talk/base/ratetracker.cc',
        'talk/base/ratetracker.h',
        'talk/base/scoped_ptr.h',
        'talk/base/sec_buffer.h',
        'talk/base/sha1.cc',
        'talk/base/sha1.h',
        'talk/base/sha1digest.h',
        'talk/base/signalthread.cc',
        'talk/base/signalthread.h',
        'talk/base/sigslot.h',
        'talk/base/sigslotrepeater.h',
        'talk/base/socket.h',
        'talk/base/socketadapters.cc',
        'talk/base/socketadapters.h',
        'talk/base/socketaddress.cc',
        'talk/base/socketaddress.h',
        'talk/base/socketaddresspair.cc',
        'talk/base/socketaddresspair.h',
        'talk/base/socketfactory.h',
        'talk/base/socketpool.cc',
        'talk/base/socketpool.h',
        'talk/base/socketserver.h',
        'talk/base/socketstream.cc',
        'talk/base/socketstream.h',
        'talk/base/ssladapter.cc',
        'talk/base/ssladapter.h',
        'talk/base/sslidentity.cc',
        'talk/base/sslidentity.h',
        'talk/base/sslsocketfactory.cc',
        'talk/base/sslsocketfactory.h',
        'talk/base/sslstreamadapter.cc',
        'talk/base/sslstreamadapter.h',
        'talk/base/sslidentity.cc',
        'talk/base/sslidentity.h',
        'talk/base/stream.cc',
        'talk/base/stream.h',
        'talk/base/stringencode.cc',
        'talk/base/stringencode.h',
        'talk/base/stringutils.cc',
        'talk/base/stringutils.h',
        'talk/base/systeminfo.cc',
        'talk/base/systeminfo.h',
        'talk/base/task.cc',
        'talk/base/task.h',
        'talk/base/taskparent.cc',
        'talk/base/taskparent.h',
        'talk/base/taskrunner.cc',
        'talk/base/taskrunner.h',
        'talk/base/thread.cc',
        'talk/base/thread.h',
        'talk/base/timeutils.cc',
        'talk/base/timeutils.h',
        'talk/base/timing.cc',
        'talk/base/timing.h',
        'talk/base/urlencode.cc',
        'talk/base/urlencode.h',
        'talk/base/worker.cc',
        'talk/base/worker.h',
        'talk/xmllite/qname.cc',
        'talk/xmllite/qname.h',
        'talk/xmllite/xmlbuilder.cc',
        'talk/xmllite/xmlbuilder.h',
        'talk/xmllite/xmlconstants.cc',
        'talk/xmllite/xmlconstants.h',
        'talk/xmllite/xmlelement.cc',
        'talk/xmllite/xmlelement.h',
        'talk/xmllite/xmlnsstack.cc',
        'talk/xmllite/xmlnsstack.h',
        'talk/xmllite/xmlparser.cc',
        'talk/xmllite/xmlparser.h',
        'talk/xmllite/xmlprinter.cc',
        'talk/xmllite/xmlprinter.h',
        'talk/xmpp/asyncsocket.h',
        'talk/xmpp/constants.cc',
        'talk/xmpp/constants.h',
        'talk/xmpp/jid.cc',
        'talk/xmpp/jid.h',
        'talk/xmpp/pingtask.h',
        'talk/xmpp/pingtask.cc',
        'talk/xmpp/plainsaslhandler.h',
        'talk/xmpp/prexmppauth.h',
        'talk/xmpp/saslcookiemechanism.h',
        'talk/xmpp/saslhandler.h',
        'talk/xmpp/saslmechanism.cc',
        'talk/xmpp/saslmechanism.h',
        'talk/xmpp/saslplainmechanism.h',
        'talk/xmpp/xmppclient.cc',
        'talk/xmpp/xmppclient.h',
        'talk/xmpp/xmppclientsettings.h',
        'talk/xmpp/xmppengine.h',
        'talk/xmpp/xmppengineimpl.cc',
        'talk/xmpp/xmppengineimpl.h',
        'talk/xmpp/xmppengineimpl_iq.cc',
        'talk/xmpp/xmpplogintask.cc',
        'talk/xmpp/xmpplogintask.h',
        'talk/xmpp/xmppstanzaparser.cc',
        'talk/xmpp/xmppstanzaparser.h',
        'talk/xmpp/xmpptask.cc',
        'talk/xmpp/xmpptask.h',
        'talk/xmpp/module.h',
        'talk/xmpp/moduleimpl.cc',
        'talk/xmpp/rostermodule.h',
        'talk/xmpp/rostermoduleimpl.cc',
      ],
      'include_dirs': [
        '<(DEPTH)/third_party/libjingle',
        '<(DEPTH)/third_party/expat/files/lib',
      ],
      'conditions': [
        ['os_posix == 1', {
          'sources': [
            'talk/base/unixfilesystem.cc',
            'talk/base/unixfilesystem.h',
            'talk/base/openssladapter.cc',
            'talk/base/openssldigest.cc',
            'talk/base/opensslidentity.cc',
            'talk/base/opensslstreamadapter.cc',
            'talk/base/posix.cc',
          ],
        }],
        ['OS=="linux"', {
          'sources': [
            'talk/base/latebindingsymboltable.cc',
            'talk/base/latebindingsymboltable.h',
            'talk/base/linux.cc',
            'talk/base/linux.h',
          ],
        }],
        ['OS=="mac"', {
          'sources': [
            'talk/base/macconversion.cc',
            'talk/base/macconversion.h',
            'talk/base/macutils.cc',
            'talk/base/macutils.h',
          ],
        }],
        ['OS=="ios"', {
          'sources': [
#            'talk/base/maccocoasocketserver.mm',
#            'talk/base/maccocoasocketserver.h',
            'talk/media/devices/iosdeviceinfo.cc',
            'talk/base/macasyncsocket.h',
            'talk/base/macasyncsocket.cc',
            'talk/base/macconversion.cc',
            'talk/base/macsocketserver.h',
            'talk/base/macsocketserver.cc',
            'talk/base/maccocoathreadhelper.mm',
            'talk/base/maccocoathreadhelper.h',
            'talk/base/macutils.cc',
            'talk/base/scoped_autorelease_pool.mm',
            'talk/base/scoped_autorelease_pool.h',
          ],
          'link_settings': {
            'xcode_settings': {
              'OTHER_LDFLAGS': [
                '-framework CoreFoundation',
                '-framework Foundation',
                '-framework IOKit',
                '-framework Security',
                '-framework SystemConfiguration',
              ],
            },
          },
        }],
        ['OS=="win"', {
          'sources': [
            'talk/base/win32socketinit.cc',
            'talk/base/schanneladapter.cc',
            'talk/base/schanneladapter.h',
            'talk/base/win32.cc',
            'talk/base/win32.h',
            'talk/base/win32filesystem.cc',
            'talk/base/win32filesystem.h',
            'talk/base/win32window.h',
            'talk/base/win32window.cc',
            'talk/base/win32securityerrors.cc',
            'talk/base/winfirewall.cc',
            'talk/base/winfirewall.h',
            'talk/base/winping.cc',
            'talk/base/winping.h',
          ],
          # Suppress warnings about WIN32_LEAN_AND_MEAN.
          'msvs_disabled_warnings': [ 4005 ],
        }],
      ],
    },  # target libjingle
    # This has to be is a separate project due to a bug in MSVS:
    # https://connect.microsoft.com/VisualStudio/feedback/details/368272/duplicate-cpp-filename-in-c-project-visual-studio-2008
    # We have two files named "constants.cc" and MSVS doesn't handle this
    # properly.
    {
      'target_name': 'libjingle_p2p',
      'IPHONEOS_DEPLOYMENT_TARGET': '7.0',
      'type': 'static_library',
      'sources': [
        'talk/p2p/base/asyncstuntcpsocket.cc',
        'talk/p2p/base/asyncstuntcpsocket.h',
        'talk/p2p/base/basicpacketsocketfactory.cc',
        'talk/p2p/base/basicpacketsocketfactory.h',
        'talk/p2p/base/candidate.h',
        'talk/p2p/base/common.h',
        'talk/p2p/base/constants.cc',
        'talk/p2p/base/constants.h',
        'talk/p2p/base/dtlstransport.h',
        'talk/p2p/base/dtlstransportchannel.cc',
        'talk/p2p/base/dtlstransportchannel.h',
        'talk/p2p/base/p2ptransport.cc',
        'talk/p2p/base/p2ptransport.h',
        'talk/p2p/base/p2ptransportchannel.cc',
        'talk/p2p/base/p2ptransportchannel.h',
        'talk/p2p/base/port.cc',
        'talk/p2p/base/port.h',
        'talk/p2p/base/portallocator.h',
        'talk/p2p/base/portallocator.cc',
        'talk/p2p/base/portallocatorsessionproxy.cc',
        'talk/p2p/base/portallocatorsessionproxy.h',
        'talk/p2p/base/portproxy.cc',
        'talk/p2p/base/portproxy.h',
        'talk/p2p/base/pseudotcp.cc',
        'talk/p2p/base/pseudotcp.h',
        'talk/p2p/base/rawtransport.cc',
        'talk/p2p/base/rawtransport.h',
        'talk/p2p/base/rawtransportchannel.cc',
        'talk/p2p/base/rawtransportchannel.h',
        'talk/p2p/base/relayport.cc',
        'talk/p2p/base/relayport.h',
        'talk/p2p/base/turnport.cc',
        'talk/p2p/base/turnport.h',
        'talk/p2p/base/session.cc',
        'talk/p2p/base/session.h',
        'talk/p2p/base/sessionclient.h',
        'talk/p2p/base/sessiondescription.cc',
        'talk/p2p/base/sessiondescription.h',
        'talk/p2p/base/sessionid.h',
        'talk/p2p/base/sessionmanager.cc',
        'talk/p2p/base/sessionmanager.h',
        'talk/p2p/base/sessionmessages.cc',
        'talk/p2p/base/sessionmessages.h',
        'talk/p2p/base/parsing.cc',
        'talk/p2p/base/parsing.h',
        'talk/p2p/base/stun.cc',
        'talk/p2p/base/stun.h',
        'talk/p2p/base/stunport.cc',
        'talk/p2p/base/stunport.h',
        'talk/p2p/base/stunrequest.cc',
        'talk/p2p/base/stunrequest.h',
        'talk/p2p/base/tcpport.cc',
        'talk/p2p/base/tcpport.h',
        'talk/p2p/base/transport.cc',
        'talk/p2p/base/transport.h',
        'talk/p2p/base/transportchannel.cc',
        'talk/p2p/base/transportchannel.h',
        'talk/p2p/base/transportchannelimpl.h',
        'talk/p2p/base/transportchannelproxy.cc',
        'talk/p2p/base/transportchannelproxy.h',
        'talk/p2p/base/transportdescriptionfactory.cc',
        'talk/p2p/base/transportdescriptionfactory.h',
        'talk/p2p/client/basicportallocator.cc',
        'talk/p2p/client/basicportallocator.h',
        'talk/p2p/client/httpportallocator.cc',
        'talk/p2p/client/httpportallocator.h',
        'talk/p2p/client/sessionmanagertask.h',
        'talk/p2p/client/sessionsendtask.h',
        'talk/p2p/client/socketmonitor.cc',
        'talk/p2p/client/socketmonitor.h',
        'talk/session/tunnel/pseudotcpchannel.cc',
        'talk/session/tunnel/pseudotcpchannel.h',
        'talk/session/tunnel/tunnelsessionclient.cc',
        'talk/session/tunnel/tunnelsessionclient.h',
      ],
      'include_dirs': [
        '<(DEPTH)/third_party/libjingle',
        '<(DEPTH)/third_party/gtest/include',
      ],
      'dependencies': [
        'libjingle',
      ],
    },  # target libjingle_p2p
    {
      'target_name': 'libjingle_peerconnection',
      'IPHONEOS_DEPLOYMENT_TARGET': '7.0',
      'type': 'static_library',
      'defines': [
        'HAVE_WEBRTC_VIDEO',
        'HAVE_WEBRTC_VOICE',
      ],
      'sources': [
        'talk/app/webrtc/audiotrack.cc',
        'talk/app/webrtc/audiotrack.h',
        'talk/app/webrtc/jsep.h',
        'talk/app/webrtc/jsepicecandidate.cc',
        'talk/app/webrtc/jsepicecandidate.h',
        'talk/app/webrtc/jsepsessiondescription.cc',
        'talk/app/webrtc/jsepsessiondescription.h',
        'talk/app/webrtc/mediastream.cc',
        'talk/app/webrtc/mediastream.h',
        'talk/app/webrtc/mediastreamhandler.cc',
        'talk/app/webrtc/mediastreamhandler.h',
        'talk/app/webrtc/mediastreaminterface.h',
        'talk/app/webrtc/mediastreamprovider.h',
        'talk/app/webrtc/mediastreamproxy.cc',
        'talk/app/webrtc/mediastreamproxy.h',
        'talk/app/webrtc/mediastreamsignaling.cc',
        'talk/app/webrtc/mediastreamsignaling.h',
        'talk/app/webrtc/mediastreamtrack.h',
        'talk/app/webrtc/mediastreamtrackproxy.cc',
        'talk/app/webrtc/mediastreamtrackproxy.h',
        'talk/app/webrtc/notifier.h',
        'talk/app/webrtc/peerconnection.cc',
        'talk/app/webrtc/peerconnection.h',
        'talk/app/webrtc/peerconnectionfactory.cc',
        'talk/app/webrtc/peerconnectionfactory.h',
        'talk/app/webrtc/peerconnectioninterface.h',
        'talk/app/webrtc/portallocatorfactory.cc',
        'talk/app/webrtc/portallocatorfactory.h',
        'talk/app/webrtc/roaperrorcodes.h',
        'talk/app/webrtc/roapmessages.cc',
        'talk/app/webrtc/roapmessages.h',
        'talk/app/webrtc/roapsession.cc',
        'talk/app/webrtc/roapsession.h',
        'talk/app/webrtc/roapsignaling.cc',
        'talk/app/webrtc/roapsignaling.h',
        'talk/app/webrtc/streamcollection.h',
        'talk/app/webrtc/videotrackrenderers.cc',
        'talk/app/webrtc/videotrackrenderers.h',
        'talk/app/webrtc/videorendererimpl.cc',
        'talk/app/webrtc/videotrack.cc',
        'talk/app/webrtc/videotrack.h',
        'talk/app/webrtc/webrtcsdp.cc',
        'talk/app/webrtc/webrtcsdp.h',
        'talk/app/webrtc/webrtcsession.cc',
        'talk/app/webrtc/webrtcsession.h',
        'talk/media/base/capturemanager.cc',
        'talk/media/base/capturerenderadapter.cc',
        'talk/media/base/codec.cc',
        'talk/media/base/codec.h',
        'talk/media/base/constants.cc',
        'talk/media/base/constants.h',
        'talk/media/base/cryptoparams.h',
        'talk/media/base/rtpdataengine.cc',
        'talk/media/base/rtpdataengine.h',
        'talk/media/base/filemediaengine.cc',
        'talk/media/base/filemediaengine.h',
        'talk/media/base/mediachannel.h',
        'talk/media/base/mediaengine.cc',
        'talk/media/base/mediaengine.h',
        'talk/media/base/rtpdump.cc',
        'talk/media/base/rtpdump.h',
        'talk/media/base/rtputils.cc',
        'talk/media/base/rtputils.h',
        'talk/media/devices/deviceinfo.h',
        'talk/media/devices/devicemanager.cc',
        'talk/media/devices/devicemanager.h',
        'talk/media/devices/filevideocapturer.cc',
        'talk/media/devices/filevideocapturer.h',
        'talk/session/media/audiomonitor.cc',
        'talk/session/media/audiomonitor.h',
        'talk/session/media/call.cc',
        'talk/session/media/call.h',
        'talk/session/media/channel.cc',
        'talk/session/media/channel.h',
        'talk/session/media/channelmanager.cc',
        'talk/session/media/channelmanager.h',
        'talk/session/media/currentspeakermonitor.cc',
        'talk/session/media/currentspeakermonitor.h',
        'talk/session/media/mediamessages.cc',
        'talk/session/media/mediamessages.h',
        'talk/session/media/mediamonitor.cc',
        'talk/session/media/mediamonitor.h',
        'talk/session/media/mediasession.cc',
        'talk/session/media/mediasession.h',
        'talk/session/media/mediasessionclient.cc',
        'talk/session/media/mediasessionclient.h',
        'talk/session/media/mediasink.h',
        'talk/session/media/rtcpmuxfilter.cc',
        'talk/session/media/rtcpmuxfilter.h',
        'talk/session/media/soundclip.cc',
        'talk/session/media/soundclip.h',
        'talk/session/media/srtpfilter.cc',
        'talk/session/media/srtpfilter.h',
        'talk/session/media/ssrcmuxfilter.cc',
        'talk/session/media/ssrcmuxfilter.h',
        'talk/session/media/typingmonitor.h',
        'talk/session/media/typingmonitor.cc',
        'talk/session/media/voicechannel.h',
        'talk/media/base/streamparams.cc',
        'talk/media/base/videocapturer.cc',
        'talk/media/base/videocapturer.h',
        'talk/media/base/videocommon.cc',
        'talk/media/base/videocommon.h',
        'talk/media/base/videoframe.cc',
        'talk/media/base/videoframe.h',
        'talk/media/webrtc/webrtccommon.h',
        'talk/media/webrtc/webrtcpassthroughrender.cc',
        'talk/media/webrtc/webrtcvideocapturer.cc',
        'talk/media/webrtc/webrtcvideocapturer.h',
        'talk/media/webrtc/webrtcvideoengine.cc',
        'talk/media/webrtc/webrtcvideoengine.h',
        'talk/media/webrtc/webrtcvideoframe.cc',
        'talk/media/webrtc/webrtcvideoframe.h',
        'talk/media/webrtc/webrtcvie.h',
        'talk/media/webrtc/webrtcvoe.h',
        'talk/media/webrtc/webrtcvoiceengine.cc',
        'talk/media/webrtc/webrtcvoiceengine.h',
      ],
      'conditions': [
          ['OS=="ios"', {
              'sources': [
                'talk/media/devices/iosdeviceinfo.cc',
              ],
          }],
      ],
      'dependencies': [
        '<(DEPTH)/third_party/libsrtp/libsrtp.gyp:libsrtp',
        '<(DEPTH)/third_party/webrtc/modules/modules.gyp:video_capture_module',
        '<(DEPTH)/third_party/webrtc/modules/modules.gyp:video_render_module',
        '<(DEPTH)/third_party/webrtc/video_engine/video_engine.gyp:video_engine_core',
        '<(DEPTH)/third_party/webrtc/voice_engine/voice_engine.gyp:voice_engine',
        '<(DEPTH)/third_party/webrtc/system_wrappers/source/system_wrappers.gyp:system_wrappers',
        'libjingle',
        'libjingle_p2p',
      ],
    },  # target libjingle_peerconnection
    {
      'target_name': 'libjingle_audio_only',
      'IPHONEOS_DEPLOYMENT_TARGET': '7.0',
      'type': 'static_library',
      'defines': [
        'HAVE_WEBRTC_VOICE',
      ],
      'include_dirs': [
        '<(DEPTH)/third_party',
        '<(DEPTH)/third_party/libjingle',
        '<(DEPTH)/third_party/webrtc',
      ],
      'sources': [
        'talk/app/webrtc/audiotrack.cc',
        'talk/app/webrtc/audiotrack.h',
        'talk/app/webrtc/videotrack.cc',
        'talk/app/webrtc/videotrack.h',
        'talk/app/webrtc/videotrackrenderers.cc',
        'talk/app/webrtc/videotrackrenderers.h',
        'talk/media/base/codec.cc',
        'talk/media/base/codec.h',
        'talk/media/base/constants.cc',
        'talk/media/base/constants.h',
        'talk/media/base/cryptoparams.h',
        'talk/media/base/filemediaengine.cc',
        'talk/media/base/filemediaengine.h',
        'talk/media/base/mediachannel.h',
        'talk/media/base/mediaengine.cc',
        'talk/media/base/mediaengine.h',
        'talk/media/devices/devicemanager.cc',
        'talk/media/devices/devicemanager.h',
        'talk/media/devices/dummydevicemanager.cc',
        'talk/media/devices/dummydevicemanager.h',
        'talk/media/devices/filevideocapturer.cc',
        'talk/media/devices/filevideocapturer.h',
        'talk/session/media/audiomonitor.cc',
        'talk/session/media/audiomonitor.h',
        'talk/session/media/call.cc',
        'talk/session/media/call.h',
        'talk/session/media/channel.cc',
        'talk/session/media/channel.h',
        'talk/session/media/channelmanager.cc',
        'talk/session/media/channelmanager.h',
        'talk/session/media/currentspeakermonitor.cc',
        'talk/session/media/currentspeakermonitor.h',
        'talk/session/media/mediamessages.cc',
        'talk/session/media/mediamessages.h',
        'talk/session/media/mediamonitor.cc',
        'talk/session/media/mediamonitor.h',
        'talk/session/media/mediasession.cc',
        'talk/session/media/mediasession.h',
        'talk/session/media/mediasessionclient.cc',
        'talk/session/media/mediasessionclient.h',
        'talk/session/media/mediasink.h',
        'talk/session/media/rtcpmuxfilter.cc',
        'talk/session/media/rtcpmuxfilter.h',
        'talk/session/media/soundclip.cc',
        'talk/session/media/soundclip.h',
        'talk/session/media/srtpfilter.cc',
        'talk/session/media/srtpfilter.h',
        'talk/session/media/ssrcmuxfilter.cc',
        'talk/session/media/ssrcmuxfilter.h',
        'talk/session/media/typingmonitor.h',
        'talk/session/media/typingmonitor.cc',
        'talk/session/media/voicechannel.h',
        'talk/media/base/capturemanager.cc',
        'talk/media/base/capturerenderadapter.cc',
        'talk/media/base/rtpdataengine.cc',
        'talk/media/base/rtpdataengine.h',
        'talk/media/base/rtpdump.cc',
        'talk/media/base/rtpdump.h',
        'talk/media/base/rtputils.cc',
        'talk/media/base/rtputils.h',
        'talk/media/base/streamparams.cc',
        'talk/media/base/videocapturer.cc',
        'talk/media/base/videocapturer.h',
        'talk/media/base/videocommon.cc',
        'talk/media/base/videocommon.h',
        'talk/media/base/videoframe.cc',
        'talk/media/base/videoframe.h',
        'talk/media/webrtc/webrtccommon.h',
        'talk/media/webrtc/webrtcpassthroughrender.cc',
        'talk/media/webrtc/webrtcvideoengine.cc',
        'talk/media/webrtc/webrtcvideoengine.h',
        'talk/media/webrtc/webrtcvideoframe.cc',
        'talk/media/webrtc/webrtcvideoframe.h',
        'talk/media/webrtc/webrtcvie.h',
        'talk/media/webrtc/webrtcvoe.h',
        'talk/media/webrtc/webrtcvoiceengine.cc',
        'talk/media/webrtc/webrtcvoiceengine.h',
      ],
      'dependencies': [
        '<(DEPTH)/third_party/libsrtp/libsrtp.gyp:libsrtp',
        #'<(DEPTH)/third_party/webrtc/modules/modules.gyp:video_capture_module',
        #'<(DEPTH)/third_party/webrtc/modules/modules.gyp:video_render_module',
        #'<(DEPTH)/third_party/webrtc/video_engine/video_engine.gyp:video_engine_core',
        '<(DEPTH)/third_party/webrtc/voice_engine/voice_engine.gyp:voice_engine',
        '<(DEPTH)/third_party/webrtc/system_wrappers/source/system_wrappers.gyp:system_wrappers',
        'libjingle',
        'libjingle_p2p',
      ],
      'conditions': [
        ['OS=="android"', {
          'link_settings': {
            'libraries': [
              '-ldl',
              '-llog',
            ],
          },
        }],
      ],
    },  # target libjingle_audio_only
    {
      'target_name': 'peerconnection_server',
      'IPHONEOS_DEPLOYMENT_TARGET': '7.0',
      'type': 'executable',
      'sources': [
        'talk/examples/peerconnection/server/data_socket.cc',
        'talk/examples/peerconnection/server/data_socket.h',
        'talk/examples/peerconnection/server/main.cc',
        'talk/examples/peerconnection/server/peer_channel.cc',
        'talk/examples/peerconnection/server/peer_channel.h',
        'talk/examples/peerconnection/server/utils.cc',
        'talk/examples/peerconnection/server/utils.h',
      ],
      'include_dirs': [
        '.',
      ],
    }, # target peerconnection_server
  ],
}
