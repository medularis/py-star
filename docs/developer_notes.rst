Developer notes
===============


Manager
-------


"Sentinel" idea
^^^^^^^^^^^^^^^

We took it from *Python Cookbook, 3rd edition - 12.3. Communicating Between Threads*.
Previously it was just a plain ``None``, which isn't a very good idea since it
can be confused with something else and is not explicit.
However, we didnt' follow the recommendation of putting the sentinel value
in the queue again so other consumers would also "receive the signal".
That's because in this case we know exactly which are the consumers of each queue
because they are defined statically.
