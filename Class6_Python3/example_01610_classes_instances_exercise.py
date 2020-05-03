# create 1 instance of Robot
# give it a the model "HAL9000"
# give it the mission "protect humans"
# print its model
# print its mission

class Robot:
    def __init__(self, model, mission):
        self.model = model
        self.mission = mission

my_robot = Robot("HAL9000", "protect humans")
    print(Robot.model)
    print(Robot.mission)


