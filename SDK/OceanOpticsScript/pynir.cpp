#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include "Python.h"
#include <numpy/arrayobject.h>
#include "NIR_DLL.h"
#pragma comment(lib,"NIR_DLL.lib")

static PyObject * get_spectrum(PyObject *self, PyObject *args)
{
	int flag, number, limit;
	double *wavelengths = NULL;
	double *spectrum = NULL;
	int intergralTimesus = 0;
	int boxcarWidth = 0;
	int scansToAverage = 0;
	int stride = sizeof(double);
	if (!PyArg_ParseTuple(args, "iii", &intergralTimesus,&scansToAverage,&boxcarWidth))
	{
		PyErr_Format(PyExc_ValueError, "input args error");
		return NULL;
	}


	if (!openSpectrometers())
	{
		PyErr_Format(PyExc_ValueError, "openSpectrometers fail");
		return NULL;
	}
	setIntegrationTime(intergralTimesus); // interger times 
	setScansToAverage(scansToAverage);
	setBoxcarWidth(boxcarWidth);
	setStrobe(true); // open led
	flag = getSpectrum(&wavelengths, &spectrum, &number);

	if (!flag)
	{
		PyErr_Format(PyExc_ValueError, "getSpectrum fail");
		return NULL;
	}

	closeSpectrometers();
	

	npy_intp dims[] = { 2, number };

	double* outArray;
	limit = number * 2;
	outArray = (double*)malloc(sizeof(double)*limit);
	memcpy(outArray, wavelengths,  stride*number);
	memcpy(outArray + number, spectrum, stride*number);

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

	int number = 6;

	PyArrayObject * out = (PyArrayObject*)
		PyArray_SimpleNewFromData(2,dims, NPY_DOUBLE, outArray);
	return PyArray_Return(out);


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

