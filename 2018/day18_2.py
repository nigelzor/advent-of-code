input = """
minute 962 score 634 351 = 222534
minute 963 score 638 349 = 222662
minute 964 score 641 354 = 226914
minute 965 score 641 354 = 226914
minute 966 score 638 360 = 229680
minute 967 score 637 355 = 226135
minute 968 score 631 360 = 227160
minute 969 score 622 362 = 225164
minute 970 score 611 367 = 224237
minute 971 score 605 356 = 215380
minute 972 score 600 350 = 210000
minute 973 score 598 343 = 205114
minute 974 score 594 344 = 204336
minute 975 score 595 330 = 196350
minute 976 score 594 335 = 198990
minute 977 score 594 332 = 197208
minute 978 score 594 338 = 200772
minute 979 score 597 334 = 199398
minute 980 score 598 338 = 202124
minute 981 score 602 330 = 198660
minute 982 score 605 334 = 202070
minute 983 score 610 329 = 200690
minute 984 score 613 337 = 206581
minute 985 score 619 334 = 206746
minute 986 score 621 344 = 213624
minute 987 score 625 343 = 214375
minute 988 score 628 348 = 218544
minute 989 score 632 344 = 217408
""".strip().split('\n')


def main():
    goal = 1000000000
    index = (goal - 962) % len(input)
    print(input[index])


if __name__ == '__main__':
    main()
