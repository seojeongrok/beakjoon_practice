if __name__ == '__main__':
    croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    word = input()

    for i in croatian :
        word = word.replace(i, '*')
    print(len(word))