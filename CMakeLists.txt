# CMake File for Quadrilateral Cowboy (Because scons and Xcode are butt)
# Written by Ethan "flibitijibibo" Lee

CMAKE_MINIMUM_REQUIRED(VERSION 3.1)
PROJECT(QuadrilateralCowboy)

# CMake Options
OPTION(STEAM "Enable Steamworks" OFF)

# Compiler Flags
IF(NOT WIN32)
	ADD_COMPILE_OPTIONS(
		-pipe
		-Wno-unknown-pragmas
		-Wno-write-strings
		-fmessage-length=0
		-fpermissive
		-fvisibility=hidden
		-fno-strict-aliasing
	)
ENDIF()
ADD_DEFINITIONS(-D_D3XP -DCTF -DID_ENABLE_CURL=0 -DUSE_SDL -DXTHREADS)
IF(CMAKE_BUILD_TYPE STREQUAL "Debug")
	ADD_DEFINITIONS(-D_DEBUG -DID_MCHECK)
ELSEIF(CMAKE_BUILD_TYPE STREQUAL "Release")
	ADD_DEFINITIONS(-DNDEBUG)
	IF(NOT WIN32)
		ADD_COMPILE_OPTIONS(
			-Winline
			-ffast-math
			-fno-unsafe-math-optimizations
			-fomit-frame-pointer
		)
	ENDIF()
ENDIF()
IF(STEAM)
	ADD_DEFINITIONS(-DSTEAM)
	INCLUDE_DIRECTORIES(steam)
	LINK_DIRECTORIES(steam)
ENDIF()

