def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32) ")

def get_user_input():
    float_list=[]
    user_str = input()
    str_list = user_str.split(",")

    for i in range(len(str_list)):
        float_list.append(float(str_list[i]))
    return float_list

def calc_average(float_list):
    avg = sum(float_list)/len(float_list)
    return avg

def find_min_max(float_list):
    maxmin_list = []
    maxmin_list.append(min(float_list))
    maxmin_list.append(max(float_list))
    return maxmin_list

def sort_temperature(slist):
    slist.sort()
    return slist

def calc_median_temperature(mlist):
    length = len(mlist)
    if length % 2 == 0:
        median = (mlist[int(length/2)-1]+mlist[int(length/2)])/2
    if length % 2 != 0:
        median = mlist[int((length-1)/2)]
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average = calc_average(num_list)
    maxmin = find_min_max(num_list)
    sort_list = sort_temperature(num_list)
    median = calc_median_temperature(sort_list)
    print("Average: " + str(average) + "\nMaximum: " + str(maxmin[0]) + "\nMinimum: " + str(maxmin[1]))
    print("Median: " + str(median))



if __name__ == "__main__":
    main()
