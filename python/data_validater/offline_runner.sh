mkdir /tmp/chenjian/histogram//20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/data/d_wiki_st_macro_sum_coec.data/* | python draw_histogram.py /tmp/chenjian/histogram//20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/d_wiki_st_macro_sum_coec.hist

echo "Done drawing feature d_wiki_st_macro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/data/c_ag_wiki_st_macro_sum_coec.data/* | python draw_histogram.py /tmp/chenjian/histogram//20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/c_ag_wiki_st_macro_sum_coec.hist

echo "Done drawing feature c_ag_wiki_st_macro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/data/gmp_score.data/* | python draw_histogram.py /tmp/chenjian/histogram//20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/gmp_score.hist

echo "Done drawing feature gmp_score"

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/data/u_uid_st_sum_click.data/* | python draw_histogram.py /tmp/chenjian/histogram//20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/u_uid_st_sum_click.hist

echo "Done drawing feature u_uid_st_sum_click"

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/data/c_cty_wiki_st_macro_sum_coec.data/* | python draw_histogram.py /tmp/chenjian/histogram//20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/c_cty_wiki_st_macro_sum_coec.hist

echo "Done drawing feature c_cty_wiki_st_macro_sum_coec"

echo "All Done"