# RPATH
IF(NOT WIN32)
	IF(APPLE)
		SET(BIN_RPATH "@executable_path/osx")
		ADD_DEFINITIONS(-DMACOS_X) # WTF? -flibit
	ELSE()
		IF(CMAKE_SIZEOF_VOID_P MATCHES 8)
			# Naming quirk for backward compatibility
			SET(BIN_RPATH "\$ORIGIN/lib64")
		ELSE()
			SET(BIN_RPATH "\$ORIGIN/lib")
		ENDIF()
		SET(CMAKE_EXE_LINKER_FLAGS "-Wl,--disable-new-dtags")
	ENDIF()
	SET(CMAKE_SKIP_BUILD_RPATH TRUE)
	SET(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
	SET(CMAKE_INSTALL_RPATH ${BIN_RPATH})
	SET(CMAKE_INSTALL_RPATH_USE_LINK_PATH FALSE)
ENDIF()

# Include Directories
INCLUDE_DIRECTORIES(. sound/OggVorbis/vorbissrc/)

# Source Lists
SET(QC_SRC
	renderer/jpeg-6/jcapimin.c
	renderer/jpeg-6/jccoefct.c
	renderer/jpeg-6/jccolor.c
	renderer/jpeg-6/jcdctmgr.c
	renderer/jpeg-6/jchuff.c
	renderer/jpeg-6/jcinit.c
	renderer/jpeg-6/jcmainct.c
	renderer/jpeg-6/jcmarker.c
	renderer/jpeg-6/jcmaster.c
	renderer/jpeg-6/jcomapi.c
	renderer/jpeg-6/jcparam.c
	renderer/jpeg-6/jcphuff.c
	renderer/jpeg-6/jcprepct.c
	renderer/jpeg-6/jcsample.c
	renderer/jpeg-6/jdapimin.c
	renderer/jpeg-6/jdapistd.c
	renderer/jpeg-6/jdatadst.c
	renderer/jpeg-6/jdatasrc.c
	renderer/jpeg-6/jdcoefct.c
	renderer/jpeg-6/jdcolor.c
	renderer/jpeg-6/jddctmgr.c
	renderer/jpeg-6/jdhuff.c
	renderer/jpeg-6/jdinput.c
	renderer/jpeg-6/jdmainct.c
	renderer/jpeg-6/jdmarker.c
	renderer/jpeg-6/jdmaster.c
	renderer/jpeg-6/jdmerge.c
	renderer/jpeg-6/jdphuff.c
	renderer/jpeg-6/jdpostct.c
	renderer/jpeg-6/jdsample.c
	renderer/jpeg-6/jdtrans.c
	renderer/jpeg-6/jerror.c
	renderer/jpeg-6/jfdctflt.c
	renderer/jpeg-6/jfdctfst.c
	renderer/jpeg-6/jfdctint.c
	renderer/jpeg-6/jidctflt.c
	renderer/jpeg-6/jidctfst.c
	renderer/jpeg-6/jidctint.c
	renderer/jpeg-6/jidctred.c
	renderer/jpeg-6/jmemmgr.c
	renderer/jpeg-6/jmemnobs.c
	renderer/jpeg-6/jquant1.c
	renderer/jpeg-6/jquant2.c
	renderer/jpeg-6/jutils.c
	sound/OggVorbis/oggsrc/bitwise.c
	sound/OggVorbis/oggsrc/framing.c
	sound/OggVorbis/vorbissrc/analysis.c
	sound/OggVorbis/vorbissrc/bitrate.c
	sound/OggVorbis/vorbissrc/block.c
	sound/OggVorbis/vorbissrc/codebook.c
	sound/OggVorbis/vorbissrc/envelope.c
	sound/OggVorbis/vorbissrc/floor0.c
	sound/OggVorbis/vorbissrc/floor1.c
	sound/OggVorbis/vorbissrc/info.c
	sound/OggVorbis/vorbissrc/lookup.c
	sound/OggVorbis/vorbissrc/lpc.c
	sound/OggVorbis/vorbissrc/lsp.c
	sound/OggVorbis/vorbissrc/mapping0.c
	sound/OggVorbis/vorbissrc/mdct.c
	sound/OggVorbis/vorbissrc/psy.c
	sound/OggVorbis/vorbissrc/registry.c
	sound/OggVorbis/vorbissrc/res0.c
	sound/OggVorbis/vorbissrc/sharedbook.c
	sound/OggVorbis/vorbissrc/smallft.c
	sound/OggVorbis/vorbissrc/synthesis.c
	sound/OggVorbis/vorbissrc/vorbisenc.c
	sound/OggVorbis/vorbissrc/vorbisfile.c
	sound/OggVorbis/vorbissrc/windowvb.c
	renderer/Cinematic.cpp
	renderer/GuiModel.cpp
	renderer/Image_files.cpp
	renderer/Image_init.cpp
	renderer/Image_load.cpp
	renderer/Image_process.cpp
	renderer/Image_program.cpp
	renderer/Interaction.cpp
	renderer/Material.cpp
	renderer/MegaTexture.cpp
	renderer/Model.cpp
	renderer/ModelDecal.cpp
	renderer/ModelManager.cpp
	renderer/ModelOverlay.cpp
	renderer/Model_beam.cpp
	renderer/Model_ase.cpp
	renderer/Model_liquid.cpp
	renderer/Model_lwo.cpp
	renderer/Model_ma.cpp
	renderer/Model_md3.cpp
	renderer/Model_md5.cpp
	renderer/Model_prt.cpp
	renderer/Model_sprite.cpp
	renderer/RenderEntity.cpp
	renderer/RenderSystem.cpp
	renderer/RenderSystem_init.cpp
	renderer/RenderWorld.cpp
	renderer/RenderWorld_demo.cpp
	renderer/RenderWorld_load.cpp
	renderer/RenderWorld_portals.cpp
	renderer/VertexCache.cpp
	renderer/cg_explicit.cpp
	renderer/draw_arb.cpp
	renderer/draw_arb2.cpp
	renderer/draw_common.cpp
	renderer/draw_exp_stub.cpp
	renderer/draw_nv10.cpp
	renderer/draw_nv20.cpp
	renderer/draw_r200.cpp
	renderer/tr_backend.cpp
	renderer/tr_deform.cpp
	renderer/tr_font.cpp
	renderer/tr_guisurf.cpp
	renderer/tr_light.cpp
	renderer/tr_lightrun.cpp
	renderer/tr_main.cpp
	renderer/tr_orderIndexes.cpp
	renderer/tr_polytope.cpp
	renderer/tr_render.cpp
	renderer/tr_rendertools.cpp
	renderer/tr_shadowbounds.cpp
	renderer/tr_stencilshadow.cpp
	renderer/tr_subview.cpp
	renderer/tr_trace.cpp
	renderer/tr_trisurf.cpp
	renderer/tr_turboshadow.cpp
	framework/CVarSystem.cpp
	framework/CmdSystem.cpp
	framework/Common.cpp
	framework/Compressor.cpp
	framework/Console.cpp
	framework/DemoFile.cpp
	framework/DeclAF.cpp
	framework/DeclEntityDef.cpp
	framework/DeclFX.cpp
	framework/DeclManager.cpp
	framework/DeclParticle.cpp
	framework/DeclPDA.cpp
	framework/DeclSkin.cpp
	framework/DeclTable.cpp
	framework/EditField.cpp
	framework/EventLoop.cpp
	framework/File.cpp
	framework/FileSystem.cpp
	framework/KeyInput.cpp
	framework/Unzip.cpp
	framework/UsercmdGen.cpp
	framework/Session_menu.cpp
	framework/Session.cpp
	framework/async/AsyncClient.cpp
	framework/async/AsyncNetwork.cpp
	framework/async/AsyncServer.cpp
	framework/async/MsgChannel.cpp
	framework/async/NetworkSystem.cpp
	framework/async/ServerScan.cpp
	cm/CollisionModel_contacts.cpp
	cm/CollisionModel_contents.cpp
	cm/CollisionModel_debug.cpp
	cm/CollisionModel_files.cpp
	cm/CollisionModel_load.cpp
	cm/CollisionModel_rotate.cpp
	cm/CollisionModel_trace.cpp
	cm/CollisionModel_translate.cpp
	tools/compilers/dmap/dmap.cpp
	tools/compilers/dmap/facebsp.cpp
	tools/compilers/dmap/gldraw.cpp
	tools/compilers/dmap/glfile.cpp
	tools/compilers/dmap/leakfile.cpp
	tools/compilers/dmap/map.cpp
	tools/compilers/dmap/optimize.cpp
	tools/compilers/dmap/output.cpp
	tools/compilers/dmap/portals.cpp
	tools/compilers/dmap/shadowopt3.cpp
	tools/compilers/dmap/tritjunction.cpp
	tools/compilers/dmap/tritools.cpp
	tools/compilers/dmap/ubrush.cpp
	tools/compilers/dmap/usurface.cpp
	tools/compilers/dmap/optimize_gcc.cpp
	tools/compilers/aas/AASBuild.cpp
	tools/compilers/aas/AASBuild_file.cpp
	tools/compilers/aas/AASBuild_gravity.cpp
	tools/compilers/aas/AASBuild_ledge.cpp
	tools/compilers/aas/AASBuild_merge.cpp
	tools/compilers/aas/AASCluster.cpp
	tools/compilers/aas/AASFile.cpp
	tools/compilers/aas/AASFile_optimize.cpp
	tools/compilers/aas/AASFile_sample.cpp
	tools/compilers/aas/AASReach.cpp
	tools/compilers/aas/AASFileManager.cpp
	tools/compilers/aas/Brush.cpp
	tools/compilers/aas/BrushBSP.cpp
	tools/compilers/roqvq/NSBitmapImageRep.cpp
	tools/compilers/roqvq/codec.cpp
	tools/compilers/roqvq/roq.cpp
	tools/compilers/roqvq/roqParam.cpp
	tools/compilers/renderbump/renderbump.cpp
	sound/snd_cache.cpp
	sound/snd_decoder.cpp
	sound/snd_efxfile.cpp
	sound/snd_emitter.cpp
	sound/snd_shader.cpp
	sound/snd_system.cpp
	sound/snd_wavefile.cpp
	sound/snd_world.cpp
	ui/BindWindow.cpp
	ui/ChoiceWindow.cpp
	ui/DeviceContext.cpp
	ui/EditWindow.cpp
	ui/FieldWindow.cpp
	ui/GameBearShootWindow.cpp
	ui/GameBustOutWindow.cpp
	ui/GameSSDWindow.cpp
	ui/gamelaserduckwindow.cpp
	ui/GuiScript.cpp
	ui/ListGUI.cpp
	ui/ListWindow.cpp
	ui/MarkerWindow.cpp
	ui/RegExp.cpp
	ui/RenderWindow.cpp
	ui/SimpleWindow.cpp
	ui/SliderWindow.cpp
	ui/UserInterface.cpp
	ui/Window.cpp
	ui/Winvar.cpp
	idlib/bv/Bounds.cpp
	idlib/bv/Frustum.cpp
	idlib/bv/Sphere.cpp
	idlib/bv/Box.cpp
	idlib/geometry/DrawVert.cpp
	idlib/geometry/Winding2D.cpp
	idlib/geometry/Surface_SweptSpline.cpp
	idlib/geometry/Winding.cpp
	idlib/geometry/Surface.cpp
	idlib/geometry/Surface_Patch.cpp
	idlib/geometry/TraceModel.cpp
	idlib/geometry/JointTransform.cpp
	idlib/hashing/CRC32.cpp
	idlib/hashing/MD4.cpp
	idlib/hashing/MD5.cpp
	idlib/math/Angles.cpp
	idlib/math/Lcp.cpp
	idlib/math/idMath.cpp
	idlib/math/Matrix.cpp
	idlib/math/Ode.cpp
	idlib/math/Plane.cpp
	idlib/math/Pluecker.cpp
	idlib/math/Polynomial.cpp
	idlib/math/Quat.cpp
	idlib/math/Rotation.cpp
	idlib/math/Simd.cpp
	idlib/math/Simd_Generic.cpp
	idlib/math/Simd_3DNow.cpp
	idlib/math/Simd_AltiVec.cpp
	idlib/math/Simd_MMX.cpp
	idlib/math/Simd_SSE.cpp
	idlib/math/Simd_SSE2.cpp
	idlib/math/Simd_SSE3.cpp
	idlib/math/Vector.cpp
	idlib/BitMsg.cpp
	idlib/LangDict.cpp
	idlib/Lexer.cpp
	idlib/Lib.cpp
	idlib/containers/HashIndex.cpp
	idlib/Dict.cpp
	idlib/Str.cpp
	idlib/Parser.cpp
	idlib/MapFile.cpp
	idlib/CmdArgs.cpp
	idlib/Token.cpp
	idlib/Base64.cpp
	idlib/Timer.cpp
	idlib/Heap.cpp
	d3xp/AF.cpp
	d3xp/AFEntity.cpp
	d3xp/Actor.cpp
	d3xp/Camera.cpp
	d3xp/Entity.cpp
	d3xp/BrittleFracture.cpp
	d3xp/Fx.cpp
	d3xp/GameEdit.cpp
	d3xp/Game_local.cpp
	d3xp/Game_network.cpp
	d3xp/Item.cpp
	d3xp/IK.cpp
	d3xp/Light.cpp
	d3xp/Misc.cpp
	d3xp/Mover.cpp
	d3xp/Moveable.cpp
	d3xp/MultiplayerGame.cpp
	d3xp/Player.cpp
	d3xp/PlayerIcon.cpp
	d3xp/PlayerView.cpp
	d3xp/Projectile.cpp
	d3xp/Pvs.cpp
	d3xp/SecurityCamera.cpp
	d3xp/SmokeParticles.cpp
	d3xp/Sound.cpp
	d3xp/Target.cpp
	d3xp/Trigger.cpp
	d3xp/Weapon.cpp
	d3xp/WorldSpawn.cpp
	d3xp/ai/AAS.cpp
	d3xp/ai/AAS_debug.cpp
	d3xp/ai/AAS_pathing.cpp
	d3xp/ai/AAS_routing.cpp
	d3xp/ai/AI.cpp
	d3xp/ai/AI_events.cpp
	d3xp/ai/AI_pathing.cpp
	d3xp/ai/AI_Vagary.cpp
	d3xp/gamesys/DebugGraph.cpp
	d3xp/gamesys/Class.cpp
	d3xp/gamesys/Event.cpp
	d3xp/gamesys/SaveGame.cpp
	d3xp/gamesys/SysCmds.cpp
	d3xp/gamesys/SysCvar.cpp
	d3xp/gamesys/TypeInfo.cpp
	d3xp/anim/Anim.cpp
	d3xp/anim/Anim_Blend.cpp
	d3xp/anim/Anim_Import.cpp
	d3xp/anim/Anim_Testmodel.cpp
	d3xp/script/Script_Compiler.cpp
	d3xp/script/Script_Interpreter.cpp
	d3xp/script/Script_Program.cpp
	d3xp/script/Script_Thread.cpp
	d3xp/physics/Clip.cpp
	d3xp/physics/Force.cpp
	d3xp/physics/Force_Constant.cpp
	d3xp/physics/Force_Drag.cpp
	d3xp/physics/Force_Field.cpp
	d3xp/physics/Force_Spring.cpp
	d3xp/physics/Physics.cpp
	d3xp/physics/Physics_AF.cpp
	d3xp/physics/Physics_Actor.cpp
	d3xp/physics/Physics_Base.cpp
	d3xp/physics/Physics_Monster.cpp
	d3xp/physics/Physics_Parametric.cpp
	d3xp/physics/Physics_Player.cpp
	d3xp/physics/Physics_RigidBody.cpp
	d3xp/physics/Physics_Static.cpp
	d3xp/physics/Physics_StaticMulti.cpp
	d3xp/physics/Push.cpp
	d3xp/Grabber.cpp
	d3xp/physics/Force_Grab.cpp
	d3xp/laserwire.cpp
	d3xp/panel.cpp
	d3xp/picker.cpp
	d3xp/turret.cpp
	d3xp/rotdoor.cpp
	d3xp/sentry.cpp
	d3xp/lever.cpp
	d3xp/steamstats.cpp
	d3xp/itemgate.cpp
	d3xp/worldmanager.cpp
	d3xp/powerscrewgeneric.cpp
	d3xp/camturret.cpp
	d3xp/zeppelinbig.cpp
	d3xp/keypad.cpp
	d3xp/screw.cpp
	d3xp/airlock.cpp
	d3xp/powersawgeneric.cpp
	d3xp/frobcube.cpp
	d3xp/weevil.cpp
	d3xp/clock.cpp
	d3xp/contractcamera.cpp
	d3xp/steamleaderboard.cpp
	d3xp/steamremote.cpp
	d3xp/qglass.cpp
	d3xp/trembler.cpp
	d3xp/button_switcher.cpp
	d3xp/commentary.cpp
	d3xp/cybervendor.cpp
	d3xp/launcher.cpp
	d3xp/bluebox.cpp
	d3xp/camerapoint.cpp
	d3xp/jellypoint.cpp
	d3xp/worldman_moveable.cpp
	d3xp/doorfolding.cpp
	d3xp/countdowntimer.cpp
	d3xp/animloop.cpp
	d3xp/tablefold.cpp
	TypeInfo/TypeInfoGen.cpp
	sys/glimp.cpp
	sys/events.cpp
	sys/sys_local.cpp
)
IF(WIN32)
	SET(QC_SRC
		${QC_SRC}
		sys/win32/win_cpu.cpp
		sys/win32/win_glimp.cpp
		sys/win32/win_input.cpp
		sys/win32/win_main.cpp
		sys/win32/win_net.cpp
		sys/win32/win_qgl.cpp
		sys/win32/win_shared.cpp
		sys/win32/win_snd.cpp
		sys/win32/win_syscon.cpp
		sys/win32/win_taskkeyhook.cpp
		sys/win32/win_wndproc.cpp
	)
ELSE()
	SET(QC_SRC
		${QC_SRC}
		sys/stub/util_stub.cpp
		sys/posix/posix_net.cpp
		sys/posix/posix_main.cpp
		sys/posix/posix_input.cpp
		sys/posix/posix_signal.cpp
		sys/posix/posix_threads.cpp
		sys/linux/stack.cpp
	)

	IF(APPLE)
		SET(QC_SRC
			${QC_SRC}
			sys/osx/DOOMController.mm
			sys/osx/macosx_event.mm
			sys/osx/macosx_glimp.mm
			sys/osx/macosx_guids.cpp
			sys/osx/macosx_misc.mm
			sys/osx/macosx_sound.cpp
			sys/osx/PickMonitor.cpp
			sys/osx/PreferencesDialog.cpp
		)
	ELSE()
		SET(QC_SRC
			${QC_SRC}
			idlib/bv/Frustum_gcc.cpp
			sys/linux/sound_oal.cpp
			sys/linux/input.cpp
			sys/linux/glimp.cpp
			sys/linux/glimp_dlopen.cpp
			sys/linux/main.cpp
		)
	ENDIF()
ENDIF()

# Executable information
SET(CMAKE_WIN32_EXECUTABLE ON)
ADD_EXECUTABLE(qc ${QC_SRC})

set_target_properties(qc PROPERTIES
    CXX_STANDARD 11
    CXX_STANDARD_REQUIRED ON)

# SDL2 Dependency (Detection pulled from FAudio)
if(WIN32)
	set(SDL2_INCLUDE_DIRS ${CMAKE_SOURCE_DIR}/sdl2/include)
	set(SDL2_LIBRARIES ${CMAKE_SOURCE_DIR}/sdl2/lib/win32/SDL2.lib)
elseif(APPLE)
	set(SDL2_INCLUDE_DIRS ${CMAKE_SOURCE_DIR}/sdl2/include)
	set(SDL2_LIBRARIES ${CMAKE_SOURCE_DIR}/sdl2/lib/osx/libSDL2-2.0.0.dylib)
endif()
if (DEFINED SDL2_INCLUDE_DIRS AND DEFINED SDL2_LIBRARIES)
	message(STATUS "using pre-defined SDL2 variables SDL2_INCLUDE_DIRS and SDL2_LIBRARIES")
	target_include_directories(qc PUBLIC "$<BUILD_INTERFACE:${SDL2_INCLUDE_DIRS}>")
	target_link_libraries(qc PUBLIC ${SDL2_LIBRARIES})
else()
	# Only try to autodetect if both SDL2 variables aren't explicitly set
	find_package(SDL2 CONFIG)
	if (TARGET SDL2::SDL2)
		message(STATUS "using TARGET SDL2::SDL2")
		target_link_libraries(qc PUBLIC SDL2::SDL2)
	elseif (TARGET SDL2)
		message(STATUS "using TARGET SDL2")
		target_link_libraries(qc PUBLIC SDL2)
	else()
		message(STATUS "no TARGET SDL2::SDL2, or SDL2, using variables")
		target_include_directories(qc PUBLIC "$<BUILD_INTERFACE:${SDL2_INCLUDE_DIRS}>")
		target_link_libraries(qc PUBLIC ${SDL2_LIBRARIES})
	endif()
endif()

# Other Dependencies
IF(APPLE)
	FIND_LIBRARY(OPENGL NAMES OpenGL)
	FIND_LIBRARY(OPENAL NAMES OpenAL)
	FIND_LIBRARY(COCOA NAMES Cocoa)
	FIND_LIBRARY(IOKIT NAMES IOKit)
	FIND_LIBRARY(COREAUDIO NAMES CoreAudio)
	TARGET_LINK_LIBRARIES(qc PUBLIC objc ${OPENGL} ${OPENAL} ${COCOA} ${IOKIT} ${COREAUDIO})
ELSEIF(NOT WIN32)
	TARGET_LINK_LIBRARIES(qc PUBLIC openal)
ENDIF()
IF(WIN32)
	TARGET_LINK_LIBRARIES(qc PUBLIC
		dbghelp.lib
		dinput8.lib
		dsound.lib
		glu32.lib
		iphlpapi.lib
		odbc32.lib
		odbccp32.lib
		opengl32.lib
		winmm.lib
		wsock32.lib
		${CMAKE_SOURCE_DIR}/openal/lib/eaxguid.lib
	)
ELSE()
	TARGET_LINK_LIBRARIES(qc PUBLIC dl pthread)
ENDIF()
IF(STEAM)
	TARGET_LINK_LIBRARIES(qc PUBLIC steam_api)
ENDIF()
