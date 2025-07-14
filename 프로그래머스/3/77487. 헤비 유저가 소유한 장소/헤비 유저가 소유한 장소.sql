SELECT ID, NAME, HOST_ID
FROM PLACES 
where host_id in (select host_id
                    from places
                    group by host_id
                    having count(id)>1)
order by id 