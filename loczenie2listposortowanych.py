class Solution:
    def mergeTwoLists(self, list1, list2):
        listagotowe = list()
        while True:
            if list1[0]<list2[0]:
                listagotowe.append(list1[0])
                pop =1
            if list1[0]==list2[0]:
                listagotowe.append(list1[0])
                listagotowe.append(list2[0])
                pop=3
            if list1[0]>list2[0]:
                listagotowe.append(list2[0])
                pop =2
            if pop ==1:
                list1.pop(0)
            if pop ==2:
                list2.pop(0)
            if pop ==3:
                list1.pop(0)
                list2.pop(0)
            if len(list1)==0:
                for x in list2:
                    listagotowe.append(x)
            if len(list2)==0:
                for x in list1:
                    listagotowe.append(x)
                break
        return listagotowe

x = Solution()
list1 = [1,2,4]
list2 = [1,3,4]
print(x.mergeTwoLists(list1,list2))