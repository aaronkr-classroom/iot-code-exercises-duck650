#3_set.py
set1={1,2,3,'a',"Hello"}
set2={"Hello",3,4,5,'b'}

union_set=set1|set2

int_set=set1&set2

diff_set=set1-set2

#대칭차집합(합집합과 교집합의 차집합)
sym_diff_set=set1^set2

print('union:', union_set)
print(f"intersection: {int_set}")
print(f"difference: {diff_set}")
print(f"symmetric difference: {sym_diff_set}")