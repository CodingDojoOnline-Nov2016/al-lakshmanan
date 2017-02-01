import math

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print julia[2]
for data in julia:
     print data
julia = julia + ("Eat Pray Love", 2010)
print julia
julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print julia

value = ("Michael", "Instructor", "Coding Dojo")
(name, position, company) = value #tuple unpacking
print name
print position
print company
(a, b, c, d) = (1, 2, 3, 4)
print a
print b
print c
tuple_data = ('physics', 'chemistry', 'x-ray', 'python')
tuple_num = (67, 89, 31, 15)
print max(tuple_data)
print max(tuple_num)
tuple_data = ('physics', 'chemistry', 'x-ray', 'python')
tuple_num = (67, 89, 31, 15)
print min(tuple_data)
print min(tuple_num)
tuple_num = (67, 89, 31, False, 0, None)
print any(tuple_num)
tuple_num = (67, 89, 31, False, 0, None)
print all(tuple_num)
num = (1, 5, 7, 3, 8)
for indesx, iteem in enumerate(num):
    print(str(indesx)+" = "+str(iteem))
num = (1, 5, 7, 3, 8)
print sorted(num)
num = (9, 1, 8, 2, 7, 3)
print tuple(reversed(num))
def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)

get_circle_area(5)
