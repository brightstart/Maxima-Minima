def maximum(arr, index, length):
    if index >= length - 2:
        if arr[index] > arr[index + 1]:
            return arr[index]
        else:
            return arr[index + 1]

    mx = maximum(arr, index + 1, length)   # recursive step

    if arr[index] > mx:
        return arr[index]
    else:
        return mx


def minimum(arr, index, length):
    if index >= length - 2:
        if arr[index] < arr[index + 1]:
            return arr[index]
        else:
            return arr[index + 1]

    mn = minimum(arr, index + 1, length)  # recursive step

    if arr[index] < mn:
        return arr[index]
    else:
        return mn


# Driver Code
if __name__ == '__main__':
    # Defining the variables
    minima, maxima = 0, -1

    try:

        input_stream = open("inputPS10.txt", "r")
        output_stream = open("outputPS10.txt", "w")
        while True:
            data = input_stream.readline().rstrip().split(" ")
            a = list(map(int, data))
            maxima = maximum(a, 0, len(a))

            minima = minimum(a, 0, len(a))

            if a[0] == maxima and a[len(a)-1] == minima:
                output_stream.write("decreasing " + str(minima) + "\n")
            elif a[0] == minima and a[len(a)-1] == maxima:
                output_stream.write("increasing " + str(minima) + "\n")
            elif a[0] == minima or a[len(a)-1] == minima:
                output_stream.write("maxima " + str(maxima) + "\n")
            else:
                output_stream.write("minima " + str(minima) + "\n")

            if not data:
                break
    except ValueError:
        input_stream.close()
        output_stream.close()
