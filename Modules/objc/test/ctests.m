/*
 * This file contains some unittests for specific functions in the extension 
 * module. 
 *
 * The PyObjC unittest objc.test.test_ctests executes the tests in this file.
 */
#include "pyobjc-api.h"
#include "pyobjc-unittest.h"

#include <fcntl.h>

#import <Foundation/Foundation.h>

struct Struct1 {
	int f1;
	double f2;
};

struct Struct2 {
	int f1;
	double f2;
	short s[5];
};

struct Struct3 {
	char ch;
	int  i;
};

struct Struct4 {
	char ch;
	long long i;
};

struct Struct5 {
	long i;
	char ch;
};

typedef struct Struct5 Struct5Array[2];



/* Helper stuff for TestNSInvoke */

static struct Struct2 invokeHelper = { 0, 0, { 0, 0, 0, 0, 0 } };

@interface PyObjCTest_NSInvoke : NSObject
{
}
-(void)methodWithMyStruct: (struct Struct2)val1 andShort:(short)val2;


@end

@implementation PyObjCTest_NSInvoke 
-(void)methodWithMyStruct: (struct Struct2)val1 andShort:(short)val2
{
	(void)val2;
	invokeHelper = val1;
}
@end

#ifndef GNU_RUNTIME


BEGIN_UNITTEST(CheckNSInvoke)
	/* This is not a 'real' unittest, but is used to disable a number of
	 * other tests (in objc.test.test_methods2) when NSInvocation isn't
	 * working correctly (MacOS X at least upto 10.2.6).
	 * [Panther previews also have this problem]
	 *
	 * GNUstep is even worse, this test causes a crash of the interpreter,
	 */
	PyObjCTest_NSInvoke* obj = [[PyObjCTest_NSInvoke alloc] init];
	NSInvocation* inv;
	struct Struct2 v1 = { 1, 2, { 3, 4, 5, 6, 7 } };
	short    v2 = 8;

	[obj methodWithMyStruct: v1 andShort: v2];
	inv = [NSInvocation invocationWithMethodSignature:
		[obj methodSignatureForSelector:@selector(methodWithMyStruct:andShort:)]];
	[inv setTarget: obj];
	[inv setSelector: @selector(methodWithMyStruct:andShort:)];
	[inv setArgument: &v1 atIndex: 2];
	[inv setArgument: &v2 atIndex: 3];

	[inv invoke];
	ASSERT_EQUALS(invokeHelper.f1, v1.f1, "%d");
	ASSERT_EQUALS(invokeHelper.f2, v1.f2, "%g");
	ASSERT_EQUALS(invokeHelper.s[0], v1.s[0], "%d");
	ASSERT_EQUALS(invokeHelper.s[1], v1.s[1], "%d");
	ASSERT_EQUALS(invokeHelper.s[2], v1.s[2], "%d");
	ASSERT_EQUALS(invokeHelper.s[3], v1.s[3], "%d");
	ASSERT_EQUALS(invokeHelper.s[4], v1.s[4], "%d");

END_UNITTEST

#else

BEGIN_UNITTEST(CheckNSInvoke)
	/* Force failure, see comment above */
	ASSERT_EQUALS(0, 1, "%d");
END_UNITTEST

#endif


BEGIN_UNITTEST(StructSize)

	ASSERT_EQUALS(
	    sizeof(struct Struct1), PyObjCRT_SizeOfType(@encode(struct Struct1)),
	    "%d");

	ASSERT_EQUALS(
	    sizeof(struct Struct2), PyObjCRT_SizeOfType(@encode(struct Struct2)),
	    "%d");

	ASSERT_EQUALS(
	    sizeof(struct Struct3), PyObjCRT_SizeOfType(@encode(struct Struct3)),
	    "%d");

	ASSERT_EQUALS(
	    sizeof(struct Struct4), PyObjCRT_SizeOfType(@encode(struct Struct4)),
	    "%d");

END_UNITTEST

BEGIN_UNITTEST(StructAlign)

	ASSERT_EQUALS(
	    __alignof__(struct Struct1), 
	    PyObjCRT_AlignOfType(@encode(struct Struct1)),
	    "%d");

	ASSERT_EQUALS(
	    __alignof__(struct Struct2), 
	    PyObjCRT_AlignOfType(@encode(struct Struct2)),
	    "%d");

	ASSERT_EQUALS(
	    __alignof__(struct Struct3), 
	    PyObjCRT_AlignOfType(@encode(struct Struct3)),
	    "%d");

	ASSERT_EQUALS(
	    __alignof__(struct Struct4), 
	    PyObjCRT_AlignOfType(@encode(struct Struct4)),
	    "%d");

