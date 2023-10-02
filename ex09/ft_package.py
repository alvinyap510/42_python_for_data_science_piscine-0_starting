def count_in_list(words_array: list, word: str) -> int:
    '''
    Count matching words in an array
    '''
    try:
        counter = 0
        for i in words_array:
            if (i == word):
                counter += 1
        return counter
    except Exception as e:
        print(f"Error: {e}")
