#ifndef MM_H
#define MM_H

#include "stdlib.h"

#define GC_THREADS
#include "gc.h"

void stm_init(void);
void *stm_malloc(size_t size);
void *stm_realloc(void* ptr, size_t size);

#endif
