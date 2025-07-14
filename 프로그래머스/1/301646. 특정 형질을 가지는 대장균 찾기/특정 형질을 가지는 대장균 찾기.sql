select count(id) as COUNT
from ecoli_data
where RIGHT(concat('0000', conv(genotype, 10, 2)), 3) in ('101', '100', '001')