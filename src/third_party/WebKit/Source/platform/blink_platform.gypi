{
  'includes': [
    'platform_generated.gypi',
  ],
  'variables': {
    'platform_files': [
      'AsyncFileSystemCallbacks.h',
      'CalculationValue.h',
      'CheckedInt.h',
      'Clock.cpp',
      'Clock.h',
      'ContentDecryptionModuleResult.h',
      'ContentSettingCallbacks.cpp',
      'ContentSettingCallbacks.h',
      'ContentType.cpp',
      'ContentType.h',
      'ContextMenu.cpp',
      'ContextMenu.h',
      'ContextMenuItem.cpp',
      'ContextMenuItem.h',
      'CrossThreadCopier.cpp',
      'CrossThreadCopier.h',
      'Crypto.cpp',
      'Crypto.h',
      'CryptoResult.h',
      'Cursor.cpp',
      'Cursor.h',
      'DateComponents.cpp',
      'DateComponents.h',
      'Decimal.cpp',
      'Decimal.h',
      'DragImage.cpp',
      'DragImage.h',
      'EventDispatchForbiddenScope.cpp',
      'EventDispatchForbiddenScope.h',
      'EventTracer.cpp',
      'EventTracer.h',
      'FileChooser.cpp',
      'FileChooser.h',
      'FileMetadata.cpp',
      'FileMetadata.h',
      'FileSystemType.h',
      'FloatConversion.h',
      'HostWindow.h',
      'JSONValues.cpp',
      'JSONValues.h',
      'KeyboardCodes.h',
      'KillRing.h',
      'KillRingNone.cpp',
      'Language.cpp',
      'Language.h',
      'LayoutTestSupport.cpp',
      'LayoutTestSupport.h',
      'LayoutUnit.h',
      'Length.cpp',
      'Length.h',
      'LengthBox.cpp',
      'LengthBox.h',
      'LengthFunctions.cpp',
      'LengthFunctions.h',
      'LengthPoint.h',
      'LengthSize.h',
      'LifecycleNotifier.h',
      'LifecycleObserver.h',
      'LinkHash.cpp',
      'LinkHash.h',
      'Logging.cpp',
      'Logging.h',
      'MIMETypeFromURL.cpp',
      'MIMETypeFromURL.h',
      'MIMETypeRegistry.cpp',
      'MIMETypeRegistry.h',
      'NotImplemented.cpp',
      'NotImplemented.h',
      'PartitionAllocMemoryDumpProvider.cpp',
      'PartitionAllocMemoryDumpProvider.h',
      'PODArena.h',
      'PODFreeListArena.h',
      'PODInterval.h',
      'PODIntervalTree.h',
      'PODRedBlackTree.h',
      'ParsingUtilities.h',
      'PasteMode.h',
      'PlatformEvent.h',
      'PlatformGestureEvent.h',
      'PlatformInstrumentation.cpp',
      'PlatformInstrumentation.h',
      'PlatformKeyboardEvent.cpp',
      'PlatformKeyboardEvent.h',
      'PlatformMouseEvent.h',
      'PlatformResourceLoader.cpp',
      'PlatformResourceLoader.h',
      'PlatformTouchEvent.h',
      'PlatformTouchPoint.h',
      'PlatformWheelEvent.h',
      'PluginScriptForbiddenScope.cpp',
      'PluginScriptForbiddenScope.h',
      'PopupMenu.h',
      'Prerender.cpp',
      'Prerender.h',
      'PrerenderClient.h',
      'PurgeableVector.cpp',
      'PurgeableVector.h',
      'RefCountedSupplement.h',
      'ScriptForbiddenScope.cpp',
      'ScriptForbiddenScope.h',
      'SecureTextInput.cpp',
      'SecureTextInput.h',
      'SerializedResource.h',
      'SharedBuffer.cpp',
      'SharedBuffer.h',
      'SharedBufferChunkReader.cpp',
      'SharedBufferChunkReader.h',
      'StorageQuotaCallbacks.h',
      'Supplementable.cpp',
      'Supplementable.h',
      'Task.h',
      'TaskSynchronizer.cpp',
      'TaskSynchronizer.h',
      'Theme.cpp',
      'Theme.h',
      'ThemeTypes.h',
      'ThreadedDataReceiver.h',
      'Timer.cpp',
      'Timer.h',
      'TraceEvent.h',
      'TraceEventCommon.h',
      'TracedValue.cpp',
      'TracedValue.h',
      'UUID.cpp',
      'UUID.h',
      'UserGestureIndicator.cpp',
      'UserGestureIndicator.h',
      'WebScheduler.cpp',
      'WebThreadSupportingGC.cpp',
      'WebThreadSupportingGC.h',
      'WebThread.cpp',
      'Widget.cpp',
      'Widget.h',
      'WindowsKeyboardCodes.h',
      'animation/AnimationUtilities.h',
      'animation/CubicBezierControlPoints.cpp',
      'animation/CubicBezierControlPoints.h',
      'animation/TimingFunction.cpp',
      'animation/TimingFunction.h',
      'animation/UnitBezier.h',
      'audio/AudioArray.h',
      'audio/AudioBus.cpp',
      'audio/AudioBus.h',
      'audio/AudioChannel.cpp',
      'audio/AudioChannel.h',
      'audio/AudioDSPKernel.cpp',
      'audio/AudioDSPKernel.h',
      'audio/AudioDSPKernelProcessor.cpp',
      'audio/AudioDSPKernelProcessor.h',
      'audio/AudioDelayDSPKernel.cpp',
      'audio/AudioDelayDSPKernel.h',
      'audio/AudioDestination.cpp',
      'audio/AudioDestination.h',
      'audio/AudioDestinationConsumer.h',
      'audio/AudioFIFO.cpp',
      'audio/AudioFIFO.h',
      'audio/AudioFileReader.h',
      'audio/AudioIOCallback.h',
      'audio/AudioProcessor.cpp',
      'audio/AudioProcessor.h',
      'audio/AudioPullFIFO.cpp',
      'audio/AudioPullFIFO.h',
      'audio/AudioResampler.cpp',
      'audio/AudioResampler.h',
      'audio/AudioResamplerKernel.cpp',
      'audio/AudioResamplerKernel.h',
      'audio/AudioSourceProvider.h',
      'audio/AudioSourceProviderClient.h',
      'audio/AudioUtilities.cpp',
      'audio/AudioUtilities.h',
      'audio/Biquad.cpp',
      'audio/Biquad.h',
      'audio/Cone.cpp',
      'audio/Cone.h',
      'audio/DenormalDisabler.h',
      'audio/DirectConvolver.cpp',
      'audio/DirectConvolver.h',
      'audio/Distance.cpp',
      'audio/Distance.h',
      'audio/DownSampler.cpp',
      'audio/DownSampler.h',
      'audio/DynamicsCompressor.cpp',
      'audio/DynamicsCompressor.h',
      'audio/DynamicsCompressorKernel.cpp',
      'audio/DynamicsCompressorKernel.h',
      'audio/EqualPowerPanner.cpp',
      'audio/EqualPowerPanner.h',
      'audio/FFTConvolver.cpp',
      'audio/FFTConvolver.h',
      'audio/FFTFrame.cpp',
      'audio/FFTFrame.h',
      'audio/FFTFrameStub.cpp',
      'audio/HRTFDatabase.cpp',
      'audio/HRTFDatabase.h',
      'audio/HRTFDatabaseLoader.cpp',
      'audio/HRTFDatabaseLoader.h',
      'audio/HRTFElevation.cpp',
      'audio/HRTFElevation.h',
      'audio/HRTFKernel.cpp',
      'audio/HRTFKernel.h',
      'audio/HRTFPanner.cpp',
      'audio/HRTFPanner.h',
      'audio/MultiChannelResampler.cpp',
      'audio/MultiChannelResampler.h',
      'audio/Panner.cpp',
      'audio/Panner.h',
      'audio/Reverb.cpp',
      'audio/Reverb.h',
      'audio/ReverbAccumulationBuffer.cpp',
      'audio/ReverbAccumulationBuffer.h',
      'audio/ReverbConvolver.cpp',
      'audio/ReverbConvolver.h',
      'audio/ReverbConvolverStage.cpp',
      'audio/ReverbConvolverStage.h',
      'audio/ReverbInputBuffer.cpp',
      'audio/ReverbInputBuffer.h',
      'audio/SincResampler.cpp',
      'audio/SincResampler.h',
      'audio/Spatializer.cpp',
      'audio/Spatializer.h',
      'audio/StereoPanner.cpp',
      'audio/StereoPanner.h',
      'audio/UpSampler.cpp',
      'audio/UpSampler.h',
      'audio/VectorMath.cpp',
      'audio/VectorMath.h',
      'audio/ZeroPole.cpp',
      'audio/ZeroPole.h',
      'audio/android/FFTFrameOpenMAXDLAndroid.cpp',
      'audio/ffmpeg/FFTFrameFFMPEG.cpp',
      'audio/ipp/FFTFrameIPP.cpp',
      'audio/mac/FFTFrameMac.cpp',
      'blob/BlobData.cpp',
      'blob/BlobData.h',
      'blob/BlobRegistry.cpp',
      'blob/BlobRegistry.h',
      'blob/BlobURL.cpp',
      'blob/BlobURL.h',
      'clipboard/ClipboardMimeTypes.cpp',
      'clipboard/ClipboardMimeTypes.h',
      'clipboard/ClipboardUtilities.cpp',
      'clipboard/ClipboardUtilities.h',
      'clipboard/ClipboardUtilitiesPosix.cpp',
      'clipboard/ClipboardUtilitiesWin.cpp',
      'credentialmanager/PlatformCredential.cpp',
      'credentialmanager/PlatformCredential.h',
      'credentialmanager/PlatformFederatedCredential.cpp',
      'credentialmanager/PlatformFederatedCredential.h',
      'credentialmanager/PlatformPasswordCredential.cpp',
      'credentialmanager/PlatformPasswordCredential.h',
      'exported/Platform.cpp',
      'exported/WebActiveGestureAnimation.cpp',
      'exported/WebActiveGestureAnimation.h',
      'exported/WebAudioBus.cpp',
      'exported/WebAudioDevice.cpp',
      'exported/WebBlobData.cpp',
      'exported/WebCompositedDisplayList.cpp',
      'exported/WebCompositorAnimationPlayerClient.cpp',
      'exported/WebContentDecryptionModule.cpp',
      'exported/WebContentDecryptionModuleAccess.cpp',
      'exported/WebContentDecryptionModuleResult.cpp',
      'exported/WebContentDecryptionModuleSession.cpp',
      'exported/WebContentSettingCallbacks.cpp',
      'exported/WebConvertableToTraceFormat.cpp',
      'exported/WebCredential.cpp',
      'exported/WebCryptoAlgorithm.cpp',
      'exported/WebCryptoKey.cpp',
      'exported/WebCryptoKeyAlgorithm.cpp',
      'exported/WebCryptoResult.cpp',
      'exported/WebCursorInfo.cpp',
      'exported/WebData.cpp',
      'exported/WebDataConsumerHandle.cpp',
      'exported/WebDeviceMotionData.cpp',
      'exported/WebDeviceOrientationData.cpp',
      'exported/WebDisplayItemClipTree.cpp',
      'exported/WebDisplayItemTransformTree.cpp',
      'exported/WebDragData.cpp',
      'exported/WebEncryptedMediaClient.cpp',
      'exported/WebEncryptedMediaKeyInformation.cpp',
      'exported/WebEncryptedMediaRequest.cpp',
      'exported/WebFederatedCredential.cpp',
      'exported/WebFileSystemCallbacks.cpp',
      'exported/WebFilterKeyframe.cpp',
      'exported/WebHTTPBody.cpp',
      'exported/WebHTTPLoadInfo.cpp',
      'exported/WebImageSkia.cpp',
      'exported/WebMediaConstraints.cpp',
      'exported/WebMediaDeviceInfo.cpp',
      'exported/WebMediaPlayerClient.cpp',
      'exported/WebMediaPlayerEncryptedMediaClient.cpp',
      'exported/WebMediaStream.cpp',
      'exported/WebMediaStreamSource.cpp',
      'exported/WebMediaStreamTrack.cpp',
      'exported/WebMediaStreamTrackSourcesRequest.cpp',
      'exported/WebMemoryAllocatorDump.cpp',
      'exported/WebMemoryDumpProvider.cpp',
      'exported/WebMessagePortChannelClient.cpp',
      'exported/WebPasswordCredential.cpp',
      'exported/WebPrerender.cpp',
      'exported/WebPrerenderingSupport.cpp',
      'exported/WebPresentationAvailabilityObserver.cpp',
      'exported/WebPresentationController.cpp',
      'exported/WebProcessMemoryDump.cpp',
      'exported/WebRTCConfiguration.cpp',
      'exported/WebRTCICECandidate.cpp',
      'exported/WebRTCOfferOptions.cpp',
      'exported/WebRTCSessionDescription.cpp',
      'exported/WebRTCSessionDescriptionRequest.cpp',
      'exported/WebRTCStatsRequest.cpp',
      'exported/WebRTCStatsResponse.cpp',
      'exported/WebRTCVoidRequest.cpp',
      'exported/WebScrollbarImpl.cpp',
      'exported/WebScrollbarImpl.h',
      'exported/WebScrollbarThemeClientImpl.cpp',
      'exported/WebScrollbarThemeClientImpl.h',
      'exported/WebScrollbarThemeGeometryNative.cpp',
      'exported/WebScrollbarThemeGeometryNative.h',
      'exported/WebScrollbarThemePainter.cpp',
      'exported/WebSecurityOrigin.cpp',
      'exported/WebServicePortProviderClient.cpp',
      'exported/WebServiceWorkerProviderClient.cpp',
      'exported/WebServiceWorkerProxy.cpp',
      'exported/WebServiceWorkerRequest.cpp',
      'exported/WebServiceWorkerResponse.cpp',
      'exported/WebSocketHandshakeRequestInfo.cpp',
      'exported/WebSocketHandshakeResponseInfo.cpp',
      'exported/WebSourceInfo.cpp',
      'exported/WebSpeechSynthesisUtterance.cpp',
      'exported/WebSpeechSynthesisVoice.cpp',
      'exported/WebSpeechSynthesizerClientImpl.cpp',
      'exported/WebSpeechSynthesizerClientImpl.h',
      'exported/WebStorageQuotaCallbacks.cpp',
      'exported/WebThreadSafeData.cpp',
      'exported/WebThreadedDataReceiver.cpp',
      'exported/WebTraceLocation.cpp',
      'exported/WebTransformKeyframe.cpp',
      'exported/WebURL.cpp',
      'exported/WebURLError.cpp',
      'exported/WebURLLoaderClient.cpp',
      'exported/WebURLLoaderTestDelegate.cpp',
      'exported/WebURLLoadTiming.cpp',
      'exported/WebURLRequest.cpp',
      'exported/WebURLRequestPrivate.h',
      'exported/WebURLResponse.cpp',
      'exported/WebURLResponsePrivate.h',
      'exported/WrappedResourceRequest.h',
      'exported/WrappedResourceResponse.h',
      'exported/linux/WebFontInfo.cpp',
      'exported/linux/WebFontRenderStyle.cpp',
      'fonts/AlternateFontFamily.h',
      'fonts/Character.cpp',
      'fonts/Character.h',
      'fonts/CustomFontData.h',
      'fonts/Font.cpp',
      'fonts/Font.h',
      'fonts/FontBaseline.h',
      'fonts/FontCache.cpp',
      'fonts/FontCache.h',
      'fonts/FontCacheClient.h',
      'fonts/FontCacheKey.h',
      'fonts/FontCustomPlatformData.h',
      'fonts/FontCustomPlatformData.cpp',
      'fonts/FontData.cpp',
      'fonts/FontData.h',
      'fonts/FontDataCache.cpp',
      'fonts/FontDataCache.h',
      'fonts/FontDescription.cpp',
      'fonts/FontFaceCreationParams.h',
      'fonts/FontFallbackList.cpp',
      'fonts/FontFallbackList.h',
      'fonts/FontFamily.cpp',
      'fonts/FontFamily.h',
      'fonts/FontFeatureSettings.cpp',
      'fonts/FontFeatureSettings.h',
      'fonts/FontPlatformData.cpp',
      'fonts/FontPlatformData.h',
      'fonts/FontRenderStyle.h',
      'fonts/GenericFontFamilySettings.cpp',
      'fonts/GenericFontFamilySettings.h',
      'fonts/GlyphBuffer.h',
      'fonts/GlyphMetricsMap.h',
      'fonts/GlyphPage.h',
      'fonts/GlyphPageTreeNode.cpp',
      'fonts/GlyphPageTreeNode.h',
      'fonts/Latin1TextIterator.h',
      'fonts/UTF16TextIterator.cpp',
      'fonts/UTF16TextIterator.h',
      'fonts/SegmentedFontData.cpp',
      'fonts/SegmentedFontData.h',
      'fonts/SimpleFontData.cpp',
      'fonts/SimpleFontData.h',
      'fonts/TextBlob.h',
      'fonts/VDMXParser.cpp',
      'fonts/VDMXParser.h',
      'fonts/android/FontCacheAndroid.cpp',
      'fonts/linux/FontCacheLinux.cpp',
      'fonts/linux/FontPlatformDataLinux.cpp',
      'fonts/mac/FontFamilyMatcherMac.h',
      'fonts/mac/FontFamilyMatcherMac.mm',
      'fonts/mac/FontCacheMac.mm',
      'fonts/mac/FontPlatformDataMac.mm',
      'fonts/opentype/OpenTypeSanitizer.cpp',
      'fonts/opentype/OpenTypeSanitizer.h',
      'fonts/opentype/OpenTypeTypes.h',
      'fonts/opentype/OpenTypeVerticalData.cpp',
      'fonts/opentype/OpenTypeVerticalData.h',
      'fonts/shaping/CachingWordShapeIterator.h',
      'fonts/shaping/CachingWordShaper.cpp',
      'fonts/shaping/CachingWordShaper.h',
      'fonts/shaping/HarfBuzzFace.cpp',
      'fonts/shaping/HarfBuzzFace.h',
      'fonts/shaping/HarfBuzzShaper.cpp',
      'fonts/shaping/HarfBuzzShaper.h',
      'fonts/shaping/ShapeCache.h',
      'fonts/shaping/Shaper.cpp',
      'fonts/shaping/Shaper.h',
      'fonts/shaping/SimpleShaper.cpp',
      'fonts/shaping/SimpleShaper.h',
      'fonts/skia/FontCacheSkia.cpp',
      'fonts/win/FontCacheSkiaWin.cpp',
      'fonts/win/FontFallbackWin.cpp',
      'fonts/win/FontFallbackWin.h',
      'fonts/win/FontPlatformDataWin.cpp',
      'geometry/DoublePoint.cpp',
      'geometry/DoublePoint.h',
      'geometry/DoubleRect.cpp',
      'geometry/DoubleRect.h',
      'geometry/DoubleSize.cpp',
      'geometry/DoubleSize.h',
      'geometry/FloatRectOutsets.h',
      'geometry/FloatPoint.cpp',
      'geometry/FloatPoint.h',
      'geometry/FloatPoint3D.cpp',
      'geometry/FloatPoint3D.h',
      'geometry/FloatPolygon.cpp',
      'geometry/FloatPolygon.h',
      'geometry/FloatQuad.cpp',
      'geometry/FloatQuad.h',
      'geometry/FloatRect.cpp',
      'geometry/FloatRect.h',
      'geometry/FloatRoundedRect.cpp',
      'geometry/FloatRoundedRect.h',
      'geometry/FloatSize.cpp',
      'geometry/FloatSize.h',
      'geometry/IntRectOutsets.h',
      'geometry/IntPoint.h',
      'geometry/IntRect.cpp',
      'geometry/IntRect.h',
      'geometry/IntSize.h',
      'geometry/IntSizeHash.h',
      'geometry/LayoutRectOutsets.cpp',
      'geometry/LayoutRectOutsets.h',
      'geometry/LayoutPoint.h',
      'geometry/LayoutRect.cpp',
      'geometry/LayoutRect.h',
      'geometry/LayoutSize.h',
      'geometry/Region.cpp',
      'geometry/Region.h',
      'geometry/TransformState.cpp',
      'geometry/TransformState.h',
      'geometry/cg/FloatPointCG.cpp',
      'geometry/cg/FloatRectCG.cpp',
      'geometry/cg/FloatSizeCG.cpp',
      'geometry/cg/IntPointCG.cpp',
      'geometry/cg/IntRectCG.cpp',
      'geometry/cg/IntSizeCG.cpp',
      'geometry/mac/FloatPointMac.mm',
      'geometry/mac/FloatRectMac.mm',
      'geometry/mac/FloatSizeMac.mm',
      'geometry/mac/IntPointMac.mm',
      'geometry/mac/IntRectMac.mm',
      'geometry/mac/IntSizeMac.mm',
      'graphics/BitmapImage.cpp',
      'graphics/BitmapImage.h',
      'graphics/Canvas2DImageBufferSurface.h',
      'graphics/Canvas2DLayerBridge.cpp',
      'graphics/Canvas2DLayerBridge.h',
      'graphics/Color.cpp',
      'graphics/Color.h',
      'graphics/ColorSpace.cpp',
      'graphics/ColorSpace.h',
      'graphics/CompositedDisplayList.h',
      'graphics/CompositingReasons.cpp',
      'graphics/CompositingReasons.h',
      'graphics/ContentLayerDelegate.cpp',
      'graphics/ContentLayerDelegate.h',
      'graphics/ContiguousContainer.cpp',
      'graphics/ContiguousContainer.h',
      'graphics/CrossfadeGeneratedImage.cpp',
      'graphics/CrossfadeGeneratedImage.h',
      'graphics/DecodingImageGenerator.cpp',
      'graphics/DecodingImageGenerator.h',
      'graphics/DeferredImageDecoder.cpp',
      'graphics/DeferredImageDecoder.h',
      'graphics/ExpensiveCanvasHeuristicParameters.h',
      'graphics/PicturePattern.cpp',
      'graphics/PicturePattern.h',
      'graphics/PictureSnapshot.h',
      'graphics/PictureSnapshot.cpp',
      'graphics/DrawLooperBuilder.cpp',
      'graphics/DrawLooperBuilder.h',
      'graphics/FirstPaintInvalidationTracking.cpp',
      'graphics/FirstPaintInvalidationTracking.h',
      'graphics/FrameData.cpp',
      'graphics/FrameData.h',
      'graphics/GeneratedImage.cpp',
      'graphics/GeneratedImage.h',
      'graphics/Gradient.cpp',
      'graphics/Gradient.h',
      'graphics/GradientGeneratedImage.cpp',
      'graphics/GradientGeneratedImage.h',
      'graphics/GraphicsContext.cpp',
      'graphics/GraphicsContext.h',
      'graphics/GraphicsContextState.cpp',
      'graphics/GraphicsContextState.h',
      'graphics/GraphicsContextStateSaver.h',
      'graphics/GraphicsLayer.cpp',
      'graphics/GraphicsLayer.h',
      'graphics/GraphicsLayerClient.h',
      'graphics/GraphicsLayerDebugInfo.cpp',
      'graphics/GraphicsLayerDebugInfo.h',
      'graphics/GraphicsLayerFactory.h',
      'graphics/GraphicsTypes.cpp',
      'graphics/GraphicsTypes.h',
      'graphics/GraphicsTypes3D.h',
      'graphics/Image.cpp',
      'graphics/Image.h',
      'graphics/ImageAnimationPolicy.h',
      'graphics/ImageBuffer.cpp',
      'graphics/ImageBuffer.h',
      'graphics/ImageBufferClient.h',
      'graphics/ImageBufferSurface.cpp',
      'graphics/ImageBufferSurface.h',
      'graphics/ImageDecodingStore.cpp',
      'graphics/ImageDecodingStore.h',
      'graphics/ImageFrameGenerator.cpp',
      'graphics/ImageFrameGenerator.h',
      'graphics/ImageObserver.cpp',
      'graphics/ImageObserver.h',
      'graphics/ImageOrientation.cpp',
      'graphics/ImageOrientation.h',
      'graphics/ImagePattern.cpp',
      'graphics/ImagePattern.h',
      'graphics/ImageSource.cpp',
      'graphics/ImageSource.h',
      'graphics/InterceptingCanvas.cpp',
      'graphics/InterceptingCanvas.h',
      'graphics/LinkHighlight.h',
      'graphics/LoggingCanvas.cpp',
      'graphics/LoggingCanvas.h',
      'graphics/PaintInvalidationReason.cpp',
      'graphics/PaintInvalidationReason.h',
      'graphics/Path.cpp',
      'graphics/Path.h',
      'graphics/PathTraversalState.cpp',
      'graphics/PathTraversalState.h',
      'graphics/Pattern.cpp',
      'graphics/Pattern.h',
      'graphics/ProfilingCanvas.cpp',
      'graphics/ProfilingCanvas.h',
      'graphics/RecordingImageBufferSurface.cpp',
      'graphics/RecordingImageBufferSurface.h',
      'graphics/ReplayingCanvas.cpp',
      'graphics/ReplayingCanvas.h',
      'graphics/StaticBitmapImage.cpp',
      'graphics/StaticBitmapImage.h',
      'graphics/StrokeData.cpp',
      'graphics/StrokeData.h',
      'graphics/ThreadSafeDataTransport.cpp',
      'graphics/ThreadSafeDataTransport.h',
      'graphics/UnacceleratedImageBufferSurface.cpp',
      'graphics/UnacceleratedImageBufferSurface.h',
      'graphics/cpu/arm/WebGLImageConversionNEON.h',
      'graphics/cpu/x86/WebGLImageConversionSSE.h',
      'graphics/filters/DistantLightSource.cpp',
      'graphics/filters/DistantLightSource.h',
      'graphics/filters/FEBlend.cpp',
      'graphics/filters/FEBlend.h',
      'graphics/filters/FEColorMatrix.cpp',
      'graphics/filters/FEColorMatrix.h',
      'graphics/filters/FEComponentTransfer.cpp',
      'graphics/filters/FEComponentTransfer.h',
      'graphics/filters/FEComposite.cpp',
      'graphics/filters/FEComposite.h',
      'graphics/filters/FEConvolveMatrix.cpp',
      'graphics/filters/FEConvolveMatrix.h',
      'graphics/filters/FEDiffuseLighting.cpp',
      'graphics/filters/FEDiffuseLighting.h',
      'graphics/filters/FEDisplacementMap.cpp',
      'graphics/filters/FEDisplacementMap.h',
      'graphics/filters/FEDropShadow.cpp',
      'graphics/filters/FEDropShadow.h',
      'graphics/filters/FEFlood.cpp',
      'graphics/filters/FEFlood.h',
      'graphics/filters/FEGaussianBlur.cpp',
      'graphics/filters/FEGaussianBlur.h',
      'graphics/filters/FELighting.cpp',
      'graphics/filters/FELighting.h',
      'graphics/filters/FEMerge.cpp',
      'graphics/filters/FEMerge.h',
      'graphics/filters/FEMorphology.cpp',
      'graphics/filters/FEMorphology.h',
      'graphics/filters/FEOffset.cpp',
      'graphics/filters/FEOffset.h',
      'graphics/filters/FESpecularLighting.cpp',
      'graphics/filters/FESpecularLighting.h',
      'graphics/filters/FETile.cpp',
      'graphics/filters/FETile.h',
      'graphics/filters/FETurbulence.cpp',
      'graphics/filters/FETurbulence.h',
      'graphics/filters/Filter.h',
      'graphics/filters/FilterEffect.cpp',
      'graphics/filters/FilterEffect.h',
      'graphics/filters/FilterOperation.cpp',
      'graphics/filters/FilterOperation.h',
      'graphics/filters/FilterOperations.cpp',
      'graphics/filters/FilterOperations.h',
      'graphics/filters/LightSource.cpp',
      'graphics/filters/LightSource.h',
      'graphics/filters/PointLightSource.cpp',
      'graphics/filters/PointLightSource.h',
      'graphics/filters/ReferenceFilter.cpp',
      'graphics/filters/ReferenceFilter.h',
      'graphics/filters/SkiaImageFilterBuilder.cpp',
      'graphics/filters/SkiaImageFilterBuilder.h',
      'graphics/filters/SourceAlpha.cpp',
      'graphics/filters/SourceAlpha.h',
      'graphics/filters/SourceGraphic.cpp',
      'graphics/filters/SourceGraphic.h',
      'graphics/filters/SpotLightSource.cpp',
      'graphics/filters/SpotLightSource.h',
      'graphics/gpu/AcceleratedImageBufferSurface.cpp',
      'graphics/gpu/AcceleratedImageBufferSurface.h',
      'graphics/gpu/DrawingBuffer.cpp',
      'graphics/gpu/DrawingBuffer.h',
      'graphics/gpu/Extensions3DUtil.cpp',
      'graphics/gpu/Extensions3DUtil.h',
      'graphics/gpu/WebGLImageConversion.cpp',
      'graphics/gpu/WebGLImageConversion.h',
      'graphics/paint/CachedDisplayItem.h',
      'graphics/paint/ClipDisplayItem.cpp',
      'graphics/paint/ClipDisplayItem.h',
      'graphics/paint/ClipPathDisplayItem.cpp',
      'graphics/paint/ClipPathDisplayItem.h',
      'graphics/paint/ClipPathRecorder.cpp',
      'graphics/paint/ClipPathRecorder.h',
      'graphics/paint/ClipRecorder.cpp',
      'graphics/paint/ClipRecorder.h',
      'graphics/paint/DisplayItem.cpp',
      'graphics/paint/DisplayItem.h',
      'graphics/paint/DisplayItemCacheSkipper.h',
      'graphics/paint/DisplayItemClient.h',
      'graphics/paint/DisplayItemList.cpp',
      'graphics/paint/DisplayItemList.h',
      'graphics/paint/DisplayItemClipTree.cpp',
      'graphics/paint/DisplayItemClipTree.h',
      'graphics/paint/DisplayItemPropertyTreeBuilder.cpp',
      'graphics/paint/DisplayItemPropertyTreeBuilder.h',
      'graphics/paint/DisplayItemTransformTree.cpp',
      'graphics/paint/DisplayItemTransformTree.h',
      'graphics/paint/DrawingDisplayItem.cpp',
      'graphics/paint/DrawingDisplayItem.h',
      'graphics/paint/DrawingRecorder.cpp',
      'graphics/paint/DrawingRecorder.h',
      'graphics/paint/FilterDisplayItem.cpp',
      'graphics/paint/FilterDisplayItem.h',
      'graphics/paint/FixedPositionContainerDisplayItem.cpp',
      'graphics/paint/FixedPositionContainerDisplayItem.h',
      'graphics/paint/FixedPositionDisplayItem.cpp',
      'graphics/paint/FixedPositionDisplayItem.h',
      'graphics/paint/FloatClipDisplayItem.cpp',
      'graphics/paint/FloatClipDisplayItem.h',
      'graphics/paint/ScrollDisplayItem.cpp',
      'graphics/paint/ScrollDisplayItem.h',
      'graphics/paint/SkPictureBuilder.h',
      'graphics/paint/SubtreeDisplayItem.h',
      'graphics/paint/SubtreeRecorder.cpp',
      'graphics/paint/SubtreeRecorder.h',
      'graphics/paint/Transform3DDisplayItem.cpp',
      'graphics/paint/Transform3DDisplayItem.h',
      'graphics/paint/TransformDisplayItem.cpp',
      'graphics/paint/TransformDisplayItem.h',
      'graphics/paint/CompositingDisplayItem.cpp',
      'graphics/paint/CompositingDisplayItem.h',
      'graphics/skia/SkSizeHash.h',
      'graphics/skia/SkiaUtils.cpp',
      'graphics/skia/SkiaUtils.h',
      'image-decoders/FastSharedBufferReader.cpp',
      'image-decoders/FastSharedBufferReader.h',
      'image-decoders/ImageAnimation.h',
      'image-decoders/ImageDecoder.cpp',
      'image-decoders/ImageDecoder.h',
      'image-decoders/ImageFrame.cpp',
      'image-decoders/ImageFrame.h',
      'image-decoders/bmp/BMPImageDecoder.cpp',
      'image-decoders/bmp/BMPImageDecoder.h',
      'image-decoders/bmp/BMPImageReader.cpp',
      'image-decoders/bmp/BMPImageReader.h',
      'image-decoders/gif/GIFImageDecoder.cpp',
      'image-decoders/gif/GIFImageDecoder.h',
      'image-decoders/gif/GIFImageReader.cpp',
      'image-decoders/gif/GIFImageReader.h',
      'image-decoders/ico/ICOImageDecoder.cpp',
      'image-decoders/ico/ICOImageDecoder.h',
      'image-decoders/jpeg/JPEGImageDecoder.cpp',
      'image-decoders/jpeg/JPEGImageDecoder.h',
      'image-decoders/png/PNGImageDecoder.cpp',
      'image-decoders/png/PNGImageDecoder.h',
      'image-decoders/webp/WEBPImageDecoder.cpp',
      'image-decoders/webp/WEBPImageDecoder.h',
      'image-encoders/skia/JPEGImageEncoder.cpp',
      'image-encoders/skia/JPEGImageEncoder.h',
      'image-encoders/skia/PNGImageEncoder.cpp',
      'image-encoders/skia/PNGImageEncoder.h',
      'image-encoders/skia/WEBPImageEncoder.cpp',
      'image-encoders/skia/WEBPImageEncoder.h',
      'mac/BlockExceptions.h',
      'mac/BlockExceptions.mm',
      'mac/ColorMac.h',
      'mac/ColorMac.mm',
      'mac/KillRingMac.mm',
      'mac/LocalCurrentGraphicsContext.h',
      'mac/LocalCurrentGraphicsContext.mm',
      'mac/NSScrollerImpDetails.h',
      'mac/ScrollAnimatorMac.h',
      'mac/ScrollAnimatorMac.mm',
      'mac/ThemeMac.h',
      'mac/ThemeMac.mm',
      'mac/VersionUtilMac.h',
      'mac/VersionUtilMac.mm',
      'mac/WebCoreNSCellExtras.h',
      'mac/WebCoreNSCellExtras.mm',
      'mediastream/MediaStreamCenter.cpp',
      'mediastream/MediaStreamCenter.h',
      'mediastream/MediaStreamComponent.cpp',
      'mediastream/MediaStreamComponent.h',
      'mediastream/MediaStreamDescriptor.cpp',
      'mediastream/MediaStreamDescriptor.h',
      'mediastream/MediaStreamSource.cpp',
      'mediastream/MediaStreamSource.h',
      'mediastream/MediaStreamTrackSourcesRequest.h',
      'mediastream/MediaStreamWebAudioSource.cpp',
      'mediastream/MediaStreamWebAudioSource.h',
      'mediastream/RTCConfiguration.h',
      'mediastream/RTCSessionDescriptionRequest.h',
      'mediastream/RTCStatsRequest.h',
      'mediastream/RTCStatsResponseBase.h',
      'mediastream/RTCVoidRequest.h',
      'mhtml/ArchiveResource.cpp',
      'mhtml/ArchiveResourceCollection.cpp',
      'mhtml/ArchiveResourceCollection.h',
      'mhtml/MHTMLArchive.cpp',
      'mhtml/MHTMLArchive.h',
      'mhtml/MHTMLParser.cpp',
      'mhtml/MHTMLParser.h',
      'network/ContentSecurityPolicyParsers.cpp',
      'network/ContentSecurityPolicyParsers.h',
      'network/ContentSecurityPolicyResponseHeaders.cpp',
      'network/ContentSecurityPolicyResponseHeaders.h',
      'network/FormData.cpp',
      'network/FormData.h',
      'network/FormDataBuilder.cpp',
      'network/FormDataBuilder.h',
      'network/HTTPHeaderMap.cpp',
      'network/HTTPHeaderMap.h',
      'network/HTTPParsers.cpp',
      'network/HTTPParsers.h',
      'network/HTTPRequest.cpp',
      'network/HTTPRequest.h',
      'network/NetworkHints.cpp',
      'network/NetworkHints.h',
      'network/ParsedContentType.cpp',
      'network/ParsedContentType.h',
      'network/ResourceError.cpp',
      'network/ResourceError.h',
      'network/ResourceRequest.cpp',
      'network/ResourceRequest.h',
      'network/ResourceResponse.cpp',
      'network/ResourceResponse.h',
      'network/ResourceTimingInfo.cpp',
      'network/ResourceTimingInfo.h',
      'network/WebSocketHandshakeRequest.cpp',
      'network/WebSocketHandshakeRequest.h',
      'network/WebSocketHandshakeResponse.cpp',
      'network/WebSocketHandshakeResponse.h',
      'plugins/PluginData.cpp',
      'plugins/PluginData.h',
      'plugins/PluginListBuilder.cpp',
      'plugins/PluginListBuilder.h',
      'scheduler/CancellableTaskFactory.cpp',
      'scheduler/CancellableTaskFactory.h',
      'scroll/ProgrammaticScrollAnimator.cpp',
      'scroll/ProgrammaticScrollAnimator.h',
      'scroll/ScrollAnimator.cpp',
      'scroll/ScrollAnimator.h',
      'scroll/ScrollAnimatorNone.cpp',
      'scroll/ScrollAnimatorNone.h',
      'scroll/ScrollTypes.h',
      'scroll/ScrollableArea.cpp',
      'scroll/ScrollableArea.h',
      'scroll/Scrollbar.cpp',
      'scroll/Scrollbar.h',
      'scroll/ScrollbarTheme.cpp',
      'scroll/ScrollbarTheme.h',
      'scroll/ScrollbarThemeAndroid.cpp',
      'scroll/ScrollbarThemeAura.cpp',
      'scroll/ScrollbarThemeAura.h',
      'scroll/ScrollbarThemeClient.h',
      'scroll/ScrollbarThemeMacCommon.h',
      'scroll/ScrollbarThemeMacCommon.mm',
      'scroll/ScrollbarThemeMacNonOverlayAPI.h',
      'scroll/ScrollbarThemeMacNonOverlayAPI.mm',
      'scroll/ScrollbarThemeMacOverlayAPI.h',
      'scroll/ScrollbarThemeMacOverlayAPI.mm',
      'scroll/ScrollbarThemeMock.cpp',
      'scroll/ScrollbarThemeMock.h',
      'scroll/ScrollbarThemeNonMacCommon.cpp',
      'scroll/ScrollbarThemeNonMacCommon.h',
      'scroll/ScrollbarThemeOverlay.cpp',
      'scroll/ScrollbarThemeOverlay.h',
      'scroll/ScrollbarThemeOverlayMock.h',
      'speech/PlatformSpeechSynthesisUtterance.cpp',
      'speech/PlatformSpeechSynthesisUtterance.h',
      'speech/PlatformSpeechSynthesisVoice.cpp',
      'speech/PlatformSpeechSynthesisVoice.h',
      'speech/PlatformSpeechSynthesizer.cpp',
      'speech/PlatformSpeechSynthesizer.h',
      'text/BidiCharacterRun.cpp',
      'text/BidiCharacterRun.h',
      'text/BidiContext.cpp',
      'text/BidiContext.h',
      'text/BidiResolver.h',
      'text/BidiRunList.h',
      'text/BidiTextRun.cpp',
      'text/BidiTextRun.h',
      'text/DateTimeFormat.cpp',
      'text/DateTimeFormat.h',
      'text/DecodeEscapeSequences.h',
      'text/LineEnding.cpp',
      'text/LineEnding.h',
      'text/LocaleICU.cpp',
      'text/LocaleICU.h',
      'text/LocaleMac.h',
      'text/LocaleMac.mm',
      'text/LocaleToScriptMapping.cpp',
      'text/LocaleToScriptMapping.h',
      'text/LocaleWin.cpp',
      'text/LocaleWin.h',
      'text/ParserUtilities.h',
      'text/PlatformLocale.cpp',
      'text/PlatformLocale.h',
      'text/QuotedPrintable.cpp',
      'text/QuotedPrintable.h',
      'text/SegmentedString.cpp',
      'text/SegmentedString.h',
      'text/StringTruncator.cpp',
      'text/StringTruncator.h',
      'text/SuffixTree.h',
      'text/TextBoundaries.cpp',
      'text/TextBoundaries.h',
      'text/TextBreakIterator.cpp',
      'text/TextBreakIterator.h',
      'text/TextBreakIteratorICU.cpp',
      'text/TextBreakIteratorInternalICU.cpp',
      'text/TextBreakIteratorInternalICU.h',
      'text/TextCheckerClient.cpp',
      'text/TextCheckerClient.h',
      'text/TextChecking.h',
      'text/TextDecoration.h',
      'text/TextEncodingDetector.cpp',
      'text/TextEncodingDetector.h',
      'text/TextPath.h',
      'text/TextRun.cpp',
      'text/TextRun.h',
      'text/TextRunIterator.h',
      'text/TextStream.cpp',
      'text/TextStream.h',
      'text/UnicodeBidi.h',
      'text/UnicodeRange.cpp',
      'text/UnicodeRange.h',
      'text/UnicodeUtilities.cpp',
      'text/UnicodeUtilities.h',
      'transforms/AffineTransform.cpp',
      'transforms/AffineTransform.h',
      'transforms/IdentityTransformOperation.h',
      'transforms/InterpolatedTransformOperation.cpp',
      'transforms/InterpolatedTransformOperation.h',
      'transforms/Matrix3DTransformOperation.cpp',
      'transforms/Matrix3DTransformOperation.h',
      'transforms/MatrixTransformOperation.cpp',
      'transforms/MatrixTransformOperation.h',
      'transforms/PerspectiveTransformOperation.cpp',
      'transforms/PerspectiveTransformOperation.h',
      'transforms/RotateTransformOperation.cpp',
      'transforms/RotateTransformOperation.h',
      'transforms/ScaleTransformOperation.cpp',
      'transforms/ScaleTransformOperation.h',
      'transforms/SkewTransformOperation.cpp',
      'transforms/SkewTransformOperation.h',
      'transforms/TransformOperations.cpp',
      'transforms/TransformationMatrix.cpp',
      'transforms/TransformationMatrix.h',
      'transforms/TranslateTransformOperation.cpp',
      'transforms/TranslateTransformOperation.h',
      'weborigin/DatabaseIdentifier.cpp',
      'weborigin/DatabaseIdentifier.h',
      'weborigin/KURL.cpp',
      'weborigin/KURL.h',
      'weborigin/KURLHash.h',
      'weborigin/KnownPorts.cpp',
      'weborigin/KnownPorts.h',
      'weborigin/OriginAccessEntry.cpp',
      'weborigin/OriginAccessEntry.h',
      'weborigin/Referrer.h',
      'weborigin/ReferrerPolicy.h',
      'weborigin/SchemeRegistry.cpp',
      'weborigin/SchemeRegistry.h',
      'weborigin/SecurityOrigin.cpp',
      'weborigin/SecurityOrigin.h',
      'weborigin/SecurityOriginCache.h',
      'weborigin/SecurityOriginHash.h',
      'weborigin/SecurityPolicy.cpp',
      'weborigin/SecurityPolicy.h',
      'win/HWndDC.h',
      'win/SystemInfo.cpp',
      'win/SystemInfo.h',
    ],
    'platform_test_files': [
      'ClockTest.cpp',
      'DecimalTest.cpp',
      'DragImageTest.cpp',
      'LayoutUnitTest.cpp',
      'LifecycleContextTest.cpp',
      'PODArenaTest.cpp',
      'PODFreeListArenaTest.cpp',
      'PODIntervalTreeTest.cpp',
      'PODRedBlackTreeTest.cpp',
      'PurgeableVectorTest.cpp',
      'SharedBufferTest.cpp',
      'TestingPlatformSupport.cpp',
      'TestingPlatformSupport.h',
      'TimerTest.cpp',
      'TracedValueTest.cpp',
      'UUIDTest.cpp',
      'WebScreenInfoTest.cpp',
      'WebVectorTest.cpp',
      'animation/TimingFunctionTest.cpp',
      'animation/UnitBezierTest.cpp',
      'blob/BlobDataTest.cpp',
      'clipboard/ClipboardUtilitiesTest.cpp',
      'fonts/FontCacheTest.cpp',
      'fonts/FontDescriptionTest.cpp',
      'fonts/FontTest.cpp',
      'fonts/GlyphBufferTest.cpp',
      'fonts/GlyphPageTreeNodeTest.cpp',
      'fonts/android/FontCacheAndroidTest.cpp',
      'fonts/mac/FontFamilyMatcherMacTest.mm',
      'fonts/shaping/CachingWordShaperTest.cpp',
      'fonts/shaping/HarfBuzzShaperTest.cpp',
      'geometry/FloatBoxTest.cpp',
      'geometry/FloatBoxTestHelpers.cpp',
      'geometry/FloatPointTest.cpp',
      'geometry/FloatPolygonTest.cpp',
      'geometry/FloatRoundedRectTest.cpp',
      'geometry/FloatSizeTest.cpp',
      'geometry/GeometryTestHelpers.cpp',
      'geometry/LayoutRectOutsetsTest.cpp',
      'geometry/RegionTest.cpp',
      'graphics/ContiguousContainerTest.cpp',
      'graphics/GraphicsContextTest.cpp',
      'graphics/RecordingImageBufferSurfaceTest.cpp',
      'graphics/ThreadSafeDataTransportTest.cpp',
      'graphics/filters/FilterOperationsTest.cpp',
      'graphics/filters/ImageFilterBuilderTest.cpp',
      'graphics/gpu/DrawingBufferTest.cpp',
      'graphics/paint/DisplayItemPropertyTreeBuilderTest.cpp',
      'graphics/paint/DisplayItemListTest.cpp',
      'graphics/paint/DisplayItemTest.cpp',
      'image-decoders/FastSharedBufferReaderTest.cpp',
      'image-decoders/ImageDecoderTest.cpp',
      'mac/VersionUtilMacTest.mm',
      'network/FormDataTest.cpp',
      'network/HTTPParsersTest.cpp',
      'network/ResourceRequestTest.cpp',
      'scheduler/CancellableTaskFactoryTest.cpp',
      'scroll/ScrollableAreaTest.cpp',
      'testing/ArenaTestHelpers.h',
      'testing/TreeTestHelpers.cpp',
      'testing/TreeTestHelpers.h',
      'text/BidiResolverTest.cpp',
      'text/DateTimeFormatTest.cpp',
      'text/SegmentedStringTest.cpp',
      'text/UnicodeUtilitiesTest.cpp',
      'transforms/TransformOperationsTest.cpp',
      'transforms/TransformTestHelper.h',
      'transforms/TransformationMatrixTest.cpp',
      'weborigin/DatabaseIdentifierTest.cpp',
      'weborigin/KnownPortsTest.cpp',
      'weborigin/KURLTest.cpp',
      'weborigin/OriginAccessEntryTest.cpp',
      'weborigin/SchemeRegistryTest.cpp',
      'weborigin/SecurityOriginTest.cpp',
      'weborigin/SecurityPolicyTest.cpp',
    ],
    # NOTE: These are legacy unit tests and tests that require a Platform
    # object. Do not add more unless the test requires a Platform object.
    # These tests are a part of the web:webkit_unit_tests binary.
    'platform_web_unittest_files': [
      'fonts/FontPlatformDataTest.cpp',
      'fonts/TestFontSelector.h',
      'graphics/BitmapImageTest.cpp',
      'graphics/Canvas2DLayerBridgeTest.cpp',
      'graphics/DeferredImageDecoderTest.cpp',
      'graphics/GraphicsLayerTest.cpp',
      'graphics/ImageDecodingStoreTest.cpp',
      'graphics/ImageFrameGeneratorTest.cpp',
      'graphics/ImageLayerChromiumTest.cpp',
      'graphics/test/MockImageDecoder.h',
      'graphics/test/MockWebGraphicsContext3D.h',
      'image-decoders/ImageDecoderTestHelpers.cpp',
      'image-decoders/bmp/BMPImageDecoderTest.cpp',
      'image-decoders/gif/GIFImageDecoderTest.cpp',
      'image-decoders/jpeg/JPEGImageDecoderTest.cpp',
      'image-decoders/webp/WEBPImageDecoderTest.cpp',
    ],
    # TODO(jbroman): Move these into platform_test_support_files.
    'platform_unittest_support_files': [
      'testing/URLTestHelpers.cpp',
      'testing/URLTestHelpers.h',
      'testing/UnitTestHelpers.cpp',
      'testing/UnitTestHelpers.h',
    ],
    'platform_test_support_files': [
      'testing/GeometryPrinters.cpp',
      'testing/GeometryPrinters.h',
    ],
    'conditions': [
      ['OS=="win"',
        {
          'platform_test_files': [
            'text/LocaleWinTest.cpp',
          ],
        }
      ],
      ['OS=="mac"',
        {
          'platform_test_files': [
            'text/LocaleMacTest.cpp',
          ]
        }
      ],
      ['os_posix==1 and OS!="mac"',
        {
          'platform_test_files': [
            'text/LocaleICUTest.cpp',
          ],
        }
      ],
    ],
  },
}
