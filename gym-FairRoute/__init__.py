from gym.envs.registration import register

register(
    id='fair_route-v0',
    entry_point='gym_fair_route.envs:FairRouteEnv',
)
register(
    id='fair_route-extrahard-v0',
    entry_point='gym_fair_route.envs:FairRouteExtraHardEnv',
)
