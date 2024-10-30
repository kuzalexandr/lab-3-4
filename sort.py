if __name__ == '__main__':
    result = sorted(data, reverse=True)
    print(result)

    result_with_lambda = lambda a: sorted(data, reverse= True)
    print(result_with_lambda(data))