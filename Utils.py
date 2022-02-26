SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


# import Live
#
#
# def scores_file_name(file_name=None):
#      if file_name is None:
#          return str("Scores.txt")
#      else:
#          return file_name
#
#  open(scores_file_name("101dalmtim.txt"), "a")
#
#
#  def bad_return_code():
#      try:
#          Live.load_game() == str("")
#
#      except UserWarning:
#          print("Cant write letters only figures , try again")
#
# from Score import add_score
# SCORES_FILE_NAME = "Scores.txt"
# BAD_RETURN_CODE = -1
#
#  with open("Scores.txt", "a")) as rw_scores:
#         rw_scores.read()
#         rw_scores.write(+ "\n")
#         rw_scores.close()
#
#

#
#  def save_score():
#      if 1 != 2:
#          return BAD_RETURN_CODE
#
#
#  def save_name(name_to_save):
#      my_file = open("names.txt", "a")
#      my_file.write(name_to_save + "\n")
#      my_file.close()
#
#
#  # importing the module
#  from Utils import SCORES_FILE_NAME
#  import json
#
#  # reading the data from the file
#  with open(SCORES_FILE_NAME) as f:
#      data = f.read()
#
#  print("Data type before reconstruction : ", type(data))
#
# # # reconstructing the data as a dictionary
#  js = json.loads(data)
#
#  print("Data type after reconstruction : ", type(js))
#  print(js)
#
#  print([item for item in js if item["username"] == "moshe" or item["username"] == "haim1"])