END_UNITTEST


BEGIN_UNITTEST(FillStruct1)

	PyObject* input;
	struct Struct1 output;
	int r;

	input = PyTuple_New(2);
	FAIL_IF(input == NULL);

	PyTuple_SET_ITEM(input, 0, PyInt_FromLong(1));
	PyTuple_SET_ITEM(input, 1, PyFloat_FromDouble(2));
	
	r = PyObjC_PythonToObjC(@encode(struct Struct1), input, &output);
	FAIL_IF(r < 0);

	Py_DECREF(input);

	ASSERT_EQUALS(output.f1, 1, "%d");
	ASSERT_EQUALS(output.f2, 2.0, "%g");

END_UNITTEST

BEGIN_UNITTEST(FillStruct2)

	PyObject* input;
	PyObject* v;
	struct Struct2 output;
	int r;

	input = PyTuple_New(3);
	FAIL_IF(input == NULL);

	v = PyTuple_New(5);
	PyTuple_SET_ITEM(v, 0, PyInt_FromLong(10));
	PyTuple_SET_ITEM(v, 1, PyInt_FromLong(11));
	PyTuple_SET_ITEM(v, 2, PyInt_FromLong(12));
	PyTuple_SET_ITEM(v, 3, PyInt_FromLong(13));
	PyTuple_SET_ITEM(v, 4, PyInt_FromLong(14));

	PyTuple_SET_ITEM(input, 0, PyInt_FromLong(1));
	PyTuple_SET_ITEM(input, 1, PyFloat_FromDouble(2));
	PyTuple_SET_ITEM(input, 2, v);
	
	r = PyObjC_PythonToObjC(@encode(struct Struct2), input, &output);
	FAIL_IF(r < 0);

	Py_DECREF(input);

	ASSERT_EQUALS(output.f1, 1,    "%d");
	ASSERT_EQUALS(output.f2, 2.0,  "%g");
	ASSERT_EQUALS(output.s[0], 10, "%d");
	ASSERT_EQUALS(output.s[1], 11, "%d");
	ASSERT_EQUALS(output.s[2], 12, "%d");
	ASSERT_EQUALS(output.s[3], 13, "%d");
	ASSERT_EQUALS(output.s[4], 14, "%d");

END_UNITTEST

BEGIN_UNITTEST(FillStruct3)

	PyObject* input;
	struct Struct3 output;
	int r;

	input = PyTuple_New(2);
	FAIL_IF(input == NULL);

	PyTuple_SET_ITEM(input, 0,  PyString_FromStringAndSize("\001", 1));
	PyTuple_SET_ITEM(input, 1, PyInt_FromLong(2));
	
	r = PyObjC_PythonToObjC(@encode(struct Struct3), input, &output);
	FAIL_IF(r < 0);

	Py_DECREF(input);

	ASSERT_EQUALS(output.ch, '\001',    "%d");
	ASSERT_EQUALS(output.i, 2,  "%d");

END_UNITTEST

BEGIN_UNITTEST(FillStruct4)

	PyObject* input;
	struct Struct4 output;
	int r;

	input = PyTuple_New(2);
	FAIL_IF(input == NULL);

	PyTuple_SET_ITEM(input, 0,  PyString_FromStringAndSize("\001", 1));
	PyTuple_SET_ITEM(input, 1, PyInt_FromLong(500000));
	
	r = PyObjC_PythonToObjC(@encode(struct Struct4), input, &output);
	FAIL_IF(r < 0);

	Py_DECREF(input);

	ASSERT_EQUALS(output.ch, '\001',    "%d");
	ASSERT_EQUALS(output.i, 500000,  "%ll");

END_UNITTEST

