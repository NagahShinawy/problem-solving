"""
In this article, we will see how can we remove an empty tuple from a given list of tuples. We will find various ways,
in which we can perform this task of removing tuples using various methods and ways in Python.
Examples:

Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
                  ('krishna', 'akbar', '45'), ('',''),()]
Output : [('ram', '15', '8'), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', '')]

Input : tuples = [('','','8'), (), ('0', '00', '000'),
                 ('birbal', '', '45'), (''), (),  ('',''),()]
Output : [('', '', '8'), ('0', '00', '000'), ('birbal', '',
          '45'), ('', '')]
"""


def remove_empty_tuple(items):
    return [item for item in items if item]


def remove_empty_tuple2(items):
    return [item for item in filter(None, items)]


print(remove_empty_tuple([(), ('ram', '15', '8'), (), ('laxman', 'sita'),
                          ('krishna', 'akbar', '45'), ('', ''), ()]))


print(remove_empty_tuple2([(), ('ram', '15', '8'), (), ('laxman', 'sita'),
                          ('krishna', 'akbar', '45'), ('', ''), ()]))