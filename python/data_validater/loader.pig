IMPORT 'coverage_macro.pig';

data = LOAD '/tmp/chenjian/20140722-20140722-crossl1-doc-user-context-coec.fv';

col = FOREACH data GENERATE $46 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_ag_wiki_st_macro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_ag_wiki_st_macro_sum_coec.cov';

col = FOREACH data GENERATE $38 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/d_wiki_st_macro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/d_wiki_st_macro_sum_coec.cov';

col = FOREACH data GENERATE $0 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/gmp_score.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/gmp_score.cov';

col = FOREACH data GENERATE $83 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/u_uid_st_sum_click.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/u_uid_st_sum_click.cov';

col = FOREACH data GENERATE $37 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/d_wiki_st_micro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/d_wiki_st_micro_sum_coec.cov';

col = FOREACH data GENERATE $54 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_cty_wiki_st_macro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_cty_wiki_st_macro_sum_coec.cov';

col = FOREACH data GENERATE $14 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/doc_wiki_squaresum_score.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/doc_wiki_squaresum_score.cov';

col = FOREACH data GENERATE $21 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/u_cty_st_micro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/u_cty_st_micro_sum_coec.cov';

col = FOREACH data GENERATE $20 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/u_ag_st_micro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/u_ag_st_micro_sum_coec.cov';

col = FOREACH data GENERATE $5 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/doc_age.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/doc_age.cov';

col = FOREACH data GENERATE $45 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_ag_wiki_st_micro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_ag_wiki_st_micro_sum_coec.cov';

col = FOREACH data GENERATE $6 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/doc_length.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/doc_length.cov';

col = FOREACH data GENERATE $82 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_uid_wiki_st_sum_click.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_uid_wiki_st_sum_click.cov';

col = FOREACH data GENERATE $53 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_cty_wiki_st_micro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_cty_wiki_st_micro_sum_coec.cov';

col = FOREACH data GENERATE $22 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/d_pub_st_micro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/d_pub_st_micro_sum_coec.cov';

col = FOREACH data GENERATE $47 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_ag_wiki_st_micro_max_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_ag_wiki_st_micro_max_coec.cov';

col = FOREACH data GENERATE $40 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/d_wiki_st_macro_max_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/d_wiki_st_macro_max_coec.cov';

col = FOREACH data GENERATE $13 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/doc_yct_squaresum_score.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/doc_yct_squaresum_score.cov';

col = FOREACH data GENERATE $39 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/d_wiki_st_micro_max_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/d_wiki_st_micro_max_coec.cov';

col = FOREACH data GENERATE $23 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_ag_pub_st_micro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_ag_pub_st_micro_sum_coec.cov';

col = FOREACH data GENERATE $19 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/context_hour_of_day.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/context_hour_of_day.cov';

col = FOREACH data GENERATE $33 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/d_yct_st_micro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/d_yct_st_micro_sum_coec.cov';

col = FOREACH data GENERATE $18 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/context_day_of_week.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/context_day_of_week.cov';

col = FOREACH data GENERATE $81 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_uid_yct_st_sum_click.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_uid_yct_st_sum_click.cov';

col = FOREACH data GENERATE $55 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_cty_wiki_st_micro_max_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_cty_wiki_st_micro_max_coec.cov';

col = FOREACH data GENERATE $70 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_yct_wiki_st_macro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_yct_wiki_st_macro_sum_coec.cov';

col = FOREACH data GENERATE $12 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/doc_wiki_sum_score.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/doc_wiki_sum_score.cov';

col = FOREACH data GENERATE $59 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_wiki_wiki_st_micro_max_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_wiki_wiki_st_micro_max_coec.cov';

col = FOREACH data GENERATE $48 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_ag_wiki_st_macro_max_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_ag_wiki_st_macro_max_coec.cov';

col = FOREACH data GENERATE $41 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_ag_yct_st_micro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_ag_yct_st_micro_sum_coec.cov';

col = FOREACH data GENERATE $11 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/doc_yct_sum_score.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/doc_yct_sum_score.cov';

col = FOREACH data GENERATE $43 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_ag_yct_st_micro_max_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_ag_yct_st_micro_max_coec.cov';

col = FOREACH data GENERATE $34 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/d_yct_st_macro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/d_yct_st_macro_sum_coec.cov';

col = FOREACH data GENERATE $35 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/d_yct_st_micro_max_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/d_yct_st_micro_max_coec.cov';

col = FOREACH data GENERATE $42 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/c_ag_yct_st_macro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/c_ag_yct_st_macro_sum_coec.cov';

col = FOREACH data GENERATE $27 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/u_yct_st_micro_max_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/u_yct_st_micro_max_coec.cov';

col = FOREACH data GENERATE $17 as value;

STORE col INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/data/user_login_status.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140722-20140722-crossl1-doc-user-context-coec.fv.validate/coverage/user_login_status.cov';

