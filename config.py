class Config:
    num_agents = 2
    state_size = 24
    action_size = 2
    random_seed = 123
    actor_fc1_units = 400
    actor_fc2_units = 300
    critic_fcs1_units = 400
    critic_fc2_units = 300
    buffer_size = int(1e6)
    batch_size = 128
    gamma = 0.99
    tau = 0.2 
    lr_actor = 1e-3
    lr_critic = 1e-3
    weight_decay = 0 
    ou_mu = 0
    ou_theta =0.15
    ou_sigma =0.1
    update_every_t_steps = 2
    num_of_updates = 1