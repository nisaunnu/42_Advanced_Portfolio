def main():
    """Modify each data object's second element into a greeting
    and print all four of them."""

    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    # --- LIST ---
    ft_list[1] = "World!"

    # --- TUPLE ---
    temp_list = list(ft_tuple)
    temp_list.pop()
    temp_list.insert(1, "Turkiye!")
    ft_tuple = tuple(temp_list)

    # --- SET ---
    ft_set.remove("tutu!")
    ft_set.add("Kocaeli!")

    # --- DICT ---
    ft_dict["Hello"] = "42Kocaeli!"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == "__main__":
    main()
