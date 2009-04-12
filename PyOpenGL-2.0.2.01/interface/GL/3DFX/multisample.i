/*
# AUTOGENERATED DO NOT EDIT

# If you edit this file, delete the AUTOGENERATED line to prevent re-generation
# BUILD api_versions [0x001]
*/

%module multisample

#define __version__ "$Revision: 1.1.2.1 $"
#define __date__ "$Date: 2004/11/15 07:38:07 $"
#define __api_version__ API_VERSION
#define __author__ "PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>"
#define __doc__ ""

%{
/**
 *
 * GL.3DFX.multisample Module for PyOpenGL
 * 
 * Authors: PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>
 * 
***/
%}

%include util.inc
%include gl_exception_handler.inc

%{
#ifdef CGL_PLATFORM
# include <OpenGL/glext.h>
#else
# include <GL/glext.h>
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_3DFX_multisample)

#endif
%}

/* FUNCTION DECLARATIONS */


/* CONSTANT DECLARATIONS */
#define            GL_MULTISAMPLE_3DFX 0x86B2
#define         GL_SAMPLE_BUFFERS_3DFX 0x86B3
#define                GL_SAMPLES_3DFX 0x86B4
#define        GL_MULTISAMPLE_BIT_3DFX 0x20000000


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_3DFX_multisample)

#endif
	NULL
};

#define glInitMultisample3DFX() InitExtension("GL_3DFX_multisample", proc_names)
%}

int glInitMultisample3DFX();
DOC(glInitMultisample3DFX, "glInitMultisample3DFX() -> bool")

%{
PyObject *__info()
{
	if (glInitMultisample3DFX())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();
