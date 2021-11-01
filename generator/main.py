import gpt_2_simple as gpt2
import datetime

model_name = "124M"

# model is saved into current directory under /models/124M/
gpt2.download_gpt2(model_name=model_name) #need to run only once. comment out once done.

sess = gpt2.start_tf_sess()

gpt2.load_gpt2(sess)
gpt2.generate(sess)

gen_file = 'gpt2_gentext_1.txt'

gpt2.generate(sess, destination_path=gen_file, length=39, include_prefix=False, nsamples=5, batch_size=5, temperature=0.7, top_p=0.9, run_name='run1', return_as_list=True)