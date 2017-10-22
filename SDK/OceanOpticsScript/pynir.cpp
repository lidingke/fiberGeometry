#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include "Python.h"

//#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <numpy/arrayobject.h>

#include "NIR_DLL.h"
#pragma comment(lib,"NIR_DLL.lib")

static PyObject * get_spectrum(PyObject *self, PyObject *args)
{
	int flag, number, limit;
	double *wavelengths = NULL;
	double *spectrum = NULL;
	double dintergralTimesms = 0.0;
	int iintergralTimesus = 0;
	int stride = sizeof(double);
	if (!PyArg_ParseTuple(args, "d", &dintergralTimesms))
	{
		PyErr_Format(PyExc_ValueError, "input args error");
		//Py_DECREF(out);
		return NULL;
	}
	iintergralTimesus = (int)dintergralTimesms;

	if (!openSpectrometers())
	{
		PyErr_Format(PyExc_ValueError, "openSpectrometers fail");
		return NULL;
	}
	setIntegrationTime(iintergralTimesus); // interger times 500ms
	setStrobe(true); // open led
	flag = getSpectrum(&wavelengths, &spectrum, &number);
	//printf("number len: %d\n", number);
	/*if (flag)
	{
		for (int i = 0; i < number; i++)
		{
			printf("Wavelength: %1.2f      Spectrum: %f \n", wavelengths[i], spectrum[i]);
		}
	}*/
	//system("pause");
	if (!flag)
	{
		PyErr_Format(PyExc_ValueError, "getSpectrum fail");
		//Py_DECREF(out);
		return NULL;
	}

	closeSpectrometers();
	
	//npy_int limit = (npy_int) number;
	//number = 512;
	npy_intp dims[] = { 2, number };
	//PyArrayObject * out = (PyArrayObject*)
	//	PyArray_NewFromDescr(&PyArray_Type,
	//		PyArray_DescrFromType(NPY_DOUBLE),
	//		1, dims, &stride, NULL, NPY_ARRAY_F_CONTIGUOUS, NULL);
	double* outArray;
	limit = number * 2;
	outArray = (double*)malloc(sizeof(double)*limit);
	//printf("%d,%d,%d,%d\n",limit, number, stride, sizeof(double)*limit);
	memcpy(outArray, wavelengths,  stride*number);
	memcpy(outArray + number, spectrum, stride*number);
	//delete(wavelengths);
	//delete(spectrum);
	//printf("%d,%d,%d\n", sizeof(&outArray), sizeof(&wavelengths), sizeof(&spectrum));
//	for (int i = 0; i<number; i++)
//	{
//		outArray[i+ number] = spectrum[i];
//	}

	PyArrayObject * out = (PyArrayObject*)
		PyArray_SimpleNewFromData(2, dims, NPY_DOUBLE, outArray);

	return PyArray_Return(out);
	//	return NULL;

}

static PyObject * test_get_darray(PyObject *self, PyObject *args)
{
	double dintergralTimesms = 0.0;
	int iintergralTimesus = 0;
	int stride = sizeof(double);
	//printf("Wavelength:");
	/*if (!PyArg_ParseTuple(args, "d", &dintergralTimesms))
		return NULL;
	iintergralTimesus = (int)dintergralTimesms;*/
	npy_int limit = 1000;
	npy_intp dims[] = { 2,500 };
	npy_double l1[3] = { 1.0,2.0,3.0 };
	npy_double l2[3] = { 10.0,20.0,30.0 };
	double* outArray;
	outArray = (double*)malloc(sizeof(double)*limit);
	for (int i = 0; i<limit; i++)
	{
		outArray[i] = i;
	}
	//PyObject* PyArray_NewFromDescr(PyTypeObject* subtype, PyArray_Descr* descr,
	//int nd, npy_intp* dims, npy_intp* strides, void* data, int flags, PyObject* obj)
	//PyArrayObject * out = (PyArrayObject*)
	//	PyArray_NewFromDescr(&PyArray_Type,
	//		PyArray_DescrFromType(NPY_DOUBLE),
	//		1, dims, &stride, l1, NPY_ARRAY_C_CONTIGUOUS, NULL);
	int number = 6;

	//outArray = (double*)malloc(sizeof(double)*number);
	//memcpy(outArray, l1, stride * number);
	//memcpy(outArray + stride * number, l2 , stride * number);
	PyArrayObject * out = (PyArrayObject*)
		PyArray_SimpleNewFromData(2,dims, NPY_DOUBLE, outArray);
	return PyArray_Return(out);
	//return NULL;

}

static PyMethodDef MindMethods[] =
{
	{ "get_spectrum", get_spectrum, METH_VARARGS, "get Spectrum" },
	{ "get_darrat", test_get_darray, METH_VARARGS, "get_darrat" },
	{ NULL, NULL, 0, NULL }

};

PyMODINIT_FUNC
initpynir(void)
{
	(void)Py_InitModule("pynir", MindMethods);
	import_array();
}

