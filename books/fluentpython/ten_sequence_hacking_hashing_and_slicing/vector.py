"""Doctest for vector

    Test init from iterables
        >>> v1 = Vector([0, 1, 2])
        >>> v2 = Vector((0, 1, 2))
        >>> v3 = Vector(range(3))

    Test repr
        >>> v1
        Vector([0.0, 1.0, 2.0])
        >>> v3
        Vector([0.0, 1.0, 2.0])

    Test str
        >>> print(v2)
        (0.0, 1.0, 2.0)

    unpack
       >>> x, y, z = v1
       >>> x, y, z
       (0.0, 1.0, 2.0)

    eq tst
       >>> v1_clone = eval(repr(v1))
       >>> v1 == v1_clone
       True

    bytes tst
       >>> octets = bytes(v1)
       >>> octets
       b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\xf0?\\x00\\x00\\x00\\x00\\x00\\x00\\x00@'

    abs tst
       >>> abs(v1)
       2.23606797749979

    bool tst
       >>> bool(v1), bool(Vector([0, 0, 0, 0]))
       (True, False)


    cls meth tst
        >>> v1_clone = Vector.frombytes(bytes(v1))
        >>> v1_clone
        Vector([0.0, 1.0, 2.0])
        >>> v1 == v1_clone
        True

    implement sequence proto
       >>> len(v1)
       3
       >>> v1[0], v1[-1]
       (0.0, 2.0)

    slicing
        >>> v1[1,2]
        Traceback (most recent call last):
          ...
        TypeError: Vector indices must be integers
        >>> v1[1]
        1.0
        >>> v1[1:4]
        Vector([1.0, 2.0])
        >>> v1[-1:]
        Vector([2.0])

    dynamic attr access
        >>> v1 = Vector(range(10))
        >>> v1.x, v1.y, v1.z, v1.t
        (0.0, 1.0, 2.0, 3.0)

    format test
        >>> format(Vector([-1, -1, -1, -1]), 'h')
        '<2.0, 2.0943951023931957, 2.186276035465284, 3.9269908169872414>'
        >>> format(Vector([2, 2, 2, 2]), '.3eh')
        '<4.000e+00, 1.047e+00, 9.553e-01, 7.854e-01>'
        >>> format(Vector([0, 1, 0, 0]), '0.5fh')
        '<1.00000, 1.57080, 0.00000, 0.00000>'
"""

from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)])
                + bytes(self._components))

    def __eq__(self, other):
        return len(self) == len(other) and any(a==b for a, b in zip(self, other))

    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)],
                                      self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))


    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