BEGIN_UNITTEST(FillStruct5Array)

	PyObject* input;
	PyObject* v;
	Struct5Array output;
	int r;

	input = PyTuple_New(2);
	FAIL_IF(input == NULL);

	v = PyTuple_New(2);
	PyTuple_SET_ITEM(v, 0, PyInt_FromLong(500000));
	PyTuple_SET_ITEM(v, 1,  PyString_FromStringAndSize("\001", 1));
	PyTuple_SET_ITEM(input, 0, v);

	v = PyTuple_New(2);
	PyTuple_SET_ITEM(v, 0, PyInt_FromLong(1000000));
	PyTuple_SET_ITEM(v, 1,  PyString_FromStringAndSize("\002", 1));
	PyTuple_SET_ITEM(input, 1, v);
	
	r = PyObjC_PythonToObjC(@encode(Struct5Array), input, &output);
	FAIL_IF(r < 0);

	Py_DECREF(input);

	ASSERT_EQUALS(output[0].ch, '\001',    "%d");
	ASSERT_EQUALS(output[0].i, 500000,  "%ll");
	ASSERT_EQUALS(output[1].ch, '\002',    "%d");
	ASSERT_EQUALS(output[1].i, 1000000,  "%ll");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct1) 

	struct Struct1 input;
	PyObject* output;

	input.f1 = 1;
	input.f2 = 2;

	output = PyObjC_ObjCToPython(@encode(struct Struct1), &input);
	FAIL_IF(output == NULL);

	ASSERT_ISINSTANCE(output, Tuple);	
	ASSERT_EQUALS(PyTuple_GET_SIZE(output), 2, "%d");
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 0), Int);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 1), Float);
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(output, 0)), 1, "%d");
	ASSERT_EQUALS(PyFloat_AsDouble(PyTuple_GET_ITEM(output, 1)), 2.0, "%g");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct2) 

	struct Struct2 input;
	PyObject* output;
	PyObject* tup;
	PyObject* v;

	input.f1 = 1;
	input.f2 = 2;
	input.s[0] = 3;
	input.s[1] = 4;
	input.s[2] = 5;
	input.s[3] = 6;
	input.s[4] = 7;

	output = PyObjC_ObjCToPython(@encode(struct Struct2), &input);
	FAIL_IF(output == NULL);

	ASSERT_ISINSTANCE(output, Tuple);	
	ASSERT_EQUALS(PyTuple_GET_SIZE(output), 3, "%d");
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 0), Int);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 1), Float);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 2), Tuple);
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(output, 0)), 1, "%d");
	ASSERT_EQUALS(PyFloat_AsDouble(PyTuple_GET_ITEM(output, 1)), 2.0, "%g");

	tup = PyTuple_GET_ITEM(output, 2);
	ASSERT_EQUALS(PyTuple_GET_SIZE(tup), 5, "%d");

	v = PyTuple_GET_ITEM(tup, 0);
	ASSERT_ISINSTANCE(v, Int);
	ASSERT_EQUALS(PyInt_AsLong(v), 3, "%d");

	v = PyTuple_GET_ITEM(tup, 1);
	ASSERT_ISINSTANCE(v, Int);
	ASSERT_EQUALS(PyInt_AsLong(v), 4, "%d");

	v = PyTuple_GET_ITEM(tup, 2);
	ASSERT_ISINSTANCE(v, Int);
	ASSERT_EQUALS(PyInt_AsLong(v), 5, "%d");

	v = PyTuple_GET_ITEM(tup, 3);
	ASSERT_ISINSTANCE(v, Int);
	ASSERT_EQUALS(PyInt_AsLong(v), 6, "%d");

	v = PyTuple_GET_ITEM(tup, 4);
	ASSERT_ISINSTANCE(v, Int);
	ASSERT_EQUALS(PyInt_AsLong(v), 7, "%d");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct3) 

	struct Struct3 input;
	PyObject* output;

	input.ch = 1;
	input.i = 2;

	output = PyObjC_ObjCToPython(@encode(struct Struct3), &input);
	FAIL_IF(output == NULL);

	ASSERT_ISINSTANCE(output, Tuple);	
	ASSERT_EQUALS(PyTuple_GET_SIZE(output), 2, "%d");
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 0), Int);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 1), Int);
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(output, 0)), 1, "%d");
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(output, 1)), 2, "%d");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct4) 

	struct Struct4 input;
	PyObject* output;

	input.ch = 1;
	input.i = 500000;

	output = PyObjC_ObjCToPython(@encode(struct Struct4), &input);
	FAIL_IF(output == NULL);

	ASSERT_ISINSTANCE(output, Tuple);	
	ASSERT_EQUALS(PyTuple_GET_SIZE(output), 2, "%d");
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 0), Int);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(output, 1), Long);
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(output, 0)), 1, "%d");
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(output, 1)), 500000, "%d");

END_UNITTEST

