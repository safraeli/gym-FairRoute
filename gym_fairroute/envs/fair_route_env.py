import gym
from gym import error, spaces, utils
from gym.utils import seeding


class FairRouteEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, num_tasks, num_drivers):
        super(FairRouteEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(num_tasks)
        # Example for using image as input:
        self.observation_space = spaces..Box(low=0, high=255, dtype=np.uint8)

        print('init')
        # Driver has it's initial location.
        self.drivers = []
        # Tasks has two locations from and to
        self.tasks = []
        # Each driver is assigned with a route
        self.routes = []

    def step(self, action):
        print('step'.format(str(action)))
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
