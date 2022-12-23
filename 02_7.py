#버블정렬
# a = [5, 4, 1, 2, 3]
# def bubble_sort(a):
#     for i in range(0,len(a)):
#         for j in range(0,len(a)-i-1):
#             if a[j] > a[j+1]:
#                 a[j] , a[j+1] = a[j+1] , a[j]
#     return a
# print(bubble_sort(a))

#선택정렬
# def sel_sort(a):
#     n = len(a)
#     for i in range(0, n - 1):
#
#         min_idx = i
#
#         for j in range(i + 1, n):
#             if a[j] < a[min_idx]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]
#         print(a)  # 정렬 과정 출력하기
# d = [2, 4, 5, 1, 3]
# sel_sort(d)
# print(d)

#삽입정렬
# a = [8, 3, 2, 7, 6]
#
# for i in range(1, len(a)):
#     for j in range(i, 0, -1):
#         if a[j - 1] > a[j]:
#             a[j - 1], a[j] = a[j], a[j - 1]
# print(a)


#정렬된 두 배열 합치기
