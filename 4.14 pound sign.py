# 14. Write a program that uses nested loops to draw this pattern:
# ##
# # #
# #  #
# #   #
# #    #
# #     #

rows = 6
for i in range(1, rows + 1):
    print("#", end ="") 
    for j in range(1, i):
        print(" ", end="")
    print("#")