#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - print basic info about Lists in python
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
    int size;
    int alloc;
    int i;

    size = Py_SIZE(p);
    alloc = ((PyListObject *)p)->allocated;
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    for (i = 0; i < size; i++)
    {
        printf("Element %d: ", i);
        printf("%s\n", ((PyList_GetItem(p, i))->ob_type)->tp_name);
    }
}