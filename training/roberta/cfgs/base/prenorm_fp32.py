from src.args import Args

seed = 111111
output_dir = "../training_outputs/"
save_last_n_checkpoints = 100
project = "xfp-base-v2"

model = Args()
model.pl_module = "src.roberta.tasks.mlm.MLMModelModule"
model.encoder_type = "src.roberta.models.prenorm.PrenormRobertaModel"
model.initializer_range = 0.02
model.vocab_size = 50265
model.type_vocab_size = 1
model.pad_token_id = 1
model.num_hidden_layers = 12
model.num_attention_heads = 12
model.attention_head_size = 64
model.layer_norm_eps = 1e-05
model.intermediate_size = 3072
model.hidden_size = 768
model.hidden_dropout_prob = 0.1
model.attention_probs_dropout_prob = 0.1
model.max_position_embeddings = 512

trainer = Args()
trainer.strategy = "ddp"
trainer.precision = 32
trainer.devices = 8
trainer.num_nodes = 1
trainer.max_steps = 300000
trainer.val_check_interval = 10000
trainer.use_distributed_sampler = False

data = Args()
data.pl_module = "src.roberta.data.data_module_pretrain.PretrainDataModule"
data.num_workers = 8
data.training_dataset_path = "/data/wiki_en_1k/train.arrow"
data.validation_dataset_path = "/data/wiki_en_1k/val.arrow"
data.tokenizer = "../pretrained/tokenizers/roberta-base"
data.collator = "src.roberta.data.pretrain.mlm.MLMCollator"
data.collator_args = Args()
data.collator_args.num_masked_tokens = 77
data.collator_args.max_sequence_length = 512
data.batch_size = 16

optimizer = Args()
optimizer.optimizer = "adam"
optimizer.adam_beta1 = 0.9
optimizer.adam_beta2 = 0.98
optimizer.adam_epsilon = 1e-6
optimizer.weight_decay = 0.01
optimizer.base_learning_rate = 5e-5
optimizer.min_lr_ratio = 0.001
optimizer.lr_scheduler_type = "linear"
optimizer.warmup_steps = 10000