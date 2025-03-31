# Average

What values belong in state?  Ask yourself: _Can I calculate this value from other values stored in state?_  If the answer is "yes", then the value should be returned from a _getter_, if the answer is "no" then you should store it in state:

- [average](./average) stores the average of the list in state, this is not ideal!  The program's `self.average` state can go _stale_ if `self.numbers` is updated without recalculating `self.average`.  
- [average with getter](./average_with_getter) uses a _getter_ to calculate the average when you need it instead of storing the average in state.  This approach is more robust because your state can not go stale.  
