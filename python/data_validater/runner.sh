mkdir /tmp/chenjian/histogram//20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/data/gmp_score.data/* | python draw_histogram.py /tmp/chenjian/histogram//20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/gmp_score.hist

echo "Done drawing feature gmp_score"

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/data/yct_rel_score.data/* | python draw_histogram.py /tmp/chenjian/histogram//20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/yct_rel_score.hist

echo "Done drawing feature yct_rel_score"

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/data/wiki_rel_score.data/* | python draw_histogram.py /tmp/chenjian/histogram//20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/wiki_rel_score.hist

echo "Done drawing feature wiki_rel_score"

hadoop fs -cat /tmp/chenjian/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv.validate/data/doc_age.data/* | python draw_histogram.py /tmp/chenjian/histogram//20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv/doc_age.hist

echo "Done drawing feature doc_age"

echo "All Done"

