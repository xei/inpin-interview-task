import math


# to compute the exact distance, we need to use some GIS database
# 	(forexample PostgGIS: http://postgis.refractions.net)
# 	However, for small distances like local map we can approximate it well
# 	in minimal computations using Great Circle Distance (Orthodromic Distance).
# 	https://en.wikipedia.org/wiki/Great-circle_distance
# 	https://stackoverflow.com/questions/51014687/convert-a-complex-sql-query-to-sqlalchemy/51018368#51018368
def orthodromic_distance(lat1, lng1, lat2, lng2, math=math):
    ang = math.acos(math.cos(math.radians(lat1)) *
                    math.cos(math.radians(lat2)) *
                    math.cos(math.radians(lng2) -
                             math.radians(lng1)) +
                    math.sin(math.radians(lat1)) *
                    math.sin(math.radians(lat2)))

    return 6371 * ang