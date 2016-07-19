mkdir /tmp/chenjian/histogram//verify_dedicate_model

hadoop fs -cat /tmp/chenjian//verify_dedicate_model.validate/data/d_wiki_st_macro_sum_coec.data/* | python draw_histogram.py /tmp/chenjian/histogram//verify_dedicate_model/d_wiki_st_macro_sum_coec.hist

echo "Done drawing feature d_wiki_st_macro_sum_coec"

hadoop fs -cat /tmp/chenjian//verify_dedicate_model.validate/data/c_ag_wiki_st_macro_sum_coec.data/* | python draw_histogram.py /tmp/chenjian/histogram//verify_dedicate_model/c_ag_wiki_st_macro_sum_coec.hist

echo "Done drawing feature c_ag_wiki_st_macro_sum_coec"

hadoop fs -cat /tmp/chenjian//verify_dedicate_model.validate/data/gmp_score.data/* | python draw_histogram.py /tmp/chenjian/histogram//verify_dedicate_model/gmp_score.hist

echo "Done drawing feature gmp_score"

hadoop fs -cat /tmp/chenjian//verify_dedicate_model.validate/data/u_uid_st_sum_click.data/* | python draw_histogram.py /tmp/chenjian/histogram//verify_dedicate_model/u_uid_st_sum_click.hist

echo "Done drawing feature u_uid_st_sum_click"

hadoop fs -cat /tmp/chenjian//verify_dedicate_model.validate/data/c_cty_wiki_st_macro_sum_coec.data/* | python draw_histogram.py /tmp/chenjian/histogram//verify_dedicate_model/c_cty_wiki_st_macro_sum_coec.hist

echo "Done drawing feature c_cty_wiki_st_macro_sum_coec"

echo "All Done"

