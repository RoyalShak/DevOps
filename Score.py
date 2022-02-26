import Live
# import Tests

import Utils


def get_player_name(name):
    player_name = name
    return player_name


def write_score_to_file(score, difficulty):
    score += difficulty * 3 + 5
    with open(Utils.SCORES_FILE_NAME, "w") as file:
        file.write(str(score))


def add_score(difficulty):
    try:
        with open(Utils.SCORES_FILE_NAME, "r") as file:
            score = int(file.read())
        write_score_to_file(score, difficulty)
    except FileNotFoundError as e:
        print(f"File NOT found - Let Me Create Scores.txt For You Master {e.args}")
        score = 0
        write_score_to_file(score, difficulty)
    except ValueError as e:
        print(f"Cant Accept Any Figures Except Numbers {e.args}")
        score = 0
        write_score_to_file(score, difficulty)

# import Utils
#
#
# def get_player_name(name):
#     player_name = name
#     return player_name
#
#
# def add_score(difficulty, name):
#     try:
#         points = int(difficulty * 3 + 5)
#         print(points)
#         name01 = name
#         score = str(points)
#         with open(Utils.SCORES_FILE_NAME, "w") as file:
#             file.write(f"\n{name01} : {score}")
#         return score, name01
#
#     except FileNotFoundError as e:
#         print(f"File NOT found! {e.args}")
#         return Utils.BAD_RETURN_CODE

# def add_score(difficulty):
#     points = int(difficulty * 3 + 5)
#     print(points)
#     Tests.save_score(points)


# with open(SCORES_FILE_NAME) as rw_scores:
#     rw_scores.read()
#     rw_scores.write()
#     rw_scores.close()
