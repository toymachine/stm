- new group of persistent objects (in the clojure sense),  dict, list/tuple, long, unicode, array
- classes/object might be later
- persistent equivalents of python objects
- runs own eval loop (peval.c)
- runs (subset of) existing python op-codes (@see dis module)
- runs without GIL in peval.c
- persistent objects live in 'world'
- world is seperate section in shared memory (mmap)
- world can be updated from multiple threads or multiple processes
- world has own garbage collection
- world has own memory management
- world stores pointers as offset from 0, allowing backing by file (world database!)
- world presents itself as a dict to out of world code
- only code of methods on persistent objects can be run in transaction
- during transaction, persistent objects are transient, allowing destructive updates using normal python style code
- at end of txn, objects are frozen in world
- persistent object code is frozen at class declaration time
- persistent objects can only be created during a transaction
- out of world code can always get a (consistent) read-only view of the world
- during a transaction, persistent objects are allocated on the stack = fast
- exceptions/traceback?
- worlds can also be used to provide php like shared nothing?
- universe of worlds (talking to worlds on other machine?)
- multiworld transactions
- agent world

from stm import world, persistent

class Member(persistent)
      def __init__(self, a, b):
          self.a, self.b = a, b

      def sum(self):

          return a + b

      def update_a(self, new_a):
          self.a = new_a  #would throw error if run outside transaction


      @transaction
      def mytrans(cls, world, init_a, init_b):

          piet = cls(init_a, init_b)
          piet.aap = {} # {} is persistent_dict when run in txn
          piet.update_a(20)

          world.piet = piet

#now member code is frozen and cannot be updated

w = world() #
w.run(Member.mytrans, 10, 20)
