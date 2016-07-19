IMPORT 'coverage_macro.pig';

data = LOAD '/user/chenjian/verification/20140918';

col = FOREACH data GENERATE $0 as value;

STORE col INTO '/tmp/chenjian//20140918.validate/data/d_wiki_st_macro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140918.validate/coverage/d_wiki_st_macro_sum_coec.cov';

col = FOREACH data GENERATE $1 as value;

STORE col INTO '/tmp/chenjian//20140918.validate/data/c_ag_wiki_st_macro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140918.validate/coverage/c_ag_wiki_st_macro_sum_coec.cov';

col = FOREACH data GENERATE $2 as value;

STORE col INTO '/tmp/chenjian//20140918.validate/data/gmp_score.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140918.validate/coverage/gmp_score.cov';

col = FOREACH data GENERATE $3 as value;

STORE col INTO '/tmp/chenjian//20140918.validate/data/u_uid_st_sum_click.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140918.validate/coverage/u_uid_st_sum_click.cov';

col = FOREACH data GENERATE $4 as value;

STORE col INTO '/tmp/chenjian//20140918.validate/data/c_cty_wiki_st_macro_sum_coec.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140918.validate/coverage/c_cty_wiki_st_macro_sum_coec.cov';

col = FOREACH data GENERATE $5 as value;

STORE col INTO '/tmp/chenjian//20140918.validate/data/doc_age.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140918.validate/coverage/doc_age.cov';

col = FOREACH data GENERATE $6 as value;

STORE col INTO '/tmp/chenjian//20140918.validate/data/doc_length.data';

cov = FEATURE_COVERAGE(col);

STORE cov INTO '/tmp/chenjian//20140918.validate/coverage/doc_length.cov';

