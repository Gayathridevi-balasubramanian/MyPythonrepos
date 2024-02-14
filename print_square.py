import time

def drawright(num):
    for i in range(num):
        print('.',end=' ')


def drawdown(num):
    for i in reversed(range(num)):
        print(''*(num-1))
        print('.')


def drawup(num):
    for i in reversed(range(num)):
        print('.')
    

drawup(5)
drawright(5)
drawdown(5)

# from scribes.terminalScribe import TerminalScribe

# class RobotScribe(TerminalScribe):
#     def up(self, distance=1):
#         self.setDirection([0, -1])
#         self.forward(distance)

#     def down(self, distance=1):
#         self.setDirection([0, 1])
#         self.forward(distance)

#     def right(self, distance=1):
#         self.setDirection([1, 0])
#         self.forward(distance)

#     def left(self, distance=1):
#         self.setDirection([-1, 0])
#         self.forward(distance)

#     def drawSquare(self, size):
#         self.right(size)
#         self.down(size)
#         self.left(size)
#         self.up(size)




# # size = 5

# # # Print square with dots
# # for i in range(size):
# #     for j in range(size):
# #         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
# #             print(".", end=" ")
# #         else:
# #             print(" ", end=" ")
# #     print()