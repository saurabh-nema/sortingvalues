class sortvalues():
    """
    this class is for sorting the elements that are stored inside a list
    """
    my_list = [] # this list will store the elements
    def add_elements(self,value=0): # functionality to append the elements to the list
        self.my_list.append(value)

    def sort_function(self): # functionality to sort the elements using bubble sort
        n = len(self.my_list)  # we are calculating the lenght.
        for i in range(0,n-1):  # this is a loop which is going to short the values.
            for j in range(i+1,n):
                if(self.my_list[i]<self.my_list[j]):
                    temp=self.my_list[i]
                    self.my_list[i]=self.my_list[j]
                    self.my_list[j]=temp

    def largest(self,k=0):
        """
        asking you to print the numbers range
        :param k: taking int as range to print
        :return:
        """
        for i in range(0,k):
            print(self.my_list[i])

if __name__ == '__main__':
    sort=sortvalues()
    sort.add_elements(5)  # appending values
    sort.add_elements(10)   # appending values
    sort.add_elements(3)    # appending values
    sort.add_elements(1)    # appending values
    sort.add_elements(4)    # appending values
    sort.add_elements(7)    # appending values
    sort.sort_function()    # calling the sorthing function and it will sort it give you results.
    sort.largest(3) #for how much numbers you want me to print the largest one