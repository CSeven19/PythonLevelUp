cdef extern from "math.h":
    double cosf(double theta)
    double sinf(double theta)
    double acosf(double theta)
 
def great_circle(double lon1,double lat1,double lon2,double lat2):
    cdef double radius = 3956.0
    cdef double pi = 3.14159265
    cdef double x = pi/180.0
    cdef double a,b,theta,c
 
    a = (90.0-lat1)*(x)
    b = (90.0-lat2)*(x)
    theta = (lon2-lon1)*(x)
    c = acosf((cosf(a)*cosf(b)) + (sinf(a)*sinf(b)*cosf(theta)))
    return radius*c