BEGIN_UNITTEST(ExtractStruct5Array) 

	Struct5Array input;
	PyObject* output;
	PyObject* v;

	input[0].ch = 1;
	input[0].i = 500000;
	input[1].ch = 2;
	input[1].i = 1000000;

	output = PyObjC_ObjCToPython(@encode(Struct5Array), &input);
	FAIL_IF(output == NULL);

	ASSERT_ISINSTANCE(output, Tuple);	
	ASSERT_EQUALS(PyTuple_GET_SIZE(output), 2, "%d");

	v = PyTuple_GET_ITEM(output, 0);
	ASSERT_ISINSTANCE(v, Tuple);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(v, 0), Int);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(v, 1), Int);
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(v, 0)), 500000, "%d");
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(v, 1)), 1, "%d");

	v = PyTuple_GET_ITEM(output, 1);
	ASSERT_ISINSTANCE(v, Tuple);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(v, 0), Int);
	ASSERT_ISINSTANCE(PyTuple_GET_ITEM(v, 1), Int);
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(v, 0)), 1000000, "%d");
	ASSERT_EQUALS(PyInt_AsLong(PyTuple_GET_ITEM(v, 1)), 2, "%d");

END_UNITTEST

#ifdef _C_BOOL

BEGIN_UNITTEST(TestSizeOfBool)

	/* Code in libffi_support.m depends on this equality. */
	ASSERT_EQUALS(sizeof(bool), sizeof(int), "%d");

END_UNITTEST

#endif

BEGIN_UNITTEST(TestTypeCode)
	
	/* These are manually defined on some platforms */
	ASSERT_EQUALS(@encode(long long)[0], 'q', "%c");
	ASSERT_EQUALS(@encode(unsigned long long)[0], 'Q', "%c");

#if defined(MACOSX) &&  MAC_OS_X_VERSION_MAX_ALLOWED > MAC_OS_X_VERSION_10_1
	ASSERT_EQUALS(@encode(bool)[0], 'B', "%#x");
#endif

END_UNITTEST

BEGIN_UNITTEST(TestSimplifySignature)
	/* Make sure PyObjCRT_SimplifySignature works */
	char b[1024];
	int  r;

	r = PyObjCRT_SimplifySignature("@1234@0:{_NSPoint=ff}02i22", b, sizeof(b));
	ASSERT(r != -1);
	ASSERT_STREQUALS("@@:{_NSPoint=ff}i", b);

	r = PyObjCRT_SimplifySignature("@@:{_NSPoint=ff}i", b, sizeof(b));
	ASSERT(r != -1);
	ASSERT_STREQUALS("@@:{_NSPoint=ff}i", b);
END_UNITTEST

BEGIN_UNITTEST(TestArrayCoding)
	/*
  	 * According to the docs on Panther, valueForKey: on an array should
	 * return [ o.valueForKey_(key) for o in anArray ]. 
	 * On MacOS X 10.2 it doesn't.
	 *
         * This test was added to make sure PyObjC is not at fault :-), the
	 * test is also used to avoid giving false positives in the unittests
 	 * for key-value coding.
         */

	NSMutableDictionary* d;
	NSMutableArray* a;
	NSObject* v;
	int haveException;

	NSAutoreleasePool* p;

	p = [[NSAutoreleasePool alloc] init];

	d = [NSMutableDictionary dictionary];

	[d setObject:@"foo" forKey:@"keyM"];

	a = [NSMutableArray arrayWithObjects: d, nil];

	NS_DURING
		v = [a valueForKey:@"keyM"];	
		haveException = 0;
	NS_HANDLER
		v = nil;
		haveException = 1;
	NS_ENDHANDLER

	[p release];

	ASSERT(!haveException);
END_UNITTEST


