source ~/.bashrc

data=/tmp/chenjian/p13n/output/20140722-20140722-coldstart-crossl1-doc-user-context-coec.fv

head -1 $data > ${data##*/}.header

hput $data /tmp/chenjian/

python data_loader_factory.py offline.conf 

hrmr /tmp/chenjian/${data##*/}.validate

runpig loader.pig

output_dir=/tmp/chenjian/${data##*/}.validate


