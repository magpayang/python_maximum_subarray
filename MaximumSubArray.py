def MaximumSubarrayBrute(input_array):
    max_sum = input_array[0];
    start_index = 0;
    end_index = 0;

    i = 0
    for idx in input_array:
        running_sum = idx;
        if running_sum > max_sum:
            max_sum = running_sum
            start_index = i
            end_index = i
        j = i + 1
        for jdx in input_array[input_array.index(idx) + 1:]:
            running_sum += jdx
            if running_sum > max_sum:
                max_sum = running_sum
                start_index = i
                end_index = j
            j += 1
        i += 1

    return input_array[start_index:end_index + 1]

def MaximumSubarrayDivideandConquer(input_array, ldx, hdx):
    if ldx == hdx:  # base case when there is only one element left
        return ldx, hdx, input_array[ldx]

    else:  # for arrays with two or more elements, calculate midpoint mdx
        mdx = (ldx + hdx)//2  # divide the array into Left[ldx:mdx] and Right[mdx+1: hdx]
        Left_ldx, Left_hdx, Left_sum = MaximumSubarrayDivideandConquer(input_array, ldx, mdx)
        Cross_ldx, Cross_hdx, Cross_sum = MaxCrossingSubArray(input_array, ldx, mdx, hdx)  # you will enter here if there are two elements left. ldx = mdx; mdx+1 = hdx
        Right_ldx, Right_hdx, Right_sum = MaximumSubarrayDivideandConquer(input_array, mdx+1, hdx)

    if Left_sum >= Right_sum and Left_sum >= Cross_sum:
        return Left_ldx, Left_hdx, Left_sum
    elif Right_sum >= Left_sum and Right_sum >= Cross_sum:
        return Right_ldx, Right_hdx, Right_sum
    else:
        return Cross_ldx, Cross_hdx, Cross_sum

def MaxCrossingSubArray(input_array, ldx, mdx, hdx):
    Left_sum = float('-inf')
    sum = 0

    # for idx in input_array[mdx:ldx:-1]:
    for idx in range(mdx,ldx-1,-1):
        sum += input_array[idx]
        if sum > Left_sum:
            Left_sum = sum
            max_left = idx

    Right_sum = float('-inf')
    sum = 0

    for idx in range(mdx+1,hdx+1):
        sum += input_array[idx]
        if sum > Right_sum:
            Right_sum = sum
            max_right = idx

    return max_left, max_right, Left_sum + Right_sum