BEGIN_UNITTEST(PythonListAsNSArray)
	PyObject* aList;
	NSMutableArray* array;
	NSArray* array2;
	
	aList = Py_BuildValue("[iiiii]", 0, 1, 2, 3, 4);
	FAIL_IF(aList == NULL);

	array = PyObjC_PythonToId(aList);
	FAIL_IF(array == nil);

	/* Check lenght */
	ASSERT_EQUALS(5, [array count], "%d");	

	/* Check basic element access */
	ASSERT([[NSNumber numberWithInt:0] isEqual:[array objectAtIndex:0]]);
	ASSERT([[NSNumber numberWithInt:1] isEqual:[array objectAtIndex:1]]);
	ASSERT([[NSNumber numberWithInt:2] isEqual:[array objectAtIndex:2]]);
	ASSERT([[NSNumber numberWithInt:3] isEqual:[array objectAtIndex:3]]);
	ASSERT([[NSNumber numberWithInt:4] isEqual:[array objectAtIndex:4]]);

	/* Check some other methods */
	array2 = [array arrayByAddingObject: [NSNumber numberWithInt:5]];
	FAIL_IF(array2 == nil);

	ASSERT_EQUALS(6, [array2 count], "%d");
	ASSERT_EQUALS(5, [array count], "%d");

	ASSERT([[NSNumber numberWithInt:0] isEqual:[array2 objectAtIndex:0]]);
	ASSERT([[NSNumber numberWithInt:1] isEqual:[array2 objectAtIndex:1]]);
	ASSERT([[NSNumber numberWithInt:2] isEqual:[array2 objectAtIndex:2]]);
	ASSERT([[NSNumber numberWithInt:3] isEqual:[array2 objectAtIndex:3]]);
	ASSERT([[NSNumber numberWithInt:4] isEqual:[array2 objectAtIndex:4]]);
	ASSERT([[NSNumber numberWithInt:5] isEqual:[array2 objectAtIndex:5]]);

	ASSERT([array containsObject:[NSNumber numberWithInt:4]]);
	ASSERT(![array containsObject:[NSNumber numberWithInt:10]]);

	/* Mutating methods */
	[array addObject: [NSNumber numberWithInt:5]];
	ASSERT_EQUALS(6, [array count], "%d");
	ASSERT([[NSNumber numberWithInt:5] isEqual:[array objectAtIndex:5]]);

	[array removeLastObject];
	ASSERT_EQUALS(5, [array count], "%d");
	ASSERT([[NSNumber numberWithInt:0] isEqual:[array objectAtIndex:0]]);
	ASSERT([[NSNumber numberWithInt:4] isEqual:[array objectAtIndex:4]]);

	[array insertObject: [NSNumber numberWithInt:6] atIndex: 1];
	ASSERT_EQUALS(6, [array count], "%d");
	ASSERT([[NSNumber numberWithInt:6] isEqual:[array objectAtIndex:1]]);

	[array removeObjectAtIndex: 1];
	ASSERT_EQUALS(5, [array count], "%d");
	ASSERT([[NSNumber numberWithInt:1] isEqual:[array objectAtIndex:1]]);

	[array replaceObjectAtIndex: 1 withObject: [NSNumber numberWithInt:7]];
	ASSERT_EQUALS(5, [array count], "%d");
	ASSERT([[NSNumber numberWithInt:7] isEqual:[array objectAtIndex:1]]);

END_UNITTEST

BEGIN_UNITTEST(PythonTupleAsNSArray)
	PyObject* aTuple;
	NSArray* array;
	NSArray* array2;

	aTuple = Py_BuildValue("(iiiii)", 0, 1, 2, 3, 4);
	FAIL_IF(aTuple == NULL);

	array = PyObjC_PythonToId(aTuple);
	FAIL_IF(array == nil);

	/* Check lenght */
	ASSERT_EQUALS(5, [array count], "%d");	

	/* Check basic element access */
	ASSERT([[NSNumber numberWithInt:0] isEqual:[array objectAtIndex:0]]);
	ASSERT([[NSNumber numberWithInt:1] isEqual:[array objectAtIndex:1]]);
	ASSERT([[NSNumber numberWithInt:2] isEqual:[array objectAtIndex:2]]);
	ASSERT([[NSNumber numberWithInt:3] isEqual:[array objectAtIndex:3]]);
	ASSERT([[NSNumber numberWithInt:4] isEqual:[array objectAtIndex:4]]);

	/* Check some other methods */
	array2 = [array arrayByAddingObject: [NSNumber numberWithInt:5]];
	ASSERT(array2 != nil);

	ASSERT_EQUALS(6, [array2 count], "%d");
	ASSERT_EQUALS(5, [array count], "%d");

	ASSERT([[NSNumber numberWithInt:0] isEqual:[array2 objectAtIndex:0]]);
	ASSERT([[NSNumber numberWithInt:1] isEqual:[array2 objectAtIndex:1]]);
	ASSERT([[NSNumber numberWithInt:2] isEqual:[array2 objectAtIndex:2]]);
	ASSERT([[NSNumber numberWithInt:3] isEqual:[array2 objectAtIndex:3]]);
	ASSERT([[NSNumber numberWithInt:4] isEqual:[array2 objectAtIndex:4]]);
	ASSERT([[NSNumber numberWithInt:5] isEqual:[array2 objectAtIndex:5]]);

	ASSERT([array containsObject:[NSNumber numberWithInt:4]]);
	ASSERT(![array containsObject:[NSNumber numberWithInt:10]]);

