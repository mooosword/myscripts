mkdir /tmp/chenjian/histogram//validate_20140923

hadoop fs -cat /tmp/chenjian/20140923.validate/data/doc_age.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/doc_age.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data doc_age /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature doc_age"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/c_ag_wiki_st_macro_sum_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/c_ag_wiki_st_macro_sum_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data c_ag_wiki_st_macro_sum_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature c_ag_wiki_st_macro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/doc_wiki_squaresum_score.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/doc_wiki_squaresum_score.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data doc_wiki_squaresum_score /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature doc_wiki_squaresum_score"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/doc_yct_squaresum_score.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/doc_yct_squaresum_score.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data doc_yct_squaresum_score /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature doc_yct_squaresum_score"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/doc_length.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/doc_length.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data doc_length /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature doc_length"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/gmp_score.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/gmp_score.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data gmp_score /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature gmp_score"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/u_cty_st_micro_sum_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/u_cty_st_micro_sum_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data u_cty_st_micro_sum_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature u_cty_st_micro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/d_wiki_st_micro_max_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/d_wiki_st_micro_max_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data d_wiki_st_micro_max_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature d_wiki_st_micro_max_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/c_cty_wiki_st_micro_sum_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/c_cty_wiki_st_micro_sum_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data c_cty_wiki_st_micro_sum_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature c_cty_wiki_st_micro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/c_uid_wiki_st_sum_click.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/c_uid_wiki_st_sum_click.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data c_uid_wiki_st_sum_click /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature c_uid_wiki_st_sum_click"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/d_wiki_st_macro_max_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/d_wiki_st_macro_max_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data d_wiki_st_macro_max_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature d_wiki_st_macro_max_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/c_ag_wiki_st_micro_max_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/c_ag_wiki_st_micro_max_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data c_ag_wiki_st_micro_max_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature c_ag_wiki_st_micro_max_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/d_wiki_st_micro_sum_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/d_wiki_st_micro_sum_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data d_wiki_st_micro_sum_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature d_wiki_st_micro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/c_ag_wiki_st_micro_sum_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/c_ag_wiki_st_micro_sum_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data c_ag_wiki_st_micro_sum_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature c_ag_wiki_st_micro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/c_cty_wiki_st_macro_sum_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/c_cty_wiki_st_macro_sum_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data c_cty_wiki_st_macro_sum_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature c_cty_wiki_st_macro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/u_ag_st_micro_sum_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/u_ag_st_micro_sum_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data u_ag_st_micro_sum_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature u_ag_st_micro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/d_pub_st_micro_sum_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/d_pub_st_micro_sum_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data d_pub_st_micro_sum_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature d_pub_st_micro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/c_ag_pub_st_micro_sum_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/c_ag_pub_st_micro_sum_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data c_ag_pub_st_micro_sum_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature c_ag_pub_st_micro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/context_hour_of_day.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/context_hour_of_day.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data context_hour_of_day /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature context_hour_of_day"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/d_yct_st_micro_sum_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/d_yct_st_micro_sum_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data d_yct_st_micro_sum_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature d_yct_st_micro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/d_wiki_st_macro_sum_coec.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/d_wiki_st_macro_sum_coec.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data d_wiki_st_macro_sum_coec /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature d_wiki_st_macro_sum_coec"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/u_uid_st_sum_click.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/u_uid_st_sum_click.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data u_uid_st_sum_click /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature u_uid_st_sum_click"

hadoop fs -cat /tmp/chenjian/20140923.validate/data/context_day_of_week.data/* > /tmp/online.data

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/data/context_day_of_week.data/* > /tmp/offline.data

python draw_two_histogram.py /tmp/online.data /tmp/offline.data context_day_of_week /tmp/chenjian/histogram//validate_20140923

echo "Done drawing feature context_day_of_week"

echo "All Done"

