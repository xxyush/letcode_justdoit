
def findMedianSortedArrays(nums1,nums2):
        def findKthElement(arr1, arr2, k):
            len1, len2 = len(arr1), len(arr2)
            if k == 1:
                return min(arr1[0], arr2[0])
            i = min(k // 2, len1) - 1  # 先比较两个数组的k//2
            j = min(k // 2, len2) - 1  # 先比较两个数组的k//2
            if arr1[i] > arr2[j]:
                if j >= len2 - 1:
                    return arr1[k - j - 2]
                else:
                    return findKthElement(arr1, arr2[j + 1:], k - j - 1)
            else:
                if i >= len1 - 1:
                    return arr2[k - i - 2]
                else:
                    return findKthElement(arr1[i + 1:], arr2, k - i - 1)

        def find_media_element(arr1, arr2):
            k = len(arr1) + len(arr2)
            mid_left = (k + 1) // 2
            mid_right = (k + 2) // 2
            if len(arr1) == 0:
                return (arr2[mid_left - 1] + arr2[mid_right - 1]) / 2
            elif len(arr2) == 0:
                return (arr1[mid_left - 1] + arr1[mid_right - 1]) / 2
            else:
                return (findKthElement(arr1, arr2, mid_left) + findKthElement(arr1, arr2, mid_right)) / 2

        return find_media_element(nums1, nums2)


if __name__=="__main__":
    num1=[9, 10, 29, 40]
    num2=[1,2,3,8]
    rs=findMedianSortedArrays(num1,num2)
    print(rs)