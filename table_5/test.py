import wandb


for run in range(3):
    wandb.init(entity="dbx", project="VCG_Booking", group="test", name=f"run{run}")
    for i in range(5):
        wandb.log({"run": i})
    wandb.finish(exit_code=1)
