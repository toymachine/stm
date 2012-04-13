cdef extern from "mm.h":
     void stm_init()
     void* stm_malloc(size_t size)
     void* stm_realloc(void* ptr, size_t size)

cdef class Persistent:
     cdef blaat(self):
          pass

cdef class PersistentVector(Persistent):
     cdef int shift
     cdef int cnt
     cdef Persistent root #array!
     cdef int root_length
     cdef Persistent tail #array!
     cdef int tail_length

     cdef cons(self, Persistent val):
          if self.tail_length < 32:
             pass

def init():
    stm_init()
    print "stm initted"

def test():
    while True:
        stm_malloc(sizeof(PersistentVector))

init()