END_UNITTEST

BEGIN_UNITTEST(PythonDictAsNSDictionary)
	// count, objectForKey:, keyEnumerator
	// setObject:forKey: removeObjectForKey:
	PyObject* aDictionary;
	NSMutableDictionary* dict;
	NSEnumerator* iter;
	NSArray* keys;

	aDictionary = Py_BuildValue(
		"{iiiiiiii}",
		1, 2, 
		2, 4, 
		3, 6,
		4, 8
	);
	FAIL_IF(aDictionary == NULL);

	dict = PyObjC_PythonToId(aDictionary);
	FAIL_IF(dict == nil);

	ASSERT_EQUALS(4, [dict count], "%d");
	ASSERT([
		[dict objectForKey:[NSNumber numberWithInt:1]] 
			isEqual: [NSNumber numberWithInt: 2]]);

	[dict setObject: [NSNumber numberWithInt:10]
	      forKey: [NSNumber numberWithInt:5]];
	ASSERT_EQUALS(5, [dict count], "%d");
	ASSERT([
		[dict objectForKey:[NSNumber numberWithInt:5]] 
			isEqual: [NSNumber numberWithInt: 10]]);

	[dict removeObjectForKey: [NSNumber numberWithInt:5]];
	ASSERT_EQUALS(4, [dict count], "%d");

	iter = [dict keyEnumerator];
	ASSERT(iter != nil);

	keys = [iter allObjects];
	ASSERT_EQUALS(4, [keys count], "%d");
	ASSERT([[keys objectAtIndex:0] isEqual:[NSNumber numberWithInt:1]]);
	ASSERT([[keys objectAtIndex:1] isEqual:[NSNumber numberWithInt:2]]);
	ASSERT([[keys objectAtIndex:2] isEqual:[NSNumber numberWithInt:3]]);
	ASSERT([[keys objectAtIndex:3] isEqual:[NSNumber numberWithInt:4]]);

END_UNITTEST

BEGIN_UNITTEST(NSLogging)
	/* This is a pretty lame test ...
	 *
	 * What this does is tests that the proxies of plain Python objects
	 * can be logged. This used to be impossible upto (and including)
	 * release 1.1!
	 */
	PyObject* o = (PyObject*)(Py_BuildValue("i", 10)->ob_type);
	NSObject* value;
	int fd;
	int stderr_orig;
	int r;

	value = PyObjC_PythonToId(o);
	FAIL_IF(value == nil);

	fd = open("/dev/null", O_WRONLY);
	ASSERT((fd != -1));
	stderr_orig = dup(2);
	ASSERT(stderr_orig != -1);
	r = dup2(fd, 2);
	ASSERT(r != -1);
	NSLog(@"%@", value);
	r = dup2(stderr_orig, 2);
	ASSERT(r != -1);
	r = close(fd);
	ASSERT(r != -1);
END_UNITTEST

static PyMethodDef unittest_methods[] = {
	TESTDEF(CheckNSInvoke),

	TESTDEF(StructSize),
	TESTDEF(StructAlign),
	TESTDEF(FillStruct1),
	TESTDEF(FillStruct2),
	TESTDEF(FillStruct3),
	TESTDEF(FillStruct4),
	TESTDEF(FillStruct5Array),
	TESTDEF(ExtractStruct1),
	TESTDEF(ExtractStruct2),
	TESTDEF(ExtractStruct3),
	TESTDEF(ExtractStruct4),
	TESTDEF(ExtractStruct5Array),
#ifdef _C_BOOL
	TESTDEF(TestSizeOfBool),	
#endif
	TESTDEF(TestTypeCode),	
	TESTDEF(TestSimplifySignature),	
	TESTDEF(TestArrayCoding),
	TESTDEF(PythonListAsNSArray),
	TESTDEF(PythonTupleAsNSArray),
	TESTDEF(PythonDictAsNSDictionary),
	TESTDEF(NSLogging),
	{ 0, 0, 0, 0 }
};

void initctests(void);
void initctests(void)
{
	PyObject* m;

	m = Py_InitModule4("ctests", unittest_methods, NULL,
			                        NULL, PYTHON_API_VERSION);


	PyObjC_ImportAPI(m);
}