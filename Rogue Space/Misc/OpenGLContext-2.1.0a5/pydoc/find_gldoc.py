"""Determine links to gl, glu, glut and gle documentation

Extremely simple version with directory listing of the
manual directory as a dictionary.
"""
from OpenGL import GL, GLU, GLUT, GLE
import os, string, sys, glob, operator

BASEURL = "http://pyopengl.sourceforge.net/documentation/manual/"

def findName( name ):
	"""The interface to the module, pass a name to check against
	a list of known documentation.  Returns a fully-qualified URL
	to the document or None."""
	baseName = SPECIALCASES.get( name, name )
	result = FILE_MAPPING.get( baseName )
	if result:
		return BASEURL+result
	else:
		while baseName and baseName[-1] in 'dfiuvbs4321':
			baseName = baseName[:-1]
			result = FILE_MAPPING.get( baseName )
			if result and baseName in ('glut', 'glu', 'gl', 'gle'):
				if name != baseName:
					return None
				else:
					return BASEURL+result
			elif result:
				return BASEURL+result
	return None

SPECIALCASES = {
	'glDisable':"glEnable",
	'glDisableClientState':"glEnableClientState",
	'glEnd':"glBegin",
	'glEndList':"glNewList",
	'glGetBoolean':"glGet",
	'glGetBooleanv':"glGet",
	'glGetDouble':"glGet",
	'glGetDoublev':"glGet",
	'glGetFloatv':"glGet",
	'glGetFloat':"glGet",
	'glGetInteger':"glGet",
	'glGetIntegerv':"glGet",
	'glPopAttrib':"glPushAttrib",
	'glPopClientAttrib':"glPushClientAttrib",
	'glPopMatrix':"glPushMatrix",
	'glPopName':"glPushName",
	
	'gluEndCurve':"gluBeginCurve",
	'gluEndPolygon':"gluBeginPolygon",
	'gluEndSurface':"gluBeginSurface",
	'gluEndTrim':"gluBeginTrim",
	'gluTessEndContour':"gluTessBeginContour",
	
	'glutBitmapLength':"glutBitmapWidth",
	'glutDetachMenu':"glutAttachMenu",
	'glutGetMenu':"glutSetMenu",
	'glutGetWindow':"glutSetWindow",
	'glutHideOverlay':"glutShowOverlay",
	'glutHideWindow':"glutShowWindow",
	'glutIconifyWindow':"glutShowWindow",
	'glutInitWindowSize':"glutInitWindowPosition",
	'glutLeaveGameMode':"glutEnterGameMode",
	'glutMenuStateFunc':"glutMenuStatusFunc",
	'glutPassiveMotionFunc':"glutMotionFunc",
	'glutPostWindowOverlayRedisplay':"glutPostOverlayRedisplay",
	'glutPostWindowRedisplay':"glutPostRedisplay",
	'glutPushWindow':"glutPopWindow",
	'glutSetIconTitle':"glutSetWindowTitle",
	'glutStrokeLength':"glutStrokeWidth",
	'glutStrokeLengthf':"glutStrokeWidth",
	'glutWireCone':"glutSolidCone",
	'glutWireCube':"glutSolidCube",
	'glutWireDodecahedron':"glutSolidDodecahedron",
	'glutWireIcosahedron':"glutSolidIcosahedron",
	'glutWireOctahedron':"glutSolidOctahedron",
	'glutWireSphere':"glutSolidSphere",
	'glutWireTeapot':"glutSolidTeapot",
	'glutWireTetrahedron':"glutSolidTetrahedron",
	'glutWireTorus':"glutSolidTorus",
	"glutRemoveLayer": "glutRemoveOverlay",

	# not there!
	"glutSpaceballMotion":"glutSpaceballMotionFunc",
	"glutRemoveItem":"glutRemoveMenuItem",
	
	'gleGetJoinStyle':"gleSetJoinStyle",
	# not there!
	'gleGetNumSides':"",
	'gleSetNumSides':"",    
}

def exists( baseName, folder ):
	return FILE_MAPPING.get( baseName )

