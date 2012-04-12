cdef class BlaatAap2:
     cdef int shift
     cdef int cnt
     cdef object bla

     cdef sum(self):
         return 10 + 20

def test():
    print sizeof(BlaatAap2)