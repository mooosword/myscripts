define LENGTH(data) returns length_res {
    
    grouped = group $data all;
    $length_res = foreach grouped generate 'count' as key, COUNT($data) as value;

};