FILE_MAPPING = {
	'glViewport':"glViewport.3G.html",
	'glVertexPointer':"glVertexPointer.3G.html",
	'glVertex':"glVertex.3G.html",
	'gluUnProject4':"gluUnProject4.3G.html",
	'gluUnProject':"gluUnProject.3G.html",
	'glutWindowStatusFunc':"glutWindowStatusFunc.3GLUT.html",
	'glutWarpPointer':"glutWarpPointer.3GLUT.html",
	'glutVisibilityFunc':"glutVisibilityFunc.3GLUT.html",
	'glutVideoResizeGet':"glutVideoResizeGet.3GLUT.html",
	'glutUseLayer':"glutUseLayer.3GLUT.html",
	'glutTimerFunc':"glutTimerFunc.3GLUT.html",
	'glutTabletMotionFunc':"glutTabletMotionFunc.3GLUT.html",
	'glutTabletButtonFunc':"glutTabletButtonFunc.3GLUT.html",
	'glutSwapBuffers':"glutSwapBuffers.3GLUT.html",
	'glutStrokeWidth':"glutStrokeWidth.3GLUT.html",
	'glutStrokeCharacter':"glutStrokeCharacter.3GLUT.html",
	'glutSpecialUpFunc':"glutSpecialUpFunc.3GLUT.html",
	'glutSpecialFunc':"glutSpecialFunc.3GLUT.html",
	'glutSpaceballRotateFunc':"glutSpaceballRotateFunc.3GLUT.html",
	'glutSpaceballMotionFunc':"glutSpaceballMotionFunc.3GLUT.html",
	'glutSpaceballButtonFunc':"glutSpaceballButtonFunc.3GLUT.html",
	'glutSolidTorus':"glutSolidTorus.3GLUT.html",
	'glutSolidTetrahedron':"glutSolidTetrahedron.3GLUT.html",
	'glutSolidTeapot':"glutSolidTeapot.3GLUT.html",
	'glutSolidSphere':"glutSolidSphere.3GLUT.html",
	'glutSolidOctahedron':"glutSolidOctahedron.3GLUT.html",
	'glutSolidIcosahedron':"glutSolidIcosahedron.3GLUT.html",
	'glutSolidDodecahedron':"glutSolidDodecahedron.3GLUT.html",
	'glutSolidCube':"glutSolidCube.3GLUT.html",
	'glutSolidCone':"glutSolidCone.3GLUT.html",
	'glutShowWindow':"glutShowWindow.3GLUT.html",
	'glutShowOverlay':"glutShowOverlay.3GLUT.html",
	'glutSetWindowTitle':"glutSetWindowTitle.3GLUT.html",
	'glutSetWindow':"glutSetWindow.3GLUT.html",
	'glutSetMenu':"glutSetMenu.3GLUT.html",
	'glutSetKeyRepeat':"glutSetKeyRepeat.3GLUT.html",
	'glutSetCursor':"glutSetCursor.3GLUT.html",
	'glutSetColor':"glutSetColor.3GLUT.html",
	'glutReshapeWindow':"glutReshapeWindow.3GLUT.html",
	'glutReshapeFunc':"glutReshapeFunc.3GLUT.html",
	'glutReportErrors':"glutReportErrors.3GLUT.html",
	'glutRemoveMenuItem':"glutRemoveMenuItem.3GLUT.html",
	'glutRemoveLayer':"glutRemoveLayer.3GLUT.html",
	'glutPostRedisplay':"glutPostRedisplay.3GLUT.html",
	'glutPostOverlayRedisplay':"glutPostOverlayRedisplay.3GLUT.html",
	'glutPositionWindow':"glutPositionWindow.3GLUT.html",
	'glutPopWindow':"glutPopWindow.3GLUT.html",
	'glutOverlayDisplayFunc':"glutOverlayDisplayFunc.3GLUT.html",
	'glutMouseFunc':"glutMouseFunc.3GLUT.html",
	'glutMotionFunc':"glutMotionFunc.3GLUT.html",
	'glutMenuStatusFunc':"glutMenuStatusFunc.3GLUT.html",
	'glutMainLoop':"glutMainLoop.3GLUT.html",
	'glutLayerGet':"glutLayerGet.3GLUT.html",
	'glutKeyboardUpFunc':"glutKeyboardUpFunc.3GLUT.html",
	'glutKeyboardFunc':"glutKeyboardFunc.3GLUT.html",
	'glutJoystickFunc':"glutJoystickFunc.3GLUT.html",
	'glutInitWindowPosition':"glutInitWindowPosition.3GLUT.html",
	'glutInitDisplayString':"glutInitDisplayString.3GLUT.html",
	'glutInitDisplayMode':"glutInitDisplayMode.3GLUT.html",
	'glutInit':"glutInit.3GLUT.html",
	'glutIgnoreKeyRepeat':"glutIgnoreKeyRepeat.3GLUT.html",
	'glutIdleFunc':"glutIdleFunc.3GLUT.html",
	'glutGetModifiers':"glutGetModifiers.3GLUT.html",
	'glutGetColor':"glutGetColor.3GLUT.html",
	'glutGet':"glutGet.3GLUT.html",
	'glutGameModeString':"glutGameModeString.3GLUT.html",
	'glutGameModeGet':"glutGameModeGet.3GLUT.html",
	'glutFullScreen':"glutFullScreen.3GLUT.html",
	'glutForceJoystickFunc':"glutForceJoystickFunc.3GLUT.html",
	'glutExtensionSupported':"glutExtensionSupported.3GLUT.html",
	'glutEstablishOverlay':"glutEstablishOverlay.3GLUT.html",
	'gluTessVertex':"gluTessVertex.3G.html",
	'gluTessProperty':"gluTessProperty.3G.html",
	'gluTessNormal':"gluTessNormal.3G.html",
	'gluTessEndPolygon':"gluTessEndPolygon.3G.html",
	'gluTessCallback':"gluTessCallback.3G.html",
	'gluTessBeginPolygon':"gluTessBeginPolygon.3G.html",
	'gluTessBeginContour':"gluTessBeginContour.3G.html",
	'glutEntryFunc':"glutEntryFunc.3GLUT.html",
	'glutEnterGameMode':"glutEnterGameMode.3GLUT.html",
	'glutDisplayFunc':"glutDisplayFunc.3GLUT.html",
	'glutDialsFunc':"glutDialsFunc.3GLUT.html",
	'glutDeviceGet':"glutDeviceGet.3GLUT.html",
	'glutDestroyWindow':"glutDestroyWindow.3GLUT.html",
	'glutDestroyMenu':"glutDestroyMenu.3GLUT.html",
	'glutCreateWindow':"glutCreateWindow.3GLUT.html",
	'glutCreateSubWindow':"glutCreateSubWindow.3GLUT.html",
	'glutCreateMenu':"glutCreateMenu.3GLUT.html",
	'glutCopyColormap':"glutCopyColormap.3GLUT.html",
	'glutChangeToSubMenu':"glutChangeToSubMenu.3GLUT.html",
	'glutChangeToMenuEntry':"glutChangeToMenuEntry.3GLUT.html",
	'glutButtonBoxFunc':"glutButtonBoxFunc.3GLUT.html",
	'glutBitmapWidth':"glutBitmapWidth.3GLUT.html",
	'glutBitmapCharacter':"glutBitmapCharacter.3GLUT.html",
	'glutAttachMenu':"glutAttachMenu.3GLUT.html",
	'glutAddSubMenu':"glutAddSubMenu.3GLUT.html",
	'glutAddMenuEntry':"glutAddMenuEntry.3GLUT.html",
	'glut':"glut.3GLUT.html",
	'gluSphere':"gluSphere.3G.html",
	'gluScaleImage':"gluScaleImage.3G.html",
	'gluQuadricTexture':"gluQuadricTexture.3G.html",
	'gluQuadricOrientation':"gluQuadricOrientation.3G.html",
	'gluQuadricNormals':"gluQuadricNormals.3G.html",
	'gluQuadricDrawStyle':"gluQuadricDrawStyle.3G.html",
	'gluQuadricCallback':"gluQuadricCallback.3G.html",
	'gluPwlCurve':"gluPwlCurve.3G.html",
	'gluProject':"gluProject.3G.html",
	'gluPickMatrix':"gluPickMatrix.3G.html",
	'gluPerspective':"gluPerspective.3G.html",
	'gluPartialDisk':"gluPartialDisk.3G.html",
	'gluOrtho2D':"gluOrtho2D.3G.html",
	'gluNurbsSurface':"gluNurbsSurface.3G.html",
	'gluNurbsProperty':"gluNurbsProperty.3G.html",
	'gluNurbsCurve':"gluNurbsCurve.3G.html",
	'gluNurbsCallbackDataEXT':"gluNurbsCallbackDataEXT.3G.html",
	'gluNurbsCallbackData':"gluNurbsCallbackData.3G.html",
	'gluNurbsCallback':"gluNurbsCallback.3G.html",
	'gluNextContour':"gluNextContour.3G.html",
	'gluNewTess':"gluNewTess.3G.html",
	'gluNewQuadric':"gluNewQuadric.3G.html",
	'gluNewNurbsRenderer':"gluNewNurbsRenderer.3G.html",
	'gluLookAt':"gluLookAt.3G.html",
	'gluLoadSamplingMatrices':"gluLoadSamplingMatrices.3G.html",
	'gluGetTessProperty':"gluGetTessProperty.3G.html",
	'gluGetString':"gluGetString.3G.html",
	'gluGetNurbsProperty':"gluGetNurbsProperty.3G.html",
	'gluErrorString':"gluErrorString.3G.html",
	'gluDisk':"gluDisk.3G.html",
	'gluDeleteTess':"gluDeleteTess.3G.html",
	'gluDeleteQuadric':"gluDeleteQuadric.3G.html",
	'gluDeleteNurbsRenderer':"gluDeleteNurbsRenderer.3G.html",
	'gluCylinder':"gluCylinder.3G.html",
	'gluCheckExtension':"gluCheckExtension.3G.html",
	'gluBuild3DMipmaps':"gluBuild3DMipmaps.3G.html",
	'gluBuild3DMipmapLevels':"gluBuild3DMipmapLevels.3G.html",
	'gluBuild2DMipmaps':"gluBuild2DMipmaps.3G.html",
	'gluBuild2DMipmapLevels':"gluBuild2DMipmapLevels.3G.html",
	'gluBuild1DMipmaps':"gluBuild1DMipmaps.3G.html",
	'gluBuild1DMipmapLevels':"gluBuild1DMipmapLevels.3G.html",
	'gluBeginTrim':"gluBeginTrim.3G.html",
	'gluBeginSurface':"gluBeginSurface.3G.html",
	'gluBeginPolygon':"gluBeginPolygon.3G.html",
	'gluBeginCurve':"gluBeginCurve.3G.html",
	'glTranslate':"glTranslate.3G.html",
	'glTexSubImage3D':"glTexSubImage3D.3G.html",
	'glTexSubImage2D':"glTexSubImage2D.3G.html",
	'glTexSubImage1D':"glTexSubImage1D.3G.html",
	'glTexParameter':"glTexParameter.3G.html",
	'glTexImage3D':"glTexImage3D.3G.html",
	'glTexImage2D':"glTexImage2D.3G.html",
	'glTexImage1D':"glTexImage1D.3G.html",
	'glTexGen':"glTexGen.3G.html",
	'glTexEnv':"glTexEnv.3G.html",
	'glTexCoordPointer':"glTexCoordPointer.3G.html",
	'glTexCoord':"glTexCoord.3G.html",
	'glStencilOp':"glStencilOp.3G.html",
	'glStencilMask':"glStencilMask.3G.html",
	'glStencilFunc':"glStencilFunc.3G.html",
	'glShadeModel':"glShadeModel.3G.html",
	'glSeparableFilter2D':"glSeparableFilter2D.3G.html",
	'glSelectBuffer':"glSelectBuffer.3G.html",
	'glScissor':"glScissor.3G.html",
	'glScale':"glScale.3G.html",
	'glRotate':"glRotate.3G.html",
	'glResetMinmax':"glResetMinmax.3G.html",
	'glResetHistogram':"glResetHistogram.3G.html",
	'glRenderMode':"glRenderMode.3G.html",
	'glRect':"glRect.3G.html",
	'glReadPixels':"glReadPixels.3G.html",
	'glReadBuffer':"glReadBuffer.3G.html",
	'glRasterPos':"glRasterPos.3G.html",
	'glPushName':"glPushName.3G.html",
	'glPushMatrix':"glPushMatrix.3G.html",
	'glPushClientAttrib':"glPushClientAttrib.3G.html",
	'glPushAttrib':"glPushAttrib.3G.html",
	'glPrioritizeTextures':"glPrioritizeTextures.3G.html",
	'glPolygonStipple':"glPolygonStipple.3G.html",
	'glPolygonOffset':"glPolygonOffset.3G.html",
	'glPolygonMode':"glPolygonMode.3G.html",
	'glPointSize':"glPointSize.3G.html",
	'glPixelZoom':"glPixelZoom.3G.html",
	'glPixelTransfer':"glPixelTransfer.3G.html",
	'glPixelStore':"glPixelStore.3G.html",
	'glPixelMap':"glPixelMap.3G.html",
	'glPassThrough':"glPassThrough.3G.html",
	'glOrtho':"glOrtho.3G.html",
	'glNormalPointer':"glNormalPointer.3G.html",
	'glNormal':"glNormal.3G.html",
	'glNewList':"glNewList.3G.html",
	'glMultMatrix':"glMultMatrix.3G.html",
	'glMultiTexCoordARB':"glMultiTexCoordARB.3G.html",
	'glMinmax':"glMinmax.3G.html",
	'glMatrixMode':"glMatrixMode.3G.html",
	'glMaterial':"glMaterial.3G.html",
	'glMapGrid':"glMapGrid.3G.html",
	'glMap2':"glMap2.3G.html",
	'glMap1':"glMap1.3G.html",
	'glLogicOp':"glLogicOp.3G.html",
	'glLoadName':"glLoadName.3G.html",
	'glLoadMatrix':"glLoadMatrix.3G.html",
	'glLoadIdentity':"glLoadIdentity.3G.html",
	'glListBase':"glListBase.3G.html",
	'glLineWidth':"glLineWidth.3G.html",
	'glLineStipple':"glLineStipple.3G.html",
	'glLightModel':"glLightModel.3G.html",
	'glLight':"glLight.3G.html",
	'glIsTexture':"glIsTexture.3G.html",
	'glIsList':"glIsList.3G.html",
	'glIsEnabled':"glIsEnabled.3G.html",
	'glInterleavedArrays':"glInterleavedArrays.3G.html",
	'glInitNames':"glInitNames.3G.html",
	'glIndexPointer':"glIndexPointer.3G.html",
	'glIndexMask':"glIndexMask.3G.html",
	'glIndex':"glIndex.3G.html",
	'glHistogram':"glHistogram.3G.html",
	'glHint':"glHint.3G.html",
	'glGetTexParameter':"glGetTexParameter.3G.html",
	'glGetTexLevelParameter':"glGetTexLevelParameter.3G.html",
	'glGetTexImage':"glGetTexImage.3G.html",
	'glGetTexGen':"glGetTexGen.3G.html",
	'glGetTexEnv':"glGetTexEnv.3G.html",
	'glGetString':"glGetString.3G.html",
	'glGetSeparableFilter':"glGetSeparableFilter.3G.html",
	'glGetPolygonStipple':"glGetPolygonStipple.3G.html",
	'glGetPointerv':"glGetPointerv.3G.html",
	'glGetPixelMap':"glGetPixelMap.3G.html",
	'glGetMinmaxParameter':"glGetMinmaxParameter.3G.html",
	'glGetMinmax':"glGetMinmax.3G.html",
	'glGetMaterial':"glGetMaterial.3G.html",
	'glGetMap':"glGetMap.3G.html",
	'glGetLight':"glGetLight.3G.html",
	'glGetHistogramParameter':"glGetHistogramParameter.3G.html",
	'glGetHistogram':"glGetHistogram.3G.html",
	'glGetError':"glGetError.3G.html",
	'glGetConvolutionParameter':"glGetConvolutionParameter.3G.html",
	'glGetConvolutionFilter':"glGetConvolutionFilter.3G.html",
	'glGetColorTableParameter':"glGetColorTableParameter.3G.html",
	'glGetColorTable':"glGetColorTable.3G.html",
	'glGetClipPlane':"glGetClipPlane.3G.html",
	'glGet':"glGet.3G.html",
	'glGenTextures':"glGenTextures.3G.html",
	'glGenLists':"glGenLists.3G.html",
	'glFrustum':"glFrustum.3G.html",
	'glFrontFace':"glFrontFace.3G.html",
	'glFog':"glFog.3G.html",
	'glFlush':"glFlush.3G.html",
	'glFinish':"glFinish.3G.html",
	'glFeedbackBuffer':"glFeedbackBuffer.3G.html",
	'glEvalPoint':"glEvalPoint.3G.html",
	'glEvalMesh':"glEvalMesh.3G.html",
	'glEvalCoord':"glEvalCoord.3G.html",
	'gleTwistExtrusion':"gleTwistExtrusion.3GLE.html",
	'gleToroid':"gleToroid.3GLE.html",
	'gleTextureMode':"gleTextureMode.3GLE.html",
	'gleSuperExtrusion':"gleSuperExtrusion.3GLE.html",
	'gleSpiral':"gleSpiral.3GLE.html",
	'gleSetNumSides':"gleSetNumSides.3GLE.html",
	'gleSetJoinStyle':"gleSetJoinStyle.3GLE.html",
	'gleScrew':"gleScrew.3GLE.html",
	'glePolyCylinder':"glePolyCylinder.3GLE.html",
	'glePolyCone':"glePolyCone.3GLE.html",
	'glEnableClientState':"glEnableClientState.3G.html",
	'glEnable':"glEnable.3G.html",
	'gleLathe':"gleLathe.3GLE.html",
	'gleHelicoid':"gleHelicoid.3GLE.html",
	'gleExtrusion':"gleExtrusion.3GLE.html",
	'glEdgeFlagPointer':"glEdgeFlagPointer.3G.html",
	'glEdgeFlag':"glEdgeFlag.3G.html",
	'gle':"gle.3GLE.html",
	'glDrawRangeElements':"glDrawRangeElements.3G.html",
	'glDrawPixels':"glDrawPixels.3G.html",
	'glDrawElements':"glDrawElements.3G.html",
	'glDrawBuffer':"glDrawBuffer.3G.html",
	'glDrawArrays':"glDrawArrays.3G.html",
	'glDepthRange':"glDepthRange.3G.html",
	'glDepthMask':"glDepthMask.3G.html",
	'glDepthFunc':"glDepthFunc.3G.html",
	'glDeleteTextures':"glDeleteTextures.3G.html",
	'glDeleteLists':"glDeleteLists.3G.html",
	'glCullFace':"glCullFace.3G.html",
	'glCopyTexSubImage3D':"glCopyTexSubImage3D.3G.html",
	'glCopyTexSubImage2D':"glCopyTexSubImage2D.3G.html",
	'glCopyTexSubImage1D':"glCopyTexSubImage1D.3G.html",
	'glCopyTexImage2D':"glCopyTexImage2D.3G.html",
	'glCopyTexImage1D':"glCopyTexImage1D.3G.html",
	'glCopyPixels':"glCopyPixels.3G.html",
	'glCopyConvolutionFilter2D':"glCopyConvolutionFilter2D.3G.html",
	'glCopyConvolutionFilter1D':"glCopyConvolutionFilter1D.3G.html",
	'glCopyColorTable':"glCopyColorTable.3G.html",
	'glCopyColorSubTable':"glCopyColorSubTable.3G.html",
	'glConvolutionParameter':"glConvolutionParameter.3G.html",
	'glConvolutionFilter2D':"glConvolutionFilter2D.3G.html",
	'glConvolutionFilter1D':"glConvolutionFilter1D.3G.html",
	'glColorTableParameter':"glColorTableParameter.3G.html",
	'glColorTable':"glColorTable.3G.html",
	'glColorSubTable':"glColorSubTable.3G.html",
	'glColorPointer':"glColorPointer.3G.html",
	'glColorMaterial':"glColorMaterial.3G.html",
	'glColorMask':"glColorMask.3G.html",
	'glColor':"glColor.3G.html",
	'glClipPlane':"glClipPlane.3G.html",
	'glClientActiveTextureARB':"glClientActiveTextureARB.3G.html",
	'glClearStencil':"glClearStencil.3G.html",
	'glClearIndex':"glClearIndex.3G.html",
	'glClearDepth':"glClearDepth.3G.html",
	'glClearColor':"glClearColor.3G.html",
	'glClearAccum':"glClearAccum.3G.html",
	'glClear':"glClear.3G.html",
	'glCallLists':"glCallLists.3G.html",
	'glCallList':"glCallList.3G.html",
	'glBlendFunc':"glBlendFunc.3G.html",
	'glBlendEquation':"glBlendEquation.3G.html",
	'glBlendColor':"glBlendColor.3G.html",
	'glBitmap':"glBitmap.3G.html",
	'glBindTexture':"glBindTexture.3G.html",
	'glBegin':"glBegin.3G.html",
	'glArrayElement':"glArrayElement.3G.html",
	'glAreTexturesResident':"glAreTexturesResident.3G.html",
	'glAlphaFunc':"glAlphaFunc.3G.html",
	'glActiveTextureARB':"glActiveTextureARB.3G.html",
	'glAccum':"glAccum.3G.html",
}


if __name__ == "__main__":
	print 'search gl'
	for name in dir(GL):
		if name[:2] == 'gl' and not findName( name):
			print '\t%s:"",'%( repr(name), )

	print 'search glu'
	for name in dir(GLU):
		if name[:2] == 'gl' and not findName( name):
			print '\t%s:"",'%( repr(name), )

	print 'search glut'
	for name in dir(GLUT):
		if name[:2] == 'gl' and not findName( name):
			print '\t%s:"",'%( repr(name), )

	print 'search gle'
	for name in dir(GLE):
		if name[:2] == 'gl' and not findName( name):
			print '\t%s:"",'%( repr(name), )
	