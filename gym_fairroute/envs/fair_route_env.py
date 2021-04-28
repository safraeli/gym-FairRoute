import gym
from gym import error, spaces, utils
from gym.utils import seeding


class FairRouteEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, df_tasks, df_drivers):
        # The input is passed as a DataFrame.
        # Columns are added/modified for the output
        super(FairRouteEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        self.df_tasks = df_tasks
        self.num_tasks = len(df_tasks)
        self.action_space = spaces.Discrete(self.num_tasks)

        print('init')
        # Driver has it's initial location.
        self.df_tasks.drivers = -1
        # Tasks has two locations from and to
        self.tasks = []
        # Each driver is assigned with a route
        self.routes = []

    def step(self, task, driver):
        # at each step a task is assigned to a driver
        self.df_tasks[task].drivers = driver
        print('A driver: {}, is assigned with is a task: {}'.format(task, driver))
        # During a step a driver is assigned with a Task

    def reset(self):
        print('reset')
        self.routes.clear()

    def render(self, mode='human'):
        print('render')

    def close(self):
        print('close')
        self.tasks = None
        self.routes = None
