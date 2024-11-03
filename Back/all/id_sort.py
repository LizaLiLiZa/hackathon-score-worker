def id_sort(reviews_dict_array):
    sorted_data = sorted(reviews_dict_array, key=lambda item: (item["id_to"], item["id_from"]))
    return sorted_data
