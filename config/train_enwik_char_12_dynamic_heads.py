# train a miniature character-level enwik model
# good for debugging and playing on macbooks and such

out_dir = 'out-enwik-char-dynamic-heads'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 200
log_interval = 10 # don't print too too often
init_from = "resume"

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'enwik-char'
wandb_run_name = 'mini-gpt'

dataset = 'enwik_char'
gradient_accumulation_steps = 1
batch_size = 128
block_size = 512 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 12
n_head = 16
n_embd = 512
dropout = 0.2
dynamic_heads = True

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 200000
lr_decay_iters = 100000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

# on macbook also add
# device = 'cpu'  # run on cpu only
compile = False # do not torch compile the model
