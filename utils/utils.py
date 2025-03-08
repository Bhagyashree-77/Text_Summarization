def get_input_from_batch(batch):
    print("Extracting input from batch")
    return batch

def get_output_from_batch(batch):
    print("Extracting output from batch")
    return batch

def calc_running_avg_loss(loss, running_loss, step):
    if running_loss is None:
        return loss
    return 0.99 * running_loss + 0.01 * loss
