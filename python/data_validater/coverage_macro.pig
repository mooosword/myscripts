define LENGTH(data) returns length_res {

    grouped = group $data all;
    $length_res = foreach grouped generate 'count' as key, COUNT($data) as value;

};


define FEATURE_COVERAGE(data) returns cov_res {
    
    not_null_data = filter $data by value is not null;

    split not_null_data into 
            zero_data if value == 0,
            non_zero_data if value > 0;
   
    --store zero_data into '/tmp/chenjian/zero_data';
    --store non_zero_data into '/tmp/chenjian/non_zero_data';

    N_data = LENGTH($data);
    N_not_null_data = LENGTH(not_null_data);
    N_zero_data = LENGTH(zero_data);
    N_non_zero_data = LENGTH(non_zero_data);

    joined = join N_data by key,
                  N_not_null_data by key,
                  --N_zero_data by key,
                  N_non_zero_data by key parallel 1;

    --store joined into '/tmp/chenjian/joined';

    projected = foreach joined generate 
            N_data::value as total_count, 
            N_not_null_data::value as not_null_data_count,
            --N_zero_data::value as zero_data_count,
            N_non_zero_data::value as non_zero_data_count;
    
    $cov_res = foreach projected generate 
            total_count,
            (total_count - not_null_data_count) as null_count,
            (not_null_data_count - non_zero_data_count) as zero_count,
            non_zero_data_count as non_zero_count,
            ((double)(total_count - not_null_data_count)) / total_count as null_ratio,
            ((double)non_zero_data_count) / total_count as coverage;

};



    
