from collections import namedtuple
from operator import attrgetter

data = [
    ('Bos Landen', 6937, 74.7, 136, (41.394874, -92.956282)),
    ('Toad Valley', 6224, 69.5, 116, (41.590168, -93.441750)),
    ('Blank', 6745, 72.3, 127, (41.512889, -93.624533)),
]

def main():


    GolfCourse = namedtuple('GolfCourse', 'name yards rating slope coord')
    LatLong = namedtuple('LatLong', 'lat long')

    golf_courses = [GolfCourse(name, yards, rating, slope, LatLong(lat, long))
        for name, yards, rating, slope, (lat, long) in data]

    name_lat = attrgetter('name', 'yards')

    for course in sorted(golf_courses, key=attrgetter('rating')):
        print(name_lat(course))

if __name__=="__main__":
    main()

